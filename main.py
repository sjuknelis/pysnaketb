import sys
import pygame
import PyTouchBar as tb

def render(screen):
    screen.fill((255, 255, 255))

def f(button):
    print("f")

def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    tb.prepare_pygame()
    button = tb.TouchBarItems.Button(title="hi",action=f,image="Chess_bdt60.png")
    tb.set_touchbar([button])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        render(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
