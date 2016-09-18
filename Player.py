import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        lives = 3
        self.direction = 0
        self.facing = 0
        self.image = pygame.image.load("images/Neutral.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 530
        self.paralyze=0
        self.bullet_group=pygame.sprite.Group()
        
    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.x -= 6

        if key[pygame.K_RIGHT]:
            self.rect.x += 6

        if key[pygame.K_UP]:
            self.rect.y -= 0

        if key[pygame.K_DOWN]:
            self.rect.y += 0
        # if self.direction == 1:
        #     self.rect.x -= 6
        # if self.direction == 2:
        #     self.rect.x += 6
        # if self.direction == 3:
        #     self.rect.y -= 0
        # if self.direction == 4:
        #     self.rect.y += 0

    
    def draw(self, surface):
        
        # blit yourself at your current position
        surface.blit(self.image, (self.rec.x, self.rec.y))

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self,player):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()
        self.image = pygame.image.load("images/Bullet.png")
        self.image2 = pygame.image.load("images/BulletLeft.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 58
        self.rect.y = player.rect.y + 24
        self.bfacing = 0
 
    def update_r(self):
        
        self.rect.x += 6
    
    def update_l(self):
        self.rect.x -= 6
    
    def draw(self, surface):
        
        # blit yourself at your current position
        if player.facing == 0:
            surface.blit(self.image, (player.rect.x + 58, player.y + 24))
        if player.facing == 1:
            surface.blit(self.image2, (player.rect.x, player.y + 24))