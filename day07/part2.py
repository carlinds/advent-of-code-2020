def main():
    with open('bags.txt') as f:
        bags = f.readlines()

    bag_rules = {bag.split('bags contain')[0].strip() : bag.split('bags contain')[1].strip()
                 for bag in bags}

    total_bags = count_bags('shiny gold', bag_rules)
    print(total_bags - 1)
    return 0


def count_bags(bag, bag_rules):
    bag_count = 1
    for k, v in bag_rules.items():
        if bag == k:
            contained_bags = [x for x in bag_rules.keys() if x in v]
            for contained_bag in contained_bags:
                multiplier = int(v[v.find(contained_bag)-2])
                bag_count += multiplier * count_bags(contained_bag, bag_rules)
    
    return bag_count


if __name__ == "__main__":
    main()