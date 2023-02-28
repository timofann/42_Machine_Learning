from datetime import datetime

k00 = (19, 42, 21)

k01 = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

k02 = (3, 30, 2019, 9, 25)

k03 = "The right format"

if __name__ == '__main__':
    print(f'The 3 numbers are {str(k00)[1:-1]}')
    for key, value in k01.items():
        print(f'{key} was created by {value}')
    print(datetime(*k02[2:], *k02[:2]).strftime('%m/%d/%Y %H:%M'))
    print(f'{k03:->42}')
