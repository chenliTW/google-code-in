
import pygame
from pygame.locals import *
from tkinter import messagebox
from tkinter import Tk
image_base_dir="./image/"

level_data=[
    {"img_src":"1200px-NewTux.svg.png","hint":"A kind of os","answer":"linux"},
    {"img_src":"g-monitor-fedoralogo.png","hint":"A linux distro","answer":"fedora"},
    {"img_src":"We-strive-to-be-the-best.jpg","hint":"Adj.","answer":"best"},
    {"img_src":"20180316-windows-10-background-01.jpg","hint":"A kind of os","answer":"windows"},
    {"img_src":"m$.png","hint":"A company","answer":"microsoft"},
    {"img_src":"money.jpg","hint":"A thing you user everday","answer":"money"},
    {"img_src":"thecrisis-1024x800.gif","hint":"Adj.","answer":"danger"},
    {"img_src":"open.png","hint":"A way of coding","answer":"opensource"},
    {"img_src":"good.png","hint":"Adj.","answer":"good"},
    {"img_src":"margaret_hamilton5.jpg","hint":"What this program made from","answer":"code"}
]

def main():
    pygame.init()

    gui = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("guessing game")

    font = pygame.font.SysFont(None, 40)
    small_font = pygame.font.SysFont(None, 30)
    textbox= pygame.Rect(125, 500, 600, 32)
    hintbox= pygame.Rect(100, 20, 80, 32)
    clock=pygame.time.Clock()
    for level in range(len(level_data)):
        raw_image = pygame.image.load(image_base_dir+level_data[level]["img_src"]).convert_alpha()
        image=pygame.transform.scale(raw_image, (600, 400))

        start_time=pygame.time.get_ticks()

        textbox_text = 'input answer'
        textbox_color = pygame.Color('gray')

        hinted=False

        while True:
            submit=False
            for event in pygame.event.get():
                print(event)
                if event.type == QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hintbox.collidepoint(event.pos):
                        hinted=True
                    if textbox.collidepoint(event.pos):
                        textbox_color=pygame.Color('blue')
                    else:
                        textbox_color=pygame.Color('gray')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(textbox_text)
                        submit=True
                    elif event.key == pygame.K_BACKSPACE:
                        textbox_text = textbox_text [:-1]
                    else:
                        textbox_text  += event.unicode
            if submit and textbox_text==level_data[level]["answer"]:
                break
            elif submit:
                submit=False
                textbox_text="Wrong Answer"
            gui.fill((255, 255, 255))

            countdown=(15000-(pygame.time.get_ticks()-start_time))//100/10
            if countdown<0:
                pygame.quit()
                Tk().wm_withdraw()
                messagebox.showinfo('You lose!!!','You lose!!!')
                exit(0)

            countdown_timer = font.render('time left: {}s'.format(countdown), True, (0, 0, 0))
            gui.blit(countdown_timer, (500, 25))

            gui.blit(image,(100,80))

            pygame.draw.rect(gui, textbox_color, textbox, 4)
            textbox_item= font.render(textbox_text, True,(0,0,0))
            gui.blit(textbox_item, (130,505))

            label=font.render("Answer: ",True,(0,0,0))
            gui.blit(label, (5,505))
            pygame.draw.rect(gui, (0,0,0), hintbox, 2)
            hintbox_item= font.render("HINT", True,(0,0,0))
            gui.blit(hintbox_item, (105,25))

            if hinted:
                hint=small_font.render("HINT: {}".format(level_data[level]["hint"]),True,(0,0,0))
                gui.blit(hint,(200,25))

            pygame.display.flip()
            #pygame.time.Clock().tick(60)


if __name__ == '__main__':    
    main()
    Tk().wm_withdraw()
    messagebox.showinfo('You Win!!!','You Win!!!\n connect all the answer and you will notice something;p')
    exit(0)