n=list(input("Введите числа ").split())#создание списка и ввод чисел для списка
x=0#начало подсчета 
for i in n:#цикл для подбора чисел из списка
    if int(i)>10:#условие: если число больше 10
        x+=1#прибавление в счетчик
print("Количество чисел больше 10: ", x)#вывод количества чисел больше 10
