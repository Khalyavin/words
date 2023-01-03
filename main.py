from classes import BasicWord, Player
from utils import load_random_word


def main():
    """Game in words. From BasicWord letters you must consist subwords"""

    # Begining of the game. Ask player name and get him BasicWord
    player_name = input('Введите имя игрока: ')

    player = Player(player_name)

    print('\n' + f'Привет, {player.name}')

    basic_word = load_random_word()

    print(f'Составьте {len(basic_word.subwords[0])} слов из слова "{basic_word.word.upper()}"')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop/стоп"')
    quest_word = input('Поехали! Ваше первое слово: ')

    # Main programm cicle
    while player.used_words() < len(basic_word.subwords[0]):
        if len(quest_word) < 3:
            print('Это слово сильно короткое!')
        elif len(quest_word) > len(basic_word.word):
            print('Это слово слишком велико!')
        elif quest_word == 'stop' or quest_word == 'стоп':
            break
        else:
            if quest_word in basic_word.subwords[0]:
                if player.check_word(quest_word):
                    print('Слово уже угадано')
                else:
                    player.add_word(quest_word)
            else:
                print('Нет такого подслова в слове!')

        print(f'Из слова "{basic_word.word.upper()}" угаданы {player.guessed_words}')
        print(f'Осталось угадать {len(basic_word.subwords[0]) - len(player.guessed_words)} слов' + '\n')
        quest_word = input('Продолжаем! Ваше следующее слово: ')

    # Finally results
    if len(basic_word.subwords[0]) == len(player.guessed_words):
        print(f'Молодец, {player.name}! Угадал все возможные варианты слов!')
    else:
        lost_words = []
        for word in basic_word.subwords[0]:
            if word not in player.guessed_words:
                lost_words.append(word)

        print(f'Неплохо постарался, {player.name}!')
        print(f'Неугадал слова: {lost_words}')
        print('В следующий раз все получится!')


if __name__ == '__main__':
    main()