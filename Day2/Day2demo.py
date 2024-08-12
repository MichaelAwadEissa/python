# def factorial(num):
#     # print(num)
#     if(num==0):
#         return 1
#     else:
#         # print(num)
#         return num*factorial(num-1)
    

# print(factorial(5))
# def mysum(n1,n2):    
   
#     print(n1+n2)


# #connect to db select two numbers
# mysum(2,3)

# n1=int(input('enter num1'))
# n2=int(input('enter num2'))
# mysum(n1,n2)


# # # formate(key=value)
# print('{id}'.format(id=10))
# def fun(**arg):
#     print(arg,type(arg))
# d={'id':10,'name':'aya'}
# fun(key1=10,key2='one')#packing pairs(key=value) into dict
# fun(k=d)#{'k':{}}
# # # min(1,2,3......n)
# # def fun(*arg):
# #     print(arg,type(arg))
# # t=(1,2,3,4,5,6)
# # fun(1,2,3)#packing--->(1,2,3)


# range(1,2,1)
# range(1,2)
# range(3)




# print('default arg')
# def fun(n2,n1=10):
#     print(n1+n2)
# # fun()
# fun(30)
# fun(30,30)



# def sayhello():
#     print('hi no arg')

# def sayhello(trackname):
#     print('good morning ',trackname)
# sayhello('')
# num=10
# num='one'
# sayhello('python')
# sayhello('php')
# sayhello('sys admin')
# #define function
# #two arg , return value
# def dosum(n1,n2):
#     return (n1+n2)
#     print('hi function')
    

# #calling
# res=dosum(3,4)
# print(res)
# print(dosum('one','two'))
# dosum(6,7)


# d={'k'+str(n):n for n in range(1,10)}
# print(d)
# l=[]
# for n in range(1,10):
#     if(n%2==0):
#         l.append(n)
# # l2=[valueappend loop  poptionalif]
# #{key:value for  ifstatmentoptionsla}
# l2=[n for n in range(1,10)  if(n%2==0)]
# print(l)
# print(l2)
# l=['aya','ali','mark']
# for name in l:
#     if(name=='aya'):
#         print('aya found')
# print('founded') if 'aya' in l else print('not found')
# for n in range(0,11,2):
#     print(n)
# r=range(1,5)#
# print(type(r))
# l=['aya','ali','mark']
# for val in l:
#     if(val=='ali'):
#         continue
#     print(val)
# else:
#     #only for loop all loops done
#     print('for finished')

#
# for index,name in enumerate(l):#[(index,value),.....()]
#     print(index,name)

# range([start=0],end,[step=1])
# r=range(13)
# for value in r:
#     if(value==6):
#         break
#     print(value)
#collection of values diff datatypes (pairs (key,value)
# #key must be unique
# t=4,5
# x,y=t
# print(x,y)
# trainee={'id':1,#--->add id (1)
#          'id':100,#--->update valuen of key id====>100
#          'name':'aya',
#          'track':'python',
#          'courselist':['bash','python'],
#          'grades':(90,100),
#          'cgrades':{'python':(100,),
#                     'bash':(90,)}}
# d={'id':1000,'dept':'os'}
# # trainee.update(d)
# print(trainee+d)#4+3
# print(trainee*3)
# for key,value in trainee.items():
#     print(key,value)
# for key in trainee:
#     print(key,trainee[key])
# trainee['palpalp']='plapal' #if key exsist--->update
# trainee['id']=100#update
#if not found i will add
# print(trainee)
# print(trainee['cgrades'])
# print(trainee)
# trainees={}
# print(type(trainees))
# trainee=[1,'aya','python','fayoum']
# trainee2=[2,'ali','python','smart']
# trainees=[trainee,trainee2]
# print(trainees[1])
#set collection of values --->different data type int,float,bool,str,[],(),{}
# s={1,1.1,True,'palpslpl',False,0,1}#remove duplicated values
# print(len(s))
# print(s[0])
# print(type(s))
# print(s)
# print(s)
# print(s)
# print(s)
# print(s)
# print(s)
#tuple collection of values --->different data type int,float,bool,str,[],(),{}
#immutable list
#collection of values sperated with ,
# t=[],1.1,1,True,'one',(),[],{}
# t=1,3.3,[]
# t[3].append(4)
#
# # t[0]=5.5
# t[0]=[4,5]
# print(t,type(t))
#list collection of values --->different data type int,float,bool,str,[],(),{}
#index,slicing,loop
# varlist=[1,5,1.1,10]
# varlist.reverse()
# # varlist.reverse()
# # varlist.sort()
# l2=[3,4]
# print(varlist+l2)
# print(varlist)
# print(l2)
# l2.extend(varlist)
# print(l2)
# # print(varlist.index(1.1))

# varlist[0]=None
# varlist.remove(True)#if(item==True)
# varlist.pop(3)
# varlist.pop()
# varlist.append('plplpalp')
# varlist.insert(1,'ali')
# print(varlist)
# varlist[7]='palpal'
#+,*
# l2=[3,4]
# print(varlist*3)
# print(l2+varlist)#[3,4,1,....{}]
# print(varlist[0::])
# print(varlist[1:3:])
# print(varlist[::-1])
# for val in varlist:
# print(val,type(val))
# varlist[0]='palplap';
# print(varlist)
# print(type(varlist))
# print(varlist,varlist[0])
# print(len(varlist))#,varlist[7])