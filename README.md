# Conway_game_of_life(Algorithm)
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
![b](https://www.mdpi.com/micromachines/micromachines-09-00339/article_deploy/html/images/micromachines-09-00339-g001.png)  
## Active
![b](https://jimblackler.net/blog/wp-content/uploads/2014/10/bigpic.png)


Link tham khảo game:
- https://playgameoflife.com
- https://notes.huy.rocks/posts/game-of-life.html
- https://conwaylife.com 
- Data_Structures_and_Algorithms_Rance_D_N.pdf(Sách của Rance Neicaise trang 58)

# Bonus
- Do ngồi fit bug nhiều quá lười viết hàm nhập vào tọa độ ô sống
- Hiện tại vẫn chưa nghĩ ra cách nào để nhập vào tọa độ ô sống mong muốn (nhập từng tọa độ 1 thì lâu quá trong khi người dùng chỉ
muốn chọn trực tiếp ô thay vì phải chạy qua từng ô 1 trong lưới
- Ai thiện chí có thể tham khảo code của mình rồi đưa ra lời khuyên
- Chương trình chưa tối ưu, một số hàm ko dùng đến nhưng vẫn cho vào để đảm bảo đủ hàm theo hướng dẫn
- Chương trình chỉ là thuật toán bên trong trò chơi chưa áp dụng GUI, users có thể fork về sử dụng thư viện của tác giả để tạo GUI
- 
