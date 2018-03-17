
# coding: utf-8

# In[13]:

# Напишите программу, которая выводит на экран числа от 1 до 100. 
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», 
# а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, 
# то программа должна выводить слово «FizzBuzz»

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# In[12]:

for i in range(1, 101):
    output = "";
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if output == "":
        output = i
    print(output)      


# In[16]:

def FizzBuzz(multiples, *args):
    for i in range(*args):
        output = ""
        for multiple in multiples:
            if i % multiple == 0:
                output += multiples[multiple]
        if output == "":
            output = i
        print(output)
            
multiples = {3: "Fizz", 5: "Buzz"}
FizzBuzz(multiples, 1, 101)


# In[ ]:



