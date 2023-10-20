def n_queens(n, column_positions=[], row=0):
    if row == n:
        print(column_positions)
        return True

    for column in range(n):
        if is_valid(column_positions, row, column):
            column_positions.append(column)
            n_queens(n, column_positions, row + 1)
            column_positions.pop(-1)

    return False


def is_valid(column_positions, row, column):
    for queen_row, queen_column in enumerate(column_positions):
        if queen_column == column or \
                queen_row - queen_column == row - column or \
                queen_row + queen_column == row + column:
            return False
    return True


n_queens(8)