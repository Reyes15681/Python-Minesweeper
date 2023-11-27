from graphics import *
from random import randint

TILE_IMAGE = "tile.gif"
FLAG_IMAGE = "flag.gif"
MINE_IMAGE = "mine.gif"
LOSE_IMAGE = "lose.gif"
SMILEY_IMAGE = "smiley.gif"
BLANK_CELL = 0
EXPOSED_CELL = 10
MINE_CELL = 13
MAX_ADJACENT_MINES = 8
WIDTH_OF_IMAGES = 30  # is originally 32 instead of 30 --- 30 fit better than 32
HEIGHT_OF_IMAGES = 30  # is originally 32 instead of 30
LEFT_OFFSET = 50    # 100
RIGHT_OFFSET = 50   # 100
TOP_OFFSET = 100   # 120
BOTTOM_OFFSET = LEFT_OFFSET // 2
X_OFFSET = LEFT_OFFSET
Y_OFFSET = TOP_OFFSET


def level_difficulty():
    """
    This function does not take any parameter. user is prompted to enter a desired level of difficulty for the game.
    based on the selected difficulty, the number of rows, columns, num_mines are assigned values.
    the number of rows, columns, num_mines are returned
    :return: a list containing the number of rows, columns, and mines based on selected difficulty
    """
    # user input
    level_of_difficulty = str(input("Enter level of difficulty (Beginner/Intermediate/Expert): "))

    if level_of_difficulty is None:
        return None
    elif level_of_difficulty == "Beginner" or level_of_difficulty == "beginner":
        rows = 9
        columns = 9
        num_mines = 10
        return rows, columns, num_mines
    elif level_of_difficulty == "Intermediate" or level_of_difficulty == "intermediate":
        rows = 16
        columns = 16
        num_mines = 40
        return rows, columns, num_mines
    elif level_of_difficulty == "Expert" or level_of_difficulty == "expert":
        rows = 16
        columns = 30
        num_mines = 99
        return rows, columns, num_mines


def create_minesweeper_matrix(rows, columns):
    """
    creates a 2d-list/matrix based on level of difficulty filled with zeros and returns the 2d list.
    level of difficulty refers to a certain number of rows and of columns.
    :param rows: number of rows
    :param columns: number of rows
    :return: a matrix/2d-list
    """
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append([])
            matrix[i][j] = 0

    return matrix


def print_matrix_in_console(matrix, level_difficulty_selected):
    """
    function prints matrix in console given a matrix/ 2d-list
    :param matrix: a 2d list
    :param level_difficulty_selected: a list containing number of rows and columns
    :return: does not return anything
    """
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(str(matrix[i][j]).rjust(4), end="")
        print()
    print(f"printed, rows: {level_difficulty_selected[0]} by columns: {level_difficulty_selected[1]} with \
{level_difficulty_selected[2]} mines to be added")
    print()


def populate_with_mines(game_board_makers, level):
    """
    given a number of mines, a mine is placed in a random spot
    :param game_board_makers: a 2d list full of zeros
    :param level: level is a list containing number of rows, columns and mines
    :return: returns mine populated 2d-list
    """
    for i in range(level[2]):
        game_board_makers[randint(0, (level[0] - 1))][randint(0, (level[1]) - 1)] = 13

    return game_board_makers


def print_updated_matrix_in_console(matrix_populated_with_mines):
    """
    prints a 2d matrix in the console
    :param matrix_populated_with_mines:  a matrix with 13 representing mines
    :return: returns nothing
    """
    for i in range(len(matrix_populated_with_mines)):
        for j in range(len(matrix_populated_with_mines[i])):
            print(str(matrix_populated_with_mines[i][j]).rjust(4), end="")
        print()
    print()
    print()

