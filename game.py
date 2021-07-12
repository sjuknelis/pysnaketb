class Snake:
    head = (5,3)
    path = [(-1,0),(-1,0),(0,1),(0,1),(1,0),(1,0),(0,1),(0,1),(-1,0),(-1,0)]
    direction = (1,0)
    move_buffer = []

    def update(self):
        self.head = (self.head[0] + self.direction[0],self.head[1] + self.direction[1])
        self.path.insert(0,(-self.direction[0],-self.direction[1]))
        self.path.pop()

        if len(self.move_buffer) > 0:
            for (index,item) in enumerate(self.move_buffer):
                if item != self.direction and item != (-self.direction[0],-self.direction[1]):
                    self.direction = item
                    del self.move_buffer[index]
                    break

    def queue(self,direction):
        self.move_buffer.insert(0,direction)

    def render(self,draw,fnum):
        scroll = self.head[1] + self.direction[1] * 0.2 * fnum
        pos = list(self.head)
        last = list(pos)
        for (index,item) in enumerate(self.path):
            pos[0] += item[0]
            pos[1] += item[1]
            if index == len(self.path) - 1:
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
    apple = (10,10)

    def render(self,draw,fnum):
        scroll = self.snake.head[1] + self.snake.direction[1] * 0.2 * fnum

        self.snake.render(draw,fnum)

        if self.snake.head[1] <= 2:
            draw.rectangle(
                [10,(- scroll) * 60,1190,(- scroll + 1) * 60 + 5],
                fill=(0,255,0,255)
            )
        if self.snake.head[1] >= 18:
            draw.rectangle(
                [10,(20 - scroll) * 60 - 5,1190,(20 - scroll + 1) * 60],
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
