size_of_chessboard = int(input())
coordinates = input().split()
row, col = int(coordinates[0]), int(coordinates[1])

# I converted them to 0-based indexing to align with Python indices.
row -= 1
col -= 1

directions = [(-1, -1), (-1, 0), (-1, 1),
              ( 0, -1),          ( 0, 1),
              ( 1, -1), ( 1, 0), ( 1, 1)]

valid_moves = []

for R, C in directions:
    new_row = row + R
    new_col = col + C
    if 0 <= new_row < size_of_chessboard and 0 <= new_col < size_of_chessboard:
        # Remember we subtracted 1 to align with Python indices? Here we are adding back that 1 for 1-based indices as answers.
        valid_moves.append((new_row+1, new_col+1))

print(len(valid_moves))
for new_position in sorted(valid_moves):
    print(new_position[0], new_position[1])
