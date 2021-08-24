# Tic tac toe text based version
import board

game_on = True
print('\n' * 80)
board_values = {"a1": "a1",
                "a2": "a2",
                "a3": "a3",
                "b1": "b1",
                "b2": "b2",
                "b3": "b3",
                "c1": "c1",
                "c2": "c2",
                "c3": "c3"
                }
board_colors = {"a1": "white",
                "a2": "white",
                "a3": "white",
                "b1": "white",
                "b2": "white",
                "b3": "white",
                "c1": "white",
                "c2": "white",
                "c3": "white"
                }

print("Welcome to  TIC TAC TOE - text based game")
player1 = input("Set name for Player1 : ")
player2 = input("Set name for Player2 : ")
letters_range = ["a", "b", "c"]

player1_turn = True

while game_on:
    for letter in letters_range:
        if board_values[f"{letter}1"] == board_values[f"{letter}2"] == board_values[f"{letter}3"] or \
                board_values["a1"] == board_values["b2"] == board_values["c3"] or \
                board_values["c1"] == board_values["b2"] == board_values["a3"]:
            if player1_turn:
                print(f"Game over, {player2} wins !!!")
                game_on = False
                break
            else:
                print(f"Game over, {player1} wins !!!")
                game_on = False
                break

    for number in range(1, 4):
        if board_values[f"a{number}"] == board_values[f"b{number}"] == board_values[f"c{number}"]:
            if player1_turn:
                print(f"Game over, {player2} wins !!!")
                game_on = False
            else:
                print(f"Game over, {player1} wins !!!")
                game_on = False

    print(board.print_board(board_values, board_colors))
    if not game_on:
        break
    else:
        if player1_turn:
            turn = input(f"{player1} is your turn, type a1,a2,a3...etc !!! : ")
            if turn not in board_values:
                print("BAD VALUE please try again")
            else:
                if board_values[turn] == " X" or board_values[turn] == " O":
                    player1_turn = True
                    print("BAD MOVE (ALREADY USED)!!! TRY AGAIN")
                else:
                    board_values[turn] = " X"
                    board_colors[turn] = "red"
                    player1_turn = False
        else:
            turn = input(f"{player2} is your turn, type a1,a2,a3...etc !!! : ")
            if turn not in board_values:
                print("BAD VALUE please try again")
            else:
                if board_values[turn] == " X" or board_values[turn] == " O":
                    player1_turn = False
                    print("BAD MOVE (ALREADY USED)!!! TRY AGAIN")
                else:
                    board_values[turn] = " O"
                    board_colors[turn] = "green"
                    player1_turn = True
