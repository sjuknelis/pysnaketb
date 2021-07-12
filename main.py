import sys,pygame,time
import PyTouchBar as tb
from PIL import Image,ImageDraw
from game import Snake

snake = Snake()

def render(screen,fnum):
    im = Image.new("RGBA",(1200,60),(0,0,0,255))
    draw = ImageDraw.Draw(im)

    pos = list(snake.head)
    last = list(pos)
    for item in snake.path:
        pos[0] += item[0]
        pos[1] += item[1]
        if abs(pos[1] - snake.head[1]) <= 1:
            draw.rectangle(
                [
                    min(pos[0],last[0]) * 60 + 10,
                    (min(pos[1],last[1]) - snake.head[1]) * 60 + 10,
                    max(pos[0],last[0]) * 60 + 50,
                    (max(pos[1],last[1]) - snake.head[1]) * 60 + 50
                ],
                fill=(0,255,0,255)
            )
        last = list(pos)
        
    draw.rectangle(
        [0,0,60,60],
        fill=(0,255,0,255)
    )
    draw.rectangle(
        [1140,0,1200,60],
        fill=(0,255,0,255)
    )

    im.save("game.png")

    screen.fill((255,255,255))

def f(button):
    print("f")

def pmain():
    pygame.init()
    screen = pygame.display.set_mode((200,200))

    tb.prepare_pygame()
    button = tb.TouchBarItems.Button(
        title=None,
        action=f,
        color=tb.Color.black,
        image_position=tb.ImagePosition.imageonly,
        image="game.png"
    )
    tb.set_touchbar([button])

    fnum = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.next_direction = (0,-1)
                elif event.key == pygame.K_DOWN:
                    snake.next_direction = (0,1)
                elif event.key == pygame.K_LEFT:
                    snake.next_direction = (-1,0)
                elif event.key == pygame.K_RIGHT:
                    snake.next_direction = (1,0)
        render(screen,fnum)
        pygame.display.update()

        fnum += 1
        fnum %= 5
        if fnum == 4:
            snake.update()
        button.image = "game.png"
        time.sleep(1/30)

if __name__ == "__main__":
    pmain()
