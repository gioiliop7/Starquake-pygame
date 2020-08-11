import pygame
import random
from room import Room1, Room2, Room3, Room4, Room5, Room6, Room7, Room8, Room9, Room10, Room11, Room12, Room13, Room14, \
    Room15
from Player import Player
from enemy import enemy
from Bullet import Bullet

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (246, 255, 0)

_TILE = 40
SPD = None

# Call this function so the Pygame library can initialize itself
pygame.init()

Enemy_img_list = ["int.png", "kitrino1.png", "prasinol.png", "redl.png"]

movingsprites = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()
# List of each block in the game
wall_list = pygame.sprite.Group()
# all_sprites_list = pygame.sprite.Group()
Enemies_list = pygame.sprite.Group()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
            elif event.type == pygame.QUIT:
                pygame.quit()

        intro_image = pygame.image.load('intro.png')
        screen.blit(intro_image, (0, 0))
        pygame.display.update()
        clock.tick(15)


def terata():
    for i in range(5):
        # This represents a enemy
        Enemy_img = random.randint(0, 3)
        Enemies = enemy(BLACK, 40, 40, Enemy_img_list[Enemy_img])
        # Set a random location for the enemy
        Enemies.rect.x = 700
        Enemies.rect.y = 500
        Enemies.change_x = random.randrange(-3, 4)
        Enemies.change_y = random.randrange(-3, 4)
        Enemies.left_boundary = 40
        Enemies.top_boundary = 160
        Enemies.right_boundary = 760
        Enemies.bottom_boundary = 560
        Enemies_list.add(Enemies)
        # Add the block to the list of objects
        movingsprites.add(Enemies)


moving_right = False
moving_left = False
stay_right = True

""" Main Program """

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
# Hide the mouse cursor
pygame.mouse.set_visible(0)

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 30)
font1 = pygame.font.Font(None, 25)

# Use this boolean variable to trigger if the game is over.
game_over = False
win = False

# Insert the scoreboard
sb = pygame.image.load('sb.png')
screen.blit(sb, (0, 0))

momentum = 0
air_timer = 0

# Set the title of the window
pygame.display.set_caption('ZX_SPECTRUM--STARQUAKE')

# Create the player paddle object
player = Player(40, 150)
terata()

movingsprites.add(player)

rooms = []

room1 = Room1()
rooms.append(room1)

room2 = Room2()
rooms.append(room2)

room3 = Room3()
rooms.append(room3)

room4 = Room4()
rooms.append(room4)

room5 = Room5()
rooms.append(room5)

room6 = Room6()
rooms.append(room6)

room7 = Room7()
rooms.append(room7)

room8 = Room8()
rooms.append(room8)

room9 = Room9()
rooms.append(room9)

room10 = Room10()
rooms.append(room10)

room11 = Room11()
rooms.append(room11)

room12 = Room12()
rooms.append(room12)

room13 = Room13()
rooms.append(room13)

room14 = Room14()
rooms.append(room14)

room15 = Room15()
rooms.append(room15)

current_room_no = 0
current_room = rooms[current_room_no]

clock = pygame.time.Clock()

