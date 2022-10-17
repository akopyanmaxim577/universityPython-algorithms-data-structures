
#імпорт модуля Random для генерування випадкових чисел у масиві
from random import *
#Користовач вводить число для цілочисельного квадратного масиву
n = int(input('Numb:'));
#Пустий масив
arr = [];
# блок коду який створює двовимірний масив,заповнює випадковими числами й форматує його
for i in range(n):
    arr.append([1]*n)
for Row in range(n):
    for Col in range(n):
        arr[Row][Col] = randint(1, 9)
for Row in range(n):
    for Col in range(n):
        print("{0:02}".format(arr[Row][Col]), end=" ");
    print();
#Обчислення сліду двомірного масиву
sum = 0;
for Row in range (n):
    sum = sum + arr[Row][Row];
print('sum:',sum);
#Блок коду для ділення непарних рядків на слід масива
print('Змінені непарні рядки');
for Row in range(n):
    if Row == 1 :
        continue;
    else:
        for Col in range(n):
            arr [Row][Col] = round(arr[Row][Col] / sum, 3);

            print("{0:02}".format(arr[Row][Col]), end=" ");
        print();
#Пустий одномірний масив
arr2 = [];
#Заповнення масиву елементами головноі діагоналі
for i in range(n):
    arr2.append(arr[i][i]);
#Заповнення масиву елементами побічноі діагоналі
for i in range(n):
        arr2.append(arr[i][n-1-i]);
#Вивід масиву
print(arr2);
#Результат:
#Numb:3
#05 03 04
#04 08 07
#07 01 08
#sum: 21
#Змінені непарні рядки
#0.238 0.143 0.19
#0.333 0.048 0.381
#Вивід одномірного масиву
#[0.238, 8, 0.381, 0.19, 8, 0.333]
#Висновок: я розробив программу яка рахує слід двомірного масиву,ділить елементи непарних рядків на слід,заповнює
#елементами головноі та побічних діагоналей двомірного масиву в одновимірний масив та виводить на єкран
