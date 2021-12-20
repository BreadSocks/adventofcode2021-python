file = "input.txt"

coordinates = []
folds = []
for line in open(file).read().splitlines():
    if line.startswith("f"):
        parts = line.replace("fold along ", "").split("=")
        if parts[0] == "x":
            folds.append((int(parts[1]), 0))
        else:
            folds.append((0, int(parts[1])))
    elif line == "":
        continue
    else:
        parts = tuple((int(x) for x in line.split(",")))
        coordinates.append(parts)

for fold in folds:
    if fold[0] == 0:  # yaxis
        y_fold = fold[1]
        to_fold = [point for point in coordinates if point[1] > y_fold]
        new_coordinates = coordinates.copy()
        for coord in to_fold:
            new_coordinates.remove(coord)
            new_coord = (coord[0], y_fold - (coord[1] - y_fold))
            new_coordinates.append(new_coord)
    else:
        x_fold = fold[0]
        to_fold = [point for point in coordinates if point[0] > x_fold]
        new_coordinates = coordinates.copy()
        for coord in to_fold:
            new_coordinates.remove(coord)
            new_coord = (x_fold - (coord[0] - x_fold), coord[1])
            new_coordinates.append(new_coord)
    coordinates = new_coordinates
    print(len(set(coordinates)))
    break

# print(len(set(coordinates)))
# print(coordinates)
# print(sorted(coordinates))