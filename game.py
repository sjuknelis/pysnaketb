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

        if self.snake.head[0] < 1 or self.snake.head[0] > 18 or self.snake.head[1] < 1 or self.snake.head[1] > GRID_HEIGHT - 2:
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

    def render(self,draw,fnum,font_path):
        if self.game_over or self.win:
            fnum = 0

        scroll = self.snake.head[1] + self.snake.direction[1] * 0.2 * fnum

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

        self.snake.render(draw,fnum)

        if abs(self.apple[1] - self.snake.head[1]) <= 1:
            draw.rectangle(
                [self.apple[0] * 60 + 10,(self.apple[1] - scroll) * 60 + 10,self.apple[0] * 60 + 50,(self.apple[1] - scroll) * 60 + 50],
                fill=(0,255,255,255)
            )

        if not (self.game_over or self.win):
            def draw_arrow(x,upward,color):
                if upward:
                    draw.line(
                        [
                            (x * 60 + 20,12),
                            (x * 60 + 30,6),
                            (x * 60 + 40,12)
                        ],
                        fill=color,
                        width=2
                    )
                else:
                    draw.line(
                        [
                            (x * 60 + 20,48),
                            (x * 60 + 30,54),
                            (x * 60 + 40,48)
                        ],
                        fill=color,
                        width=2
                    )

            if self.snake.head[1] <= 2:
                draw_arrow(1,True,(255,0,0,255))
                draw_arrow(18,True,(255,0,0,255))
            elif self.snake.head[1] >= GRID_HEIGHT - 3:
                draw_arrow(1,False,(255,0,0,255))
                draw_arrow(18,False,(255,0,0,255))

            if self.apple[1] < self.snake.head[1]:
                draw_arrow(self.apple[0],True,(0,255,255,255))
            elif self.apple[1] > self.snake.head[1]:
                draw_arrow(self.apple[0],False,(0,255,255,255))

        def draw_centered_text(text,color):
            font = ImageFont.truetype(font_path,48)
            dims = draw.textsize(text,font=font)
            draw.text([600 - dims[0] / 2,30 - dims[1] / 2],text,fill=color,font=font,align="center")
        if self.win:
            draw_centered_text("YOU WIN",(0,255,255,255))
        elif self.game_over:
            draw_centered_text("GAME OVER",(255,0,0,255))
