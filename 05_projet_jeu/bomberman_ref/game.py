# IMPORT
import pygame
import time
import random

# MAP FUNCTIONS
# Create a list from a file (dimension are 20 by 15)
def parse_file(file):
    f = open(file, "r")

    L = [[0 for i in range(20)] for j in range(15)]

    for i in range(15):
        line = f.readline()
        for j in range(20):
            if line[j] == "1":
                L[i][j] = 1

    return L

# Display sprites according to map list
def parse_map(png, bomb, flame, bomb_bonus):
    rect = png.get_rect()
    rect.y = -17

    for i in range(15):
        rect.x = -11
        for j in range(20):
            if map[i][j] == 1:
                display.blit(png, rect)
            elif map[i][j] == 2:
                # Ugly but necessary to align the sprite
                rect.x += 11
                rect.y += 15
                display.blit(bomb, rect)
                rect.x -= 11
                rect.y -= 15
            elif map[i][j] == 3:
                rect.x += 11
                rect.y += 19
                display.blit(flame, rect)
                rect.x -= 11
                rect.y -= 19
            elif map[i][j] == 4:
                rect.x += 11
                rect.y += 19
                display.blit(bomb_bonus, rect)
                rect.x -= 11
                rect.y -= 19

            # Add 40 to get to the next "position" in the map
            rect.x +=  40
        rect.y += 40

# Create map
map = parse_file("map.txt")

# Start Pygame
pygame.init()

# Create display
display = pygame.display.set_mode((800,607))

# Load images
floor = pygame.image.load("sprites/grass.png").convert_alpha()
box = pygame.image.load("sprites/box.png").convert_alpha()
explo = pygame.image.load("sprites/explosion.png").convert_alpha()
bomb_sprite = pygame.image.load("sprites/bomb.png").convert_alpha()
pingu_right = pygame.image.load("sprites/tux.png").convert_alpha()
flame_bonus = pygame.image.load("sprites/flame_power.png").convert_alpha()
bomb_bonus = pygame.image.load("sprites/bomb_bonus.png").convert_alpha()

# Convert images to the right scale
explo = pygame.transform.scale(explo, (37, 37))
bomb_sprite =  pygame.transform.scale(bomb_sprite, (40, 40))
flame_bonus = pygame.transform.scale(flame_bonus, (40,40))
bomb_bonus = pygame.transform.scale(bomb_bonus, (40,40))

# Reverse images to create the opposite direction face
pingu_left = pygame.transform.flip(pingu_right, True, False)

# GLOBAL VARIABLES
sleep_time = 0.099
list_bomb = []

