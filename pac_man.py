with open("test_input.txt", "r") as f:
    lst = f.readline().split(' ')
    size_x, size_y = int(lst[0]), int(lst[1])

    lst = f.readline().split(' ')
    start_x, start_y = int(lst[0]), int(lst[1])

    path = f.readline()

    wall = []
    for line in f:
        line = line.split(' ')
        wall.append((int(line[0]), int(line[1])))

    print(wall)
