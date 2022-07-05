
import random, tkinter
from tkinter import messagebox

# Объявляем глобальные переменные в пикселях

CELL_SIZE = 40
FIELD_SIZE = 10
WIDTH = 400
HEIGHT = 400
GEOM = f'{WIDTH}x{HEIGHT}'

# Создаём игровое поле

root = tkinter.Tk()

# Размеры поля

root.geometry(GEOM)

# Название в title

root.title('Обратные крестики-нолики')


# Главная функция main

def main():
    window = Window(root)
    window.grid()
    game = Game()

    # Функцию для опредления координат клика
    def position(event):
        x = event.x
        y = event.y
        # Переход хода
        if game.click_position(x, y, window):
            game.computer_move(window)

    # Определяем клик левой кнопкой мыши
    root.bind("<Button-1>", position)
    
    # Цикл для обработки событий
    root.mainloop()


# Создаём класс работы графики
class Window:
    # Создаём поле серого цвета
    def __init__(self, rt):
        self.game_window = tkinter.Canvas(rt, width=WIDTH, height=WIDTH, bg='grey')
        self.game_window.pack()

    # Создаём сетку, сначала внешние линии, затем внутренние
    def grid(self):
        self.game_window.create_rectangle(2, 2, WIDTH - 3, WIDTH)
        for i in range(FIELD_SIZE):
            self.game_window.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, WIDTH)
            self.game_window.create_line(0, i * CELL_SIZE, HEIGHT, i * CELL_SIZE)

    # Рисуем крестик
    def draw_x(self, x, y, color):
        self.game_window.create_line(CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE * x + CELL_SIZE,
                                     CELL_SIZE * y + CELL_SIZE, width=3, fill=color)
        self.game_window.create_line(CELL_SIZE * x + CELL_SIZE, CELL_SIZE * y, CELL_SIZE * x,
                                     CELL_SIZE * y + CELL_SIZE, width=3, fill=color)

    # Рисуем нолик
    def draw_o(self, x, y, color):
        self.game_window.create_oval(CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE * x + CELL_SIZE,
                                     CELL_SIZE * y + CELL_SIZE, width=3, outline=color)


# Создаём класс в котором будет логика игры

class Game:
    def __init__(self):
        # Создаём массив и заполняем его отрезками под клетки нашего поля
        self.grid_field = [[i * CELL_SIZE, (i + 1) * CELL_SIZE] for i in range(FIELD_SIZE)]
        # Создаём массив и заполняем его нулями - это будет наше поле
        self.dot_field = [[0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

    # Создаём функцию проверки победы(горизонт, вертикаль и две диагонали), если находит подряд 5 одинаковых,
    # заполненных клеточек, возвращает true
    def check_win(self):
        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE - 4):
                if self.dot_field[i][j] == self.dot_field[i][j + 1] == self.dot_field[i][j + 2] == \
                        self.dot_field[i][j + 3] == self.dot_field[i][j + 4] != 0:
                    return True
        for i in range(FIELD_SIZE - 4):
            for j in range(FIELD_SIZE):
                if self.dot_field[i][j] == self.dot_field[i + 1][j] == self.dot_field[i + 2][j] == \
                        self.dot_field[i + 3][j] == self.dot_field[i + 4][j] != 0:
                    return True
        for i in range(FIELD_SIZE - 4):
            for j in range(FIELD_SIZE - 4):
                if self.dot_field[i][j] == self.dot_field[i + 1][j + 1] == self.dot_field[i + 2][j + 2] == \
                        self.dot_field[i + 3][j + 3] == self.dot_field[i + 4][j + 4] != 0:
                    return True
        for i in range(FIELD_SIZE - 4):
            for j in range(4, FIELD_SIZE):
                if self.dot_field[i][j] == self.dot_field[i + 1][j - 1] == self.dot_field[i + 2][j - 2] == \
                        self.dot_field[i + 3][j - 3] == self.dot_field[i + 4][j - 4] != 0:
                    return True

    # Создаём функцию для хода компьютера
    def computer_move(self, window):
        y = random.randint(0, 9)
        x = random.randint(0, 9)
        # Рандомно подставляем координаты и проверяем клетку, если она пуста(==0),
        # то ставим 2, выбираем черный цвет, рисуем О, проверяем на победу, иначе повторяем
        if self.dot_field[y][x] == 0:
            self.dot_field[y][x] = 2
            color = 'black'
            window.draw_o(x, y, color)
            # Проверяем на победу, если функция проверки == true, то вызываем
            # всплывающее сообщение с надписью о проигравшем и закрываем окно с игрой
            if self.check_win():
                messagebox.showinfo("Конец игры!", "Вы выиграли!")
                root.destroy()
        else:
            return self.computer_move(window)

    # Создаём функцию для хода пользователя
    def click_position(self, x, y, window):
        # Определяем какой клетке(х, у) принадлежат координаты клика
        for i in range(FIELD_SIZE):
            if self.grid_field[i][0] <= x <= self.grid_field[i][1]:
                x = i
            if self.grid_field[i][0] <= y <= self.grid_field[i][1]:
                y = i
        # Проверяем клетку после клика, если она пуста(==0),то ставим 1, выбираем белый цвет,
        # рисуем Х, проверяем на победу, возвращаем true, иначе false
        if self.dot_field[y][x] == 0:
            self.dot_field[y][x] = 1
            color = 'white'
            window.draw_x(x, y, color)
            if self.check_win():
                messagebox.showinfo("Конец игры!", "Вы проиграли!")
                root.destroy()
                return False
            return True
        else:
            return False


if __name__ == "__main__":
    main()
