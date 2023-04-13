# Conway_game_of_life
Sự tiến hóa của tế bào (cell) qua các thế hệ
# 2.5.1 Rules of the Game
The game uses an infinite-sized rectangular grid of cells in which each cell is either
empty or occupied by an organism. The occupied cells are said to be alive, whereas
the empty ones are dead. The game is played over a specific period of time with each
turn creating a new “generation” based on the arrangement of live organisms in
the current configuration. The status of a cell in the next generation is determined
by applying the following four basic rules to each cell in the current configuration:
1. If a cell is alive and has either two or three live neighbors, the cell remains
alive in the next generation. The neighbors are the eight cells immediately
surrounding a cell: vertically, horizontally, and diagonally.  
    ![description](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTEyCe27XvtN0AvN4Gt1QZXGIPug8tNXD9E4L0hOjwrx76Wh72)
2. A living cell that has no live neighbors or a single live neighbor dies from
isolation in the next generation.
3. A living cell that has four or more live neighbors dies from overpopulation in
the next generation.
4. A dead cell with exactly three live neighbors results in a birth and becomes
alive in the next generation. All other dead cells remain dead in the next
generation.

## Some description(Rules)
![b](https://www.researchgate.net/publication/339605473/figure/fig5/AS:869062565437443@1584212070801/Rules-of-Conways-Game-of-Life.png)  
## Active
![b](https://jimblackler.net/blog/wp-content/uploads/2014/10/bigpic.png)
