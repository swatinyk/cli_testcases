# # print("deatorsmmmmm")
# # print("ddddddd")
# # def decor1(func):
# #     def inner(name):
# #             print("decor1",end=' ')
# #             func(name)
# #
# #             print("decor1", end=' ')
# #
# #     return inner
# #
# # def decor2(func):
# #     def inner(name):
# #         print("decor2",end=' ')
# #         func(name)
# #
# #         print("decor2", end=' ')
# #
# #     return inner
# #
# # @decor2
# # @decor1
# # def wish(name):
# #     print("hello",name,"gm",end='')
# #
# #
# # #
# # # wish("sunny")
# # # wish("bunny")
# #
# # def decor_1(func):
# #     def inner():
# #         num=func()
# #         return num*num
# #     return inner
# #
# # def decor_2(func):
# #     def inner():
# #         num=func()
# #         return num*num*num
# #     return inner
# #
# #
# # @decor_1
# # @decor_1
# # def num():
# #     return 10
# #
# # print(num())
#
# # import heapq
# # a=[3,2,1,5,6,4]
# # n=len(a)
# # k=3
# # p=[]
# # heapq.heapify(p)
# # for i in range(n):
# #     heapq.heappush(p,-1*a[i])
# #     print(p)
# #
# #     if len(p)>k:
# #         heapq.heappop(p)
# #         print(p)
# #
# # while(len(p) != 0):
# #         print(heapq.heappop(p)*-1, end=' ')
# # print()
#
#
#
# s='durga'
# n=len(s)
# # print(n)
# # i=0
# # while(i<n):
# #     print(s[i])
# #     i=i+1
# #
# # i=n-1
# # while(i>-1):
# #     print(s[i])
# #     i=i-1
#
# # i=-1
# # while(i>=-n):
# #     print(s[i])
# #     i = i - 1
#
# # s='mississippi'
# # d={}
# # k=[]
# # for i in s:
# #     if i in d:
# #         d[i]+=1
# #     else:
# #         d[i]=1
# #
# # print(d)
# #
# # for k,v in d.items():
# #     if d[k]>1:
# #         print(k,v)
#
# # for i in s:
# #     if i not in k:
# #         k.append(i)
# # print(k)
#
#
# # s='Durga Software'
# #
# # p=s.split()
# # print(p)
# # l=[]
# # for i in p[::-1]:
# #     print(i[::-1],end=' ')
# #     # l.append(i[::-1])
# # print(l,end='')
#
# # s='Durga Software solutions'
# # p=s.split()
# # i=len(p)-1
# #
# # while(i>-1):
# #     print(p[i])
# #     i=i-1
#
#
# #
# # for i in p[::-1]:
# #     print(i[::-1],end=' ')
#
# s1='Ravi'
# s2='Teja'
# # i=0
# # while(i<len(s1)):
# #     print(s1[i])
# #     i=i+2
# # i=1
# # while(i<len(s1)):
# #     print(s1[i])
# #     i=i+2
# # s=s1+s2
# # print(s)
# # #
# # print(s[1::2]+s[::2])
#
# # s='az4b3c2'
# # previous=''
# # output=''
# #
# # for i in s:
# #     if i.isalpha():
# #         output=output+i
# #         previous=i
# #     else:
# #         output=output+previous*(int(i)-1)
# #
# # print(output)
#
# # s='a4k3c2'
# # op=''
# # prev=''
# # newchar=''
# # for i in s:
# #     if i.isalpha():
# #         op=op+i
# #         prev=i
# #     else:
# #         newchar=chr(ord(prev)+int(i))
# #         op=op+newchar
# #
# # print(op)
#
# # p1='Ravi'
# # p2='tejas'
# # i=j=0
# # op=''
# # while i<len(p1) or j<len(p2):
# #     if i<len(p1):
# #         op=op+p1[i]
# #     if j<len(p2):
# #         op=op+p2[j]
# #     i=i+1
# #     j=j+1
# #
# # print(op)
# #
# # l=['1','2','b','a','0']
# # l.sort()
# # print(l)
# #
# # s='durgasoftware'
# # v={'a','e','i','o','u'}
# # p=set(s)
# #
# # for i in v:
# #     if i in s:
# #         print(i)
#
# # print(p)
# # final=v.intersection(p)
# # print(final)
#
# a=['id,name,age,quantity,address,pin,roll,contact','1,nitin,10,20,aaa,111,123,1234','2,abc,30,40,bbb,222,456,0000',
#    '3,xyz,30,80,cccc,43434,5555,9999999']
# l=[]
# p=[]
# for i in a:
#     l.append(i.split(','))
#
# for j in range(1,len(l)):
#     i=0  #this will take care of adding keys and values irrespective of length of keys in a dictionary
#     d={}
#     while(i<len(l[0])):
#         d[l[0][i]]=l[j][i]
#         i=i+1
#     p.append(d)
#
# print('final output in json format......',p)
#
#
# s='durga software'
# x=s.split()
# l=[]
# for i in x[::-1]:
#     l.append(i)
#
# print(' '.join(l))


#
#
#
#
#
#
# l=[1,4,2,1,5,3,4,8,2,8,4,1,2,5,2,1,1]
# d={}
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
#
# print(d)
# p = sorted(d.items(),key=lambda x:x[1])
# print(p)
# for k,v in d.items():
#     if p[0]==v or p[5]==v:
#         print(k)


#
# class Abc:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def summ(self):
#         p=self.a+self.b
#         print(p)
#
# s=Abc(2,3)
# s.summ()

#
# l=[5,3,2,7,9]
# p=[3,1,8,7,4]
#
# m=[]
# import heapq
# heapq.heapify(m)
# i,j=0,0
# while (i<len(l) or j<len(p)):
#     if i<len(l):
#         heapq.heappush(m,l[i])
#     if j<len(p):
#         heapq.heappush(m,p[j])
#     i=i+1
#     j=j+1
#
# for i in range(len(l)+len(p)):
#     s=heapq.heappop(m)
#     print(s)






# n=[]
# l.extend(p)
# l.sort()
# print(l)


#
# def mygen(n):
#     for i in range(n):
#         yield i*i*i
#
#
# s=mygen(3)
# print(s)
#
# for i in s:
# #     print(i)
#
# s='Test@Gmail' #Taei@Glmst
# p=list(s)
# d={}
# l=[]
# for i in p:
#     if i.islower() :
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
# print(d)
#
# a=sorted(d.keys())
# print(a)
# j = 0
#
# for i in range(len(p)):
#     if p[i].islower():
#         p.pop(i)
#         p.insert(i,a[j])
#         j=j+1
#
# print(''.join(p))


import paramiko
import psutil
import ast
#
client=paramiko.SSHClient()
# client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname='127.0.0.1', port=2222,username='swati',password='SP@gslab')
key_file=paramiko.RSAKey.from_private_key_file('/home/gslab/.ssh/id_rsa')
client.connect(hostname='127.0.0.1',port=2222,username='swati',pkey=key_file)
stdin,stdout,stderr=client.exec_command('free -m')
res = stdout.read()
print(res)
s=res.split()
print(s[7:10:2])
# if s[-1].decode('utf-8') !=10:
#     print('uuu')

# stdin,stdout,stderr=client.exec_command('python main.py')
# print(repr(stdout))
# print(stdout.read())
# print("\n")
# res = stdout.read()
# print('resssss',res.decode('utf-8'))




