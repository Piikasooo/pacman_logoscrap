"""Module for simulation of Pac-Man movement"""


def get_coin(position, position_without_coin):
    """
    The function checks if PacMan was in this cell
    :param position: cell where PacMan is located
    :param position_without_coin: a list of coordinates where PacMan was
    :return: 0 if Pacman was in this cell,  1 if not
    """
    if (position[0], position[1]) not in position_without_coin:
        position_without_coin.append((position[0], position[1]))
        return 1
    return 0


def walk_in_maze(size, position, path, walls):
    """
    This function calculates the number of coins
    collected by the PacMan in its path
    :param size: size of maze
    :param position: start position of PacMan
    :param path:
    :param walls: wall coordinates
    :return: the number of coins collected by the PacMan
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
            raise Exception("Only WESN letter are allowed")
    return count_coins


def simulation_pacman(file_name):
    """
    The main function to simulate the game PacMan
    :param file_name: name file with input data
    :return: coordinates of cell where Pac-Man finished \
            the game and total amount of collected coins
    """

    with open(file_name, "r") as file:
        try:
            lst = file.readline().split(' ')
            size = (int(lst[0]), int(lst[1]))
            lst = file.readline().split(' ')
            position = [int(lst[0]), int(lst[1])]
            path = file.readline()[:-1]
            walls = []
            for line in file:
                line = line.split(' ')
                walls.append((int(line[0]), int(line[1])))

            if (position[0], position[1]) in walls or \
                    position[0] not in range(1, size[0]) or \
                    position[1] not in range(1, size[1]):
                return "[-1, -1, 0]"

            count_coins = walk_in_maze(size, position, path, walls)
            return f"[{position[0]}, {position[1]}, {count_coins}]"
        except ValueError:
            raise ValueError("Could not convert data to an integer.")


if __name__ == '__main__':
    print(simulation_pacman("test.txt"))