def update_neighbor_count(game_board_with_mines, level):
    """
    this function checks every item in the 2d-list and adds one if a neighbor of it is a mine (13)
    :param game_board_with_mines: 2d-list with 13 at random location representing mines
    :param level: a list containing number of rows and columns
    :return: returns a 2d-list the contains the updated neighbor count
    """
    num_of_rows = int(level[0])
    num_of_columns = int(level[1])
    for i in range(num_of_rows):
        for j in range(num_of_columns):
            if game_board_with_mines[i][j] >= 13:
                if i == 0 and j == 0:
                    game_board_with_mines[i + 1][j] += 1
                    game_board_with_mines[i + 1][j + 1] += 1
                    game_board_with_mines[i][j + 1] += 1
                elif i == 0 and 0 < j < num_of_columns - 1:
                    game_board_with_mines[i][j - 1] += 1
                    game_board_with_mines[i + 1][j - 1] += 1
                    game_board_with_mines[i + 1][j] += 1
                    game_board_with_mines[i + 1][j + 1] += 1
                    game_board_with_mines[i][j + 1] += 1
                elif 0 < i < num_of_rows - 1 and j == 0:
                    game_board_with_mines[i - 1][j] += 1
                    game_board_with_mines[i - 1][j + 1] += 1
                    game_board_with_mines[i][j + 1] += 1
                    game_board_with_mines[i + 1][j + 1] += 1
                    game_board_with_mines[i + 1][j] += 1
                elif i == num_of_rows - 1 and 0 < j < num_of_columns - 1:
                    game_board_with_mines[i][j - 1] += 1
                    game_board_with_mines[i - 1][j - 1] += 1
                    game_board_with_mines[i - 1][j] += 1
                    game_board_with_mines[i - 1][j + 1] += 1
                    game_board_with_mines[i][j + 1] += 1
                elif 0 < i < num_of_rows - 1 and j == num_of_columns - 1:
                    game_board_with_mines[i + 1][j] += 1
                    game_board_with_mines[i + 1][j - 1] += 1
                    game_board_with_mines[i][j - 1] += 1
                    game_board_with_mines[i - 1][j - 1] += 1
                    game_board_with_mines[i - 1][j] += 1
                if 0 < i < num_of_rows - 1 and 0 < j < num_of_columns - 1:
                    game_board_with_mines[i - 1][j] += 1
                    game_board_with_mines[i + 1][j] += 1
                    game_board_with_mines[i][j - 1] += 1
                    game_board_with_mines[i][j + 1] += 1
                    game_board_with_mines[i - 1][j - 1] += 1
                    game_board_with_mines[i - 1][j + 1] += 1
                    game_board_with_mines[i + 1][j - 1] += 1
                    game_board_with_mines[i + 1][j + 1] += 1

    return game_board_with_mines


# Starting from this point down these function deal with drawing the internal components using graphics
def draw_the_grid(rows, columns, window):
    """
    draws the grid board
    :param rows: number of rows
    :param columns: number of columns
    :param window: the window to which to draw the grid into
    :return: return nothing
    """
    x_1 = X_OFFSET
    y_1 = Y_OFFSET
    for i in range(columns + 1):
        for j in range(columns + 1):
            p1 = Point(x_1, y_1)
            p2 = Point(x_1, y_1 + WIDTH_OF_IMAGES * rows)
            v_line = Line(p1, p2)
            v_line.setFill("white")
            v_line.draw(window)
        x_1 += WIDTH_OF_IMAGES

    x_2 = X_OFFSET
    y_2 = Y_OFFSET
    for g in range(rows + 1):
        for d in range(rows + 1):
            p_1 = Point(x_2, y_2)
            p_2 = Point(x_2 + WIDTH_OF_IMAGES * columns, y_2)
            h_line = Line(p_1, p_2)
            h_line.setFill("white")
            h_line.draw(window)
        y_2 += HEIGHT_OF_IMAGES


