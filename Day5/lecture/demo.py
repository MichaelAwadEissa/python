var=lambda  x,y:x+y
print(var(1,2))
# lambda (x,y):body
# with  open('asd,t xt','r') as f:
#         f.write()


# trackname=input('enter track name')
#
# query=f'select * from track where name={trackname}'
# query=query.replace(';','\;')
# print(query)
# # from db import create
# class Track:
#     def __init__(self,_id,_name):
#         self.id=id
#         self.name=_name
# #
# class Trainee:
#     def __init__(self,id,name,trackobj):
#         self.id=id
#         self.name=name
#         self.__track=trackobj #fk represntaion as object of track
#     def settrack(self,newtrack  ):
#         self.__track=newtrack
#     def gettrack(self):
#         return self.__track
# #
# trck=Track(5,'da')
# create('track',(trck.id,trck.name))
# tr=Trainee(10,'sayed',trck)
# create('traineedata',(tr.id,tr.name,tr.track.id))

# class Car:
#     def __init__(self,model,color):
#         self.model=model
#         self.color=color
# class Human:
#     # normal reference of object human(prent)
#     # self reference to object of employee(child)
#     def __init__(self,_id=None,name=None,address=None,bdate=None,cars=None):
#         print('iam human const')
#         self.id=_id
#         self.name=name
#         self.address=address
#         self.bdate=bdate
#         self.cars=cars
#     def eat(self):#self human,employee
#         print('eat',self.id)
#
#     def sleep(self):
#         print('sleep')
#     def speek(self):
#         print('iam ',self.name)
#
# objcar=Car('bmw','black')
# objcar2=Car('bmw','red')
# l=[objcar,objcar2]
# objhuman=Human(1,'aya','fayoum','24-1-2000',l)
# print(objhuman.id)
# print(objhuman.cars[0].color)

# human own car


# class Hummal:
#     def __init__(self):
#         print('iam hummal constructor')
# class Employee(Human):
#     def __init__(self, _id, name, address, bdate,position,salary):
#         #calling constructor parent manuall
#         super(Employee,self).__init__(_id,name,address,bdate)
#         self._position=position
#         self.__salary=salary
#     #set
#     @property
#     def Salary(self):
#         return self.__salary
#     @Salary.setter
#     def Salary(self,newsalary):
#         if(newsalary>=5000 and newsalary <=10000):
#             self.__salary=newsalary
#         else:
#             raise ('invalid salary value')
#     # def setsalary(self,newsalary):
#     #     if(newsalary >=5000 and newsalary<=10000):
#     #         self.__salary=newsalary
#     #     else:
#     #         raise ('invalid salary value')
#     # def getsalaey(self):
#     #     return self.__salary
#
#     def speek(self):
#         super().speek()
#         print('my salary:',self.__salary,'my positition',self._position,self.id)
#         # print('iam ',self.name,'mysalary:',self.salary,'my positition',self.position)
#     def __str__(self):
#         return 'iam '+self.name
#     def __len__(self):
#         return len(self.name)#int(self.__salary/1000)
#
# objemp=Employee(1,'aya','fayoum','24-1-2000','sw eng',8000)
# #rule salary 5000:10000
# # objemp.setsalary(0)
# # print(objemp.__salary)
# # print(objemp.getsalaey())
# print(objemp.id)
# print(objemp._position)
# objemp.speek()
# objemp.Salary=5001
# print(objemp.Salary)
# print(objemp)
# print(len(objemp))
#
# # objemp.speek()
# # objhumna=Human(1,'mark','cairo','14-8-2024')
# # objhumna.speek()
# # print(objhumna.speek)
# # print(objemp.speek)
# # # class Sweng(Employee):
# #     def __init__(self, _id, name, address, bdate,position,salary,lang):
# #         super().__init__(_id,name,address,bdate,position,salary)
# #         self.language=lang
# # sweng is employee & sweng is human
# #
# # objhuman=Human(1,'aya','fayoum','24-1-2000')
# # objhuman.eat()
# # objemployee=Employee(2,'mark','cairo','10-8-2002','python developer',8000)
# # objemployee.eat()
# # objsw=Sweng(2,'mark','cairo','10-8-2002','python developer',8000,'python')
# # objsw.eat()
