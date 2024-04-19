import json

pict = """
MY SECOND SKRIPT

    /------/
   /      /|
  /      / |
 /------/  |
 |      |  /
 |      | /
 |______|/

I LOVE PYTHON
"""
print(pict)

with open('your_data.json', 'r') as f: 
    data = json.load(f)    

my_cars_stats = {}

for i in data:
    brand = i['brand']
    price = i['selling_price']
    year = i['year']
    fuel = i['fuel']

    if brand in my_cars_stats:
        my_cars_stats[brand]['count'] += 1
        my_cars_stats[brand]['mean_price'] += price
    else:
        my_cars_stats[brand] = {'count': 1, 'mean_price': price, 'old_year': year, 'new_year': year, 'fuel_count': {fuel: 1}}

    my_cars_stats[brand]['old_year'] = min(my_cars_stats[brand]['old_year'], year)
    my_cars_stats[brand]['new_year'] = max(my_cars_stats[brand]['new_year'], year)

    if 'fuel_count' in my_cars_stats[brand]:
        my_cars_stats[brand]['fuel_count'][fuel] = my_cars_stats[brand]['fuel_count'].get(fuel, 0) + 1
    else:
        my_cars_stats[brand]['fuel_count'] = {fuel: 1}

for i, j in my_cars_stats.items():
    j['mean_price'] /= j['count']

for i, j in my_cars_stats.items():
    moda_fuel = max(j['fuel_count'], key=j['fuel_count'].get, default=None)
    j['moda_fuel'] = moda_fuel

res = {}
for i, j in my_cars_stats.items():
    res[i] = {
        'count': j['count'],
        'mean_price': round(j['mean_price'], 1),
        'old_year': j['old_year'],
        'new_year': j['new_year'],
        'moda_fuel': j['moda_fuel']
    }

for i, j in res.items():
    print(f'Марка: {i}, Количество авто: {j["count"]}, Средняя стоимость: {j["mean_price"]}, '
          f'Год самого старого авто: {j["old_year"]}, Год самого нового авто: {j["new_year"]}, '
          f'Преобладающий тип топлива: {j["moda_fuel"]}')
    print()

with open('res_statistics.json', 'w') as file: 
    json.dump(res, file, indent=4)

print()

print('---------Script END Thanks for your attention------------')
