def intersectionSet(first_list, second_list):
    set_first = set(first_list)
    set_second = set(second_list)
    set_intersection = set_first.intersection(set_second)
    
    return list(set_intersection)


def unionSet(first_list, second_list):
    set_first = set(first_list)
    set_second = set(second_list)
    set_union = set_first.union(set_second)

    return list(set_union)


