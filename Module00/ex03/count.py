import string
import sys


def text_analyzer(text=None, *args):
    """
    This function counts the number of upper characters, lower characters, \
    punctuation and spaces in a given text.
    """
    if args or not (isinstance(text, str) or text is None):
        print('ERROR')
    if text is None:
        print('What is the text to analyse?')
        text = ''.join([line for line in sys.stdin])
        # text = input()
    print(f'The text contains {len(text)} characters:')
    print(f'- {len(list(filter(str.isupper, list(text))))} upper letters')
    print(f'- {len(list(filter(str.islower, list(text))))} lower letters')
    print(f'- {len(list(filter(lambda x: x in string.punctuation, list(text))))} punctuation marks')
    print(f'- {len(list(filter(str.isspace, list(text))))} spaces')


if __name__ == '__main__':
    text_analyzer()



