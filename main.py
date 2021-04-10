import math


def make_move(game_board, player, enemy, move):
    i = move[0]
    j = move[1]
    game_board[i][j] = player
    for positions in get_enemy_neighbors(game_board, enemy, i, j):
        right = positions[0] - i
        up = positions[1] - j
        x = i
        y = j
        while x != -1 and y != -1 and x != 8 and y != 8 and game_board[x][y] != '-':
            x = x + right
            y = y + up
            if x == -1 or x == 8 or y == -1 or y == 8:
                break
            if game_board[x][y] == player:
                while game_board[x - right][y - up] == enemy:
                    x = x - right
                    y = y - up
                    game_board[x][y] = player
                break
    return game_board


def get_positions_can_play(game_board, player, enemy):
    avalible_position = []
    for i in range(0, 8):
        for j in range(0, 8):
            if game_board[i][j] == player:
                # Check Enemy in neighbors
                for positions in get_enemy_neighbors(game_board, enemy, i, j):
                    right = positions[0] - i
                    up = positions[1] - j
                    x = i
                    y = j
                    while x != -1 and y != -1 and x != 8 and y != 8:
                        if game_board[x][y] == '-':
                            avalible_position.append([x, y])
                            break
                        x = x + right
                        y = y + up
    return avalible_position


def get_enemy_neighbors(game_board, enemy, row, column):
    neighbors = []
    for i in range(max(row - 1, 0), min(row + 2, 8)):
        for j in range(max(column - 1, 0), min(column + 2, 8)):
            if game_board[i][j] == enemy:
                neighbors.append([i, j])
    return neighbors


# Initialize Board for Beginning
board = [['-' for i in range(8)] for j in range(8)]
board[3][3], board[4][4], board[4][3], board[3][4] = ["X", "X", "O", "O"]
for line in board:
    print(line)

step = 4
while step != 64:
    pcp = get_positions_can_play(board, 'X', 'O')
    print(pcp)
    if len(pcp) != 0:
        player_X_move = list(int(x) for x in input("Insert Position you want to fill: ").split(' '))
        print(player_X_move)
        while player_X_move not in pcp:
            print("You Can't Do This!!!!")
            player_X_move = list(int(x) for x in input("Insert Position you want to fill: ").split(' '))
            print(player_X_move)
        board = make_move(board, 'X', 'O', player_X_move).copy()
        for line in board:
            print(line)
        step += 1
    else:
        print("Player X out of move!")

    pcp = get_positions_can_play(board, 'O', 'X')
    print(pcp)
    if len(pcp) != 0:
        player_X_move = list(int(x) for x in input("Insert Position you want to fill: ").split(' '))
        print(player_X_move)
        while player_X_move not in pcp:
            print("You Can't Do This!!!!")
            player_X_move = list(int(x) for x in input("Insert Position you want to fill: ").split(' '))
            print(player_X_move)
        board = make_move(board, 'O', 'X', player_X_move).copy()
        for line in board:
            print(line)
        step += 1
    else:
        print("Player O out of move!")

