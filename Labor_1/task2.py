from task1 import Coworking, Boat, Puzzle

if __name__ == "__main__":
    # Инстанцирование
    coworking = Coworking("Просто", 50)
    boat = Boat("Чижик", 30.0, 4)
    puzzle = Puzzle("Котята в корзинке", 300)

    # Тестирование класса Coworking
    try:
        coworking = Coworking("Просто", -1)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        coworking.is_full(-3)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        coworking = Coworking("Просто", "Коворкинг")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        coworking = Coworking(1, 50)
    except TypeError:
        print('Ошибка: неправильные данные')

    # Тестирование класса Boat
    try:
        boat = Boat("Чижик", 30.0, 0)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        boat.set_speed(-5)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        boat.distance(-100)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        boat_error = Boat("Чижик", 30.0, "1")
    except TypeError:
        print('Ошибка: неправильные данные')

    # Тестирование класса Puzzle
    try:
        puzzle_error = Puzzle("Котята в корзинке", -10)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        puzzle.is_completed(400)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        puzzle.get_progress(-300)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        puzzle_error = Puzzle(123, 300)
    except TypeError:
        print('Ошибка: неправильные данные')



