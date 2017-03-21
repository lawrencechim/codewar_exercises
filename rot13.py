import string
from codecs import encode as _dont_use_this_

def rot13(message):
    s = ''
    all_letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    all_letters_upper = all_letters_lower.upper()
    for i in xrange(len(message)):
        letter = message[i]
        if letter.isalpha() and letter.islower():
            ind = all_letters_lower.find(letter)
            s += all_letters_lower[(ind + 13) % 26]
        elif letter.isalpha() and letter.isupper():
            ind = all_letters_upper.find(letter)
            s += all_letters_upper[(ind + 13) % 26]
        else:
            s += letter
    return s

if __name__ == '__main__':
    print rot13('grfg')
