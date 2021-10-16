import datetime
b=0
c=0
a=float(input())
if a>=30:
    while a>=30:
        a-=30
        b+=1
    if b>=20:
        while b>=20:
            b-=20
            c+=1
            print(a,b,c)






def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))