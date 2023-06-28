
class Fit:
    """класс поиска в матрице """
    def __init__(self, bow1, bow2, vect2):
        self.bow1 = bow1
        self.bow2 = bow2
        self.vect2 = vect2

    def fit(self):
        """находит совпадении в векторах"""
        mdict = {}
        searchlist = []
        result = []
        for i, x in enumerate(self.bow1):
            if x not in mdict.keys():
                for k, y in enumerate(self.bow2):
                    if y == x:
                        for j in range(len(self.vect2)):
                            if self.vect2[j][k] != 0:
                                mdict[x] = self.vect2[j][k]
                                searchlist.append((self.vect2[j][k], j))
                                break
                        break
        for i in range(len(searchlist)):
            trlist = []
            for j in searchlist:
                if i == j[1]:
                    trlist.append(j[0])
            if len(trlist) != 0:
                result.append((i, trlist))
        return result
