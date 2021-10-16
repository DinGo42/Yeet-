import datetime
a = 0
b = 0
while  True:
    age = input("Введіть вік відвідувача: ")
    if age == "":
      
        break
    age = int(age)
    b += 1
    if age < 3:
        a += 0
    elif age < 12:
        a += 16
    elif age > 60:
        a += 18
    elif age >= 12 and age <= 60:
        a += 25


if b > 10:
    a = (10*a)/100
    print("Загальна вартість: ", "%.2f" % a)
else:
    print("Загальна вартість: ", "%.2f" % a)


def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("DinGo-Ivan Nesterenko")
