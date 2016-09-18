import pygame
import random
from Player import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.direction=random.randint(-1,1)
        self.facing = 0
        self.counter=0
        self.face_time=0
        self.stop=0
        self.paralyze=0
        self.image = pygame.image.load("images/NeutralEnemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(400,900)
        self.rect.y = 530
        self.bullet_group=pygame.sprite.Group()
        
    def update(self,player,all_group):
        if abs(self.rect.x-player.rect.x)>350:
            if self.rect.x<50 or self.rect.x>1030:
                self.direction=-self.facing
            elif self.face_time>1:
                self.direction=random.randint(-1,1)
                self.face_time=0
            if (self.direction==-1):
                self.facing=-1
                self.counter += 1
                if self.counter < 6:
                    self.image = pygame.image.load("images/EnemyWalking1Left.png")
                if self.counter >= 6 and self.counter < 12:
                    self.image = pygame.image.load("images/EnemyWalking2Left.png")
                if self.counter >= 12 and self.counter < 18:
                    self.image = pygame.image.load("images/EnemyWalking3Left.png")
                if self.counter >= 18 and self.counter < 24:
                    self.image = pygame.image.load("images/EnemyWalking4Left.png")
                if self.counter >= 24 and self.counter < 30:
                    self.image = pygame.image.load("images/EnemyWalking5Left.png")
                if self.counter >= 30 and self.counter < 36:
                    self.image = pygame.image.load("images/EnemyWalking6Left.png")
                if self.counter >= 36 and self.counter < 42:
                    self.image = pygame.image.load("images/EnemyWalking7Left.png")
                if self.counter >= 42 and self.counter < 48:
                    self.image = pygame.image.load("images/EnemyWalking8Left.png")
                if self.counter >= 48:
                    self.counter = 0
                    self.face_time+=1
                self.rect.x -= 3
            elif (self.direction==1):
                self.facing=1
                self.counter += 1            
                if self.counter < 6:
                    self.image = pygame.image.load("images/EnemyWalking1.png")
                if self.counter >= 6 and self.counter < 12:
                    self.image = pygame.image.load("images/EnemyWalking2.png")
                if self.counter >= 12 and self.counter < 18:
                    self.image = pygame.image.load("images/EnemyWalking3.png")
                if self.counter >= 18 and self.counter < 24:
                    self.image = pygame.image.load("images/EnemyWalking4.png")
                if self.counter >= 24 and self.counter < 30:
                    self.image = pygame.image.load("images/EnemyWalking5.png")
                if self.counter >= 30 and self.counter < 36:
                    self.image = pygame.image.load("images/EnemyWalking6.png")
                if self.counter >= 36 and self.counter < 42:
                    self.image = pygame.image.load("images/EnemyWalking7.png")
                if self.counter >= 42 and self.counter < 48:
                    self.image = pygame.image.load("images/EnemyWalking8.png")
                if self.counter >= 48:
                    self.counter = 0
                    self.face_time+=1            
                self.rect.x += 3
            else:
                self.counter+=1
                if self.facing == 1:
                    self.image = pygame.image.load("images/NeutralEnemy.png")
                if self.facing == -1:
                    self.image = pygame.image.load("images/NeutralEnemyLeft.png") 
                if self.counter >=48:
                    self.counter=0
                    self.face_time+=1
        else:
            if self.stop>0:
                if self.stop>24:
                    self.stop=0
                    self.shoot(all_group)
                else:
                    if self.facing == 1:
                        self.shoot(all_group)
                    if self.facing == -1:
                        self.shoot(all_group) 
                    self.stop+=1
            elif abs(player.rect.x-self.rect.x)<80:
                self.stop=1
                self.shoot(all_group)
            elif player.rect.x<self.rect.x:
                if self.direction ==-1:
                    self.counter+=1
                    if self.counter < 6:
                        self.image = pygame.image.load("images/EnemyWalking1Left.png")
                    if self.counter >= 6 and self.counter < 12:
                        self.image = pygame.image.load("images/EnemyWalking2Left.png")
                    if self.counter >= 12 and self.counter < 18:
                        self.image = pygame.image.load("images/EnemyWalking3Left.png")
                    if self.counter >= 18 and self.counter < 24:
                        self.image = pygame.image.load("images/EnemyWalking4Left.png")
                    if self.counter >= 24 and self.counter < 30:
                        self.image = pygame.image.load("images/EnemyWalking5Left.png")
                    if self.counter >= 30 and self.counter < 36:
                        self.image = pygame.image.load("images/EnemyWalking6Left.png")
                    if self.counter >= 36 and self.counter < 42:
                        self.image = pygame.image.load("images/EnemyWalking7Left.png")
                    if self.counter >= 42 and self.counter < 48:
                        self.image = pygame.image.load("images/EnemyWalking8Left.png")
                    if self.counter >= 48:
                        self.counter = 0
                    self.rect.x -= 3
                    self.shoot(all_group)
                else:
                    self.direction=-1
                    self.counter=0
                    self.facing=-1
            else:
                if self.direction==1:
                    self.counter+=1
                    if self.counter < 6:
                        self.image = pygame.image.load("images/EnemyWalking1.png")
                    if self.counter >= 6 and self.counter < 12:
                        self.image = pygame.image.load("images/EnemyWalking2.png")
                    if self.counter >= 12 and self.counter < 18:
                        self.image = pygame.image.load("images/EnemyWalking3.png")
                    if self.counter >= 18 and self.counter < 24:
                        self.image = pygame.image.load("images/EnemyWalking4.png")
                    if self.counter >= 24 and self.counter < 30:
                        self.image = pygame.image.load("images/EnemyWalking5.png")
                    if self.counter >= 30 and self.counter < 36:
                        self.image = pygame.image.load("images/EnemyWalking6.png")
                    if self.counter >= 36 and self.counter < 42:
                        self.image = pygame.image.load("images/EnemyWalking7.png")
                    if self.counter >= 42 and self.counter < 48:
                        self.image = pygame.image.load("images/EnemyWalking8.png")
                    if self.counter >= 48:
                        self.counter = 0           
                    self.rect.x += 3
                    self.shoot(all_group)
                else:
                    self.direction=1
                    self.counter=0
                    self.facing=1
        for b in self.bullet_group:
            if b.rect.x < 0 or b.rect.x > 1080:
                all_group.remove(b)
                self.bullet_group.remove(b)
            elif b.bfacing == 0:
                b.update_r()
            else:
                b.update_l()

    def shoot(self,all_group):
        bullet=Bullet(self)
        if self.paralyze>0:
            if self.paralyze>80:
                self.paralyze=0
            else:
                if self.facing == 1:
                    self.image = pygame.image.load("images/EnemyShootingStance.png")
                if self.facing == -1:
                    self.image = pygame.image.load("images/EnemyShootingStanceLeft.png")
                self.paralyze+=1
        else:
            all_group.add(bullet)
            self.bullet_group.add(bullet)
            if self.facing == 1:
                self.image = pygame.image.load("images/EnemyShootingStance.png")
                bullet.bfacing = 0
                bullet.rect.x = self.rect.x + 65
                bullet.rect.y = self.rect.y + 22
            if self.facing == -1:
                self.image = pygame.image.load("images/EnemyShootingStanceLeft.png")
                bullet.bfacing = 1
                bullet.rect.x = self.rect.x - 16
                bullet.rect.y = self.rect.y + 22
            self.paralyze=1

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.rect.x, self.y))