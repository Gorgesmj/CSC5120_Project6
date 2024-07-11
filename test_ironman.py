import pytest
import contextlib
import io

from ironman import IronMan


@pytest.fixture
def ai_ironMan():
    ai_ironMan = IronMan(False)
    ai_ironMan.maxHitPoints = 100
    ai_ironMan.hitPoints = 50
    return ai_ironMan


@pytest.fixture
def player_ironMan():
    player_ironMan = IronMan(True)
    player_ironMan.maxHitPoints = 100
    player_ironMan.hitPoints = 50
    player_ironMan.suitCharged = 0
    return player_ironMan


def test_take_damage_noCharge(player_ironMan):
    player_ironMan.takeDamage(10)

    assert player_ironMan.getHitPoints() == 40


def test_take_damage_Charged(player_ironMan):
    player_ironMan.suitCharged = 1
    player_ironMan.takeDamage(10)
    assert player_ironMan.getHitPoints() == 45


def test_attack(ai_ironMan):
    with contextlib.redirect_stdout(io.StringIO()):
        value = ai_ironMan.attack()
    assert isinstance(value, int)


def test_isAplayer(ai_ironMan, player_ironMan):
    assert player_ironMan.isPlayer
    assert ai_ironMan.isPlayer == False
