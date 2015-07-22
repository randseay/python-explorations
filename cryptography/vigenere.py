from itertools import starmap, cycle
from sys import argv

def encrypt(message, key):

    def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('a'))

    return ''.join(starmap(enc, zip(message, cycle(key))))

def decrypt(message, key):

    def dec(c,k): return chr(((ord(c) - ord(k)) % 26) + ord('a'))

    return ''.join(starmap(dec, zip(message, cycle(key))))

def main():
    # The key is 'h'. Pass it in as the first argument when running the script.
    MESSAGE1 = 'gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk'
    KEY1 = argv[1] if len(argv) > 1 else 'h'
    print(decrypt(MESSAGE1, KEY1))

    # The key is ''. Pass it in as the second argument when running the script.
    MESSAGE2 = 'vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr'
    KEY2 = argv[2] if len(argv) > 2 else 'd'
    print(decrypt(MESSAGE2, KEY2))

    MESSAGE3 = 'klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn'
    KEY3 = argv[3] if len(argv) > 3 else 'sskkuullll'
    print(decrypt(MESSAGE3, KEY3))

if __name__ == '__main__':
    main()
