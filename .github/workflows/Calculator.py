def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Оберіть операцію:\n 1)Додавання \n 2)Віднімання \n 3)Множення \n 4)Ділення")
ch=int(input("Ваш вибір: "))
x=float(input('Ваше перше число: '))
y=float(input('Ваше друге число: '))
if ch ==1:
    print("Результат: {} + {} = {}".format(x,y,add(x,y)))
elif ch ==2:
    print("Результат: {} - {} = {}".format(x,y,subtract(x,y)))
elif ch==3:
    print("Результат: {} * {} = {}".format(x,y,multiply(x,y)))
elif ch==4:
    print("Результат: {} / {} = {}".format(x,y,divide(x,y)))
else:
    print("Не вірно вибрана операція.")
