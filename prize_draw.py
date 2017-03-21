import string

def rank(st, we, n):
    d = {}
    alphabet = dict(zip(string.ascii_lowercase, range(1,27)))
    lst = st.split(",")

    if st == "":
        return "No participants"
    elif n > len(lst):
        return "Not enough participants"
    else:
        for i in xrange(len(lst)):
            name_len = len(lst[i])
            we_i = we[i]
            count = 0
            for j in xrange(name_len):
                letter = lst[i][j].lower()
                count += alphabet.get(letter)
            total = (name_len + count) * we_i
            d.update({lst[i]:total})
        return sorted(d.items(), key=lambda x: (-x[1], x[0]))[n-1][0]

if __name__ == '__main__':
    print rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)
    # print rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8)
    # print rank("", [4, 2, 1, 4, 3, 1, 2], 6)
    # print rank("COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH", [1, 4, 4, 5, 2, 1], 2)
    # print rank("Lagon,Lily", [1, 5], 2)
