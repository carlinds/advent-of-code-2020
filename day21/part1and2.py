import collections

def main():
    with open('foodlist.txt') as f:
        lines = f.readlines()

    allergen_map = collections.defaultdict(list)
    all_ingredients = []
    for line in lines:
        [ingredients, allergens] = line.split('(contains ')
        ingredients = ingredients.strip().split()
        allergens = allergens.strip()[:-1].split(', ')     
        all_ingredients.extend(ingredients)

        for a in allergens:
            allergen_map[a].append(ingredients)

    for a, ingredients in allergen_map.items():
        common = set.intersection(*map(set, ingredients))
        allergen_map[a] = list(common)

    def remove_ingredient(ingredient, exclude_allergen):
        removed = False
        for allergen in allergen_map:
            if allergen != exclude_allergen:
                if ingredient in allergen_map[allergen]:
                    allergen_map[allergen].remove(ingredient)
                    removed = True
        return removed

    def solve_allergens():
        for allergen, possible_ingredients in allergen_map.items():
            if len(possible_ingredients) == 1:
                if remove_ingredient(possible_ingredients[0], allergen):
                    solve_allergens()

    solve_allergens()
    allergen_free = all_ingredients[:]
    for _, [i] in allergen_map.items():
        allergen_free = list(filter(lambda j: j != i, allergen_free))

    dangerous_list = ''
    for a in sorted(allergen_map.keys()):
        dangerous_list += allergen_map[a][0] + ','

    print('Part 1: ', len(allergen_free))
    print('Part 2: ', dangerous_list[:-1])
    return 0


if __name__ == "__main__":
    main()