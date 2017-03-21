def tower_builder(n_floors):
    lst = []
    stars = 0
    while n_floors > 0:
        lst.append(' '*(n_floors-1) + '*'*(2*stars + 1) + ' '*(n_floors-1))
        stars += 1
        n_floors -= 1
    return lst
