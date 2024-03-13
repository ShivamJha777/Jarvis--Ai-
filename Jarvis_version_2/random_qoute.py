import random

from quote import quote
sample = ['money','power','love','family']
def random_qoute(w):
    if w == '':
        w = random.choice(sample)
    try:
        res = quote(w,1)
        for i in range(len(res)):
            quot = res[i]['quote']
            length = len(quot)
            if length > 175:
                print(length)
                author = res[i]['author']
                try:
                    book = res[i]['book']
                except:
                    print(quot + '\n-' + author)
                print(quot + '\n-' + author + f'({book})')
                return 'Quote is too big to be read out.Printing in terminal'
            author = res[i]['author']
            try:
                book = res[i]['book']
            except:
                print(quot + '\n-' + author)
                return quot + '\n-' + author
            print(quot + '\n-'+author+f'({book})')
            return quot + '\n-'+author+f'({book})'
    except:
        print('Some error occurred')