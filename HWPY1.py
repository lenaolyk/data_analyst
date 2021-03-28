#!/usr/bin/env python
# coding: utf-8

# задание 1

# In[16]:


phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(phrase_1) > len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
elif len(phrase_1) < len(phrase_2): 
    print("Фраза 2 длиннее фразы 1")
else: 
    print("Фразы равной длинны")


# In[17]:


phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'

if len(phrase_1) > len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
elif len(phrase_1) < len(phrase_2): 
    print("Фраза 2 длиннее фразы 1")
else: 
    print("Фразы равной длинны")


# In[18]:


phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'

if len(phrase_1) > len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
elif len(phrase_1) < len(phrase_2): 
    print("Фраза 2 длиннее фразы 1")
else: 
    print("Фразы равной длинны")


# задание 2

# In[ ]:


year = int(input())
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный год")
    else:
        print("Обычный год")
else:
    print("Високосный год")


# задание 3

# In[14]:


date=int(input("Введите день рождения:"))
month=int(input("Введите месяц рождения:"))
year=int(input("Введите год рождения:"))


if (date>=21 and date<=31 and month==3) or( month==4 and date>=1 and date<=19):
   print("Знак зодиака:Овен")
elif (date>=20 and date<=30 and month==4) or( month==5 and date>=1 and date<=20):
   print("Знак зодиака:Телец")
elif (date>=21 and date<=31 and month==5) or( month==6 and date>=1 and date<=21):
  print("Знак зодиака:Близнецы")
elif (date>=22 and date<=30 and month==6) or( month==7 and date>=1 and date<=22):
   print("Знак зодиака:Рак")
elif (date>=23 and date<=31 and month==7) or( month==8 and date>=1 and date<=22):
   print("Знак зодиака:Лев")
elif (date>=23 and date<=31 and month==8) or( month==9 and date>=1 and date<=22):
   print("Знак зодиака:Дева")
elif (date>=23 and date<=30 and month==9) or( month==10 and date>=1 and date<=23):
   print("Знак зодиака:Весы")
elif (date>=24 and date<=31 and month==10) or( month==11 and date>=1 and date<=22):
   print("Знак зодиака:Скорпион")
elif (date>=23 and date<=30 and month==11) or( month==12 and date>=1 and date<=21):
   print("Знак зодиака:Стрелец")
elif (date>=22 and date<=31 and month==12) or( month==1 and date>=1 and date<=20):
   print("Знак зодиака:Козерог")
elif (date>=21 and date<=31 and month==1) or( month==2 and date>=1 and date<=18):
   print("Знак зодиака:Водолей")
elif (date>=19 and date<=29 and month==2) or( month==3 and date>=1 and date<=20):
   print("Знак зодиака:Рыбы")


# задание 4

# In[15]:


d = 0
a = input('Введите  ширину в см: ')
b = input('Введите  длину в см: ')
c = input('Введите  высоту в см: ')
while True:
    if (a.isnumeric() and b.isnumeric() and c.isnumeric()):
        a = int(a)
        b = int(b)
        c = int(c)
        break
    else:
        print('Вводить можно только числа')
        a = input('Введите  ширину в см: ')
        b = input('Введите  длину в см: ')
        с = input('Введите  высоту в см: ')
    
if (a > 200 or b > 200 or c > 200):
    print('Упаковка для лыж')
elif (a <= 15 and b <= 15 and c <= 15):
    print('Коробка№1')
elif (15 < a <= 50 or 15 < b <= 50  or 15 < c <= 50):
    print('Коробка№2')
else:
    print('Коробка№3')


# In[ ]:




