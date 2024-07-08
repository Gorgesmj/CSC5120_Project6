import pytest
import contextlib
import io

from mugwump import Mugwump


@pytest.fixture
def ai_mug():
    ai_mug = Mugwump(False)
    ai_mug.maxHitPoints = 20
    ai_mug.hitPoints = 0
    return ai_mug



@pytest.fixture
def player_mug():
    player_mug = Mugwump(True)
    return player_mug


def test_init_hitpoint(ai_mug):
    initHitPoint = ai_mug.getHitPoints()
    assert initHitPoint == 0


def test_set_hitPoint(ai_mug):
    ai_mug.setInitialHitPoints()
    assert ai_mug.hitPoints == 20

def test_attack(ai_mug):
    ai_mug.setInitialHitPoints()
    with contextlib.redirect_stdout(io.StringIO()):
        value = ai_mug.attack()
    assert isinstance(value, int)

def test_take_damage(ai_mug):
    ai_mug.setInitialHitPoints()
    ai_mug.takeDamage(10)
    assert ai_mug.hitPoints == 10
    ai_mug.takeDamage(-5)
    assert ai_mug.hitPoints == 15

    ai_mug.takeDamage(10000)
    assert ai_mug.hitPoints == 0





def test_ai_or_player(ai_mug, player_mug):
    assert player_mug.isPlayer
    assert ai_mug.isPlayer == False

