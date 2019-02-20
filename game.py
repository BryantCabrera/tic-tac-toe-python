print('----------------------\nLet\'s play Py-Pac-Poe!\n----------------------')

# gameboard = [[],[],[]]
game_state = {
    'turn': 1,
    'gameboard': []
}

def init_game():
    game_state['gameboard'] = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board(game_state['gameboard'])
    play_game()

def play_game():
    print('~~~~~~~~~~~~~~~\nIt is Player', game_state['turn'], '\'s turn.  Please select a space to fill (case-sensitive).')

def print_board(gameboard):
    # gameboard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print('\n   A   B   C\n1)', gameboard[0][0],'|', gameboard[0][1], '|', gameboard[0][2],'\n  -----------\n2)', gameboard[1][0],'|', gameboard[1][1], '|', gameboard[1][2],'\n  -----------\n3)', gameboard[2][0],'|', gameboard[2][1], '|', gameboard[2][2],'\n')

init_game()