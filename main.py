import sys,pygame,time
import PyTouchBar as tb
from PIL import Image,ImageDraw

def render(screen,fnum):
    im = Image.new("RGBA",(1200,60),(0,0,0,255))
    draw = ImageDraw.Draw(im)
    draw.rectangle([fnum,20,fnum + 20,40],outline = (255,255,255,255))
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
        render(screen,fnum)
        pygame.display.update()

        fnum += 10
        fnum %= 1200
        button.image = "game.png"
        time.sleep(1/30)


if __name__ == "__main__":
    pmain()
