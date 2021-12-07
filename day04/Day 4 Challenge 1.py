file = "input.txt"

lines = open(file).read().splitlines()

draw_numbers = [int(x) for x in lines[0].split(",")]

boards = []
board = dict()
column = 0
for line in lines[2:]:
    if line == '':
        boards.append(board)
        column = 0
        board = dict()
        continue

    for index, number in enumerate([int(x) for x in line.split()]):
        board[index, column] = number
    column += 1
boards.append(board)  # final board
print(boards)

results = []
for board in boards:
    results.append([])

for number in draw_numbers:
    # first find out if the number exists in each board, and mark the location for each
    for index, board in enumerate(boards):
        if number in board.values():
            key_index = list(board.values()).index(number)
            key = list(board.keys())[key_index]
            results[index].append(key)

    # then loop through a 5x5 grid and see if a column or row can be found against the locations found above
    for index, result in enumerate(results):
        list1 = [0, 1, 2, 3, 4]
        for num in range(5):
            list2 = [num] * 5
            row = list(zip(list1, list2))
            column = list(zip(list2, list1))
            if all(x in result for x in row):
                print("found on board " + str(index + 1) + " row " + str(num + 1))
                print(boards[index])
                print(result)
                print(number)
                total = 0
                for key, value in boards[index].items():
                    if key not in result:
                        total += value
                print(total)
                print(total * number)
                quit()
                break
            elif all(x in result for x in column):
                print("found on board " + str(index + 1) + " column " + str(num + 1))
                print(boards[index])
                print(result)
                print(number)
                total = 0
                for key, value in boards[index].items():
                    if key not in result:
                        total += value
                print(total)
                print(total * number)
                quit()
                break
