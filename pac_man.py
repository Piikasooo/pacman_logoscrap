"""Module"""


def get_coin(position, position_without_coin):
    """
    :param position:
    :param position_without_coin:
    :return:
    """
    if (position[0], position[1]) not in position_without_coin:
        position_without_coin.append((position[0], position[1]))
        return 1
    return 0


def walk_in_maze(size, position, path, walls):
    """
    :param size:
    :param position:
    :param path:
    :param walls:
    :return:
    """
    count_coins = 0
    position_without_coin = [(position[0], position[1])]
    for step in path:
        if step == "S":
            if position[1] != size[1] and \
                    (position[0], position[1] + 1) not in walls:
                position[1] += 1
                count_coins += get_coin(position, position_without_coin)
        elif step == "N":
            if position[1] - 1 != 0 and \
                    (position[0], position[1] - 1) not in walls:
                position[1] -= 1
                count_coins += get_coin(position, position_without_coin)
        elif step == "E":
            if position[0] != size[0] and \
                    (position[0] + 1, position[1]) not in walls:
                position[0] += 1
                count_coins += get_coin(position, position_without_coin)
        elif step == "W":
            if position[0] - 1 != 0 and \
                    (position[0] - 1, position[1]) not in walls:
                position[0] -= 1
                count_coins += get_coin(position, position_without_coin)
        else:
            raise ValueError("Only WESN letter are allowed")
    return count_coins


def simulation_pacman(file):
    """
    :return:
    """
    try:
        with open(file, "r") as file:
            lst = file.readline().split(' ')
            size = (int(lst[0]), int(lst[1]))
            lst = file.readline().split(' ')
            position = [int(lst[0]), int(lst[1])]
            path = file.readline()[:-1]
            walls = []
            for line in file:
                line = line.split(' ')
                walls.append((int(line[0]), int(line[1])))
    except ValueError:
        print("Could not convert data to an integer.")

    if (position[0], position[1]) in walls or \
            position[0] not in range(1, size[0]) or \
            position[1] not in range(1, size[1]):
        return "[-1, -1, 0]"

    count_coins = walk_in_maze(size, position, path, walls)
    return f"[{position[0]}, {position[1]}, {count_coins}]"


if __name__ == '__main__':
    print(simulation_pacman("test_input.txt"))
