import sys,pygame,time
import PyTouchBar as tb
from PIL import Image,ImageDraw
from game import Snake

snake = Snake()

def render(screen,fnum):
    im = Image.new("RGBA",(1200,60),(0,0,0,255))
    draw = ImageDraw.Draw(im)

    scroll = snake.head[1] + snake.direction[1] * 0.2 * fnum

    pos = list(snake.head)
    last = list(pos)
    for (index,item) in enumerate(snake.path):
        pos[0] += item[0]
        pos[1] += item[1]
        if index == len(snake.path) - 1:
            pos[0] -= item[0] * 0.2 * fnum
            pos[1] -= item[1] * 0.2 * fnum
        if abs(pos[1] - snake.head[1]) <= 1:
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

    ext = (snake.head[0] + snake.direction[0] * 0.2 * fnum,snake.head[1] + snake.direction[1] * 0.2 * fnum)
    draw.rectangle(
        [
            min(snake.head[0],ext[0]) * 60 + 10,
            (min(snake.head[1],ext[1]) - scroll) * 60 + 10,
            max(snake.head[0],ext[0]) * 60 + 50,
            (max(snake.head[1],ext[1]) - scroll) * 60 + 50
        ],
        fill=(0,255,0,255)
    )

    if snake.head[1] <= 2:
        draw.rectangle(
            [10,(- scroll) * 60,1190,(- scroll + 1) * 60 + 5],
            fill=(0,255,0,255)
        )
    if snake.head[1] >= 18:
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

    im.save("game.png")

    screen.fill((255,255,255))

def f(button):
    print("f")

def main():
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
                    snake.queue((0,-1))
                elif event.key == pygame.K_DOWN:
                    snake.queue((0,1))
                elif event.key == pygame.K_LEFT:
                    snake.queue((-1,0))
                elif event.key == pygame.K_RIGHT:
                    snake.queue((1,0))

        fnum += 1
        fnum %= 5
        if fnum == 0:
            snake.update()

        render(screen,fnum)
        pygame.display.update()
        button.image = "game.png"

        time.sleep(1/30)

if __name__ == "__main__":
    main()
