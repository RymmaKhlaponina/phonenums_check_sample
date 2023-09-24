import re


def phone_checking(numbers):
    """Функция выполняет проверку номера из списка на соответствие паттерну, добавляет номер в список номеров
    соответствующей страны (если номер не соответствует ни одному паттерну, доавляется в список некорректных"""
    polish_numbers = []
    ukrainian_numbers = []
    czech_numbers = []
    incorrect_numbers = []
    for number in range(len(numbers)):
        if re.fullmatch(r'\+48([0-9]){9}', numbers[number]) is not None:
            polish_numbers.append(numbers[number])
        elif re.fullmatch(r'\+380([0-9]){9}', numbers[number]) is not None:
            ukrainian_numbers.append(numbers[number])
        elif re.fullmatch(r'\+420([0-9]){9}', numbers[number]) is not None:
            czech_numbers.append(numbers[number])
        else:
            incorrect_numbers.append(numbers[number])
    print('Polish numbers ' + str(polish_numbers) + '\n' 'Ukrainian numbers ' + str(ukrainian_numbers) + '\n' 
          'Czech numbers ' + str(czech_numbers) + '\n' 'Incorrect numbers ' + str(incorrect_numbers) + '\n')


phone_numbers = []
phone_numbers.extend(input("Write phone numbers:\n ").split())  # Добавление номеров в общий список с учетом разделителя
phone_checking(phone_numbers)  # Передача пользовательского списка в функцию проверки


