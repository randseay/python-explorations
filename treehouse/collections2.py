# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]
# If you use list.append(), you'll want to pass it a tuple of new values.
# Using enumerate() here can save you a variable or two.

testIter1 = list(range(1,27))
testIter2 = list("abcdefghijklmnopqrstuvwxyx")

def combo(iter1, iter2):
    comboList = []
    for i, j in enumerate(iter1):
        comboList.append((iter1[i], iter2[i]))
    return comboList

def main():
    print(combo(testIter1, testIter2))

main()
