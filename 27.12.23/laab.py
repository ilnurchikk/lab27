

# a = 13335
# print(a)
# print(str(a))
# print(len(str(a)))
#
#
#
# for i  in  str(a): #hello
#     print(i)
#
# print(str(a).count("3"))


##################################1
#while True:
#    print("Это приложение определяет кол-во цифр средне арефметическое сколько 0")
#    start = input("Если хотите работать с приложение  нажмите:start")
#
#    if start =="start":
#
#        b = 0
#        c = 1
#
#        a = int(input('введите число:'))
#        for i in str(a):
#           b +=int(i)
#        c = b/len(str(a))
#
#
#        print(len(str(a)))
#        print("Сумма:", b)
#        print("сумма средн. арефметич:", c)
#        print("Количество нулей:")
#        print(str(a).count("0"))
#
#    else:
#        print("приложение завершено")
#        break
###############################################2
#b = 8
#c = 8
#
#print("Это приложение делает шахматную доску")
#a = int(input('введите число:'))
#for i in range(b):
#    for j in range(c):
#        if (i + j) % 2 == 0:
#
#            print("*" * a, end="")
#        else:
#
#            print("_" * a, end="")
#    print()
###################################3
# import random
# print("Это приложение позволяет узнать как вы владеете табл умнож .")
# i = 3
# j = 0
# while j < i:
#
#     print("Это приложение определяет кол-во цифр средне арефметическое сколько 0")
#     x, y = random.randint(0,11), random.randint(0, 11)
#     a = int(input(f'введите ответ:{x} * {y} = '))
#     if a == (x * y):
#         print("вЕРНЫЙ ОТВЕТ")
#         j += 1
#     else:
#        print("НЕ ВЕРНЫЙ ОТВЕТ")
#        break
# print("Вы дали три правельных ответа")
########################4

a = int(input("ведите размер ромба"))
for i in range(a):
    print(" " *(a - i - 1) + "* " * (i + 1))
for i in range(a - 1, 0, -1):
    print(" " * (a - i) + "* " * i)
