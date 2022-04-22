# Damavis Challenge

This repository contains the solution to the Damavis Challenge. 

## Challenge Description

The following is provided problem statement:

*Consider a rectangular board consisting of n × m cells. There is a snake lying on some of the
cells, and all of the other cells are empty. The snake consists of one or more cells such that
cells with consecutive numbers are either horizontally or vertically adjacent. The first cell is
the snake's head, and the last cell is the snake's tail.*

*On each turn, the snake's head moves to one of the horizontally or vertically adjacent cells,
the second cell of the snake moves to the cell where the head was situated, the third cell
takes the former place of the second cell, etc. All these movements happen simultaneously,
so the head could potentially take the place of the tail. There are two configurations of the
snake's cells that are prohibited: self-intersection (meaning that after each step any pair of
snake cells should have pairwise different coordinates), and crossing the board's border.
The path is a sequence of characters L, R, D, and U(corresponding to left, right, down, and up,
respectively) describing the movements of snake's head on each turn.*

**How many distinct valid paths of length p can the snake make on the board?**

## Formal definition

The input of the problem are:

#### board

The **board** is an array of integers of length 2 describing the dimensions of the board.`board[0]` stands
for the number of rows, and `board[1]` corresponds to the number of columns. Board constraints are:

- board.length = 2
- 1 <= board[0] <= 10
- 1 <= board[1] <= 10

#### snake

The **snake** is an array of integers. `snake[i]` corresponds to coordinates of i-th cell of the snake
(e.g. `snake[0]` corresponds to the head). Snake constraints are:

- 3 <= snake.length <= 7
- snake[i].length = 2
- 0 <= snake[i, j] < board[j] (all cells are in the board)
- snake[i] and snake[i+1] are horizontally or vertically adjacent

#### depth

The **depth** is an integer representing the paths depth. Depth constraints are:

- 1 <= depth <= 20

