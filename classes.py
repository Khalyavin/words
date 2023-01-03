class BasicWord:
    """Class BasicWord containes main word and subwords from letters of main word"""
    def __init__(self, word : str, *args : list):
        self.word = word
        self.subwords = args

    def check_subword(self, subword : str) -> bool:
        return subword in self.subwords

    def subwords_set(self) -> int:
        return len(self.subwords)

    def __repr__(self) -> str:
        return self.word + '\n' + str(self.subwords)

class Player:
    def __init__(self, name : str):
        self.name = name
        self.guessed_words = []

    def used_words(self) -> int:
        return len(self.guessed_words)

    def add_word(self, word : str) -> None:
        self.guessed_words.append(word)

    def check_word(self, word : str) -> bool:
        return word in self.guessed_words

    def __repr__(self) -> str:
        return self.name + '\n' + str(self.guessed_words)


if __name__ == '__main__':
    a = BasicWord('питон', "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт")

    assert (a.word) == 'питон'
    assert (a.subwords[0]) == 'пони'
    assert (a.subwords_set()) == 9
    assert (a.check_subword('тон'))
    assert (not a.check_subword('тонн'))

    b = Player('Василий')
    b.add_word('тон')
    b.add_word('опт')

    assert (b.name) == 'Василий'
    assert (b.used_words()) == 2
    assert (b.check_word('тон'))
    assert (not b.check_word('тонн'))