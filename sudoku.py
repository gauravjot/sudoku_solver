sample_board = [
   ["5","3","0","0","7","0","0","0","0"],
   ["6","0","0","1","9","5","0","0","0"],
   ["0","9","8","0","0","0","0","6","0"],
   ["8","0","0","0","6","0","0","0","3"],
   ["4","0","0","8","0","3","0","0","1"],
   ["7","0","0","0","2","0","0","0","6"],
   ["0","6","0","0","0","0","2","8","0"],
   ["0","0","0","4","1","9","0","0","5"],
   ["0","0","0","0","8","0","0","7","9"]]

def is_valid(board, number, key):

    # Check Row
    if number in board[key[0]]:
        # print("row failed")
        return False
    
    #Check Column
    for i in board:
        if number == i[key[1]]:
            # print("column failed")
            return False

    #Check Box
    box_start = ((key[0] // 3) * 3, (key[1] // 3) * 3)
    box_end = (box_start[0] + 2, box_start[1] + 2)
    for i in range(box_start[0],box_end[0] + 1):
        for j in range(box_start[1],box_end[1] + 1):
            if number == board[i][j]:
                # print("box failed")
                return False

print(is_valid(sample_board,'4',(5,2)))
