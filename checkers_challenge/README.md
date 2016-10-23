# checkers challenge

Watch the following YouTube video clip. Your task is to compute the number of possible ways the white player can win from an opening state of a single white piece in a game of Turkish Draughts. For more information on the game, you can view the Wikipedia page.

For this challenge, we will use the following variation on the official rules:

1. The black pieces can be arbitrary placed, and will not necessarily be located at places reachable in a legal game
1. A single white piece is a king if, and only if, it is placed in or reaches the top most line. Once a piece is a king it remains a king throughout.
1. A white piece can capture by jumping over a single black piece to the left, right or upwards, landing in the adjacent square
1. A white king can capture by jumping left, right, upwards or backwards and can skip arbitrary number of blank squares before and after the black piece
1. After capturing a black piece, the white piece (or king) must turn 90 degrees or keep moving in the same direction (no 180 degree turns are allowed).
1. We ask for the number of different ways the white player can win a single move. White wins by capturing all black pieces.

## Input Format

Each input begins with an integer *t*, on a line by itself, indicating how many testcases are present.

Each testcase will contain 8 lines with the state of the board. The board will have a single white piece `o`, some black pieces `x`, and empty places `.`. White's side of the board is at the bottom of the board. So if the white piece were to reach to top row of the board, it would become a king.

In between each testcase is a blank line.

## Constraints

1 ≤ *t* ≤ 5

There will always be at least 1, and no more than 16, black pieces in each game.

The game board will always be 8×8 squares in size.

## Output Format

For each testcase, output, on a line by itself, the number of possible ways the white can win, or `0` if he cannot.

## Sample Input
```
3
.......o
.x.x.x..
xxxx.xx.
........
........
.x.xx..x
x.......
..x...x.

........
........
....o...
........
....x...
........
........
........

...o....
........
...x....
........
........
........
........
........
```

## Sample Output
```
12
0
5
```

## Explanation

The first testcase is the state of the board in the 56th second of the YouTube video. There are 12 ways in which this game can be won. These ways are represented below:

1. down 7, left 3, up 6, left 2, down 4, right 4, up 4, left 3, down 4, left 3, up 4, right 5, down 6, left 5, up 5, right 2
1. down 7, left 3, up 6, left 2, down 4, right 4, up 4, left 3, down 4, left 3, up 4, right 5, down 6, left 5, up 5, right 3
1. down 7, left 3, up 6, left 2, down 4, right 4, up 4, left 3, down 4, left 3, up 4, right 5, down 6, left 5, up 5, right 4
1. down 7, left 3, up 6, left 2, down 4, right 4, up 4, left 3, down 4, left 3, up 4, right 5, down 6, left 5, up 5, right 5
1. down 7, left 3, up 6, left 2, down 4, right 4, up 4, left 3, down 4, left 3, up 4, right 5, down 6, left 5, up 5, right 6
1. down 7, left 3, up 6, left 2, down 4, right 4, up 4, left 3, down 4, left 3, up 4, right 5, down 6, left 5, up 5, right 7
1. down 7, left 3, up 6, right 2, down 4, left 4, up 4, right 3, down 4, left 5, up 4, right 3, down 6, left 3, up 5, right 2
1. down 7, left 3, up 6, right 2, down 4, left 4, up 4, right 3, down 4, left 5, up 4, right 3, down 6, left 3, up 5, right 3
1. down 7, left 3, up 6, right 2, down 4, left 4, up 4, right 3, down 4, left 5, up 4, right 3, down 6, left 3, up 5, right 4
1. down 7, left 3, up 6, right 2, down 4, left 4, up 4, right 3, down 4, left 5, up 4, right 3, down 6, left 3, up 5, right 5
1. down 7, left 3, up 6, right 2, down 4, left 4, up 4, right 3, down 4, left 5, up 4, right 3, down 6, left 3, up 5, right 6
1. down 7, left 3, up 6, right 2, down 4, left 4, up 4, right 3, down 4, left 5, up 4, right 3, down 6, left 3, up 5, right 7

There is no way for white to win the second testcase.

For the final testcase, white has a king, and white can capture the single black piece, and land on any of the five spaces below the piece.


[yt:video]: https://youtu.be/8l8mvXHyCOY
[wiki:Turkish draughts]: https://en.wikipedia.org/wiki/Turkish_draughts
