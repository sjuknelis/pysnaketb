import sys,pygame,time
import PyTouchBar as tb
from PIL import Image,ImageDraw
from game import Game

FONT_PATH = "CourierPrime-Regular.ttf"

reset = False

def render(screen,game,fnum):
    im = Image.new("RGBA",(1200,60),(0,0,0,255))
    draw = ImageDraw.Draw(im)
    game.render(draw,fnum,FONT_PATH)
    im.save("game.png")

    screen.fill((255,255,255))

    if game.game_over:
        text = ["Game over","Score: " + str(len(game.snake.path) + 1),"","Tap the touchbar","to play again"]
        color = (255,0,0)
    elif game.win:
        text = ["You win!","","Tap the touchbar","to play again"]
        color = (0,200,200)
    else:
        text = ["Play on the touchbar"]
        color = (0,0,0)

    for (index,line) in enumerate(text):
        font = pygame.font.Font(FONT_PATH,20)
        rendered = font.render(line,False,color)
        text_rect = rendered.get_rect(center=(150,150 + 20 * (-len(text) / 2 + index)))
        screen.blit(rendered,text_rect)

def button_press(button):
    global reset
    reset = True

def main():
    global reset
    game = Game()

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((300,300))

    tb.prepare_pygame()
    button = tb.TouchBarItems.Button(
        title=None,
        action=button_press,
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

        fnum = (fnum + 1) % 5
        if fnum == 0:
            game.update()
            if reset:
                game.reset()
                reset = False

        render(screen,game,fnum)
        pygame.display.update()
        button.image = "game.png"

        time.sleep(1/30)

if __name__ == "__main__":
    main()
