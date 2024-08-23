def searchMatrix(matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    val_r, val_c = 0,0
    while (val_r < row):
        if target >= matrix[val_r][val_c] or target <= matrix[val_r][col - 1]:
            left = 0
            right = col - 1
            while(left <= right):
                mid = (left + right) // 2
                if target < matrix[val_r][mid]:
                    right = mid - 1
                elif target > matrix[val_r][mid]:
                    left = mid + 1
                else:
                    return True
        
        val_r += 1
    return False

def searchMatrix2(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    top, bot = 0 , ROWS - 1
    while (top <= bot):
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top += 1
        elif target < matrix[row][0]:
            bot -= 1
        else:
            break
    if not(top <= bot):
        return False

    row = (top + bot) // 2
    left, right = 0, COLS - 1
    while (left <= right):
        mid = (left + right) // 2
        if target < matrix[row][mid]:
            right = mid - 1
        elif target > matrix[row][mid]:
            left = mid + 1
        else:
            return True
    return False


    
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],99))
print(searchMatrix2([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))