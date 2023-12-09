from random import randint

WIDTH = 4
HEIGHT = 4
START_VALUE = 2

UP_KEY = "w"
DOWN_KEY = "s"
LEFT_KEY = "a"
RIGHT_KEY = "d"


def run():
    matrix = create_start_matrix()
    output(matrix)
    while True:
        do_step(matrix)


def create_start_matrix() -> list[list[int]]:
    matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    matrix[randint(0, HEIGHT - 1)][randint(0, WIDTH - 1)] = START_VALUE
    matrix[randint(0, HEIGHT - 1)][randint(0, WIDTH - 1)] = START_VALUE
    return matrix


def output(matrix: list[list[int]]):
    for col in range(WIDTH):
        print("-" * WIDTH, end="")
    print()
    for row in range(len(matrix)):
        print("| ", end="")
        for col in range(WIDTH):
            print(str(matrix[row][col]) + " | ", end="")
        print()
        for col in range(WIDTH):
            print("-" * WIDTH, end="")
        print()


def do_step(matrix: list[list[int]]):
    key = input("Сделайте ход: ").lower()
    if key == UP_KEY:
        transform_matrix(matrix, 1, 0)
    if key == DOWN_KEY:
        transform_matrix(matrix, -1, 0)
    if key == LEFT_KEY:
        transform_matrix(matrix, 0, -1)
    if key == RIGHT_KEY:
        transform_matrix(matrix, 0, 1)


def transform_matrix(matrix: list[list[int]], y_inc=0, x_inc=0) -> list[list[int]]:
    for row in range(len(matrix)):
        for col in range(WIDTH):
            elem = matrix[row][col]
            

    if __name__ == '__main__':
        run()
