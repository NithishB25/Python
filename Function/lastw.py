s= "hellow world"
def last_word(s):
    w = s.split()
    l_w = w[-1]

    return len(l_w)
print(last_word(s))