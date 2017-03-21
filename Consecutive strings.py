def longest_consec(strarr, k):
    len_count = 0
    ind_count = 0
    str = ''
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    else:
        for i in xrange(n-k+1):
            counter = 0
            for j in xrange(i, i+k):
                counter += len(strarr[j])
                if counter > len_count:
                    len_count = counter
                    ind_count = j-k+1

    for ind in xrange(ind_count, ind_count+k):
        str += strarr[ind]
    return str
