'''Resolutor de Sudoku
Utiliza la biblioteca pygame (consulta las instrucciones de instalación de pip) para
implementar una interfaz gráfica (GUI) que resuelve automáticamente los rompecabezas de
Sudoku.
Para resolver un rompecabezas de Sudoku, puedes crear un programa que utilice un algoritmo
de retroceso (backtracking) que verifica incrementalmente soluciones, adoptando o
abandonando la solución actual si no es viable.
Este paso de abandonar una solución es la característica definitoria de un enfoque de
retroceso, ya que el programa retrocede para probar una nueva solución hasta que encuentra
una válida. Este proceso se lleva a cabo de manera incremental hasta que todo el tablero se
haya completado correctamente. (cg)
'''

# -----------------------------------------------------
# Paso 1: Instalar Dependencias
import pygame          # pip install pygame --> comandos necesarios para instalar pygame
import numpy as np


# -----------------------------------------------------
'''Paso 2: Crear el Solucionador de Sudoku
Antes de trabajar en la interfaz gráfica, es una buena idea implementar 
la lógica de resolución del Sudoku. 
Usaremos el algoritmo de retroceso (backtracking) para esto
'''
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):
    # Verifica fila
    if num in board[row]:
        return False
    
    # Verifica columna
    if num in board[:, col]:
        return False
    
    # Verifica cuadrícula 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row, col] = num
                        if solve(board):
                            return True
                        board[row, col] = 0
                return False
    return True

# Ejemplo de uso
if __name__ == "__main__":
    board = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    if solve(board):
        print("Sudoku resuelto:")
        print_board(board)
    else:
        print("No se pudo resolver el Sudoku")


#---------------------------------------------------
'''Paso 3: Crear la Interfaz Gráfica con Pygame
Ahora vamos a construir una interfaz gráfica simple con pygame 
que muestre el tablero y permita interactuar con él.
'''

# Inicializar pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Configuración de la pantalla
SIZE = (540, 540)
GRID_SIZE = 9
CELL_SIZE = SIZE[0] // GRID_SIZE
FONT = pygame.font.SysFont('arial', 40)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Sudoku Solver')

def draw_grid(board):
    screen.fill(WHITE)
    
    for i in range(GRID_SIZE + 1):
        thickness = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SIZE[1]), thickness)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (SIZE[0], i * CELL_SIZE), thickness)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row, col] != 0:
                text = FONT.render(str(board[row, col]), True, BLACK)
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 8))
    
    pygame.display.flip()

def main():
    board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    draw_grid(board)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Resuelve el Sudoku al presionar 'r'
                    if solve(board):
                        draw_grid(board)
                elif event.key == pygame.K_q:  # Salir al presionar 'q'
                    running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()

    

'''Explicación
1- Lógica de Solución: La función solve resuelve el Sudoku utilizando el algoritmo de retroceso. 
La función is_valid verifica si un número es válido en una posición dada.

2- Interfaz Gráfica: La interfaz gráfica en pygame muestra el tablero de Sudoku y dibuja una cuadrícula. 
Al presionar la tecla 'r', intenta resolver el Sudoku y actualiza la pantalla con el tablero resuelto.
'''

