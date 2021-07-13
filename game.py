import sys,time,random
from PIL import ImageFont
from snake import Snake
GRID_HEIGHT = 10

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.move_apple()
        self.game_over = False
        self.win = False

    def update(self):
        if self.game_over or self.win:
            return

        self.snake.update()

        if self.snake.head == self.apple:
            self.snake.eaten = True
            self.move_apple()

        if len(self.snake.path) >= 18 * (GRID_HEIGHT - 2) - 1:
            self.win = True

        if self.snake.head[0] < 1 or self.snake.head[0] > 18 or self.snake.head[1] < 1 or self.snake.head[1] > GRID_HEIGHT - 1:
            self.game_over = True
        pos = list(self.snake.head)
        for item in self.snake.path:
            pos[0] += item[0]
            pos[1] += item[1]
            if list(self.snake.head) == pos:
                self.game_over = True
                break

    def move_apple(self):
        while True:
            self.apple = (random.randrange(1,19),random.randrange(1,GRID_HEIGHT - 1))
            pos = list(self.snake.head)
            if list(self.apple) == pos:
                continue
            valid = True
            for item in self.snake.path:
                pos[0] += item[0]
                pos[1] += item[1]
                if list(self.apple) == pos:
                    valid = False
            if valid:
                break

    def render(self,draw,fnum):
        if self.game_over or self.win:
            fnum = 0

        scroll = self.snake.head[1] + self.snake.direction[1] * 0.2 * fnum

        self.snake.render(draw,fnum)

        draw.rectangle(
            [self.apple[0] * 60 + 10,(self.apple[1] - scroll) * 60 + 10,self.apple[0] * 60 + 50,(self.apple[1] - scroll) * 60 + 50],
            fill=(0,255,255,255)
        )

        if self.snake.head[1] <= 2:
            draw.rectangle(
                [0,(- scroll) * 60,1200,(- scroll + 1) * 60 + 5],
                fill=(0,255,0,255)
            )
        if self.snake.head[1] >= GRID_HEIGHT - 3:
            draw.rectangle(
                [0,(GRID_HEIGHT - 1 - scroll) * 60 - 5,1200,(GRID_HEIGHT - 1 - scroll + 1) * 60],
                fill=(0,255,0,255)
            )
        draw.rectangle(
            [0,0,60,60],
            fill=(0,255,0,255)
        )
        draw.rectangle(
            [1140,0,1200,60],
            fill=(0,255,0,255)
        )

        if self.snake.head[1] <= 2:
            draw.line(
                [
                    (1 * 60 + 20,10),
                    (1 * 60 + 30,2),
                    (1 * 60 + 40,10)
                ],
                fill=(255,0,0,255),
                width=2
            )
            draw.line(
                [
                    (18 * 60 + 20,10),
                    (18 * 60 + 30,2),
                    (18 * 60 + 40,10)
                ],
                fill=(255,0,0,255),
                width=2
            )
        elif self.snake.head[1] >= GRID_HEIGHT - 3:
            draw.line(
                [
                    (1 * 60 + 20,50),
                    (1 * 60 + 30,58),
                    (1 * 60 + 40,50)
                ],
                fill=(255,0,0,255),
                width=2
            )
            draw.line(
                [
                    (18 * 60 + 20,50),
                    (18 * 60 + 30,58),
                    (18 * 60 + 40,50)
                ],
                fill=(255,0,0,255),
                width=2
            )

        if self.apple[1] < self.snake.head[1]:
            draw.line(
                [
                    (self.apple[0] * 60 + 20,10),
                    (self.apple[0] * 60 + 30,2),
                    (self.apple[0] * 60 + 40,10)
                ],
                fill=(0,255,255,255),
                width=2
            )
        elif self.apple[1] > self.snake.head[1]:
            draw.line(
                [
                    (self.apple[0] * 60 + 20,50),
                    (self.apple[0] * 60 + 30,58),
                    (self.apple[0] * 60 + 40,50)
                ],
                fill=(0,255,255,255),
                width=2
            )

        def draw_centered_text(text,color):
            font = ImageFont.truetype("CourierPrime-Regular.ttf",48)
            dims = draw.textsize(text,font=font)
            draw.text([600 - dims[0] / 2,30 - dims[1] / 2],text,fill=color,font=font,align="center")
        if self.win:
            draw_centered_text("YOU WIN",(0,255,255,255))
        elif self.game_over:
            draw_centered_text("GAME OVER",(255,0,0,255))
