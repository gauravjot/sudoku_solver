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

solved_fields = {}

def main():
    solve()
    
def solve():
    global sample_board
    global solved_fields
    empty_fields = find_empty_fields(sample_board)
    index = 0
    while index < len(empty_fields):
        success = False
        fld = empty_fields[index]
        # print(fld, end=" => ")
        for i in range(1,10): 
            if fld in solved_fields.keys():
                previously_solved_values = solved_fields[fld]
                # print(("$$ at {}").format(str(i)), end=" -- ")
                # print(previously_solved_values)
                if str(i) in previously_solved_values:
                    # print("continue called {}".format(str(i)))
                    if (i==9):
                        del solved_fields[fld]
                        index -= 1
                        remove_number(sample_board,fld)
                        success = True
                    continue
            if(is_valid(sample_board,str(i),fld)):
                # print("success at {}".format(str(i)))
                insert_number(sample_board,str(i),fld)
                success = True
                index += 1
                break
            else:
                if fld in solved_fields.keys() and i == 9:
                    del solved_fields[fld]
                    remove_number(sample_board,fld)
                    break
                # else:
                #     print("failed at {}".format(str(i)), end=" -- ")
                #     if i==9:
                #         print("")
            
        if success == False:
            # need to back track
            index -=1

    print(sample_board)


def is_valid(board, number, key):
    number = remove_astericks(number)

    # Check Row
    if number in board[key[0]] or '*'+number in board[key[0]]:
        # print("row failed", end=" -- ")
        return False
    
    #Check Column
    for i in board:
        if number == remove_astericks(i[key[1]]):
            # print("column failed", end=" -- ")
            return False

    #Check Box
    box_start = ((key[0] // 3) * 3, (key[1] // 3) * 3)
    box_end = (box_start[0] + 2, box_start[1] + 2)
    for i in range(box_start[0],box_end[0] + 1):
        for j in range(box_start[1],box_end[1] + 1):
            if number == remove_astericks(board[i][j]):
                # print("box failed", end=" -- ")
                return False
    
    return True

def insert_number(board, number, key):
    global solved_fields
    board[key[0]][key[1]] = '*'+str(number)
    if key in solved_fields:
        solved_field_values = solved_fields[key]
        solved_fields[key] = solved_field_values + tuple(number)
    else:
        solved_fields[key] = tuple(number)

def remove_number(board,key):
    global solved_fields
    board[key[0]][key[1]] = '0'
    # del solved_fields[key]

def find_empty_fields(board):
    empty_fields = []
    for row, i in enumerate(board):
        for col, j in enumerate(i):
            if j == '0':
                field = (row, col)
                empty_fields.append(field)
    return empty_fields

def remove_astericks(string):
    return string.replace("*","")

print(sample_board)     
main()

# print(sample_board)

# if(is_valid(sample_board,'1',(5,2))):
#     insert_number(sample_board,'1',(5,2))
# else:
#     print("no luck")

# if(is_valid(sample_board,'3',(5,2))):
#     insert_number(sample_board,'3',(5,2))
# else:
#     print("no luck")

# print(solved_fields)
# print(sample_board)
