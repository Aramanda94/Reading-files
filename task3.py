# Пример открытиия файла
# Шаг 1 - Открыть файл
file = open('menu.txt',encoding='utf8')
print(type(file), "\n")

# Шаг 2 - Выполнить работу (пока читаем файл)
while True:
    line = file.readline()
    if not line:
        break
    print(line.strip())
print(type(line), "\n")

# Шаг 3 - Закрыть файл
file.close()

# Задача №1
def open_file():
    ST_TITLE = 1
    ST_COUNT = 2
    ST_INGREDIENTS = 3

    cook_book = {}
    state = ST_TITLE
    with open("menu.txt", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if state == ST_TITLE:
                title = line
                cook_book[title] = []
                state = ST_COUNT
            elif state == ST_COUNT:
                count = int(line)
                state = ST_INGREDIENTS
            else: # if state == ST_INGREDIENTS:
                data = [x.strip() for x in line.split('|')]
                data[1] = int(data[1])
                cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
                count -= 1
                if count == 0:
                    state = ST_TITLE

    print(cook_book)
    return

open_file()

# Задача №2
def dict_collector(file_path):
    with open(file_path, 'r', encoding='utf8') as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # - временный словарь с ингридиетом
                ingridient = file_work.readline().strip().split(' | ') # - вот так перемещаемся по файлу
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline()

    return(menu)

dict_collector('menu.txt')

def get_shop_list_by_dishes(dishes, persons_int):

    menu = dict_collector('menu.txt')
    print('Наше меню выглядит вот так:')
    print(menu)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):

                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons_int})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item
                else:
                    shopping_list.update(items_list)
        print(f"Для приготовления блюд на {persons_int} человек  нам необходимо купить:")
        print(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4)

# Задача №3
import os


def create_combined_list(directory):
    file_list = os.listdir(directory)
    combined_list = []

    for file in file_list:
        with open(directory + "/" + file) as cur_file:
            combined_list.append([file, 0, []])
            for line in cur_file:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1

    return sorted(combined_list, key=lambda x: x[2], reverse=True)


def create_file_from_directory(directory, filename):
    with open(filename + '.txt', 'w+') as newfile:
        for file in create_combined_list(directory):
            newfile.write(f'File name: {file[0]}\n')
            newfile.write(f'Length: {file[1]} string(s)\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('-------------------\n')

create_file_from_directory('text', 'my_text')