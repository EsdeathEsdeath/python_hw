# ==================
# ДЗ №1: простые типы данных, изменяемые и неизменяемые типы, работа со строками, списки

# Задание: сделайте анализ выгрузки квартир с ЦИАН:

# 1) Измените структуру данных, используемую для хранения данных о квартире. Сейчас квартира = список. Сделайте вместо этого квартира = словарь следующего вида: flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}. В задании используйте поля: идентификатор квартиры на ЦИАН, количество комнат, тип (новостройка или вторичка), стоимость

# 2) Подсчитайте количество новостроек, расположенных у каждого из метро

import csv
flats_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)
print(flats_list)
header = flats_list.pop(0)
# создаем словарь с информацией о квартирах
subway_dict = {}
for flat in flats_list:
	subway = flat[3].replace("м.", "")
	subway_dict.setdefault(subway, [])
# TODO 1: добавьте код, который генерирует новую структуру данных с информацией о квартире - словарь вместо списка
	flat_info = {"id": int(flat[0]), "rooms": flat[1], "type": flat[2], "price": int(flat[11])}
	#print(flat_info)
	# subway_dict[subway].append(flat_info)

# TODO 2: подсчитайте и выведите на печать количество новостроек, расположенных рядом с каждым из метро. Используйте вариант прохода по словарю, который вам больше нравится

subways_dict = {}
for flat in flats_list:
	subways = flat[3]
	subways_dict.setdefault(subways, [])
for k in subways_dict:
	i = 0
	for flat in flats_list:
		if k == flat[3] and flat[2] == 'новостройка':
			i += 1
	print("У метро", k, i, "новостроек")