def draw_number_on_grid(rows, columns, window):
    """
    Draws the number of the row and column in the grid
    :param rows: number of rows
    :param columns: number of columns
    :param window: the window on which to draw the numbers in
    :return: return Nothing
    """

    h_x = X_OFFSET + (WIDTH_OF_IMAGES // 2)
    h_y = Y_OFFSET - (HEIGHT_OF_IMAGES // 2)
    for j in range(columns):
        h_point = Point(h_x, h_y)
        text = Text(h_point, j)
        text.setTextColor("white")
        text.draw(window)
        h_x += WIDTH_OF_IMAGES

    v_x = X_OFFSET - (WIDTH_OF_IMAGES // 2)
    v_y = Y_OFFSET + (HEIGHT_OF_IMAGES // 2)
    for d in range(rows):
        v_point = Point(v_x, v_y)
        text = Text(v_point, d)
        text.setTextColor("white")
        text.draw(window)
        v_y += HEIGHT_OF_IMAGES


def draw_cover_titles(rows, columns, window):
    """
    Draw and covers mine board information
    :param rows:
    :param columns:
    :param window:
    :return:
    """
    list_of_images = []
    x = X_OFFSET + (WIDTH_OF_IMAGES // 2)
    y = Y_OFFSET + (HEIGHT_OF_IMAGES // 2)
    for i in range(rows):
        list_of_images.append([])
        for j in range(columns):
            point = Point(x, y)
            picture = Image(point, TILE_IMAGE)
            list_of_images[i].append(picture)
            picture.draw(window)
            x += WIDTH_OF_IMAGES
        x = X_OFFSET + (WIDTH_OF_IMAGES // 2)
        y += HEIGHT_OF_IMAGES
    return list_of_images


def draw_board_content_graphics(rows, columns, two_d_list, window):
    for i in range(rows):
        for j in range(columns):
            if two_d_list[i][j] >= 13:
                x = X_OFFSET + ((WIDTH_OF_IMAGES // 2) + (WIDTH_OF_IMAGES * j))
                y = Y_OFFSET + ((HEIGHT_OF_IMAGES // 2) + (HEIGHT_OF_IMAGES * i))
                point = Point(x, y)
                picture = Image(point, MINE_IMAGE)
                picture.draw(window)
            elif two_d_list[i][j] != 0:
                x = X_OFFSET + ((WIDTH_OF_IMAGES // 2) + (WIDTH_OF_IMAGES * j))
                y = Y_OFFSET + ((HEIGHT_OF_IMAGES // 2) + (HEIGHT_OF_IMAGES * i))
                point = Point(x, y)
                text = Text(point, two_d_list[i][j])
                text.setTextColor("white")
                text.draw(window)


def draw_exit_circle(window):
    """
    Draws the exit circle in the window
    :param window: graphic window from graphics.py
    :return: NONE
    """
    center = Point(30, 30)
    circle = Circle(center, 15)
    circle.setFill("red")
    circle.setOutline("white")
    circle.draw(window)


def in_exit_circle(click):
    """
    This function checks if a user mouse click is in the exit circle
    :param click: a Point that denotes the location that a user has click in the graphics window
    :return: returns true if is in the circle and false if it is not in the circle
    """
    x = click.getX()
    y = click.getY()
    if 15 < x < 45 and 15 < y < 45:
        return True
    else:
        return False


# def draw_entire_board_and_internals(level_difficulty_selected):
#     win = GraphWin("MINESWEEPER", (level_difficulty_selected[1] * 50), (level_difficulty_selected[0] * 50), False)
#     win.setBackground("black")
#     game_board_markers = create_minesweeper_matrix(level_difficulty_selected[0], level_difficulty_selected[1])
#     print_matrix_in_console(game_board_markers, level_difficulty_selected)  # prints to console
#     game_board_with_mines = populate_with_mines(game_board_markers, level_difficulty_selected)
#     print_updated_matrix_in_console(game_board_with_mines)  # print game-board with mines in the matrix
#     game_board_with_mines_and_ones = update_neighbor_count(game_board_with_mines, level_difficulty_selected)
#     print_updated_matrix_in_console(game_board_with_mines_and_ones)  # print game-board w/ m, and neighbors
#     draw_the_grid(level_difficulty_selected[0], level_difficulty_selected[1], win)
#     draw_number_on_grid(level_difficulty_selected[0], level_difficulty_selected[1], win)
#     draw_board_content_graphics(level_difficulty_selected[0], level_difficulty_selected[1], \
#                                 game_board_with_mines_and_ones, win)
#     draw_exit_circle(win)
#     return win


def determine_row_clicked(click, number_of_rows):
    """
    This function takes a click point and the number of rows and determines what row the click was in
    :param click: a location of a Point that a user has clicked
    :param number_of_rows:  number of rows in the matrix
    :return: Returns the index of the row
    """
    y_click = click.getY()
    if Y_OFFSET < y_click < Y_OFFSET + HEIGHT_OF_IMAGES * number_of_rows:
        row_index = int((y_click - Y_OFFSET) // HEIGHT_OF_IMAGES)
        return row_index


def determine_column_clicked(click, number_of_columns):
    x_click = click.getX()
    if X_OFFSET < x_click < X_OFFSET + WIDTH_OF_IMAGES * number_of_columns:
        column_index = int((x_click - X_OFFSET) // WIDTH_OF_IMAGES)
        return column_index


def expose_all_mines(game_board_markers, game_board_images, win):
    for i in range(len(game_board_markers)):
        for j in range(len(game_board_markers[i])):
            if game_board_markers[i][j] >= 13:
                game_board_images[i][j].undraw()
    return None


def expose_empty_cells(game_board_markers, game_board_images, row, column, win, num_of_rows, num_of_columns):
    """
    USING RECURSION THE FUNCTION TAKES A ROW AND COLUMN THAT WAS CLICKED AND CHECKS THE NEIGHBORS FOR BLANK SPACES AND
    NUMBERS TO THEN UNCOVER, ONCE ONE CELL CHECKS THE NEIGHBORS IT THEN TELLS ITS NEIGHBOR TO CHECKS THEIR NEIGHBORS
    FOR BLANK SPACES AND NUMBERS TO UNCOVER. ONCE A TITLE IS UNCOVERED ITS VALUE CHANGES TO 10 TO INDICATE THE TITLE
    IS NO LONGER SHOWN ON THE GRAPHICS WINDOW
    TO AVOID AND INFINITE LOOP IF THE NEIGHBOR IS ALREADY UNCOVER(EQUAL TO 10) THEN IT RETURNS AND STOPS THE FUNCTION
    :param game_board_markers: game board with all locations of bombs none bombs and blank squares
    :param game_board_images: a list of tiles that cover the board
    :param row: the row that was clicked
    :param column: column that was clicked
    :param win: graphics window
    :param num_of_rows: number of rows on the board
    :param num_of_columns:  number of columns on the board
    :return: NONE
    """
    if 0 <= row < num_of_rows and 0 <= column < num_of_columns and game_board_markers[row][column] != 10 and \
            game_board_markers[row][column] < 13:
        if game_board_markers[row][column] == 10:
            return
        elif 1 <= game_board_markers[row][column] <= 8:
            game_board_images[row][column].undraw()
            game_board_markers[row][column] = 10
        else:
            game_board_images[row][column].undraw()
            game_board_markers[row][column] = 10
            expose_empty_cells(game_board_markers, game_board_images, row - 1, column - 1, win, num_of_rows,
                               num_of_columns)
            expose_empty_cells(game_board_markers, game_board_images, row - 1, column, win, num_of_rows, num_of_columns)
            expose_empty_cells(game_board_markers, game_board_images, row - 1, column + 1, win, num_of_rows,
                               num_of_columns)
            expose_empty_cells(game_board_markers, game_board_images, row, column - 1, win, num_of_rows, num_of_columns)
            expose_empty_cells(game_board_markers, game_board_images, row, column + 1, win, num_of_rows, num_of_columns)
            expose_empty_cells(game_board_markers, game_board_images, row + 1, column - 1, win, num_of_rows,
                               num_of_columns)
            expose_empty_cells(game_board_markers, game_board_images, row + 1, column, win, num_of_rows, num_of_columns)
            expose_empty_cells(game_board_markers, game_board_images, row + 1, column + 1, win, num_of_rows,
                               num_of_columns)


def draw_rest_button(window, rows, w_of_images):
    x_point = (((rows * w_of_images) + LEFT_OFFSET + RIGHT_OFFSET) /  2)
    center = Point(x_point, 30)
    image = Image(center, "smiley.gif")
    image.draw(window)
    return x_point


def in_reset_button(mouse_click, x_point):
    x = mouse_click.getX()
    y = mouse_click.getY()
    if x_point - WIDTH_OF_IMAGES < x < x_point + WIDTH_OF_IMAGES and 30 - WIDTH_OF_IMAGES < y < 30 + WIDTH_OF_IMAGES:
        return True


def main():
    level_difficulty_selected = level_difficulty()  # is a list, index 0  is rows, index 1 is columns, index 3 is mines
    win = GraphWin("MINESWEEPER", ((level_difficulty_selected[1] * WIDTH_OF_IMAGES) + LEFT_OFFSET + RIGHT_OFFSET ), \
                   ((level_difficulty_selected[0] * HEIGHT_OF_IMAGES) + TOP_OFFSET * 1.5 ), False)
    win.setBackground("black")
    game_board_markers = create_minesweeper_matrix(level_difficulty_selected[0], level_difficulty_selected[1])
    print_matrix_in_console(game_board_markers, level_difficulty_selected)  # prints to console
    game_board_with_mines = populate_with_mines(game_board_markers, level_difficulty_selected)
    print_updated_matrix_in_console(game_board_with_mines)  # print game-board with mines in the matrix
    game_board_markers = update_neighbor_count(game_board_with_mines, level_difficulty_selected)
    print_updated_matrix_in_console(game_board_markers)  # print game-board w/ m, and neighbors
    draw_the_grid(level_difficulty_selected[0], level_difficulty_selected[1], win)
    draw_number_on_grid(level_difficulty_selected[0], level_difficulty_selected[1], win)
    draw_board_content_graphics(level_difficulty_selected[0], level_difficulty_selected[1], \
                                game_board_markers, win)
    draw_exit_circle(win)
    if level_difficulty_selected is not None:
        list_of_titles = draw_cover_titles(level_difficulty_selected[0], level_difficulty_selected[1], win)
        mouse_click = win.getMouse()
        while in_exit_circle(mouse_click) is False:
            row = determine_row_clicked(mouse_click, level_difficulty_selected[0])
            column = determine_column_clicked(mouse_click, level_difficulty_selected[1])
            if row is None or column is None:
                pass
            elif game_board_markers[row][column] == EXPOSED_CELL:
                pass
            elif 1 <= game_board_markers[row][column] <= 8:
                # remove tile at row and column index
                list_of_titles[row][column].undraw()
                game_board_markers[row][column] = EXPOSED_CELL
            elif game_board_markers[row][column] >= 13:
                expose_all_mines(game_board_markers, list_of_titles, win)
            elif game_board_markers[row][column] == BLANK_CELL:
                expose_empty_cells(game_board_markers, list_of_titles, row, column, win, level_difficulty_selected[0], \
                                   level_difficulty_selected[1])
            win.update()
            print_updated_matrix_in_console(game_board_markers)
            mouse_click = win.getMouse()
        print("click was in exit circle")
    else:
        print("Not a valid level!!")


main()
