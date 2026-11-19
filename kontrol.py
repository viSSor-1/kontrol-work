
# def enter_numbers():
#     n = int(input())
#     if n not in range(1,801):
#         print("Ошибка. Число должно быть в диапазоне от 1 до 800")
#     #Создаем список из введенных N чисел в заданном диапазоне
#     nums = list(map(int, input().split()))
#     #Обработка ошибок
#     if (len(nums) != n) or any(x for x in nums if x not in range(-1000,1001)) : 
#         print("Ошибка. Список длиной не N чисел или число вышло за границы от -1000 до 1000. Проверьте введенное")
#     else:
#         print(f'Изначальный список: {nums}')
#     return nums
   
# def new_list(nums):
#     #Создаем новый список согласно условиям 
#     nums2 = nums
#     for i in range(len(nums)):
#         if nums[i]%2==0 and nums[i]>0 and nums[i]!=0: 
#             nums2[i]=(nums[i]**2)
#         elif abs(nums[i])%2!=0 and nums[i]!=0:
#             nums2[i]=nums[i]*3
#         elif nums[i]<0:
#             nums2[i]=abs(nums[i])
#     print(f'Список после преобразований по условиям: {nums2}')
#     return nums2

# def delete_5(nums2):
#     #Удаляем все числа, кратные 5
#     nums2_no5 = [x for x in nums2 if x%5!=0]
#     print(f'Список без чисел, кратных 5: {nums2_no5}')
#     return nums2_no5
    
# def count(nums2_no5):
#     #Вычисляем сумму, среднее, минимум, максимум, колво элементов, которые больше среднего 
#     sums = sum(nums2_no5)
#     sr = sums/len(nums2_no5)
#     print(f'Сумма чисел: {sum(nums2_no5)}')
#     print(f'Среднее: {(sums/len(nums2_no5)):.2f}')
#     print(f'Минимум: {min(nums2_no5)}')
#     print(f'Максимум: {max(nums2_no5)}')
#     print(f'Кол-во чисел, больше среднего: {sum(1 for c in nums2_no5 if c>sr)}')

# # #Сортировка оставшегося списка
# # print(sorted(nums2_no5))

# # max_2=nums2_no5[-2]

# def spisok():
#     nums=enter_numbers()
#     nums2=new_list(nums)
#     nums2_no5=delete_5(nums2)
#     try: 
#         count(nums2_no5)
#         print(f'Отсортированный список по возрастанию: {sorted(nums2_no5)}')
#     except:
#         print('Список пуст. Расчеты невозможны')
#     try: 
#         print(f'Второй максимум: {sorted(nums2_no5)[-2]}')
#     except:
#         pass 
# spisok()

    
    

# import re

# def text():
#     text= input("Введите текст: ")

#     #Разбиваем текст на предложения
#     sentences = [x.strip() for x in re.split(r'[.!?]+', text) if x.strip()]
#     print('Предложения: ')
#     for i, sentences in enumerate(sentences, 1):
#         print(f'Предложение {i}: {sentences}')

#     # Подсчитваем частоту каждой гласной русской и англ буквы и выводим в виде таблицы 
#     glas = "аеёиоуыэюяaeiou"
#     text_lower = text.lower()
#     print('Частота гласных: ')
#     print(f'{'Гласная':<10} | {'Количество':<10}')
#     print('-' * 23)
#     for i in glas:
#         count = text_lower.count(i)
#         if count>0:
#             print(f'{i:<10} | {count:<10}')

#     # Найдем все слова длиной больше 6 символов в алфавитном порядке без дубликатов
#     words= text.split()
#     word_6 = list()
#     for w in words:
#         clean_words= w.strip('.,!?:;-()').lower()
#         if len(clean_words) >6 and clean_words not in word_6:
#             word_6.append(clean_words)
#     word_6=sorted(word_6)
#     print('Слова больще, чем из 6 символов:', ', '.join(word_6))

#     #Проверяем наличие чисел, извлекаем и находим сумму
#     num_strings = re.findall(r'[+-]?\d+(?:\.\d+)?', text)
#     numbers = [float(n) for n in num_strings]
#     if numbers:
#         print(f'Найденные числа в тексте: {numbers}')
#         print(f'Сумма чисел в тексте: {sum(numbers)}')
#     else:
#         print('Чисел в тексте не найдено')

