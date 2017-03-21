def tribonacci(signature,n):
    lst2 = signature
    i = 0
    if n == 0:
        return []
    elif n >= 1 and n < 3:
        return signature[:n]
    else:
        while i < n-3:
            lst2.append(sum(lst2[i:i+3]))
            i += 1
    return lst2

if __name__ == '__main__':
    print tribonacci([0,0,1],10)
