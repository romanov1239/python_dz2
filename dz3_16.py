# ; Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# ; Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# ; В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите размер массива: "))  
arr = []  
for i in range(n):
    num = int(input(f"Введите {i+1}-е число: "))
    arr.append(num)
x = int(input("Введите искомое число: "))  
print("Массив: ", arr)
count = 0
for i in range(n):
    if arr[i] == x:
        count += 1

print(f"Искомое число встречается {count} раз(а) ")