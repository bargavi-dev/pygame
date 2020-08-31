'''
Demo of your game
Most challenging problem - arguably everything, but making the hero disappear
Most Fun discovery- understanding the game as a part of a graph, controlling the speed of the characters
What would you do differently next time - find ways to shortcut some steps, such as in lines 140-152
'''



import pygame
import time 
import random
import math

# class Block(pygame.sprite.Sprite):
#     def __init__(self, color, width, height):
#        # Call the parent class (Sprite) constructor
#        pygame.sprite.Sprite.__init__(self)

#        self.image = pygame.Surface([width, height])
#        self.image.fill(color)
#        self.rect = self.image.get_rect()
#        self.kill()

class Hero():
        def __init__ (self, width, height):
            self.x = width/2
            self.y = height/2
            self.timer = 0
            self.speed = 4
            self.killed = False
            
            
        def move(self, width, height, x_position, y_position):
            ''' This is to create the boundaries to keep the hero within the width
            and height of the box'''
            if self.x + 32 > width: self.x = width - 32
            elif self.x < 0: self.x = 0
            if self.y < 0: self.y = 0
            elif self.y + 32 > height: self.y = height - 32

        # The player moves in the xdirection and the ydirection with a speed of 2:

        # This is to move down at level 2 speed
            if y_position == 0: self.y -= self.speed
        # This is to move up at a 2 speed
            elif y_position == 1: self.y += self.speed
        # This is to move to the right at 2 speed
            if x_position == 0: self.x += self.speed
         # This is to move to left with 2 speed   
            elif x_position == 1: self.x -= self.speed

# The villlian class is is for the Monster and Goblins
class Villian():

    def __init__ (self, width, height):
        self.x = width/10
        self.y = height/10
        self.timer = 0
        self.speed = 2
        self.x_position = random.randint(0, 1)
        self.y_position = random.randint(0, 1)
        self.killed = False

    def move(self, width, height):
#If the monster is moving right, it will come back to the left, which equals 0 
        if self.x > width: self.x = 0 
        if self.x < 0: self.x = width
        if self.y < 0: self.y = height
        if self.y > height: self.y = 0

# This part of the code is taking properties from the direction to make it go diagnal.
        if self.y_position == 0: self.y -= self.speed
        elif self.y_position == 1: self.y += self.speed
        if self.x_position == 0: self.x += self.speed
        elif self.x_position == 1:  self.x -= self.speed

class Monster(Villian):
    pass
class Goblin(Villian):
    pass


#The width and height was the measurements of our screen game.
def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Load Images
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    goblin_image = pygame.image.load('images/goblin.png'). convert_alpha()

    #Load Sounds
    win_sound = pygame.mixer.Sound ('sounds/win.wav')
    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play()
    lose_sound = pygame.mixer.Sound ('sounds/lose.wav')

    # Game initialization
    monster = Monster(width, height)
    player = Hero(width, height)
    goblin1 = Goblin(width, height)
    goblin2 = Goblin (width, height)
    goblin3 = Goblin (width, height)

#font formula from Schoology
    f = pygame.font.Font(None, 32)
    surf = f.render("Press Enter to play again", 1, (255, 0, 255))
    surf_youlose = f.render("You LOST! Press Enter to play again", 1, (255, 0, 255))

#The false statement is to say the game is still continuing 
    stop_game = False
    while not stop_game:
        monster.move(width, height)
        goblin1.move(width, height)
        goblin2.move(width, height)
        goblin3.move(width, height)
        
        for event in pygame.event.get():

        # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        #Here the distance formula is used to know when the images collide
        if math.sqrt((player.x - monster.x)**2 + (player.y - monster.y)**2) <= 32: 
            monster.killed = True
            win_sound.play()

        # The win sound plays when the hero and monster hit
        if math.sqrt((player.x - goblin1.x)**2 + (player.y - goblin1.y)**2) <= 32: 
            player.killed = True
            lose_sound.play()
            # player.kill()

        if math.sqrt((player.x - goblin2.x)**2 + (player.y - goblin2.y)**2) <= 32: 
            player.killed = True
            lose_sound.play()
            # player.kill()
           
        if math.sqrt((player.x - goblin3.x)**2 + (player.y - goblin3.y)**2) <= 32: 
            player.killed = True
            lose_sound.play()
            # player.kill()
    
        # This code is to be able to use the arrow keys to move the player
        x_position = 2
        y_position = 2
        key = pygame.key.get_pressed()

        if key [pygame.K_RIGHT]: x_position = 0
        if key [pygame.K_LEFT]: x_position = 1
        if key [pygame.K_UP]: y_position = 0
        if key [pygame.K_DOWN]: y_position = 1

        # We can try to catch the monster again after pressing enter, and the monster
        # will appear in a new random location

        if key [pygame.K_RETURN] and monster.killed:
            monster.killed = False
            monster.x = random.randint(0, width)
            monster.y = random.randint(0, height)
        if key [pygame.K_RETURN] and player.killed:
            player.killed = False
            player.x = random.randint(0, width)
            player.y = random.randint(0, height)


        player.move(width, height, x_position, y_position)

        # Draw background
        screen.blit(background_image, [0, 0])
        screen.blit(hero_image, [player.x, player.y])
        screen.blit(goblin_image, [goblin1.x, goblin1.y])
        screen.blit(goblin_image, [goblin2.x, goblin2.y])
        screen.blit(goblin_image, [goblin3.x, goblin3.y])
        if not monster.killed:
            screen.blit(monster_image, [monster.x, monster.y])
        if monster.killed:
            screen.blit(surf, [width/5, height/2])
        
        # if not player.killed:
        #     screen.blit(hero_image, [player.x, player.y])
        # if player.killed:
        #     screen.blit(surf_youlose, [width/5, height/2]

        # Game display

        pygame.display.update()
        monster.timer += clock.tick(60)

        if monster.timer >= 2000:
            monster.timer = 0
#The random function will redirect the monster into another direction inside the box.
            monster.x_position = random.randint(0, 1)
            monster.y_position = random.randint(0, 1)

            goblin1.x_position = random.randint(0, 1)
            goblin1.y_position = random.randint(0, 1)

            goblin2.x_position = random.randint(0, 1)
            goblin2.y_position = random.randint(0, 1)

            goblin3.x_position = random.randint(0, 1)
            goblin3.y_position = random.randint(0, 1)

    pygame.quit()

if __name__ == '__main__':
    main()