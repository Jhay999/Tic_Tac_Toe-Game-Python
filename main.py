import os
import random


def clear_console():
    """
    Clear the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    """
    Print the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """
    Check if the current player has won the game.
    """
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    """
    Check if the board is full (i.e., no more empty cells).
    """
    for row in board:
        if ' ' in row:
            return False
    return True


def player_move(board, player):
    """
    Get the player's move and update the board.
    """
    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            break
        else:
            print("That cell is already taken! Try again.")
            clear_console()


def computer_move(board, computer, player):
    """
    Implement a simple AI for the computer's move.
    """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == ' ':
            board[row][col] = computer
            break


def main():
    while True:
        clear_console()
        print("Welcome to Tic-Tac-Toe!")
        print("-----------------------")

        print("\nOptions:")
        print("1. Play against the computer")
        print("2. Play with a friend")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            play_with_computer()
        elif choice == '2':
            play_with_friend()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")
            clear_console()


def play_with_computer():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    computer = 'O'

    while True:
        clear_console()
        print_board(board)

        if current_player == 'X':
            player_move(board, current_player)
        else:
            computer_move(board, computer, current_player)

        # Check if the current player has won
        if check_winner(board, current_player):
            clear_console()
            print_board(board)
            if current_player == 'X':
                print("Congratulations! You win!")
            else:
                print("Computer wins!")
            break

        # Check if the board is full
        if is_board_full(board):
            clear_console()
            print_board(board)
            print("It's a tie!")
            break

        # Switch turns
        current_player = 'O' if current_player == 'X' else 'X'
        clear_console()


def play_with_friend():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        clear_console()
        print_board(board)
        player_move(board, current_player)

        # Check if the current player has won
        if check_winner(board, current_player):
            clear_console()
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check if the board is full
        if is_board_full(board):
            clear_console()
            print_board(board)
            print("It's a tie!")
            break

        # Switch turns
        current_player = 'O' if current_player == 'X' else 'X'
        clear_console()


if __name__ == "__main__":
    main()
