class Piece:
    def __init__(self, color, piece_type, position):
        self.color = color
        self.piece_type = piece_type
        self.position = position

    def available_moves(self, board):
        row, col = self.position
        moves = 0

        if self.piece_type.lower() == 'king':
            moves = self.available_moves_king(board, row, col)
        elif self.piece_type.lower() == 'queen':
            moves = self.available_moves_queen(board, row, col)
        elif self.piece_type.lower() == 'rook':
            moves = self.available_moves_rook(board, row, col)
        elif self.piece_type.lower() == 'bishop':
            moves = self.available_moves_bishop(board, row, col)
        elif self.piece_type.lower() == 'knight':
            moves = self.available_moves_knight(board, row, col)
        elif self.piece_type.lower() == 'pawn':
            moves = self.available_moves_pawn(board, row, col)

        return moves

    def available_moves_king(self, board, row, col):
        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '0' or (board[r][c].islower() if self.color == 'white' else board[r][c].isupper()):
                    moves += 1
        return moves

    def available_moves_queen(self, board, row, col):
        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '0':
                    moves += 1
                    r, c = r + dr, c + dc
                elif (self.color == 'white' and board[r][c].islower()) or (self.color == 'black' and board[r][c].isupper()):
                    moves += 1
                    break
                else:
                    break
        return moves

    def available_moves_rook(self, board, row, col):
        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '0':
                    moves += 1
                    r, c = r + dr, c + dc
                elif (self.color == 'white' and board[r][c].islower()) or (self.color == 'black' and board[r][c].isupper()):
                    moves += 1
                    break
                else:
                    break
        return moves

    def available_moves_bishop(self, board, row, col):
        moves = 0
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '0':
                    moves += 1
                    r, c = r + dr, c + dc
                elif (self.color == 'white' and board[r][c].islower()) or (self.color == 'black' and board[r][c].isupper()):
                    moves += 1
                    break
                else:
                    break
        return moves

    def available_moves_knight(self, board, row, col):
        moves = 0
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == '0' or (board[r][c].islower() if self.color == 'white' else board[r][c].isupper())):
                moves += 1
        return moves

    def available_moves_pawn(self, board, row, col):
        moves = 0
        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1 

        if 0 <= row + direction < 8 and board[row + direction][col] == '0':
            moves += 1
            if row == start_row and board[row + 2 * direction][col] == '0' and board[row + direction][col] == '0':
                moves += 1

        if 0 <= row + direction < 8 and 0 <= col - 1 < 8:
            if board[row + direction][col - 1] != '0' and (
                (self.color == 'white' and board[row + direction][col - 1].islower()) or
                (self.color == 'black' and board[row + direction][col - 1].isupper())
            ):
                moves += 1
        
        if 0 <= row + direction < 8 and 0 <= col + 1 < 8:
            if board[row + direction][col + 1] != '0' and (
                (self.color == 'white' and board[row + direction][col + 1].islower()) or
                (self.color == 'black' and board[row + direction][col + 1].isupper())
            ):
                moves += 1

        return moves

def main():
    chessboard = [['0' for _ in range(8)] for _ in range(8)]
    
    pieces = []

    while True:
        user_input = input("Enter color, piece type, row, and column (or 'done' to finish): ").split()
        if user_input[0].lower() == 'done':
            break
        color, piece_type, row, col = user_input
        row = int(row)
        col = int(col)
        piece = Piece(color, piece_type, (row, col))
        pieces.append(piece)
        chessboard[row][col] = piece_type[0].upper() if color.lower() == 'white' else piece_type[0].lower()

    for row in chessboard:
        print(' '.join(row))
        
    piece = Piece("white", "queen", (0, 0))
    moves = piece.available_moves(chessboard)
    print("Total moves: ", moves)
        
if __name__ == "__main__":
    main()