#     #Заменяем пробелы на "_" и меняем регистр букв по выбору 
#     print("1 — заменить пробелы на '_' и перевести заглавные в строчные")
#     print("2 — заменить пробелы на '_' и перевести строчные в заглавные")
#     choice = input("Выберите режим (1 или 2): ")

#     text2 = text.replace(" ", "_")
#     if choice == "1":
#         text2 = text2.lower()
#     elif choice == "2":
#         text2 = text2.upper()
#     else:
#         print('Неверный выбор, выполнена только замена пробелов.')
#     print(f'Результат: {text2}')

#     #Проверка айпи адреса
#     i = input("Введите строку для проверки на IPv4: ").strip()
#     parts = i.split(".")
#     valid_i = False

#     if len(parts) == 4:
#         valid_i = True
#         for part in parts:
#             # Проверяем, что часть состоит из цифр, в диапазоне 0..255 и без ведущих нулей (кроме самого "0")
#             if not part.isdigit() or not (0 <= int(part) <= 255) or (len(part) > 1 and part.startswith("0")):
#                 valid_i = False
#                 break

#     if valid_i:
#         print(f"Строка '{i}' является корректным IPv4-адресом.")
#     else:
#         print(f"Строка '{i}' не является корректным IPv4-адресом.")


# text()

def run_catalog():
    items = [
        ('Ноутбук ASUS', 'Электроника', 75000, 3),
        ('Мышь Logitech', 'Электроника', 2500, 15),
        ('Книга «Python', 'Книги', 1200, 8),
        ('Клавиатура', 'Электроника', 4500, 4),
        ('Тетрадь', 'Канцтовары', 80, 50),
        ('Монитор', 'Электроника', 32000, 2),
        ('Ручка', 'Канцтовары', 45, 100),
    ]

    # Общая стоимость всех товаров 
    total = sum(price * qty for x, y, price, qty in items)
    print(f'Общая стоимость всех товаров: {total} руб')
    print('')

    # Самый дорогой и самый дешёвый товар 
    top = max(items, key=lambda x: x[2])
    low = min(items, key=lambda x: x[2])
    print(f'Самый дорогой: {top[0]} ({top[2]} руб.)')
    print(f'Самый дешёвый: {low[0]} ({low[2]} руб.)')
    print(' ')

    # Группировка по категориям: количество позиций, суммарная стоимость, средняя цена
    cats = {}
    for name, cat, price, qty in items:
        if cat not in cats:
            cats[cat] = {"count": 0, "sum_val": 0, "sr_price": 0}
        cats[cat]["count"] += 1
        cats[cat]["sum_val"] += price * qty
        cats[cat]["sr_price"] += price

    for cat, data in cats.items():
        avg_price = data["sr_price"] / data["count"]
        print(f'{cat}: позиций — {data['count']}, суммарная стоимость — {data['sum_val']} руб., средняя цена — {avg_price:.2f} руб.')
    print(' ')

    # Сортировка по цене (убывание), при равенстве — по названию (возрастание)
    sorted_items = sorted(items, key=lambda x: (-x[2], x[0]))
    print('Товары по убыванию цены:')
    for name, cat, price, qty in sorted_items:
        print(f'{name} — {price} руб. ({cat}, {qty} шт.)')
    print(' ')

    # Товары, у которых количество на складе меньше 5 («заканчиваются»)
    low_tov = [x for x in items if x[3] < 5]
    print('Заканчиваются (меньше 5 шт.):')
    for name, cat, price, qty in low_tov:
        print(f'{name} — осталось {qty} шт.')
    print(' ')

    #  Таблица всех товаров 
    print('Полный каталог товаров:')
    print(f'{'Название':<18} | {'Категория':<14} | {'Цена':<8} | {'Остаток':<8}')
    print("-" * 57)
    for name, cat, price, qty in items:
        print(f'{name:<18} | {cat:<14} | {price:<8} | {qty:<8}')


run_catalog()