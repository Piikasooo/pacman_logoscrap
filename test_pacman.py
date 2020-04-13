import os
import pytest
import pac_man

@pytest.fixture
def file():
    file = test_input.txt"
    with open(file, "wt") as f:
        f.write("7 7\n")
        f.write("1 6\n")
        f.write("EESWSSWNWW\n")
        f.write("1 4\n")
    yield file
    os.remove(file)


def test_game(file):
    assert pac_man.simulation_pacman(file) == "[1, 6, 5]"
