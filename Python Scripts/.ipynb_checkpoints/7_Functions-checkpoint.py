# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:45:34 2022

@author: rodol
"""

# # 93. Function to print "Hello Python!"
# print("\nExercise # 93")
# def my_func():
#     print("Hello Python!")
    
# my_func()

# # 94.Function to add two numbers and print results
# print("\nExercise # 94")
# def my_func():
#     add = 10 + 20
#     print(add)
    
# my_func()

# # 95. Function to multiply x * 10
# print("\nExercise # 95")
# def my_func(x):
#     return x * 10

# result = my_func(7)
# print(result)

# # 96. Divide x by y
# print("\nExercise # 96")
# def my_func(x, y):
#     return x / y

# result = my_func(38, 19)
# print(result)

# # 97. x ** y + z
# print("\nExercise # 97")
# def my_func(x, y, z):
#     return x ** y + z

# result = my_func(3,3,3)
# print(result)

# # 98. 
# print("\nExercise # 98")
# def my_func(x):
#     my_new_list = []
#     for i in range(5):
#         my_new_list.append(i * x)
#     return my_new_list
    
# result = my_func(2)
# print(result)

# # # 99. Text to upper case
# print("\nExercise # 99")
# def my_func(x):
#     return x.upper()

# result = my_func("Edcorner Learning")
# print(result)

# # 100. Divide x by y
# print("\nExercise # 100")
# def my_func(x):
#     return list(set(x))

# result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
# print(result)

# # 101. 
# print("\nExercise # 101")
# def my_func(x):
#     my_new_list = []
#     for i in x:
#         if i > 4:
#             my_new_list.append(i ** 2)
#     return my_new_list
        
# result = my_func((2, 3, 5, 6, 4, 8, 9))
# print(result)

# # 102. 
# print("\nExercise # 102")
# def my_func(x):
#     # Option 1    
#     return len(x) * sorted(x.keys())[-1]
#     # Option 2
#     #return len(x) * max(x.keys())
                        
# result = my_func({1:3, 2:3, 4:5, 5:9, 6:8, 3:7, 7:0})
# print(result)

# # 103. 
# print("\nExercise # 103")
# def my_func(x, y = 10):
#     return (x * y)
# result = my_func(5)
# print(result)

# # 104
# print("\nExercise # 104")
# def my_func(x, y = 100, z = 200):
#     return( x + y + z)
# result = my_func(50)
# print(result)

# # 105 Return x postioned at y
# print("\nExercise # 105")
# def my_func(x, y):
#     return x[y]
# result = my_func(list(range(2, 25, 2)), 4) 
# print(result)
   
# # 106. 
# print("\nExercise # 106")
# def my_func(x,*args):
#     return x * args[1]
# result = my_func(5, 10, 20, 30, 50)
# print(result)

# # 107.
# print("\nExercise # 107")
# def my_func(x, **kwargs):
#     return x * max(kwargs.values())
# result = my_func(10, val1 = 10, val2 = 15, val3 = 20, val4 = 25, val5 = 30)
# print(result)

# # 108.
# print("\nExercise # 108")
# var = 10
# def my_func(x):
#     print( x * var) 
# my_func(20)

# # 109. 
# print("\nExercise # 109")
# var = 10
# def my_func(x):
#     var = 5
#     print( x * var) 
# my_func(20)

# # 110.
# print("\nExercise # 110")
# var = 12
# def my_func(x):
#     print(x * var)
# my_func(10)

# # 111.
# print("\nExercise # 111")
# var = 8
# def my_func(x):
#     global var
#     print(x * var)
#     var = 12
# my_func(10)

# # 112.
# print("\nExercise # 112")
# from math import pi
# print("%.4f" % pi)

# # 113.
# print("\nExercise # 113")
# f = open("test.txt", "r")
# print(f.read())

# # 114.
# print("\nExercise # 114")
# f = open("test.txt", "r")
# print(f.readlines())

# # 115. 
# print("\nExercise # 115")
# f = open("test sql.txt", "r")
# f.read()
# f.seek(0)
# print(f.read())

# # 116. 
# print("\nExercise # 116")
# f = open("test.txt", "r")
# f.read(5)
# print(f.tell())

# # 117. 
# print("\nExercise # 117")
# f = open("test.txt", "r")
# f.read(5)
# print(f.mode())

# # 118. 
# 
# f = open("test.txt", "a+")
# priprint("\nExercise # 118")nt(f.mode())

# # 119.
# print("\nExercise # 119")
# f=open("test.txt", "w")
# f.write("python")
# f.close()
# f=open("test.txt", "r")
# print(f.read())

# #120.
# print("\nExercise # 120")
# f=open("test.txt", "w")
# f.writelines(['python',' ','and',' ', 'java'])
# f.close()
# f=open("test.txt", "r")
# print(f.read())

# # 121.
# print("\nExercise # 121")
# with open("test.txt", "w") as f:
#     f.write('python')
# f=open("test.txt", "r")
# print(f.read())

# #122.
print("\nExercise # 122")
with open("test.txt", "w")as f:
    f.write('python')
f=open("test.txt", "r+")
f.truncate()
f=open("test.txt", "r")
print(f.read())
