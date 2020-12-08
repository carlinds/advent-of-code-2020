def main():
    with open('bags.txt') as f:
        bags = f.readlines()

    bag_rules = {bag.split('bags contain')[0].strip() : bag.split('bags contain')[1].strip()
                 for bag in bags}

    contains_shiny = search_bags('shiny gold', bag_rules)
    print(len(contains_shiny))
    return 0


def search_bags(bag, bag_rules):
    contains_bag = []
    for k, v in bag_rules.items():
        if bag in v:
            contains_bag.append(k)
            contains_bag.extend(search_bags(k, bag_rules))
    
    return set(contains_bag)


if __name__ == "__main__":
    main()