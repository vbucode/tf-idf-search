import re

class Sentences:
    """класс создает список с предложениями по точке, вопросительному знаку, восклицательному знаку"""
    def __init__(self, text):
        self.text = text

    def load(self):
        """ токенизация по предложениям """
        self.lowertext = self.text.lower()
        self.clearstring = re.sub("[\t\r\n\f\v]", "", self.lowertext)
        self.onestring = re.sub("[ё]", "е", self.clearstring)
        self.sentlist = re.split("(?<!\w\.\w)(?<![a-z]\.\s)(?<=\.)(\s|[a-z].*)", self.onestring)
        self.filtered = [x for x in self.sentlist if x not in " "]
        return self.filtered

