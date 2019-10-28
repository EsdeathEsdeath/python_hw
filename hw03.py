# ==================
# ДЗ №3: функции
# Дедлайн: 04 ноября 18:14
# Результат присылать на адрес nike64@gmail.com

# также прочитайте раздел "Функции" из книги "A byte of Python" (с.59)

# Задание: сделайте анализ возрастного состава группы студентов, используя функции.
# Помните, что а) у некоторых студентов отсутствуют данные по возрасту, б) возраст может быть задан диапазоном, например, 25-35. Поэтому не забывайте обрабатывать ошибки и исключения!

import csv

# помним, что в этот раз мы читаем не список списков, а список словарей!
# ключи в словаре для каждого студента называются по первой строчке из файла student_ages.csv: "Номер в списке", "Возраст"
ages_list = list()
with open('ages.csv', encoding="utf-8-sig") as csvfile:
    ages_dictreader = csv.DictReader(csvfile, delimiter=',')
    ages_list = list(ages_dictreader)

# подсказка: вот так мы можем получить данные из списка словарей
# именно так мы уже делали в коде лекции с квартирами
dict_val = {}
count = 0
for al in ages_list:
    count +=1
    dict_val[count] = al["Возраст"]
    print(f'"Номер в списке": {al["Номер в списке"]}, "Возраст": {al["Возраст"]}')

#print(dict_val)
# Задание 1: напишите функцию, которая разделяет выборку студентов на две части: меньше или равно указанного возраста и больше указанного возраста
# вернуться должна пара "Номер в списке, Возраст"
def filter_students_1(age):
    under_list = list()
    upper_list = list()
    unknownage_count = 0

    # TODO 1: напишите ваш код проверки.
    # не забудьте исключить студентов, у которых возраст не указан, и подсчитать их количество
    c = 0
    for k in dict_val:
        c += 1
        if dict_val[k] != '' and len(dict_val[k]) < 3:
            if int(dict_val[k]) > age:
                upper_list.append([c, dict_val[k]])
            else:
                under_list.append([c, dict_val[k]])
        else:
            unknownage_count += 1
    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию:
und_list, upp_list, unknwncount = filter_students_1(30)
# TODO 2: выведите результат:
#print(f'Список студентов старше: {upp_list}, младше: {und_list}, без указания/некорректный возраст кол-во: {unknwncount}')

# Задание 2: улучшите функцию filter_students_1
# напишите функцию, которая принимает переменное количество параметров, каждый из которых может быть необязательным:
# Список и пример передачи параметров: age=30, warn=True, show_average=True
# 1) warn=True (False) - параметр, указывающий, что делать со студентами, которые не указали возраст:
# если возраст не указали значительно большее количество студентов, чем указали, выводите дополнительно предупреждение, что выборка неточная
# 2) show_average=True (False) нужно ли подсчитать и отобразить средний возраст студента.

# все параметры передавайте как **kwargs, т.е. пару "название параметра - значение параметра"
def filter_students_2(**kwargs):
    under_list = list()
    upper_list = list()
    unknownage_count = 0
    fin_sum = 0

    # TODO 3: скопируйте сюда текст функции filter_students_1, которую вы написали ранее, и измените ее так, чтобы она работала с параметрами **kwargs
    c = 0
    for k in dict_val:
        c += 1
        if dict_val[k] != '' and len(dict_val[k]) < 3:
            if int(dict_val[k]) > kwargs.get("age"):
                upper_list.append([c, dict_val[k]])
            else:
                under_list.append([c, dict_val[k]])
        else:
            unknownage_count += 1
    # возвращаем результат из функции:
    # TODO 4: получите остальные два параметра по аналогии:
    warn_if_toomany = kwargs.get("warn")
    need_show_average = kwargs.get("show_average")

    # TODO 5: сделайте проверку. Если значение параметра warn, show_average = True, выполните соответствующую обработку. Например:
    if warn_if_toomany:
        if unknownage_count > (len(dict_val) - unknownage_count):
            print("Необходимо больше данных")
    if need_show_average:
        sum = 0
        med = (len(upp_list)+len(under_list))
        for age in upp_list:
            sum += int(age[1])
        for age in under_list:
            sum += int(age[1])
        fin_sum = (sum / med)
    else:
        fin_sum = "вычислять не нужно"
    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count, fin_sum


# вызываем функцию filter_students_2
und_list, upp_list, unknwncount, average = filter_students_2(age=30, warn=True, show_average=True)
print(f'Список студентов старше: {upp_list}, младше: {und_list}, без указания/некорректный возраст кол-во: {unknwncount}, среднее: {average}')
