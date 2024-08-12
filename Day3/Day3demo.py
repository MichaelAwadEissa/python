# import  sys
# try:
    # 5/0#zero devision
    # open('asd.txt', 'r')
#     num1 = int(input('enter num1'))
#     num1=int(input('enter num1'))
# except ZeroDivisionError:
#     print('القسمه ع صفر')
# except FileNotFoundError:
#     print('ملف لا يوجد')
# except:#general exept
#     # print('error happend')
#     print(sys.exc_info()[1])
# else:
#     print('else ---try is ok')
# finally:
#     print('finally intpertaing if try run ok or enter excpt')
# print('after enter except')
# #handel user maked by user
# num1=(input('enter num1'))
# if(num1.isdecimal()):
#     num1=int(num1)
#     num2 = eval(input('enter num2'))
#     print(num1 + num2)  # str+str  490
#
# else:
#     print('num1 must be numbers')
# l=eval(input('enter list of names'))
# # l=l.replace('[','').replace(']','').replace("'",'').replace('"','')
# # l=l.split(',')
# print(type(l),l)
# #global scope
# name='python'
# #local scope from start function to end function
# #define function
# def fun():
#      name='func'
#     def fun2():
#         global name   #fun2  accsess global var name & modified
#         # nonlocal  name #fun2 accceses local var for edit and read
#         print(name) #acccsess name in fun for read
#         name='changed by fun2'
#     fun2()
#     print(name)#interpreting ?????
# fun()#func
# print(name)#python