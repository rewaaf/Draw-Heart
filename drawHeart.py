grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print('Heart with while loop:')
new_string = ''
index_y = 0
while index_y < 6:
    index_x = 0
    while index_x < 9:
        new_string = new_string + grid[index_x][index_y]
        index_x += 1
    print(new_string)
    new_string = ''
    index_y += 1

print('---------')

print('Heart with for loop:')
new_str = ''
for y in range(6):
    for x in range(9):
        new_str = new_str + grid[x][y]
    print(new_str)
    new_str = ''
