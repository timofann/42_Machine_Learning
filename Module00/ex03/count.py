from sys import stdin

def text_analyzer(text=None, *args):
    lower_cnt = 0
    upper_cnt = 0
    punct_cnt = 0
    space_cnt = 0
    if args or not (isinstance(text, str) or text is None):
        print('ERROR')
    if text is None:
        print('What is the text to analyse?')
        text = input()



if __name__ == '__main__':
    text_analyzer()



