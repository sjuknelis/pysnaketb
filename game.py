import sys,time,random
from PIL import ImageFont
GRID_HEIGHT = 10

class Snake:
    head = (10,5)
    path = [(-1,0),(-1,0)]
    direction = (1,0)
    move_buffer = []
    eaten = False

    def update(self):
        self.head = (self.head[0] + self.direction[0],self.head[1] + self.direction[1])
        self.path.insert(0,(-self.direction[0],-self.direction[1]))
        if not self.eaten:
            self.path.pop()
        else:
            self.eaten = False

        if len(self.move_buffer) > 0:
            for (index,item) in enumerate(self.move_buffer):
                if item != self.direction and item != (-self.direction[0],-self.direction[1]):
                    self.direction = item
                    del self.move_buffer[index]
                    break

    def queue(self,direction):
        if not direction in self.move_buffer:
            self.move_buffer.insert(0,direction)

    def render(self,draw,fnum):
        scroll = self.head[1] + self.direction[1] * 0.2 * fnum
        pos = list(self.head)
        last = list(pos)
        for (index,item) in enumerate(self.path):
            pos[0] += item[0]
            pos[1] += item[1]
            if index == len(self.path) - 1 and not self.eaten:
                pos[0] -= item[0] * 0.2 * fnum
                pos[1] -= item[1] * 0.2 * fnum
            if abs(pos[1] - self.head[1]) <= 1:
                draw.rectangle(
                    [
                        min(pos[0],last[0]) * 60 + 10,
                        (min(pos[1],last[1]) - scroll) * 60 + 10,
                        max(pos[0],last[0]) * 60 + 50,
                        (max(pos[1],last[1]) - scroll) * 60 + 50
                    ],
                    fill=(0,255,0,255)
                )
            last = list(pos)

        ext = (self.head[0] + self.direction[0] * 0.2 * fnum,self.head[1] + self.direction[1] * 0.2 * fnum)
        draw.rectangle(
            [
                min(self.head[0],ext[0]) * 60 + 10,
                (min(self.head[1],ext[1]) - scroll) * 60 + 10,
                max(self.head[0],ext[0]) * 60 + 50,
                (max(self.head[1],ext[1]) - scroll) * 60 + 50
            ],
            fill=(0,255,0,255)
        )

class Game:
    snake = Snake()
    game_over = False

    def __init__(self):
        self.move_apple()

    def update(self):
        if self.game_over:
            return

        self.snake.update()

        if self.snake.head == self.apple:
            self.snake.eaten = True
            self.move_apple()

        if self.snake.head[0] < 1 or self.snake.head[0] > 18 or self.snake.head[1] < 1 or self.snake.head[1] > GRID_HEIGHT - 1:
            self.game_over = True

    def move_apple(self):
        while True:
            self.apple = (random.randrange(1,19),random.randrange(1,GRID_HEIGHT - 1))
            pos = list(self.snake.head)
            if list(self.apple) == pos:
                continue
            for item in self.snake.path:
                pos[0] += item[0]
                pos[1] += item[1]
                if list(self.apple) == pos:
                    continue
            break

    def render(self,draw,fnum):
        if self.game_over:
            fnum = 0

        scroll = self.snake.head[1] + self.snake.direction[1] * 0.2 * fnum

        self.snake.render(draw,fnum)

        draw.rectangle(
            [self.apple[0] * 60 + 10,(self.apple[1] - scroll) * 60 + 10,self.apple[0] * 60 + 50,(self.apple[1] - scroll) * 60 + 50],
            fill=(255,0,0,255)
        )

        if self.snake.head[1] <= 2:
            draw.rectangle(
                [0,(- scroll) * 60,1200,(- scroll + 1) * 60 + 5],
                fill=(0,255,0,255)
            )
        if self.snake.head[1] >= GRID_HEIGHT - 2:
            draw.rectangle(
                [0,(GRID_HEIGHT - scroll) * 60 - 5,1200,(GRID_HEIGHT - scroll + 1) * 60],
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

        if self.game_over:
            font = ImageFont.truetype("CourierPrime-Regular.ttf",48)
            dims = draw.textsize("GAME OVER",font=font)
            draw.text([600 - dims[0] / 2,30 - dims[1] / 2],"GAME OVER",fill=(255,255,255,255),font=font,align="center")
