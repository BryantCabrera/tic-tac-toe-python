print('----------------------\nLet\'s play Py-Pac-Poe!\n----------------------')

game_state = {
    'turn': 1,
    'gameboard': [], #gameboard array is an array of rows
    'winner': ''
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
    if playerInput[0] == 'A':
        inputCol = 0
    elif playerInput[0] == 'B':
        inputCol = 1
    elif playerInput[0] == 'C':
        inputCol = 2
    else:
        print('this is not a valid placement')
    game_state['gameboard'][inputRow][inputCol] = game_state['turn']  
    print_board()
    checkWin()

def checkWin():
    for row in game_state['gameboard']:
        sum = 0
        for i in range(0, 3):
            if row[i] != ' ':
                sum += abs(row[i])
        if sum == 3:
            game_state['winner'] = game_state['turn']
    game_state['turn'] *= -1
    print('~~~~~~~~~~~~~~~~~~~\n' + game_state['winner'] + ' has won the game!\n~~~~~~~~~~~~~~~~~~~') if game_state['winner'] else play_game()

def print_board():
    # gameboard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    gameboard = game_state['gameboard']
    print('\n   A   B   C\n1)', gameboard[0][0],'|', gameboard[0][1], '|', gameboard[0][2],'\n  -----------\n2)', gameboard[1][0],'|', gameboard[1][1], '|', gameboard[1][2],'\n  -----------\n3)', gameboard[2][0],'|', gameboard[2][1], '|', gameboard[2][2],'\n')

init_game()