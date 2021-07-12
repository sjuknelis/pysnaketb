import sys,pygame,time
import PyTouchBar as tb
from PIL import Image,ImageDraw
from game import Game

game = Game()

def render(screen,fnum):
    im = Image.new("RGBA",(1200,60),(0,0,0,255))
    draw = ImageDraw.Draw(im)
    game.render(draw,fnum)
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
                    game.snake.queue((0,-1))
                elif event.key == pygame.K_DOWN:
                    game.snake.queue((0,1))
                elif event.key == pygame.K_LEFT:
                    game.snake.queue((-1,0))
                elif event.key == pygame.K_RIGHT:
                    game.snake.queue((1,0))

        fnum += 1
        fnum %= 5
        if fnum == 0:
            game.snake.update()

        render(screen,fnum)
        pygame.display.update()
        button.image = "game.png"

        time.sleep(1/30)

if __name__ == "__main__":
    main()
