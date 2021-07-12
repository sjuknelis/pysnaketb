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
