from time import sleep
import sys


def ft_progress(lst):
    for i in range(len(lst)):
        clear = "\r" * (30 + 9)
        print(clear, flush=True, end='')
        part = i/len(lst)
        bar = u"█" * int(part*30)
        print(f"{part*100:>6.1f}% {bar:-<30}", flush=True, end='')
        yield lst[i]
    clear = "\r" * (30 + 6)
    print(clear, flush=True, end='')
    part = 1.0
    bar = u"█" * int(part*30)
    print(f"{part*100:>6.1f}% {bar:-<30}", flush=True, end='')


if __name__ == '__main__':
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.001)
    print()
    print(ret)
