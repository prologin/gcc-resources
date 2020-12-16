# Bomberman reference
by Viri0x/Quentin

This is a bomberman game replica.

## Rules
At the start, you can drop up to 3 bombs at the same time.
Each have a 1 fire radius arount it (without diagonal).
A bomb takes 3 seconds to explode.
If a bomb is in the radius of another bomb exploding, this bomb immediatly explodes too.
If a player is caught in a fire, he loses.

## Controls
* Player 1 controls are A,S,W,D to move and SPACE to drop bomb.
* Player 2 controls are UP,DOWN,LEFT,RIGHT arrows to move and NUMPAD 0 to drop bomb.
* Use ESCAPE to quit the game.

## Map
Map dimensions are 20 by 15.
You can change map by parsing another file.

## Power-up
There are 2 power-up:
* Add 1 fire range to your bombs (fire sprite).
* Add 1 bomb to the maximum you can drop simultaneously (bomb sprite).

## Winner
The winner is the one who destroy the other opponent with bombs.
The game quit and print the name of the winner in the console.

## Improvements
* There is only one sprite for players and only right and left faces, you can had more.
* You can had more power-up.
* Explosions sprites are not always easy to see.
* Add real end screen for winner.