# CHARACTER CLASS
class Pingu:
    # All those s_* variables are the different sides of the character sprite
    def __init__(self, X, Y, s_r, s_l, s_u, s_d, s_b, username):
        pass
        # Initiate variables
        # Values in self.block are the one that collides with the player
        self.block = [1,2]
        self.username = username

        # Current looking direction (R-U-L-D)
        self.faces = [0,1,0,0]

        # End game if False
        self.is_alive = True

        # Bomb attributes (for power-ups)
        self.nb_bomb = 3
        self.radius = 1

        # Current pos of pingu
        self.coordX = X
        self.coordY = Y

        # Create sprite rectangle
        self.rect_tux = s_r.get_rect()
        self.rect_tux.x = 40 * X
        self.rect_tux.y = 40 * Y

        # Get 4 sprites (RULD)
        self.sprites = [s_r,s_u,s_l,s_d]
        self.bomb_sprite = s_b

    # Death
    def death(self):
        self.is_alive = False

    # Moves
    def move_right(self):
        self.faces = [1,0,0,0]

        # Check if the player is inside the display and not collinding with something
        if self.rect_tux.x + 40 >= 800 or map[self.coordY][self.coordX + 1] in self.block:
            return
        else:
            self.rect_tux.x += 40
            self.coordX += 1


    def move_left(self):
        self.faces = [0,0,1,0]

        if self.rect_tux.x - 40 < 0 or map[self.coordY][self.coordX - 1] in self.block:
            return
        else:
            self.rect_tux.x -= 40
            self.coordX -= 1


    def move_up(self):
        self.faces = [0,1,0,0]

        if self.rect_tux.y - 40 < 0 or map[self.coordY - 1][self.coordX] in self.block:
            return
        else:
            self.rect_tux.y -= 40
            self.coordY -= 1


    def move_down(self):
        self.faces = [0,0,0,1]

        if self.rect_tux.y + 40 >= 600 or map[self.coordY + 1][self.coordX] in self.block:
            return
        else:
            self.rect_tux.y += 40
            self.coordY += 1

    # Create a bomb to explode attached to this player
    def drop_bomb(self):
        # Prevent pygame to see more than one SPACE tap at a time.
        time.sleep(0.2)

        if self.nb_bomb > 0:
            bomb = Bomb(self.coordX, self.coordY, self.bomb_sprite, self)
            # 2 is the value in the map list for bombs
            map[self.coordY][self.coordX] = 2
            self.nb_bomb -= 1
            # Getting the tick allows to create a countdown before exploding
            tick = pygame.time.get_ticks()
            list_bomb.append((bomb, tick))

    # Check if the player is walking on a power-up and grant him power if so.
    def get_power_up(self):
        # 3 is the value in the map list for range bonus
        if map[self.coordY][self.coordX] == 3:
            self.radius += 1
            map[self.coordY][self.coordX] = 0
        # 4 is the value in the map list for bomb bonus
        elif map[self.coordY][self.coordX] == 4:
            self.nb_bomb += 1
            map[self.coordY][self.coordX] = 0

    # Display the pingu sprite according to coordinates
    def display_pingu(self):
        face_i = self.faces.index(1)
        display.blit(self.sprites[face_i], self.rect_tux)

# Create both player 
# (Spawn coordinates are hardcoded, so check that the map has free space for them)
pingu_1 = Pingu(3,1, pingu_right, pingu_left, pingu_right, pingu_right, bomb_sprite, "Player 1")
pingu_2 = Pingu(16,13, pingu_right, pingu_left, pingu_right, pingu_right, bomb_sprite, "Player 2")
players = [pingu_1, pingu_2]

# Bomb recursive explosion function
# dir is the direction for the next burst of the explosion
def explosion(x, y, dir, radius):
    # Check if x and y are out of list range
    # or stop recursion if radius is at 0
    if radius == 0 or x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
        return

    stop = False
    exp_rect = explo.get_rect()

    # Stop if the explosion is hitting a wall
    if map[y][x] == 1:
        stop = True

    power_up = random.randint(1, 10)

    if power_up > 8 and stop: # give 20% chances to create +1 range powerup
        map[y][x] = 3
    elif power_up < 2 and stop: # give 10% chances to create +1 bomb powerup
        map[y][x] = 4
    else:
        map[y][x] = 0

    # If another bomb is caught in the explosion, start the other bomb explosion.
    for bomb in list_bomb:
        if bomb[0].y == y and bomb[0].x == x:
            list_bomb.remove(bomb)
            bomb[0].explode()

    # Check if a player died on bomb
    for pingu in players:
        if pingu.coordX == x and pingu.coordY == y:
            pingu.death()

    # Print an explosion at x,y coordinates
    exp_rect.x = x * 40
    exp_rect.y = y * 40
    display.blit(explo, exp_rect)

    # Stop the recursion if the explosion touches a box
    if stop:
        return

    # Recursive call for 4 dimensions
    if dir == 1:             # up
        explosion(x - 1, y, 1, radius - 1)
    elif dir == 2:           # down
        explosion(x + 1, y, 2, radius - 1)
    elif dir == 3:           # right
        explosion(x, y + 1, 3, radius - 1)
    elif dir == 4:           # left
        explosion(x, y - 1, 4, radius - 1)


