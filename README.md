# cars-statistics
Полученные данные, хранящиеся в переменной data, имеют следующую структуру:
[
  {'brand': 'Ford',
    'fuel': 'Diesel',
    'year': 2012,
    'selling_price': 280000},

  {'brand': 'Ford',
    'fuel': 'Diesel',
    'year': 2011,
    'selling_price': 170000},
 ....
]
Кждый словарь - это отдельный автомобиль, продаваемый на вторичном рынке где-то в Индии. Для каждого автомобиля нам даны такие признаки:
brand - Марка авто
fuel - Тип топлива
year - Год выпуска
selling_price - Стоимость в Рупиях (вероятнее всего)
Task
Собственно задача. Нам бы очень хотелось сделать некоторое обобщение рынка на основании вашей выборки. Cоберите словарь по этой форме:
{
    "seed": 20,
    "BMW": {
        "count": 20,
        "mean_price": 4177750.0,
        "old_year": 2010,
        "new_year": 2019,
        "moda_fuel": "Diesel"
    },
    "Ford": {
        "count": 58,
        "mean_price": 506137.9,
        "old_year": 2003,
        "new_year": 2019,
        "moda_fuel": "Diesel"
    },
    "Volkswagen": {
        "count": 22,
        "mean_price": 479409.1,
        "old_year": 2010,
        "new_year": 2018,
        "moda_fuel": "Diesel"
    }
}
По глобальным ключам словарь содержит:
seed - ваш идентификатор (число, которое вы указали при генерации выборки)
Все Марки (уникальные) которые встречаются в данных. В вашей выборке может быть иной набор марок авто. Данный пример описывает выборку, которая представлена тремя марками.
Каждой марке авто в качестве ключа мы ставим в соответствие словарь, который содержит:
count - Количество авто данной марки
mean_price - Средняя стоимость автомобилей данной марки (Округлите до целого числа)
old_year - Год самого старого авто данной марки
new_year - Год самого нового авто данной марки
moda_fuel - Какой тип топлива преобладает для авто данной марки. Например если больше дизельных авто, то тут будет значение "Diesel". Если Не получится выявить самый популярный тип топлива, то этому ключу присвойте значение None.
Если какой-либо из критериев вам вычислить не удастся, то на место значения поставте также None.
