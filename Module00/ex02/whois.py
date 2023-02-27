import sys

if __name__ == '__main__':

    try:
        assert len(sys.argv) == 2
        integer = int(sys.argv[1])
        if integer == 0:
            print("I'm Zero.")
        else:
            print("I'm Odd.") if integer % 2 else print("I'm Even.")
    except:
        print('ERROR')