# BOMB CLASS
class Bomb:
    def __init__(self, X, Y, sprite, player):
        # Create sprite rectangle
        self.rect_bomb = sprite.get_rect()
        self.rect_bomb.x = 40 * X
        self.rect_bomb.y = 40 * Y

        # Bomb coordinates
        self.y = Y
        self.x = X

        # Bomb attributes
        self.explode_time = 3
        self.radius = player.radius
        self.owner = player

    def explode(self):
        self.owner.nb_bomb  += 1

        # Explode the current location
        explosion(self.x, self.y, 0, self.radius)

        # Recursive call on 4 dimensions
        explosion(self.x - 1, self.y, 1, self.radius)
        explosion(self.x + 1, self.y, 2, self.radius)
        explosion(self.x, self.y + 1, 3, self.radius)
        explosion(self.x, self.y - 1, 4, self.radius)

        # Sleep time to see the sprites
        time.sleep(0.06)

## Display sprites for floor
def display_floor(floor):
    rect = floor.get_rect()
    for i in range(0, 800, 40):
        rect.x = i
        for j in range(0, 600, 40):
            rect.y = j
            display.blit(floor, rect)

## Commands
def player1_moves(touches):
    pingu = players[0]

    if touches[pygame.K_RIGHT] == 1:
        pingu.move_right()
        return True

    elif touches[pygame.K_LEFT] == 1:
        pingu.move_left()
        return True

    elif touches[pygame.K_UP] == 1:
        pingu.move_up()
        return True

    elif touches[pygame.K_DOWN] == 1:
        pingu.move_down()
        return True

    elif touches[pygame.K_KP0] == 1:
        pingu.drop_bomb()

    elif touches[pygame.K_ESCAPE] == 1:
        print("Thanks for playing !")
        pygame.quit()
        exit()

    return False

def player2_moves(touches):
    pingu = players[1]

    if touches[pygame.K_d] == 1:
        pingu.move_right()
        return True

    elif touches[pygame.K_a] == 1:
        pingu.move_left()
        return True

    elif touches[pygame.K_w] == 1:
        pingu.move_up()
        return True

    elif touches[pygame.K_s] == 1:
        pingu.move_down()
        return True

    elif touches[pygame.K_SPACE] == 1:
        pingu.drop_bomb()

    return False

### MAIN ###
# Game function
def game():
    # Create the floor
    #display_floor(floor)

    # Put the boxes
    #parse_map(box, bomb_sprite, flame_bonus, bomb_bonus)

    # Game loop
    while True:

        # Create the floor
        display_floor(floor)

        # Put the boxes and power-up on the map
        parse_map(box, bomb_sprite, flame_bonus, bomb_bonus)

        # This function need to be called to make get_pressed() work
        pygame.event.get()
        touches = pygame.key.get_pressed()

        # Get moves from both players
        move_1 = player1_moves(touches)
        move_2 = player2_moves(touches)

        # Sleep time after moving players
        if move_1 or move_2:
            time.sleep(sleep_time)

        # check if players are on power-up
        for player in players:
            player.get_power_up()

        # check if players bombs need to explode
        for bomb in list_bomb:
            #calculate how many seconds has passed since the tick of bomb[1]
            seconds=(pygame.time.get_ticks()-bomb[1])/1000 
            if seconds > bomb[0].explode_time:
                list_bomb.remove(bomb)
                bomb[0].explode()

        # Display winner on console if someone wins
        for i in range(2):
            if not players[i].is_alive:
                # little python tricks ([-1] get the last of the list anyway)
                print(players[i-1].username + " wins !")
                pygame.quit()
                return

        # Display Pingus
        for pingu in players:
            pingu.display_pingu()

        # Update
        pygame.display.update()

# Launch main game function
game()
