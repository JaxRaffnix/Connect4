def minmax(board, is_max_turn, depth, alpha=-math.inf, beta=math.inf):
    if depth == DEPTH_MAX:
        return 0
    if eng.Check_Win(board, AI_PLAYER):
        return 1
    elif eng.Check_Win(board, eng.Switch_Player(AI_PLAYER)):
        return -1
    elif eng.Check_Draw(board, AI_PLAYER):
        return 0

    if is_max_turn:
        value = -math.inf
        for column in possible_moves(board):
            pl.Set_Mark(board, AI_PLAYER, column)
            value = max(value, minmax(board, False, depth+1, alpha, beta))
            pl.Undo_Mark(board, column)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
    else:
        value = math.inf
        for column in possible_moves(board):
            pl.Set_Mark(board, eng.Switch_Player(AI_PLAYER), column)
            value = min(value, minmax(board, True, depth+1, alpha, beta))
            pl.Undo_Mark(board, column)
            beta = min(beta, value)
            if beta <= alpha:
                break

    return value