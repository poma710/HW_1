""" Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника). """

N = int(input ('ВВедите количество кубиков длины шоколадки: '))
M = int(input ('ВВедите количество кубиков ширины шоколадки: '))
K = int(input ('ВВедите количество кубиков, которые надо отломить от шоколадки: '))
if K == N or M == K:
 print("Получилось!!!")
elif K % N == 0 and K // N <= M or K % M == 0 and K // M<= N:
 print("Получилось!!!")

else:
 print("Что-то пошло не так!!!")
    

