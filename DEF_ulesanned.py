#ül 8
def XOR_cipher(text: str, võti: int) -> str:
    """Sõne kodeerimine ASCII võtmega (0-255)."""
    kodeeritud = ""
    for symbol in text:
        kodeeritud += chr(ord(symbol) ^ võti)
    return kodeeritud

def XOR_uncipher(kodeeritud_text: str, võti: int) -> str:
    """Sõne dekodeerimine ASCII võtmega (0-255)."""
    dekodeeritud = ""
    for symbol in kodeeritud_text:
        dekodeeritud += chr(ord(symbol) ^ võti) #непонял но списа!
    return dekodeeritud

 

#Ül7
import calendar

def date(day, month, year):
    try:
        return calendar.monthrange(year, month)[1] >= day > 0
    except ValueError:
        return False

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
print(date(day, month, year))
#Ül 6
def is_prime(a=randint(0,1000))->bool:
    """
    """
    print(a)
    v=True

    for i in range(2, a):
        if n % i == 0:
            v=False
    return v

n = int(input("Введите число от 0 до 1000: "))
print(is_prime(n))
#Ül 5 
def bank(a, years):
    for _ in range(years):
        a += a * 0.10
    return a

a = float(input("Введите сумму вклада (в евро): "))
years = int(input("Введите срок вклада (в годах): "))
print(f"Сумма на счете через {years} лет: {bank(a, years)} евро")
#Ül 4
def season(month):
    if month in [12, 1, 2]:
        return "talv"
    elif month in [3, 4, 5]:
        return "kevad"
    elif month in [6, 7, 8]:
        return "suvi"
    elif month in [9, 10, 11]:
#сделал так, потому что красивее
        return "sügis"
    else:
        return "Неверный номер месяца"

month = int(input("Введите номер месяца (от 1 до 12): "))
print(season(month))
#Ül3 
import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal

side = float(input("Введите сторону квадрата: "))
perimeter, area, diagonal = square(side)
print("Периметр:", perimeter)
print("Площадь:", area)
print("Диагональ:", diagonal)


#Ül2
def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input("Введите год: "))
print(is_year_leap(year))
#Ül1
def arithmetic(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Деление на ноль невозможно"
    else:
        return "Неизвестная операция"

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

result = arithmetic(a, b, op)
print("Результат:", result)



