class BasicWord:
    """Class BasicWord containes main word and subwords from letters of main word"""
    def __init__(self, word : str, *args : list):
        self.word = word
        self.subwords = args

    def check_subword(self, subword : str) -> bool:
        return subword in self.subwords

    def subwords_set(self) -> int:
        return len(self.subwords)

    def __repr__(self) -> None:
        return self.word + '\n' + str(self.subwords)


if __name__ == '__main__':
    a = BasicWord('питон', "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт")

    assert (a.word) == 'питон'
    assert (a.subwords[0]) == 'пони'
    assert (a.subwords_set()) == 9
    assert (a.check_subword('тон'))
    assert (not a.check_subword('тонн'))
