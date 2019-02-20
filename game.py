print('----------------------\nLet\'s play Py-Pac-Poe!\n----------------------')

game_state = {
    'turn': 1,
    'gameboard': [], #gameboard array is an array of rows
    'winner': 0,
    'tie': False
}

def init_game():
    game_state['gameboard'] = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board()
    play_game()

def play_game():
    print('~~~~~~~~~~~~~~~\nIt is Player', game_state['turn'], '\'s turn.  Please select a space to fill (case-sensitive).')
    playerInput = input()
    inputRow = int(playerInput[1]) - 1
    inputCol = -1
    if playerInput[0] == 'A' or playerInput[0] == 'a':
        inputCol = 0
    elif playerInput[0] == 'B' or playerInput[0] == 'b':
        inputCol = 1
    elif playerInput[0] == 'C' or playerInput[0] == 'c':
        inputCol = 2
    else:
        print('this is not a valid placement')
    if game_state['gameboard'][inputRow][inputCol] == ' ':
        game_state['gameboard'][inputRow][inputCol] = game_state['turn']
    else:
        print('~~~~~~~~~~~~~~~~~~~\nThis spot is already taken, please choose another.\n~~~~~~~~~~~~~~~~~~~')
        play_game()
    print_board()
    check_win()

def check_win():
    #check row winner
    for row in game_state['gameboard']:
        rowSum = 0
        for i in range(0, 3):
            if row[i] != ' ':
                rowSum += row[i]
        if abs(rowSum) == 3:
            game_state['winner'] = game_state['turn']
    
    #check col winner
    for j in range(0, 3):
        colSum = 0
        for row in game_state['gameboard']:
            if row[j] != ' ':
                colSum += row[j]
        if abs(colSum) == 3:
            game_state['winner'] = game_state['turn']

    #check diag winner
    diagDownSum = 0
    for k in range(0, 3):
        #check diagonal from top left to bottom right
        if game_state['gameboard'][k][k] != ' ':
            diagDownSum += game_state['gameboard'][k][k]
        if abs(diagDownSum) == 3:
            game_state['winner'] = game_state['turn']
            break

    #check diagonal from bottom left to top right
    diagUpSum = 0
    for m in range(0, 3):
        for l in range(2, -1, -1):
            if game_state['gameboard'][m][l] != ' ':
                diagUpSum += game_state['gameboard'][m][l]
        if abs(diagUpSum) == 3:
            game_state['winner'] = game_state['turn']
        print(diagUpSum, ' this is diagupsum')

    #check tie
    totalSum = 0
    for row in game_state['gameboard']:
        for cell in row:
            if cell != ' ':
                totalSum += abs(cell)
    if totalSum == 9 and not game_state['winner']:
        game_state['tie'] = True
        print('~~~~~~~~~~~~~~~~~~~\nIt was a tie!\n~~~~~~~~~~~~~~~~~~~')
    
    game_state['turn'] *= -1
    if game_state['tie'] == False:
        print('~~~~~~~~~~~~~~~~~~~\n', game_state['winner'], ' has won the game!\n~~~~~~~~~~~~~~~~~~~') if game_state['winner'] else play_game()

def print_board():
    gameboard = game_state['gameboard']
    print('\n   A   B   C\n1)', gameboard[0][0],'|', gameboard[0][1], '|', gameboard[0][2],'\n  -----------\n2)', gameboard[1][0],'|', gameboard[1][1], '|', gameboard[1][2],'\n  -----------\n3)', gameboard[2][0],'|', gameboard[2][1], '|', gameboard[2][2],'\n')

init_game()