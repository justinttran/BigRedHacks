import pygame,sys,random
from Player import Player
from Enemy import Enemy
from Player import Bullet
#from Bullet import Bullet

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [1080, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Secret Operatives')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

background = pygame.image.load("images/GUI.png").convert_alpha()
screen.blit(background, (0,0))
myfont = pygame.font.SysFont("monospace", 20)

# render text
label = myfont.render("This is a sustainable app. Trust me", True, (255,255,0))
screen.blit(label, (100, 100))



all_group = pygame.sprite.Group()
free_bullet_group = pygame.sprite.Group()
player = Player()
enemy_group = pygame.sprite.Group()
for _ in range(random.randint(1,3)):
    enemy_group.add(Enemy())



counter = 0
standing = 1
velocity = 0
state=0

#all_group = pygame.sprite.Group()
for enemy in enemy_group:
    all_group.add(enemy)



# Loop until the user clicks close button
while True:
    bullet = Bullet(player)
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # write game logic here
 
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 
    # write draw code here
    screen.blit(background, (0, 0))
    if state == 0:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                background = pygame.image.load("images/BackgroundSavannah.png").convert_alpha()
                screen.blit(background, (0,0))
                all_group.add(player)
                for enemy in enemy_group:
                    all_group.add(enemy)
                state = 1
                
            if event.key == pygame.K_2:
                background = pygame.image.load("images/BackgroundForest.png").convert_alpha()
                screen.blit(background, (0,0))
                all_group.add(player)
                for enemy in enemy_group:
                    all_group.add(enemy)
                state = 1
            
            if event.key == pygame.K_3:
                background = pygame.image.load("images/BackgroundArctic.png").convert_alpha()
                screen.blit(background, (0,0))
                all_group.add(player)
                for enemy in enemy_group:
                    all_group.add(enemy)
                state = 1
            
            if event.key == pygame.K_4:
                background = pygame.image.load("images/BackgroundCornell.png").convert_alpha()
                screen.blit(background, (0,0))
                all_group.add(player)
                for enemy in enemy_group:
                    all_group.add(enemy)
                state = 1

    if state==1:
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                if player.rect.x<0:
                    player.rect.x=0
                if player.rect.x>1019:
                    player.rect.x=1019    
                player.direction = 1
                counter += 1
                player.facing = 1
                
                if player.rect.y < 530:
                    velocity -= 1
                    player.rect.y = player.rect.y - velocity
                
                if player.rect.y > 530:
                    player.rect.y = 530

                if counter < 6:
                    player.image = pygame.image.load("images/Walking1Left.png")
                if counter >= 6 and counter < 12:
                    player.image = pygame.image.load("images/Walking2Left.png")
                if counter >= 12 and counter < 18:
                    player.image = pygame.image.load("images/Walking3Left.png")
                if counter >= 18 and counter < 24:
                    player.image = pygame.image.load("images/Walking4Left.png")
                if counter >= 24 and counter < 30:
                    player.image = pygame.image.load("images/Walking5Left.png")
                if counter >= 30 and counter < 36:
                    player.image = pygame.image.load("images/Walking6Left.png")
                if counter >= 36 and counter < 42:
                    player.image = pygame.image.load("images/Walking7Left.png")
                if counter >= 42 and counter < 48:
                    player.image = pygame.image.load("images/Walking8Left.png")
                if counter >= 48:
                    counter = 0
            elif (event.key == pygame.K_RIGHT):
                if player.rect.x<0:
                    player.rect.x=0
                if player.rect.x>1019:
                    player.rect.x=1019 
                player.direction = 2
                counter += 1
                player.facing = 0
                
                if player.rect.y < 530:
                    velocity -= 1
                    player.rect.y = player.rect.y - velocity    
                
                if player.rect.y > 530:
                    player.rect.y = 530

                if counter < 6:
                    player.image = pygame.image.load("images/Walking1.png")
                if counter >= 6 and counter < 12:
                    player.image = pygame.image.load("images/Walking2.png")
                if counter >= 12 and counter < 18:
                    player.image = pygame.image.load("images/Walking3.png")
                if counter >= 18 and counter < 24:
                    player.image = pygame.image.load("images/Walking4.png")
                if counter >= 24 and counter < 30:
                    player.image = pygame.image.load("images/Walking5.png")
                if counter >= 30 and counter < 36:
                    player.image = pygame.image.load("images/Walking6.png")
                if counter >= 36 and counter < 42:
                    player.image = pygame.image.load("images/Walking7.png")
                if counter >= 42 and counter < 48:
                    player.image = pygame.image.load("images/Walking8.png")
                if counter >= 48:
                    counter = 0
            elif (event.key == pygame.K_UP):
                if player.rect.x<0:
                    player.rect.x=0
                if player.rect.x>1019:
                    player.rect.x=1019 
                if player.facing == 0 and player.rect.y != 530:
                    if counter < 8:
                        player.image = pygame.image.load("images/Jump1.png")
                    if counter >= 8 and counter < 16:
                        player.image = pygame.image.load("images/Jump2.png")
                    if counter >= 16 and counter < 24:
                        player.image = pygame.image.load("images/Jump3.png")
                    if counter >= 24 and counter < 32:
                        player.image = pygame.image.load("images/Jump4.png")
                    if counter >= 32 and counter < 40:
                        player.image = pygame.image.load("images/Jump5.png")
                        
                if player.facing == 1 and player.rect.y != 530:
                    if counter < 8:
                        player.image = pygame.image.load("images/Jump1Left.png")
                    if counter >= 8 and counter < 16:
                        player.image = pygame.image.load("images/Jump2Left.png")
                    if counter >= 16 and counter < 24:
                        player.image = pygame.image.load("images/Jump3Left.png")
                    if counter >= 24 and counter < 32:
                        player.image = pygame.image.load("images/Jump4Left.png")
                    if counter >= 32 and counter < 40:
                        player.image = pygame.image.load("images/Jump5Left.png")
                
                if standing == 1 and player.rect.y == 530:
                    counter += 1
                    standing = 0
                    velocity = 20
                    player.rect.y -= velocity
                if standing == 0:
                    if player.rect.y < 530:
                        counter += 1
                        velocity -= 1
                        player.rect.y = player.rect.y - velocity
                    if player.rect.y == 530:
                        if player.facing == 0:
                            player.image = pygame.image.load("images/Neutral.png")
                        if player.facing == 1:
                            player.image = pygame.image.load("images/NeutralLeft.png")


                
            elif (event.key == pygame.K_DOWN):
                if player.rect.x<0:
                    player.rect.x=0
                if player.rect.x>1019:
                    player.rect.x=1019 
                player.direction = 4
                if player.rect.y < 530:
                    velocity -= 1
                    player.rect.y = player.rect.y - velocity
                if player.rect.y > 530:
                    player.rect.y = 530
                if player.rect.y == 530:
                    player.rect.y = 571
                if player.facing == 0:
                    player.image = pygame.image.load("images/Crouch.png")
                if player.facing == 1:
                    player.image = pygame.image.load("images/CrouchLeft.png")
            
            elif (event.key == pygame.K_SPACE):
                if player.rect.x<0:
                    player.rect.x=0
                if player.rect.x>1019:
                    player.rect.x=1019 
                if player.rect.y < 530:
                    velocity -= 1
                    player.rect.y = player.rect.y - velocity
                if player.rect.y > 530:
                    player.rect.y = 530   
                if player.paralyze>0:
                    if player.paralyze>8:
                        player.paralyze=0
                    else:
                        if player.facing == 0:
                            player.image = pygame.image.load("images/ShootingStance.png")
                        if player.facing == 1:
                            player.image = pygame.image.load("images/ShootingStanceLeft.png")
                        player.paralyze+=1
                else:
                    all_group.add(bullet)
                    player.bullet_group.add(bullet)
                    if player.facing == 0:
                        player.image = pygame.image.load("images/ShootingStance.png")
                        bullet.bfacing = 0
                        bullet.rect.x = player.rect.x + 65
                        bullet.rect.y = player.rect.y + 22
                    if player.facing == 1:
                        player.image = pygame.image.load("images/ShootingStanceLeft.png")
                        bullet.bfacing = 1
                        bullet.rect.x = player.rect.x - 16
                        bullet.rect.y = player.rect.y + 22
                    player.paralyze=1
        else:
            if player.rect.x<0:
                player.rect.x=0
            if player.rect.x>1019:
                player.rect.x=1019 
            player.direction = 0
            counter = 0
            if player.rect.y == 530:
                standing = 1
            if player.rect.y < 530:
                velocity -= 1
                player.rect.y = player.rect.y - velocity
            if player.rect.y > 530:
                player.rect.y = 530
            if player.facing == 0:
                player.image = pygame.image.load("images/Neutral.png")
            if player.facing == 1:
                player.image = pygame.image.load("images/NeutralLeft.png")


        for abullet in player.bullet_group:
            
            # See if it hit a block
            enemy_hit_list = pygame.sprite.spritecollide(abullet, enemy_group, True)
            if len(enemy_group)==0:
                state=2
                all_group.empty()
                enemy_group.empty()
                free_bullet_group.empty()
                continue
            #remove player bullet if it hits target enemy
            if len(enemy_hit_list) >=1:
                player.bullet_group.remove(abullet)
                all_group.remove(abullet)

            for enemy in enemy_hit_list:
                for b in enemy.bullet_group:
                    free_bullet_group.add(b)
                all_group.remove(enemy)

        
        #display the screen
        player.update()
        for enemy in enemy_group:
            enemy.update(player,all_group)
        
        for b in player.bullet_group:
            if b.rect.x < 0 or b.rect.x > 1080:
                all_group.remove(b)
                player.bullet_group.remove(b)
            elif b.bfacing == 0:
                b.update_r()
            else:
                b.update_l()
        for b in free_bullet_group:
            if b.rect.x < 0 or b.rect.x > 1080:
                all_group.remove(b)
                player.bullet_group.remove(b)
            elif b.bfacing == 0:
                b.update_r()
            else:
                b.update_l()
        bk=0
        for enemy in enemy_group:
            if len(pygame.sprite.spritecollide(player, enemy.bullet_group, True))>=1:
                all_group.remove(player)
                bk=1
        if bk==1:
            state=3
            all_group.empty()
            enemy_group.empty()
            free_bullet_group.empty()
            continue

        label = myfont.render("This is a sustainable app. Your goal is the kill the poacher, ", True, (0,0,0))
        label2 = myfont.render("who is about to kill HARAMBE. Please save him.", True, (0,0,0))
        screen.blit(label, (100, 100))
        screen.blit(label2, (100, 200))
        all_group.draw(screen)
    #end screen
    if state==2:
        label = myfont.render("Congratulations!", True, (0,0,0))
        label2 = myfont.render("You Have Achieved World Peace!", True, (0,0,0))
        label3 = myfont.render("Press Enter to Restart!", True, (0,0,0))
        screen.blit(label, (100, 100))
        screen.blit(label2, (100, 200))
        screen.blit(label3, (100, 300))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            player=Player()
            for _ in range(random.randint(1,3)):
                enemy_group.add(Enemy())
            background = pygame.image.load("images/GUI.png").convert_alpha()
            state = 0
    if state==3:
        label = myfont.render("Oh No! Harambe Is Doomed!", True, (0,0,0))
        label2 = myfont.render("Press Enter to Restart!", True, (0,0,0))
        screen.blit(label, (100, 100))
        screen.blit(label2, (100, 200))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            player=Player()
            for _ in range(random.randint(1,3)):
                enemy_group.add(Enemy())
            background = pygame.image.load("images/GUI.png").convert_alpha()
            state = 0
    clock.tick(60)
 
 
# close the window and quit
    pygame.display.update()