"""Игра угадай число Компьютер сам загадывает и сам угадывает число."""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    predict_number = np.random.randint(1, 101)  # предполагаемое число

    while number != predict_number:
        count += 1

        if number > predict_number:
            predict_number += 10

        elif number < predict_number:
            predict_number -= 3

    return count


def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш
    алгоритм.

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за:{score} попыток')

    return score


if __name__ == '__main__':
    # RUN
    score_game(game_core_v3)
