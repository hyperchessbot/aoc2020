from collections import defaultdict
from functools import reduce

foods = defaultdict(list)
all_ingredients = set()
confirmed_allergens = {}
recipes = []

with open('02.txt', 'r') as f:
    for line in f.readlines():
        ingredients, allergens = line.strip().split(' (contains ')
        ingredients = set(ingredients.split())
        recipes.append(ingredients)
        all_ingredients.update(ingredients)
        for allergen in allergens[:-1].split():
            foods[allergen.replace(',', '').strip()].append(ingredients)

while confirmed_allergens.keys() != foods.keys():
    for allergen in foods.keys():
        if allergen in confirmed_allergens:
            continue
        filter_1 = reduce(lambda a, b: a & b, foods[allergen])
        if len(filter_1) == 1:
            confirmed_allergens[allergen] = filter_1.pop()
        else:
            filter_2 = filter_1 - set(confirmed_allergens.values())
            if len(filter_2) == 1:
                confirmed_allergens[allergen] = filter_2.pop()
allergen_set = set(confirmed_allergens.values())
total = 0
for meal in recipes:
    total += len(meal-allergen_set)

print('Part 1:', total)

print('Part 2:', ','.join([confirmed_allergens[x] for x in sorted(confirmed_allergens.keys())]))
