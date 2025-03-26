import pygame
import sys

# Configurações do tabuleiro
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Inicializa o pygame
pygame.init()

# Carrega as imagens das peças
PIECES = {
    "r": pygame.image.load("peao.webp"),
    "n": pygame.image.load("peao.webp"),
    "b": pygame.image.load("peao.webp"),
    "q": pygame.image.load("peao.webp"),
    "k": pygame.image.load("peao.webp"),
    "p": pygame.image.load("peao.webp"),
    "R": pygame.image.load("peao.webp"),
    "N": pygame.image.load("peao.webp"),
    "B": pygame.image.load("peao.webp"),
    "Q": pygame.image.load("peao.webp"),
    "K": pygame.image.load("peao.webp"),
    "P": pygame.image.load("peao.webp"),
}

# Redimensiona as imagens para caberem nos quadrados
for key in PIECES:
    PIECES[key] = pygame.transform.scale(PIECES[key], (SQUARE_SIZE, SQUARE_SIZE))


class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    def move_piece(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        piece = self.board[start_x][start_y]
        if piece == ".":
            return False

        # Implementa as regras de movimento de cada peça
        def is_valid_pawn_move(piece, start, end):
            direction = -1 if piece.isupper() else 1
            start_x, start_y = start
            end_x, end_y = end

            # Movimento para frente
            if start_y == end_y and self.board[end_x][end_y] == ".":
                if end_x - start_x == direction:
                    return True
            # Movimento inicial de dois quadrados
            if (start_x == 6 and piece.isupper()) or (start_x == 1 and piece.islower()):
                if end_x - start_x == 2 * direction and self.board[start_x + direction][start_y] == ".":
                    return True

            # Captura diagonal
            if abs(start_y - end_y) == 1 and end_x - start_x == direction:
                if self.board[end_x][end_y] != "." and self.board[end_x][end_y].islower() != piece.islower():
                    return True

            return False

        def is_valid_knight_move(start, end):
            start_x, start_y = start
            end_x, end_y = end
            dx, dy = abs(start_x - end_x), abs(start_y - end_y)
            return (dx, dy) in [(2, 1), (1, 2)]

        def is_valid_bishop_move(start, end):
            start_x, start_y = start
            end_x, end_y = end
            dx, dy = abs(start_x - end_x), abs(start_y - end_y)
            if dx == dy:
                step_x = (end_x - start_x) // dx
            step_y = (end_y - start_y) // dy
            for i in range(1, dx):
                if self.board[start_x + i * step_x][start_y + i * step_y] != ".":
                    return False
            return True
            return False

        def is_valid_rook_move(start, end):
            start_x, start_y = start
            end_x, end_y = end
            if start_x == end_x or start_y == end_y:
                step_x = (end_x - start_x) // max(1, abs(end_x - start_x))
            step_y = (end_y - start_y) // max(1, abs(end_y - start_y))
            for i in range(1, max(abs(end_x - start_x), abs(end_y - start_y))):
                if self.board[start_x + i * step_x][start_y + i * step_y] != ".":
                    return False
            return True
            return False
    
        def is_valid_queen_move(start, end):
            return is_valid_bishop_move(start, end) or is_valid_rook_move(start, end)

        def is_valid_king_move(start, end):
            start_x, start_y = start
            end_x, end_y = end
            dx, dy = abs(start_x - end_x), abs(start_y - end_y)
            return max(dx, dy) == 1

        # Determina se o movimento é válido
        piece = self.board[start_x][start_y]
        if piece.lower() == "p" and not is_valid_pawn_move(piece, start, end):
            return False
        if piece.lower() == "n" and not is_valid_knight_move(start, end):
            return False
        if piece.lower() == "b" and not is_valid_bishop_move(start, end):
            return False
        if piece.lower() == "r" and not is_valid_rook_move(start, end):
            return False
        if piece.lower() == "q" and not is_valid_queen_move(start, end):
            return False
        if piece.lower() == "k" and not is_valid_king_move(start, end):
            return False

        # Verifica se o destino contém uma peça do mesmo time
        if self.board[end_x][end_y] != "." and self.board[end_x][end_y].islower() == piece.islower():
            return False

        # Move a peça
        self.board[start_x][start_y]


def draw_board(screen, board):
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            piece = board[row][col]
            if piece != ".":
                screen.blit(PIECES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))


def parse_position(pos):
    col = ord(pos[0].lower()) - ord('a')
    row = 8 - int(pos[1])
    return row, col


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo de Xadrez")
    clock = pygame.time.Clock()

    board = ChessBoard()

    selected_piece = None
    selected_pos = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                row, col = mouse_y // SQUARE_SIZE, mouse_x // SQUARE_SIZE
                if board.board[row][col] != ".":
                    selected_piece = board.board[row][col]
                    selected_pos = (row, col)

            elif event.type == pygame.MOUSEBUTTONUP:
                if selected_piece:
                    mouse_x, mouse_y = event.pos
                    row, col = mouse_y // SQUARE_SIZE, mouse_x // SQUARE_SIZE
                    if board.move_piece(selected_pos, (row, col)):
                        selected_piece = None
                        selected_pos = None

        screen.fill(WHITE)
        draw_board(screen, board.board)

        # Desenha a peça sendo arrastada
        if selected_piece:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(PIECES[selected_piece], (mouse_x - SQUARE_SIZE // 2, mouse_y - SQUARE_SIZE // 2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()