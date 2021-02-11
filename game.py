from settings import *
from objects import *
import time

class Game:
    def __init__(self, tk, canvas):
        self.tk = tk
        self.canvas = canvas

        self.paddle = Paddle(self.canvas, COLOR_PADDLE)
        self.score = Score(self.canvas, COLOR_SCORE)
        self.ball = Ball(self.canvas, self.paddle, self.score, COLOR_BALL)

        self.canvas.bind_all('<KeyPress-Right>', self.paddle.turn_right)         # Биндим клавиши
        self.canvas.bind_all('<KeyPress-Left>', self.paddle.turn_left)
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

        self.game_started = False

    def start_game(self, event):            # Запуск игры
        self.game_started = True

    def game_run(self):                    # Основной цикл игры и конец игры, если ball коснулся дна
        while not self.ball.hit_bottom:
            if self.game_started:
                self.ball.draw()
                self.paddle.draw()
            self.tk.update_idletasks()          # Обновляем интерфейс
            self.tk.update()
            time.sleep(0.01)

        time.sleep(3) 