import time


def make_move(gameboard, player, enemy, move):
    game_board = gameboard.copy()
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


def check_score(game_board, player, enemy):
    score = 0
    for row in game_board:
        for item in row:
            if item == player:
                score += 1
            elif item == enemy:
                score -= 1
    return score


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


'''def get_best_move(game_board, depth, player, enemy, avalible_moves):
    best_move = []
    if depth == 0:
        best_score = -100
        for move in avalible_moves:
            this_score = check_score(game_board, player, enemy)
            if this_score > best_score:
                best_score = this_score
                best_move = move.copy()
    else:
        for move in avalible_moves:
            best_score = -100
            this_score = check_score(make_move(game_board, enemy, player,
                                               get_best_move(game_board, depth - 1, enemy, player,
                                                             get_positions_can_play(game_board, enemy, player))),
                                     player, enemy)
            if this_score > best_score:
                best_score = this_score
                best_move = move.copy()
            board_after_this_move = make_move(game_board.copy(), player, enemy, move)
            avalible_moves_after_this_move = get_positions_can_play(board_after_this_move, enemy, player)
            for sencond_move in avalible_moves_after_this_move:
                enemy_move = get_best_move(board_after_this_move, depth - 1, enemy, player,
                                           avalible_moves_after_this_move)
            board_after_this_move_2 = make_move(board_after_this_move.copy(), enemy, player, enemy_move)
            avalible_moves_after_this_move = get_positions_can_play(board_after_this_move_2, player, enemy)
            fbestmove = get_best_move(board_after_this_move_2, depth - 1, player, enemy, avalible_moves_after_this_move)
            fnew_board = make_move(board_after_this_move_2.copy(), player, enemy, fbestmove)
            if check_score(fnew_board, player, enemy) > best_score:
                best_score = check_score(fnew_board, player, enemy)
                best_move = move
                print("kiiiiiiiiiiiiir")
                return best_move
    return best_move
'''


def max_value(game_board, avalible_moves, depth):
    best_score = -100
    if depth == 0:
        return check_score(game_board.copy(), 'X', 'O')
    for move in avalible_moves:
        board_after_this_move = make_move(game_board.copy(), 'X', 'O', move)
        avalible_moves_after_this_move = get_positions_can_play(board_after_this_move, 'X', 'O')
        best_score = max(best_score, min_value(board_after_this_move.copy(), avalible_moves_after_this_move, depth - 1))
    return best_score


def min_value(game_board, avalible_moves, depth):
    best_score = 100
    if depth == 0:
        return check_score(game_board, 'X', 'O')
    for move in avalible_moves:
        board_after_this_move = make_move(game_board.copy(), 'X', 'O', move)
        avalible_moves_after_this_move = get_positions_can_play(board_after_this_move, 'X', 'O')
        best_score = min(best_score, max_value(board_after_this_move.copy(), avalible_moves_after_this_move, depth - 1))
    return best_score


def minimax(gameboard, avalible_moves, depth):
    game_board = gameboard.copy()
    best_move = []
    best_score = -100
    for move in avalible_moves:
        board_after_this_move = make_move(game_board.copy(), 'X', 'O', move)
        avalible_moves_after_this_move = get_positions_can_play(board_after_this_move.copy(), 'X', 'O')
        this_score = min_value(board_after_this_move.copy(), avalible_moves_after_this_move, depth - 1)
        if this_score > best_score:
            best_score = this_score
            best_move = move
    return best_move


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
    print("Score for X is: " + str(check_score(board, 'X', 'O')))

    pcp = get_positions_can_play(board.copy(), 'O', 'X')
    print(pcp)
    if len(pcp) != 0:
        # player_X_move =
        # player_X_move = get_best_move(board, 2, 'O', 'X', pcp)
        tic = time.time()
        print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        for line in board:
            print(line)
        print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        player_X_move = minimax(board.copy(), pcp, 1)
        print(player_X_move)
        print("_____________________")
        print(time.time() - tic)
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
    print("Score for O is: " + str(check_score(board, 'O', 'X')))
