class Snake:
    head = (5,3)
    path = [(-1,0),(-1,0),(0,1),(0,1),(1,0),(1,0),(0,1),(0,1),(-1,0),(-1,0)]
    direction = (1,0)
    next_direction = (1,0)

    def update(self):
        direction = next_direction
        self.head = (self.head[0] + self.direction[0],self.head[1] + self.direction[1])
        self.path.insert(0,(-self.direction[0],-self.direction[1]))
        self.path.pop()