pygame.mixer.music.load('Starquake.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play(-1)

loop = 1
score = 0
life = 10
ezises = False

game_intro()
while loop:

    screen.fill(BLACK)
    # Tiles are blitted  ==========================
    tile_rects = []
    y = 0
    for line_of_symbols in current_room.game_map:
        x = 0
        for symbol in line_of_symbols:
            if symbol in current_room.tl:
                # draw the symbol for image
                screen.blit(
                    current_room.tl[symbol], (x * _TILE, y * _TILE))
            # draw a rectangle for every symbol except for the empty one
            if symbol != "-":
                tile_rects.append(pygame.Rect(x * _TILE, y * _TILE, _TILE, _TILE))
            x += 1
        y += 1
    # ================================================

    # --- Event Processing ---

    # MOVEMENT OF THE PLAYER
    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 3
    if moving_left:
        player_movement[0] -= 3
    player_movement[1] += momentum
    momentum += 0.3
    if momentum > 3:
        momentum = 3

    player.rect, collisions = player.move(player.rect, player_movement, tile_rects)

    if collisions['bottom']:
        air_timer = 0
        momentum = 0
    else:
        air_timer += 0.5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
                stay_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
                stay_right = False
            if event.key == pygame.K_SPACE:
                if air_timer < 6:
                    momentum = -7
            if event.key == pygame.K_a:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet(stay_right)
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                bullet_list.add(bullet)
                movingsprites.add(bullet)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False

        if stay_right:
            player.image = pygame.image.load("playerr.png").convert()
            player.image.set_colorkey(BLACK)
        else:
            player.image = pygame.image.load("playerl.png").convert()
            player.image.set_colorkey(BLACK)

    # --- Game Logic ---
    # ΔΕΞΙΑ
    # player.move(current_room.wall_list)
    if player.rect.x > 790:
        if current_room_no == 0:
            current_room_no = 1
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0

        elif current_room_no == 1:
            current_room_no = 2
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0

        elif current_room_no == 2:
            current_room_no = 3
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0

        elif current_room_no == 3:
            current_room_no = 4
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0

        elif current_room_no == 7:
            current_room_no = 8
            ezises = True
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0

        elif current_room_no == 11:
            current_room_no = 10
            ezises = True
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0
        elif current_room_no == 12:
            current_room_no = 11
            ezises = True
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0
        elif current_room_no == 14:
            current_room_no = 7
            ezises = True
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0

        elif current_room_no == 13:
            current_room_no = 12
            ezises = True
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 0

    if player.rect.x < -15:
        if current_room_no == 1:
            current_room_no = 0
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790

        elif current_room_no == 2:
            current_room_no = 1
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790
        elif current_room_no == 3:
            current_room_no = 2
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790
        elif current_room_no == 4:
            current_room_no = 3
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790
        elif current_room_no == 8:
            current_room_no = 7
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790
        elif current_room_no == 7:
            current_room_no = 14
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790
        elif current_room_no == 10:
            current_room_no = 11
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790
        elif current_room_no == 11:
            current_room_no = 12
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790

        elif current_room_no == 12:
            current_room_no = 13
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.x = 790

    # PROS T KATO
    if player.rect.y > 540:
        if current_room_no == 2:
            current_room_no = 5
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 0

        elif current_room_no == 5:
            current_room_no = 6
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 0

        elif current_room_no == 6:
            current_room_no = 7
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 0

        elif current_room_no == 13:
            current_room_no = 12
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 0

        elif current_room_no == 14:
            current_room_no = 13
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 0
        elif current_room_no == 8:
            current_room_no = 9
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 0
        elif current_room_no == 9:
            current_room_no = 10
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 0

    # PROS TA PANO
    if player.rect.y < -15:
        if current_room_no == 12:
            current_room_no = 13
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 500
        elif current_room_no == 13:
            current_room_no = 14
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 500
        elif current_room_no == 7:
            current_room_no = 6
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 500
        elif current_room_no == 6:
            current_room_no = 5
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 500
        elif current_room_no == 5:
            current_room_no = 2
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 500
        elif current_room_no == 10:
            current_room_no = 9
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 500
        elif current_room_no == 9:
            current_room_no = 8
            for Enemies in Enemies_list:
                Enemies.kill()
            for bullet in bullet_list:
                movingsprites.remove(bullet)
                bullet_list.remove(bullet)
            terata()
            print("ROOM = ", current_room_no + 1)
            current_room = rooms[current_room_no]
            player.rect.y = 500

    # --- Drawing ---

    current_room.wall_list.draw(screen)

    blocks_hit_list = pygame.sprite.spritecollide(player, Enemies_list, True)
    # Check the list of collisions.
    for block in blocks_hit_list:
        life -= 1
        if life > 0:
            print("life=", life)
            print("efe dmg ston pexti")
        else:
            print("GAME OVER")

    screen.blit(sb, (0, 0))

    # See if it hit a block
    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, Enemies_list, True)
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            movingsprites.remove(bullet)
            score += 500
            print("score=", score)

        # Remove the bullet if it goes right off the screen
        if bullet.rect.x > 800:
            bullet_list.remove(bullet)
            movingsprites.remove(bullet)

    text = font.render(str(score), True, WHITE)
    screen.blit(text, [505, 40])

    text = font1.render("0" + str(life), True, YELLOW)
    screen.blit(text, [350, 70])

    if life == 0:
        game_over = True

    elif not Enemies_list and ezises == True:
        win = True

    if game_over:
        # If game over is true, draw game over
        go = pygame.image.load('go.png')
        screen.blit(go, (0, 0))
        movingsprites.remove(player)
        for enemies in Enemies_list:
            enemies.kill()
        for bullet in bullet_list:
            movingsprites.remove(bullet)

    if win:
        # If game over is true, draw game over
        go = pygame.image.load('win.png')
        screen.blit(go, (0, 0))
        movingsprites.remove(player)
        for bullet in bullet_list:
            movingsprites.remove(bullet)

    movingsprites.update()
    movingsprites.draw(screen)
    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
