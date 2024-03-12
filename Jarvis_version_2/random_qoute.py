import random
from quote import quote
import requests
categories = ['age','alone','amazing','anger','architecture','art','attitude','beauty','best','birthday','business','car','change','communication','computers','cool','courage','dad','dating'
              ,'death','design','dreams','education','environmental','equality','experience','failure','faith','family','famous','fear','fitness','food','forgiveness','freedom','friendship',
              'funny','future','god','good','government','graduation','great','happiness','health','history','home','hope','humor','imagination','inspirational','intelligence','jealousy',
              'knowledge','leadership','learning','legal','life','love','marriage','medical','men','mom','money','morning','movies','success']
def random_qoute(catgory):
    w = catgory
    if catgory == '':
        from random_word import RandomWords
        r = RandomWords()
        w = r.get_random_word()
    try:
        res = quote(w,1)
        for i in range(len(res)):
            quot = res[i]['quote']
            length = len(quot)
            if length > 50:
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
random_qoute('money')