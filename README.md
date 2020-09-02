# Game of Life

## Premise
This is the first README that I'm writing for a project. I'm opening up to external contributions so, please, feel free to suggest me any way of improving this file and every other part of this project. Thank you! 

## The game
With this project I'm trying to build **The game of Life**, a famous cellular-automata simulation designed by John Conway.
You can read more about this project [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

The general concept is this. We have a screen full of different cells. Every cell has only one attribute: **alive** or **dead**. This attribute depends on the number of alive neighbours of a cell. 
Every cell has 8 neighbours.

![alt text](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcodiecollinge.files.wordpress.com%2F2012%2F08%2Fcell-neighbours.jpg&f=1&nofb=1 "Cell with neighbours")

There are 4 rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

With these 4 rules, a world of possibilities opens up.
The simulation creates a complex behaviour that is impossible to anticipate from the start of the game.

## The software
For this project I'm using:
* Python 3.6;
* Pygame module;




