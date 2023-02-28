import sys
from string import punctuation

if __name__ == '__main__':
    try:
        assert len(sys.argv) == 3
        n = int(sys.argv[2])
        string = sys.argv[1]
        assert not string.isnumeric()
        for char in punctuation:
            string.replace(char, '')
        print(list(filter(lambda x: len(x) >= n, string.split(' '))))
    except:
        print('ERROR')
