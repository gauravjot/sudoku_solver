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

# Dictionary of tuple as key and value
# eg. { (0,2): ('1','2',), }
# (0,2) is field on board; ('1','2',) are tried values in that spot
solved_fields = {}

def main():
    solve()
    
def solve():
    global sample_board
    global solved_fields
    empty_fields = find_empty_fields(sample_board)
    index = 0
    while index < len(empty_fields):
        # success tells if we successfully found value or not
        success = False

        # current field we are working on, format: tuple eg. (0,2)
        current_field = empty_fields[index]

        for i in range(1,10): 
            if current_field in solved_fields.keys():
                if str(i) in solved_fields[current_field]:
                    if (i==9):
                        # 9 is last possible value but already in solved_fields
                        # hence no possible solution and we have to back-track
                        del solved_fields[current_field]
                        remove_number(sample_board,current_field)
                    continue
            if(is_valid(sample_board,str(i),current_field)):
                insert_number(sample_board,str(i),current_field)
                success = True
                index += 1
                break
            else:
                if current_field in solved_fields.keys() and i == 9:
                    # 9 was last possible value but is not valid
                    # we need to back-track
                    del solved_fields[current_field]
                    remove_number(sample_board,current_field)
                    break
            
        if success == False:
            # back-tracking because we did not have success
            index -=1

    show_board(sample_board)

def is_valid(board, number, key):
    number = remove_astericks(number)

    # Check Row
    if number in board[key[0]] or '*'+number in board[key[0]]:
        return False
    
    #Check Column
    for i in board:
        if number == remove_astericks(i[key[1]]):
            return False

    #Check Box
    box_start = ((key[0] // 3) * 3, (key[1] // 3) * 3)
    box_end = (box_start[0] + 2, box_start[1] + 2)
    for i in range(box_start[0],box_end[0] + 1):
        for j in range(box_start[1],box_end[1] + 1):
            if number == remove_astericks(board[i][j]):
                return False
    
    return True

def insert_number(board, number, key):
    global solved_fields
    board[key[0]][key[1]] = '*'+str(number)
    if key in solved_fields:
        solved_fields[key] = solved_fields[key] + tuple(number)
    else:
        solved_fields[key] = tuple(number)

def remove_number(board,key):
    global solved_fields
    board[key[0]][key[1]] = '0'

def find_empty_fields(board):
    # eg. [(0,2),(0,3),...]
    empty_fields = []
    for row, i in enumerate(board):
        for col, j in enumerate(i):
            if j == '0':
                field = (row, col)
                empty_fields.append(field)
    return empty_fields

def remove_astericks(string):
    return string.replace("*","")

def show_board(board):
    print("\n")
    for index,i in enumerate(board):
        if(index%3 == 0 and index != 0):
            print("---------------------------------")
        for indexj,j in enumerate(i):
            if(indexj%3 == 0 and indexj!= 0):
                print(" | ", end="")
            if(j.startswith("*")):
                print(j,end=" ")
            else:
                print(" "+j, end=" ")
        print("")
    print("\n")


show_board(sample_board)     
main()