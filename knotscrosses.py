# KNOTS AND CROSSES
import sys

# MATRIX CHECK FUNCTION
def gamecheck(matrix, size):

    # CHECK FOR HORIZONTAL
    for i in range(size):
        listHor = []
        for j in range(size):
            listHor.append(matrix[i][j])

        buffer = list(set(listHor))
        if 0 not in buffer and len(buffer) == 1:
            return 1

    # CHECK FOR VERTICAL
    for i in range(size):
        listVer = []
        for j in range(size):
            listVer.append(matrix[j][i])

        buffer = list(set(listVer))
        if 0 not in buffer and len(buffer) == 1:
            return 1

    # CHECK FOR DOWN DIAG
    listDownDiag = []
    for i in range(size):
        listDownDiag.append(matrix[i][i])

    buffer = list(set(listDownDiag))
    if 0 not in buffer and len(buffer) == 1:
        return 1

    # CHECK FOR UP DIAG
    listUpDiag = []
    end = size-1
    for i in range(size):
        listUpDiag.append(matrix[i][end])
        end -= 1

    buffer = list(set(listDownDiag))
    if 0 not in buffer and len(buffer) == 1:
        return 1


# ---------------------- TAKING USER INPUT AND MATRIX CODE -------------------------

print("WHATS THE SIZE OF YOUR BOARD: (SIZE MUST BE AN ODD NUMBER)")
size = int(input())

if size % 2 == 0:
    print("THE NUMBER IS NOT ODD")
    sys.exit()

gameOver = 0
matrix = []

for i in range(size):
    y = [0 for z in range(size)]
    matrix.append(y)

# print(matrix)


gameMatrix = []

for i in range(size):
    x = ['-' for z in range(size)]
    gameMatrix.append(x)

for i in range(size):
    for j in range(size):
        print(gameMatrix[i][j],end=" ")
    print()

# ---
counter = 0
while gameOver == 0 and counter <= (size*size):

    print("PLAYER 1 ENTER CO-ORDINATES:")
    counter += 1
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 1
    gameMatrix[x-1][y-1] = 'X'

    for i in range(size):
        for j in range(size):
            print(gameMatrix[i][j], end=" ")
        print()

    result = gamecheck(matrix,size)
    if result == 1:
        print("PLAYER 1 WINS")
        sys.exit()

    if counter == (size*size):
        print("GAME OVER. RESULT -> TIE :|")
        sys.exit()


    print("PLAYER 2 ENTER CO-ORDINATES:")
    counter += 1
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 2
    gameMatrix[x-1][y-1] = 'O'

    for i in range(size):
        for j in range(size):
            print(gameMatrix[i][j], end=" ")
        print()

    result = gamecheck(matrix, size)
    if result == 1:
        print("PLAYER 2 WINS")
        sys.exit()

    if counter == (size * size):
        print("GAME OVER. RESULT -> TIE :|")
        sys.exit()



print("GAME OVER. RESULT -> TIE :|")



