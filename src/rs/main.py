import json
from wordvector.wordvector import WordVector
from wordvector.fit import Fit
from wordvector.cossim import CosSim
from nlp.sentences import Sentences
from nlp.words import Words

cold = 0
history = []
dlist = []

with open("data.json", "r") as file:
    data = json.load(file)

for i in data:
    w = Words(i)
    wl = w.load()
    dlist.append(wl)

# vector with tf-idf
ivect = WordVector(dlist)
vect = ivect.load()
while True:
    tlist = []
    wlist = []
    result = []
    if cold == 0: 
        print("Recomendation movie: ", data[1])
        history.append(1)
        inp = input("continue?(y/n) ")
        if inp == "y":
            cold = 1
        else:
            exit()
    else:
        for i in history:
            sen = Sentences(data[i])
            tsen = sen.load()
        for i in tsen:
            tok = Words(i)
            wtok = tok.load()
            tlist.append(wtok)
        ivect2 = WordVector(tlist)
        vect2 = ivect2.load()
        f = Fit(vect2[0], vect[0], vect[1])
        fr = f.fit()
        for i in vect2[1]:
            for j in i:
                if j != 0:
                    wlist.append(j)
        for i in fr:
            c = CosSim(wlist, i[1])
            cw = c.cossim()
            result.append((i[0], cw))
        result.sort(key = lambda x: x[1])
        print(result)
        if result[-1][0] not in history:
            print("Recomendation movie: ", data[result[-1][0]])
            inp = input("continue?(y/n) ")
            if inp == "y":
                history.append(result[-1][0])
        else:
            print("Recomendation movie: ", data[result[-2][0]])
            inp = input("continue?(y/n) ")
            if inp == "y":
                history.append(result[-2][0])
        
