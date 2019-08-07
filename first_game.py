#Rakshith Raghu(rr5de)
import pygame
import gamebox


camera = gamebox.Camera(800,600)


#prep work:the boxes, sounds, and variables
logo = gamebox.from_image(0,0, "http://www.pygame.org/docs/_static/pygame_tiny.png")
#music = gamebox.load_sound("https://commons.wikimedia.org/wiki/File:Flow,_my_tears.ogg")    #audio from audioblocks
score = 0
main_character = gamebox.from_image(20,20, "http://opengameart.org/sites/default/files/styles/medium/public/archer.png") #image from opengameart
coin = gamebox.from_image(20,20, "http://www.superluigibros.com/images/sprites/3ds/nsmb2/StarCoin___NSMB2.png")
grass = gamebox.from_image(1000,100,"http://orig06.deviantart.net/27bc/f/2013/356/7/2/grass_field_backround_by_imtooyoungtobehere-d6yyln0.png")
tower = gamebox.from_image(10,10,"http://opengameart.org/sites/default/files/Tower_1.png")

title = gamebox.from_text(390,50,"Collect the Coins!","Times New Roman",20, "white", bold=True)
enter = gamebox.from_text(390,100,"Press space to began","Times New Roman", 20, "white", bold=True)
directions = gamebox.from_text(390,400, "Directions: press space to jump, arrows keys to move","Times New Roman", 15,"white", bold=True)

walls = [grass,tower]
main_character1 = main_character.copy_at(50,100)
main_character.center = [50,540]
tower.center = [700,460]
grass.size= 1000,100
grass.center = [350,550]
coin1 = coin
coin1.center = [490,520]
coin2= coin.copy_at(300,400)
coin3 = coin.copy_at(120,490)
coins = [0,0,0]
time = 20
pressed = False

def ticks(keys):
    global time
    global pressed
    count = coins[1] + coins[0] + coins[2]
    count_str = "The coins collected is:" + str(count)
    counter = gamebox.from_text(390,100,count_str,"Times New Roman",20,"black", bold=True)
    if time > 0 and sum(coins) < 3 and pressed == True:
        time -= .07
    timer = gamebox.from_text(390,50,'There is ' + str(int(time)) + ' seconds left', "Times New Roman", 20, "black", bold=True)

    if(pressed == False):
        camera.clear("black")
        camera.draw(title)
        camera.draw(enter)
        camera.draw(directions)
        if pygame.K_SPACE in keys:
            pressed = True
    else:
        if time > 0 and sum(coins) < 3:

            camera.clear("lightblue")
            camera.draw(grass)
            camera.draw(tower)
            camera.draw(counter)
            camera.draw(timer)

            if coins[0] == 0:    #draws coins
                camera.draw(coin1)
            if coins[1] == 0:
                camera.draw(coin2)
            if coins[2] == 0:
                camera.draw(coin3)

            camera.draw(main_character)

            if pygame.K_SPACE in keys and main_character.bottom_touches(grass):           #controls to move character
                main_character.y -= 100
            if main_character.bottom_touches(grass) == False and main_character.top_touches(grass) == False:
                main_character.y += 4
            if pygame.K_RIGHT  in keys:
               main_character.x += 5
               #camera.move(5,0)
            if pygame.K_LEFT in keys:
              main_character.x -= 5
              #camera.move(-5,0)
            if pygame.K_UP in keys:
                main_character.y -= 3
            if pygame.K_DOWN in keys and main_character.bottom_touches(grass) == True:
                main_character.y += 3

            if main_character.top_touches(coin1):     #collects coins
                coins[0] = 1
            if main_character.touches(coin2):
                coins[1] = 1
            if main_character.touches(coin3):
                coins[2] = 1
        else:
            if(sum(coins) < 3):
                camera.clear("black")
                timer = gamebox.from_text(390,50,'You had ' + str(int(time)) + ' seconds left', "Times New Roman", 20, "white", bold=True)
                lose = gamebox.from_text(390,100,"You failed the game since you only collected:" + str(sum(coins)) + " coins","Times New Roman",20,"white", bold=True)
                camera.draw(timer)
                camera.draw(lose)
            if(sum(coins) == 3):
                camera.clear("black")
                timer = gamebox.from_text(390,50,'You had ' + str(int(time)) + ' seconds left', "Times New Roman", 20, "white", bold=True)
                lose = gamebox.from_text(390,100,"You win, Congratulations!" ,"Times New Roman",20,"white", bold=True)
                camera.draw(timer)
                camera.draw(lose)
    camera.display()

gamebox.timer_loop(30, ticks)