# Program:
""" Tic-Tac-Toe with numbers. A board of 3 x 3 is displayed and player 1 takes odd numbers 1,
3, 5, 7, 9 and player 2 takes even numbers 0, 2, 4, 6, 8. Players take turns to write their
numbers. Odd numbers start. Use each number only once. The first person to complete a line
that adds up to 15 is the winner. The line can have both odd and even numbers.
"""
# Author: Ibrahim Reda Mohamed - Section: None - ID: 20230597
# Version: V3.0
# Date: 29 Feb 2024




def print_board(board):
    """
    Function to print the Tic-Tac-Toe board.
    """
    for row in board:
        print("|".join(map(str, row)))
        print("-" * 5)


def check_winner(board):
    """
    Function to check if the current player has won.
    """
    # Check rows and columns
    for i in range(3):
        if sum(board[i][j] for j in range(3)) == 15 or sum(board[j][i] for j in range(3)) == 15:
            return True

    # Check diagonals
    if sum(board[i][i] for i in range(3)) == 15 or sum(board[i][2 - i] for i in range(3)) == 15:
        return True

    return False


def tic_tac_toe():
    """
    Function to play the Tic-Tac-Toe game with numbers.
    """
    # Initialize the board with 0 in all cells
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    selected_numbers = set()

    # Main game loop
    for _ in range(9):
        print_board(board)

        # Player 1's turn
        while True:
            try:
                num = int(input("Player 1: Enter an odd number between 1 and 9: "))
                while (num > 9 or num < 1) or (num % 2 == 0) or num in selected_numbers:
                    num = int(input("Player 1: Enter an odd number between 1 and 9: "))
                selected_numbers.add(num)
                row = int(input("Player 1: Enter row (1-3): "))
                while (row > 3 or row < 1):
                    row = int(input("Player 1: Enter row (1-3): "))
                col = int(input("Player 1: Enter column (1-3): "))
                while (col > 3 or col < 1):
                    col = int(input("Player 1: Enter column (1-3): "))
                if row < 1 or row > 3 or col < 1 or col > 3 or num < 1 or num > 9:
                    print("Invalid input. Row and column should be between 1 and 3, and number between 1 and 9.")
                elif not board[row - 1][col - 1] == 0:
                    print("This position is already taken. Try again.")
                else:
                    board[row - 1][col - 1] = num
                    print_board(board)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number: ")

        # Check if player 1 wins
        if check_winner(board):
            print_board(board)
            print("Player 1 wins!")
            return

        # Player 2's turn
        while True:
            try:
                num = int(input("Player 2: Enter an even number between 1 and 9: "))
                while (num > 9 or num < 1) or (num % 2 != 0) or num in selected_numbers:
                    num = int(input("Player 2: Enter an even number between 1 and 9: "))
                selected_numbers.add(num)
                row = int(input("Player 2: Enter row (1-3): "))
                while (row > 3 or row < 1):
                    row = int(input("Player 2: Enter row (1-3): "))
                col = int(input("Player 2: Enter column (1-3): "))  # <- Corrected prompt message
                while (col > 3 or col < 1):  # <- Corrected validation condition for column input
                    col = int(input("Player 2: Enter column (1-3): "))  # <- Corrected prompt message
                if row < 1 or row > 3 or col < 1 or col > 3 or num < 1 or num > 9:
                    print("Invalid input. Row and column should be between 1 and 3, and number between 1 and 9.")
                elif not board[row - 1][col - 1] == 0:
                    print("This position is already taken. Try again.")
                else:
                    board[row - 1][col - 1] = num
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number: ")

        # Check if player 2 wins
        if check_winner(board):
            print_board(board)
            print("Player 2 wins!")
            return

    # If all moves are exhausted and no winner is found
    print_board(board)
    print("It's a tie!")


if __name__ == "__main__":
    print("\nWelcome to Tic-Tac-Toe with numbers!\n")
    tic_tac_toe()
