fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

print 'You have...'
for f in fruits:
    first_char = f[0]
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    if first_char in vowels:
        print 'An', f
    else:
        print 'A', f
else:
    print 'A fine selection of fruits!'