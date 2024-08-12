# dbpath='fayoum'
# def getrainees():
#     print('iam in filesdemo sctipt')

# from pkg1.filebaseddb import dbpath as alias1,gettrainees as alias2
# print(dbpath)
# getrainees()
# print(alias1)
# print(alias2('traineedb',1))


# dbpath='db2'
# from filebaseddb import dbpath as palpl ,gettrainees
# print(dbpath)
# print(palpl)
# print(gettrainees('traineedb',0))
# import filebaseddb
# print(filebaseddb.dbpath)
# print(filebaseddb.gettrainees('traineedb',1))

# print(gettrainees('traineedb'))
# print(gettrainees('traineedb',1))

# inserttrainee('traineedb',1,'aya','python')
# inserttrainee('traineedb','2','mark','python')

# # #read
# try:
#     # open
#     file=open('asd.txt','r')#open cusrsor at 0
#     for line in file:
#         print(line)
#     if(file.readable()):
#         trainees=file.readlines()
#         for trainee in trainees:
#             print(trainee.split(','))
#         # s=file.read(2)#move to position 2
#         # print(s)
#         # s=file.read()#move to end of string
#         # print(s)
#         # s=file.readline()#line1
#         # print(s)
#         # s = file.readline()#line2
#         # print(s)
#         # s = file.readline()#line3
#         # print(s)
#         # s = file.readline()#no lines to read
#         # print('-',s,'-')
#
#     # close
#     file.close()
#
# except:
#     print(sys.exc_info())
#
# #append

# try:
#     #open file in write mode
#     file=open('asd2.txt','a')#seek cusrsor to end or create file
#     if(file.writable()):
#         # print(type(file))
#         file.write('line4')
#         file.write('''line2
#         line3''')
#         l=['aya\n','mai','ali']
#         file.writelines(l)
#     #close stream
#     file.close()
#
# except:
#     print(sys.exc_info())
# # try:
# #     #open file in write mode
#     file=open('asd.txt','w')#clear or create file
#     if(file.writable()):
#         # print(type(file))
#         file.write('line4')
#         file.write('''line2
#         line3''')
#         l=['aya\n','mai','ali']
#         file.writelines(l)
#     #close stream
#     file.close()
#
# except:
#     print(sys.exc_info())