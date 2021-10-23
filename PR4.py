import datetime
a=float(input("Введіть свій вік , щоб дізнатися наскільки ви стара собака : "))
if a<0:
  print("Псина не вводи отрицательных чисел")
elif  a<=10.5 :
  b=a/5.25
  print("Ви собака , але ви виглядаєте на всі :",b,"собачих років")
if a>10.5:
  b=((a-10.5)/4)+2
  print(b)
  print("Ви собака , але ви виглядаєте на всі :",b,"собачих років")
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("DinGo-Ivan Nesterenko")





