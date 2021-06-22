# pong
trying to learn the basics of the pygame module

## Bugs:
- prev_winner getting the ball doesn't work since prev_winner gets reset to random.randint(1,2) everytime main() is called
- handle_ball function doesn't work for some reason, only works when the code is copy pasted into the main while loop
- collision is buggy -- ball goes through paddles randomly (mostly on paddle_2)
- hit sound plays more than once per hit
- make it so the path of the ball is determined by where the paddle hits it

## Implementation ideas:
- Make GUI (main menu)
  - slider to be able to change speed/ size of paddles and ball
  - button to customize background 
  - choose whether to have rounds or infinite
- choose whether the ball speeds up per hit or is constant
- add # of rounds in main game
- Machine Learning co-op mode bot
- multiplayer implementation
