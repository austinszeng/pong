import pygame 
import random
import os

pygame.mixer.init()

wid = 900
hei = 600
win = pygame.display.set_mode((wid, hei))

clock = pygame.time.Clock()

paddle_hit = pygame.USEREVENT + 1
hitsound = pygame.mixer.Sound('Assets/hitsound.wav')
pygame.mixer.Sound.set_volume(hitsound, 0.2)

def draw_screen(ball, paddle_1, paddle_2):
    win.fill((0,0,0))  
    pygame.draw.rect(win, (255, 255, 255), paddle_1)
    pygame.draw.rect(win, (255, 255, 255), paddle_2)
    pygame.draw.rect(win, (255, 255, 255), ball)
    pygame.display.update()

def paddle_movement(keys_pressed, paddle_1, paddle_2, paddle_spd):
    if keys_pressed[pygame.K_w] and paddle_1.top > 0:
        paddle_1.y -= paddle_spd
    if keys_pressed[pygame.K_s] and paddle_1.bottom < hei:
        paddle_1.y += paddle_spd
    if keys_pressed[pygame.K_UP] and paddle_2.top > 0:
        paddle_2.y -= paddle_spd
    if keys_pressed[pygame.K_DOWN] and paddle_2.bottom < hei:
        paddle_2.y += paddle_spd

# def handle_ball(ball, paddle_1, paddle_2, ball_spd_x, ball_spd_y, prev_winner):


def main():
    paddle_size = 75
    paddle_1 = pygame.Rect(50, 262, 10, paddle_size)
    paddle_2 = pygame.Rect(850, 262, 10, paddle_size)
    paddle_spd = 10

    p1_score = 0
    p2_score = 0

    ball_size = 10
    ball_spd_x = 5
    ry_spd = random.randint(1, ball_spd_x)
    ball_spd_y = ry_spd
    ball = pygame.Rect(wid/2-ball_size/2, hei/2-ball_size/2, ball_size, ball_size)

    prev_winner = random.randint(1,2) # this always gets called after a game, so it isn't based off of the winner yet...
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == paddle_hit:
                hitsound.play()

        clock.tick(60)
        draw_screen(ball, paddle_1, paddle_2)
        keys_pressed = pygame.key.get_pressed()
        paddle_movement(keys_pressed, paddle_1, paddle_2, paddle_spd)
        # handle_ball(ball, paddle_1, paddle_2, ball_spd_x, ball_spd_y, prev_winner)

        if ball.right > wid:
            p1_score += 1
            prev_winner = 1
            break
        if ball.left < 0:
            p2_score += 1
            prev_winner = 2
            break

        # choose which way it goes based on winner
        if prev_winner == 1:
            ball.x -= ball_spd_x
            ball.y -= ball_spd_y
        else:
            ball.x += ball_spd_x
            ball.y -= ball_spd_y

        # FOR SOME REASON vvv THIS CODE DOESN'T WORK WHEN PUT INTO A FUNCTION LIKE THE OTHER FUNCTIONS...

        # ball bounces off top and bottom of screen
        if ball.top < 0:
            ball_spd_y *= -1
        if ball.bottom > hei:
            ball_spd_y *= -1

        # paddle hit
        collision_tolerance = 10 # bug where ball just goes through the paddle...
        if paddle_1.colliderect(ball):
            if abs(paddle_1.top - ball.bottom) == collision_tolerance and ball_spd_y > 0:
                ball_spd_y *= -1
            if abs(paddle_1.bottom - ball.top) == collision_tolerance and ball_spd_y < 0:
                ball_spd_y *= -1
            if abs(paddle_1.right - ball.left) == collision_tolerance and ball_spd_x > 0:
                ball_spd_x *= -1
            if abs(paddle_2.left - ball.right) == collision_tolerance and ball_spd_x < 0:
                ball_spd_x *= -1
            pygame.event.post(pygame.event.Event(paddle_hit))
            
        if paddle_2.colliderect(ball):
            if abs(paddle_2.top - ball.bottom) == collision_tolerance and ball_spd_y > 0:
                ball_spd_y *= -1
            if abs(paddle_2.bottom - ball.top) == collision_tolerance and ball_spd_y < 0:
                ball_spd_y *= -1
            if abs(paddle_1.right - ball.left) == collision_tolerance and ball_spd_x > 0:
                ball_spd_x *= -1
            if abs(paddle_2.left - ball.right) == collision_tolerance and ball_spd_x < 0:
                ball_spd_x *= -1
            pygame.event.post(pygame.event.Event(paddle_hit))


    main()


if __name__ == '__main__':
    main()