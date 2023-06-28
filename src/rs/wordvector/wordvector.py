import math

class WordVector:
    """класс для создания матрицы tf, idf, tf-idf, ngrams по умолчанию 1"""
    def __init__(self, getlist, tfidf = "tf-idf", ngrams = 1):
        self.getlist = getlist
        self.tfidf = tfidf
        self.ngrams = ngrams

    def load(self):
        """вектор"""
        klist = []
        instv = []
        c = 0
        countw = 0

        def fngrams(text, ngrams):
            nlist = []
            for i in text:
                trlist = []
                for x, j in enumerate(i):
                    tc = ""
                    tx = x
                    for k in range(ngrams):
                        if k == 0:
                            tc = str(i[tx])
                        elif k > 0:
                            try:
                                tc += " " + str(i[tx])
                            except IndexError:
                                break
                        trlist.append(tc)
                        tx += 1
                nlist.append(trlist)
            return nlist


        if self.ngrams >= 1 and self.ngrams <= 4:
            glist = fngrams(self.getlist, self.ngrams)
            for i in glist:
                for j in i:
                    instv.append(j)

        elif self.ngrams == 1:
            for i in self.getlist:
                for j in i:
                    instv.append(j)
            glist = self.getlist.copy()

        if self.tfidf == "tf":
            for i in glist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    c = instv.count(j)
                    tlist.append([c / len(instv)])
                tlist.append([0] * (len(instv) - countw))
                for k in tlist:
                    tlist2.extend(k)
                klist.append(tlist2)
            return klist

        elif self.tfidf == "idf":
            for i in glist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    tlist.append([math.log10(len(glist)/sum([1.0 for i in glist if j in i]))])
                tlist.append([0] * (len(instv) - countw))
                for k in tlist:
                    tlist2.extend(k)
                klist.append(tlist2)
            return klist

        elif self.tfidf == "tf-idf":
            for i in glist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    c = instv.count(j)
                    vartf = c / len(instv)
                    varidf = math.log10(len(glist)/sum([1.0 for i in glist if j in i]))
                    tlist.append([vartf * varidf])
                tlist.append([0] * (len(instv) - countw))
                for k in tlist:
                    tlist2.extend(k)
                klist.append(tlist2)
            return instv, klist
