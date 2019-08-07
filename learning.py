import gamebox
import pygame

screen = gamebox.Camera(800, 600)

main_character = gamebox.from_color(400,300,"red",20,20)
police1 = gamebox.from_color(200,500,"blue",20,20)
police2 = police1.copy_at(500,200)
police_list = [police1,police2]
sighted = [0,0]

def main_character_mov(value):
    if(value == 1):                      #move right
        main_character.x += 2
    if(value == 2):                          #move left
        main_character.x -= 2
    if(value == 3):                      #jump up
        main_character.y -= 6

def police_movement(value,police_number):
    if(value == 1):      #passive state
        for i in range(10):
            police_list[police_number].x += 2




def main(keys):
    screen.clear("black")
    screen.draw(main_character)
    for hostiledrawn in range(len(police_list)):
        screen.draw(police_list[hostiledrawn])

    for i in range(len(police_list)):
        police_movement(1,i)

    if pygame.K_SPACE in keys:
        main_character_mov(3)
    if pygame.K_a in keys:
        main_character_mov(2)
    if pygame.K_d in keys:
        main_character_mov(1)
    screen.display()


gamebox.timer_loop(30, main)