import pygame
pygame.init()

win = pygame.display.set_mode((400, 400))

pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png')]
walkLeft = [pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png'),pygame.image.load('s2.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('s2.png')

clock = pygame.time.Clock()

score = 0

screenWidth = 400
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 8
        self.standing = True
        self.hitbox = (self.x + 5, self.y + 16, 36, 54)

    def draw(self, win):
        if self.walkCount + 1 >= 21:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1

        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 5, self.y + 16, 36, 54)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 21 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('e1.png'), pygame.image.load('e1.png'), pygame.image.load('e1.png'),
                 pygame.image.load('e1.png'), pygame.image.load('e1.png'), pygame.image.load('e1.png'),
                 pygame.image.load('e1.png')]
    walkLeft = [pygame.image.load('e1.png'), pygame.image.load('e1.png'), pygame.image.load('e1.png'),
                 pygame.image.load('e1.png'), pygame.image.load('e1.png'), pygame.image.load('e1.png'),
                 pygame.image.load('e1.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 8
        self.hitbox = (self.x + 2, self.y + 2, 54, 52)
        self.health = 9
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[0], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 2, self.y + 2, 54, 52)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (100, 100, 0))
    win.blit(text, (320, 80))
    man.draw(win)
    food.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

#mainloop
font = pygame.font.SysFont('comicsans', 24, True)
man = player(195, 330, 50,87)
food = enemy(5,3,60,53,320)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(21)
    pygame.time.delay(100)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    for bullet in bullets:
        if bullet.y - bullet.radius < food.hitbox[1] + food.hitbox[3] and bullet.y + bullet.radius > food.hitbox[1]:
            if bullet.x + bullet.radius > food.hitbox[0] and bullet.x - bullet.radius < food.hitbox[0] + \
                    food.hitbox[2]:
                food.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.y < 400 and bullet.y > 0:
            bullet.y += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 405 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -8:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
