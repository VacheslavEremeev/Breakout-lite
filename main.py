from tkinter import *
from settings import *
from objects import *
from game import Game
from PIL import ImageTk, Image

tk = Tk()
tk.title(GAME_NAME)          # Инициализация окна Tkinter
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, highlightthickness=0 )    # Инициализация Canvas, на котором мы можем рисовать
#bg = ImageTk.PhotoImage(Image.open('bg.jpg').resize((WIDTH, HEIGHT)))     # Можно поставить фон приложения
#canvas.create_image(WIDTH / 2, HEIGHT / 2, image=bg)
canvas.pack()
tk.update()


game = Game(tk, canvas)        # Инициализация игры

if __name__ == '__main__':       # Запуск игры
    game.game_run()









