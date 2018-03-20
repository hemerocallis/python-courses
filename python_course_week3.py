
# coding: utf-8

# In[21]:

# Ввести с клавиатуры строку латиницей (1-3 слова). 
# Зашифровать ее с использованием гарантированных алгоритмов шифрования. 
# Сформировать словарь, где в качестве ключа используется название 
# гарантированного алгоритма шифрования (md5, sha1, sha224, sha256, sha384, sha512),  
# а в качестве значения - результат шифрования в шестнадцатеричном представлении 
# { 'sha1': 'd0b…', 'md5', '1f3…',…}.
# Итог вывести отдельными операторами вывода в виде пар ключа и значения, 
# отсортированных по возрастанию ключа:
# md5 1f3…
# sha1 d0b…

import hashlib

s = str(input())

md5 = (hashlib.md5(s.encode())).hexdigest()
sha1 = (hashlib.sha1(s.encode())).hexdigest()
sha224 = (hashlib.sha224(s.encode())).hexdigest()
sha256 = (hashlib.sha256(s.encode())).hexdigest()
sha384 = (hashlib.sha384(s.encode())).hexdigest()
sha512 = (hashlib.sha512(s.encode())).hexdigest()

encoded_dict = {'md5': md5, 'sha1': sha1, 'sha224': sha224, 'sha256': sha256, 'sha384': sha384, 'sha512': sha512}

for key, value in sorted(encoded_dict.items()):
    print(key, value)


# In[ ]:



