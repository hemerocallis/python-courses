from random import shuffle

class Card:
    suits = ["пикей",
            "червей",
            "бубей",
            "треф"]
    
    values = [None, None, "2", "3",
             "4", "5", "6", "7",
             "8", "9", "10",
             "валета", "даму",
             "короля", "туза"]
    
    def __init__(self, v, s):
        """suit и value - целые числа"""
        self.value = v
        self.suit = s
        
    def __lt__(self, c2):
        """метод сравнения - less than"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
            
    def __gt__(self, c2):
        """метод сравнения - greater than"""
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
            
    def __repr__(self):
        """вывод карты"""
        v = self.values[self.value] + " " \
        + self.suits[self.suit]
        return v
    
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
        
    def rm_card(self):
        """метод удаляет карту из колоды 
           и возвращает ее значение"""
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
        
class Game:
    def __init__(self):
        name1 = input("Имя первого игрока: ")
        name2 = input("Имя второго игрока: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
    def wins(self, winner):
        w = "{} забирает карты"
        w = w.format(winner)
        print(w)
        
    def draw(self, p1n, p1c, p2n, p2c):
        d = """{} кладет {}, а {} кладет {}"""
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            wn = "выиграл {}".format(p1.name)
            return wn
        if p1.wins < p2.wins:
            wn = "выиграл {}".format(p2.name)
            return wn
        return "победила дружба"
        
    def play_game(self):
        """метод отвечает за процесс игры"""
        cards = self.deck.cards
        print("Игра началась!")
        while len(cards) >= 2:
            m = """Нажмите 'x' для выхода. Нажмите любую другую клавишу для хода: """
            response = input(m)
            if response == "x":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
                
        win = self.winner(self.p1, self.p2)
        print("Игра окончена. Результат: {}.".format(win))
        
game = Game()
game.play_game()
