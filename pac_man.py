with open("test_input.txt", "r") as f:
    lst = f.readline().split(' ')
    size_x, size_y = int(lst[0]), int(lst[1])

    lst = f.readline().split(' ')
    pos_x, pos_y = int(lst[0]), int(lst[1])

    path = f.readline()

    wall = []
    for line in f:
        line = line.split(' ')
        wall.append((int(line[0]), int(line[1])))
count_coins = 0
position_withot_coin = []
for step in path:
    print(f"step = {step}")
    print(f" befor coord = {pos_x} , {pos_y}")
    if step == "E":
        if pos_y != size_y and (pos_x, pos_y + 1) not in wall:
            pos_y += 1
            count_coins += 1
    elif step == "W":
        if pos_y - 1 != 0 and (pos_x, pos_y - 1) not in wall:
            pos_y -= 1
            count_coins += 1
    elif step == "S":
        if pos_x != size_x and (pos_x + 1, pos_y) not in wall:
            pos_x += 1
            count_coins += 1
    elif step == "N":
        if pos_x - 1 != 0 and (pos_x - 1, pos_y) not in wall:
            pos_x -= 1
            count_coins += 1
    print(f" after coord = {pos_x} , {pos_y}")
    #else:
    #    raise ValueError

print(f"[{pos_x} {pos_y}]  count = {count_coins}")