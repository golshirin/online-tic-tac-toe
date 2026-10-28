import pygame as pg
import sys
from random import randint
import socket
import threading




class TicTacToe:
    def __init__(self, game):
        self.WIN_SIZE = 400
        self.CELL_SIZE = self.WIN_SIZE // 3
        self.INF = float('inf')
        self.vec2 = pg.math.Vector2
        self.CELL_CENTER = self.vec2(self.CELL_SIZE / 2)
        self.game = game
        self.field_image = self.get_scaled_image(path='C:\\Users\\Sony\\Desktop\\Online Tic Tac Toe\\Picture3.png', res=[self.WIN_SIZE] * 2)
        self.O_image = self.get_scaled_image(path='C:\\Users\\Sony\\Desktop\\Online Tic Tac Toe\\Picture2.png', res=[self.CELL_SIZE] * 2)
        self.X_image = self.get_scaled_image(path='C:\\Users\\Sony\\Desktop\\Online Tic Tac Toe\\Picture1.png', res=[self.CELL_SIZE] * 2)

        self.game_array = [[self.INF, self.INF, self.INF],
                           [self.INF, self.INF, self.INF],
                           [self.INF, self.INF, self.INF]]
        self.player = randint(0, 1)

        self.line_indices_array = [[(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],
                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],
                                   [(0, 0), (1, 1), (2, 2)],
                                   [(0, 2), (1, 1), (2, 0)]]
        self.winner = None
        self.game_steps = 0
        self.font = pg.font.SysFont('Verdana', self.CELL_SIZE // 4, True)

        
    def check_winner(self):
        for line_indices in self.line_indices_array:
            sum_line = sum([self.game_array[i][j] for i, j in line_indices])
            if sum_line in {0, 3}:
                self.winner = 'XO'[sum_line == 0]
                self.winner_line = [self.vec2(line_indices[0][::-1]) * self.CELL_SIZE + self.CELL_CENTER,
                                    self.vec2(line_indices[2][::-1]) * self.CELL_SIZE + self.CELL_CENTER]

    def run_game_process(self):
        current_cell = self.vec2(pg.mouse.get_pos()) // self.CELL_SIZE
        col, row = map(int, current_cell)
        left_click = pg.mouse.get_pressed()[0]

        if left_click and self.game_array[row][col] == self.INF and not self.winner:
            self.game_array[row][col] = self.player
            self.player = not self.player
            self.game_steps += 1
            self.check_winner()

    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                if obj != self.INF:
                    self.game.screen.blit(self.X_image if obj else self.O_image, self.vec2(x, y) * self.CELL_SIZE)

    def draw_winner(self):
        if self.winner:
            pg.draw.line(self.game.screen, 'red', *self.winner_line, self.CELL_SIZE // 8)
            label = self.font.render(f'Player "{self.winner}" wins!', True, 'white', 'black')
            self.game.screen.blit(label, (self.WIN_SIZE // 2 - label.get_width() // 2, self.WIN_SIZE // 4))

    def draw(self):
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()
        self.draw_winner()

    @staticmethod
    def get_scaled_image(path, res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img.convert_alpha(), res)

    def print_caption(self):
        pg.display.set_caption(f'Player "{"OX"[self.player]}" turn!')
        if self.winner:
            pg.display.set_caption(f'Player "{self.winner}" wins! Press Space to Restart')
        elif self.game_steps == 9:
            pg.display.set_caption(f'Game Over! Press Space to Restart')

    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()


class Game:
    def __init__(self):
        pg.init()
        self.WIN_SIZE = 400
        self.screen = pg.display.set_mode([self.WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = TicTacToe(self)

    def new_game(self):
        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()

    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


game = Game()
game.run()
