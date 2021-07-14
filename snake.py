class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.head = (9,5)
        self.path = [(-1,0),(-1,0)]
        self.direction = (1,0)
        self.move_buffer = []
        self.eaten = False

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

        if self.direction[0] > 0 or self.direction[1] > 0:
            x_offset = 30
        else:
            x_offset = 20

        draw.rectangle(
            [
                ext[0] * 60 + x_offset,
                (ext[1] - scroll) * 60 + 20,
                ext[0] * 60 + x_offset + 10,
                (ext[1] - scroll) * 60 + 30
            ],
            fill=(255,0,0,255)
        )
