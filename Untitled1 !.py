#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б ="))
y=math.sqrt(a**2+b*22)
p=y+a+b
print(p) 


# In[5]:


a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
с = int(input("Введите число С = "))
S = a + b
S = S + c
print(S)


# In[8]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
g = math.sqrt(a*b)
print(g)


# In[1]:


import math
x = int(input("Введите число X = "))
if x>0:
    y = x**2
else:
    y = math.sqrt(x)
print(x,y)


# In[4]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
c = int(input("Введите число С = "))
D = b**2-4*a*c
if D>=0:
    x1 = ((-b-math.sqrt(D))/2*a)
    x2 = ((-b+math.sqrt(D))/2*a)
    print(x1,x2)
else:
    print("Решение НЕТ")


# x = int(input("Введите число X = "))
# y = int(input("Введите число Y = "))
# if x=-0
#     print("ERROR")
# else:
#      z = y/x
#      print(x,y,z)
#      

# In[5]:
import math
x = int(input("Введите число X = "))
if x>=0:
    y = math.sqrt(x)
else:
    y = x**2 
print(x,y)       

#5

# In[6]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
c = int(input ("BBдите число С = "))
D = b**2-4*a*c
if D >= 0:
    x1 = (-b-math.sqrt(D))/(2*a)
    x2 = (-b+math.sqrt(D))/(2*a)
    print(x1,x2)
else:
    print("ERROR")
    
# In[7]:


x = int(input("Введите число X = "))
y = int(input("Введите число Y = "))
if x==0:
    print("ERROR")
else:
    z = y/x
    print(x,y,z)
    
#7


# In[8]:


a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
s = a*b
if s>500:
    s= s+0,9
else:
    print(s)
    
#8


# In[9]:


a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
if a == b:
    print(a)
else:
    if a> b:
        a = a-b
    else:
        b = b - a

#9


# In[10]:


n = int(input("Введите число n = "))
S = 0
i = 1
if i <= n:
    S = S + i
    i = i + 2
else:
    print(S)
    
#10


# In[11]:
import math
i = int(input("Write "))
i = i + 1
P = 1
if P<=30:
    P = P*i
    i = i + 1
    print(i)
else:
    print("end")

#11



# In[12]:


Q = int(input("Введите число Q = "))
S = 0
i = 1
if S>Q:
    S = S + i
    i = i + 1
else:
    print(i-2)
    
    
#12




# In[13]:


n = 3
i = 1
S = 0
if i<=n:
    i = i + 1
    S = S + (3*i+2)
else: 
    print("END")
    
#13


# In[14]:


x = int(input("Введите число X = "))
if x<0:
    y = x**2+1
else:
    if x>=1:
        y = 4x-1
    else:
        y = 2x+1
print(y)

#14


# In[15]:


a = int(input("Введите число A = "))
if a == 0:
    x = 2
else:
    if a>0:
        x<c
    else:
        x>c
print(x)

#15

# In[16]:
import math
a = int(input("Write a: "))
b = int(input("Write b: "))
if a != 0:
    print("Уравнение имеет один корень b/a")

if b !=0:
    print("Любое число - корень уравнения")
else:
    print("Уравнения не имеет корней")

#16

# In[17]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
if a == 0:
    if b == 0:
        x = 2
    else:
        print("ERROR")
else:
    c = b/a
    if  a> 0:
        x>c
    else:
        x<c
print(x)

#17


# In[18]:


import math
a = int(input("Введите число А = "))
b = int(input("Введите число Б = "))
c = int(input ("BBдите число С = "))
min = a
if min >b:
    min = b
elif min >c:
    min = c
print(min)

#18


# In[19]:
import math
ST = int(input("Введите число ST = "))
if ST < 5:
    ZP = 130
elif ST <= 15:
    ZP=180
else:
    ZP = 180+(ST-15)*10
print(ZP)

#19


# In[20]:
import math
A = int(input("Введите число А = "))
B = int(input("Введите число Б = "))
X = int(input("Введите число X = "))
if X < 10:
    y = X+A
elif X<= 23:
    y = X+B
else:
    y = X + A**2
print(y)

#20

# In[21]:
import math
A = int(input("Введите число А = "))
B = int(input("Введите число Б = "))
C = int(input("Введите число C = "))
X = int(input("Введите число X = "))
Y = int(input("Введите число Y = "))
if A > B:
    R = A
    A = B
    B = R
    if B>C:
        R = B
        B = C
        C = R
        if A > B:
            R = A
            A = B
            B = R
            if X > Y:
                R = X
                X = Y
                Y = R
if A < X and B < Y:
    print("Пройдет")
else:
    print("Не пройдет")
 #22




