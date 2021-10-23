import datetime
x=float(input())
n=int(input())
if n>0 :
    res=1-2*x/2+4*x/4-+(-1)*n*x*2*n/2*n
    print(res)
elif n<=0 :
    print("Введіть число >0")



def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))