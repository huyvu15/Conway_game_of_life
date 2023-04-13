#the game of line
import life
import numpy as np


def numRows():
    nrows = int(input("Nhập vào số hàng: "))
    return nrows

def numCols():
    ncols = int(input("Nhập vào số cột: "))
    return ncols

# hàm tạo grid
def LifeGrid():
    # that function show a grid include nrows and ncols
    nrows = 20 #numRows()
    ncols = 20 #numCols()

    grid = np.zeros((nrows, ncols), dtype=int)
    # print(grid)
    # gắn cho 1 ô is alive
    grid[2][2] = 1
    print(grid)
    
    # 1 is alive, 0 is dead
'''    
#configre grid for evlving the next generation 
coordList: tượng trưng cho vị trí của 1 ô trong grid
với tọa độ (r, c) have value 1 is alive
- tất cả ô còn lại đặt là 0 is dead
'''
def configre(coordList):
    # create tọa độ alive
    coordList = list(map(int, input("Just enter two value: ").split()))
    
# def clearCell(a, row, col):
#     # xóa ô riêng lẻ và set it thành trạng thái dead
#     b = a
#     if a[row, col] == 1:
#         if numLiveNeighbors(a, row, col) == 0 or numLiveNeighbors(a, row, col) == 1 or numLiveNeighbors(a, row, col) >= 4:
#             b[row, col] = 0
#     a = b
     
def clearCell(a, row, col):
    # xóa ô riêng lẻ và set it thành trạng thái dead
    b = np.zeros((10, 10), dtype=int )   
    for i in range(1, row-1):
        for j in range(1, col-1):
            if a[i, j] == 1:
                if numLiveNeighbors(a, i, j) == 0 or numLiveNeighbors(a, i, j) == 1 or numLiveNeighbors(a, i, j) >= 4:
                    b[i, j] = 0
                if numLiveNeighbors(a, i, j) == 2 or numLiveNeighbors(a, i, j) == 3:
                    b[i, j] =1
             
    return b


# def setCell(a, row, col):
#     # set ô chỉ định (row, col) sống
#     # chú ý: (row, col) phải nằm trong phạm vi hợp lệ
#     if a[row, col] == 0:
#         if numLiveNeighbors(a, row, col) == 3:
#           a[row, col] = 1
#     else:
#         if numLiveNeighbors(a, row, col) == 2 or numLiveNeighbors(a, row, col) == 3:
#             a[row, col] = 1  

def setCell(a, row, col):
    b = np.zeros((10, 10), dtype=int )   
    for i in range(1, row-1):
        for j in range(1, col-1):
            if a[i, j] == 0:
                    if numLiveNeighbors(a, i, j) == 3:
                        b[i, j] = 1
            else:
                if numLiveNeighbors(a, i, j) == 2 or numLiveNeighbors(a, i, j) == 3:
                    b[i, j] = 1   
    return b
    
    
def isLiveCell(a, row, col):
    # trả về giá trị boolean cho biết ô đã cho (row, col) có chứa 1 sinh vật sống hay không
    # chú ý: chỉ số ô phải nằm trong phạm vi hợp lệ
    if a[row, col] == 0:
        return 0
    else:
        return 1

def numLiveNeighbors(a, row, col):
    # trả về số lượng hàng xóm của ô đã cho (row, col)
    # các hàng xóm nằm bên ngoài lưới coi như chết
    # chú ý: chỉ số hàng và cột của ô phải nằm trong phạm vi cho phép
    count = 0
    if a[row-1, col-1] == 1:
        count+=1
    if a[row-1, col] == 1:
        count+=1
    if a[row-1, col+1] == 1:
        count+=1
    if a[row, col-1] == 1:
        count+=1
    if a[row, col+1] == 1:
        count+=1
    if a[row+1, col-1] == 1:
        count+=1
    if a[row+1, col] == 1:
        count+=1
    if a[row+1, col+1] == 1:
        count+=1
    return count

    
nrows = numRows()
ncols = numCols()

cell1 = np.zeros((nrows, ncols), dtype=int )   

# thay vì gắn ô sống như thế này thì mình dùng configue

cell1[5,5] = 1
cell1[4,5] = 1
cell1[4,4] = 1
cell1[4,3] = 1
cell1[5,3] = 1
cell1[6,3] = 1
cell1[6,5] = 1
cell1[6,4] = 1


cell2 = cell1

# LifeGrid()
# print("The number of Neighbors of coordList là: ",numLiveNeighbors(cell1,5, 5))
# print("Ô này còn sống: ", isLiveCell(cell1, 5, 5))
print(cell1) 




        

cell2 = setCell(cell2, 9, 9)
cell1 = clearCell(cell1, 9, 9)        

sum = cell1+cell2
for i in range(len(sum)):
    for j in range(len(sum)):
        if sum[i, j]>1:
            sum[i, j] =1
            
print(sum)

