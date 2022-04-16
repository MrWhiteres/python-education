#!/usr/bin/env python3
from random import choice


def touch_word():
    with open("word.txt", 'r') as file:
        file = [i.rstrip('\n') for i in file.readlines()]
        return ''.join(choice(file))


def locking_word():
    with open("word off.txt", 'r') as file:
        file = [i.rstrip('\n') for i in file.readlines()]
        if len(file) > 0:
            print(*file, sep='\n')
        else:
            print('Пока тут пусто')


def check_command(command):
    while True:
        if command in ['старт', 'выход']:
            return True if command == 'старт' else False
        elif command == "слово":
            locking_word()
            command = input('Возвращаемся к выбору старт игры или выход: ')
        else:
            command = input('Некорректная команда, попробуй еще: ')


def end_result(quiting):
    return mid_game() if quiting == "да" else print('Спасибо за игру!)')


def result(word, func):
    word_off(word)
    if func:
        quiting = input('Отлично, секретное слово было найдено. Продолжим?) да/нет: ').lower()
        end_result(quiting)
    else:
        quiting = input(
            f'К сожаление у тебя не вышло(\nСекретным словом было {word},'
            f' Попробуешь еще раз? да/нет: ').lower()
        end_result(quiting)


def mid_game():
    word = touch_word()
    print(f'Итак мы начинаем, длинна секретного слова = {len(word)}')
    result(word, games(word))


def word_checker(word, later):
    return True if later in word else False


def word_off(word):
    with open('word off.txt', 'a') as file:
        file.write(word + '\n')


def word_changer(word, later, words_secret):
    words_secret = [i for i in words_secret]
    for i in range(len(word)):
        if later == word[i]:
            words_secret[i] = later
    return words_secret


def tacker_later(not_later):
    while True:
        later = input('Введите букву: ').lower()
        if later in not_later:
            print('Этой буквы нет в слове')
        else:
            if len(later) == 1 and later != ' ':
                return later
            else:
                print('Необходимо ввести букву, не строку и не пробел')
        print()


def games(word):
    life = 8
    words_secret = '-' * len(word)
    not_later = []
    print(f'Секретное слово {words_secret}\nТвои жизни = {life}\n')
    while life > 0:
        if '-' not in words_secret:
            return True
        later = tacker_later(not_later)
        if word_checker(word, later):
            words_secret = word_changer(word, later, words_secret)
            print("".join(words_secret), '\n')
        else:
            life -= 1
            if later not in not_later:
                not_later.append(later)
            print(f'Этой буквы нет в слове\nТвои жизни = {life}\n'
                  f'Буквы которых нет в слове: {",".join(not_later)}\n')
    return False


def start_game():
    first_step = input(
        "Привет, добро пожаловать в игру 'Hangman' чтобы начать игру нужно написать"
        " 'старт', для того чтобы увидеть все слова которые уже встречались пишем 'слово'"
        " , а чтобы выйти нужно написать 'выход': ")
    if check_command(first_step.lower()):
        mid_game()
    else:
        print('Возвращайся поскорее.')


if __name__ == '__main__':
    start_game()
