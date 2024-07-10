import mock
import builtins

import pytest

import project6
import project6 as battleSim
from mugwump import Mugwump
from warrior import Warrior
from ironman import IronMan
from michael_new_char import MichaelNewChar
from chris_new_char import ChrisNewChar

"I don't have the attack choice in my battle sim "
@pytest.fixture
def player():
    player = project6.Player(1, True)
    player.nickName = "Genius"
    player.className= "IronMan"
    return player
def test_initiative():
    output = battleSim.initiative()
    assert isinstance(output, int)
    assert 0 < output and output < 3
    # create a different one
    output = battleSim.initiative()
    assert isinstance(output, int)
    assert 0 < output and output < 3
    # create a different one
    output = battleSim.initiative()
    assert isinstance(output, int)
    assert 0 < output and output < 3
    # create a different one
    output = battleSim.initiative()
    assert isinstance(output, int)
    assert 0 < output and output < 3


def test_play_again():
    with mock.patch.object(builtins, 'input', lambda _: 'Y'):
        assert battleSim.playAgain() == True
    with mock.patch.object(builtins, 'input', lambda _: 'Yes'):
        assert battleSim.playAgain() == True
    with mock.patch.object(builtins, 'input', lambda _: '0'):
        assert battleSim.playAgain() == False
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert battleSim.playAgain() == False


def test_pause_and_save():
    with mock.patch.object(builtins, 'input', lambda _: 'Y'):
        assert battleSim.pauseAndSave()  == True
    with mock.patch.object(builtins, 'input', lambda _: 'Yes'):
        assert battleSim.pauseAndSave() == True
    with mock.patch.object(builtins, 'input', lambda _: '0'):
        assert battleSim.pauseAndSave() == False
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert battleSim.pauseAndSave() == False


def test_new_game_ask():
    with mock.patch.object(builtins, 'input', lambda _: 'Y'):
        assert battleSim.newGameAsk() == True
    with mock.patch.object(builtins, 'input', lambda _: 'Yes'):
        assert battleSim.newGameAsk() == True
    with mock.patch.object(builtins, 'input', lambda _: '0'):
        assert battleSim.newGameAsk() == False
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert battleSim.newGameAsk() == False


def test_choose_char(player):
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        x = battleSim.chooseChar(player)
        assert isinstance(x, Mugwump)

        player.chara_choose =2
    with mock.patch.object(builtins, 'input', lambda _: '2'):
        x = battleSim.chooseChar(player)
        assert isinstance(x, Warrior)

    player.chara_choose =3
    with mock.patch.object(builtins, 'input', lambda _: '2'):
        x = battleSim.chooseChar(player)
        assert isinstance(x, IronMan)

    player.chara_choose =4
    with mock.patch.object(builtins, 'input', lambda _: '2'):
        x = battleSim.chooseChar(player)
        assert isinstance(x, MichaelNewChar)

    player.chara_choose =5
    with mock.patch.object(builtins, 'input', lambda _: '2'):
        x = battleSim.chooseChar(player)
        assert isinstance(x, ChrisNewChar)

    player.chara_choose = 4
    with mock.patch.object(builtins, 'input', lambda _: '2'):
        x = battleSim.chooseChar(player)
        assert isinstance(x, ChrisNewChar) == False