def max_rot(n):
    lst = []
    lst2 = []
    for i in xrange(len(str(n))):
        lst.append(str(n)[i])

    k = 1
    while len(lst2) < len(str(n)):
        temp = lst[0]
        lst[-1] = temp
        lst[i] = lst[i+1]
        lst2.append(lst[0])
        del lst[0]
        k += 1
    return lst2

if __name__ == '__main__':
    max_rot(19678)
