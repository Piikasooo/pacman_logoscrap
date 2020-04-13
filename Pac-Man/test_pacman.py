import os
import pytest
import pac_man

@pytest.fixture
def file():
    file = "test_input.txt"
    with open(file, "wt") as f:
        f.write("7 7\n")
        f.write("1 6\n")
        f.write("EESWSSWNWW\n")
        f.write("1 4\n")
    yield file
    os.remove(file)

@pytest.fixture
def file_with_path_error():
    file = "test_input.txt"
    with open(file, "wt") as f:
        f.write("8 8\n")
        f.write("1 6\n")
        f.write("EESWSSKXDFWWSSEENN\n")
        f.write("1 4\n")
    yield file
    os.remove(file)

@pytest.fixture
def file_with_value_error():
    file = "test_input.txt"
    with open(file, "wt") as f:
        f.write("7 r\n")
        f.write("1 6\n")
        f.write("EESWSSWNWW\n")
        f.write("1 4\n")
    yield file
    os.remove(file)


def test_game(file):
    assert pac_man.simulation_pacman(file) == "[1, 6, 5]"


def test_value_error(file_with_value_error):
    with pytest.raises(ValueError):
        pac_man.simulation_pacman(file_with_value_error)


def test_path_error(file_with_path_error):
    with pytest.raises(Exception) as e:
        pac_man.simulation_pacman(file_with_path_error)


