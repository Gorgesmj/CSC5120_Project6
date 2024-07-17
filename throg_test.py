import pytest
from throg import Throg


def test_throg_initialization():
    """Tests Throg object is initialized properly."""
    throg = Throg(isPlayer=True)
    assert throg.name == "Throg"
    assert throg.hitPoints > 0
    assert throg.thunderCharge == 1
    assert throg.resistance == 0
    print("test_throg_initialization passed")


def test_throg_attack_player_choice(monkeypatch):
    """Tests that Player attack damage is valid"""
    throg = Throg(isPlayer=True)
    # Use monkeypatch to replace input
    monkeypatch.setattr('builtins.input', lambda *args: '1')
    damage = throg.attack()
    assert damage >= 0
    print("test_throg_attack_player_choice passed")


def test_throg_attack_ai_choice():
    """Tests that AI attack damage is valid"""
    throg = Throg(isPlayer=False)
    damage = throg.attack()
    assert damage >= 0
    print("test_throg_attack_ai_choice passed")


def test_throg_take_damage():
    """Tests that Throg's health aligns with damage after attack."""
    throg = Throg(isPlayer=True)
    initial_hit_points = throg.hitPoints
    throg.takeDamage(10)
    assert throg.hitPoints == initial_hit_points - 10
    print("test_throg_take_damage passed")


def test_throg_resistance():
    """Tests that resistance attribute calculation works as expected."""
    throg = Throg(isPlayer=True)
    throg.resistance = 1
    initial_hit_points = throg.hitPoints
    throg.takeDamage(10)
    assert throg.hitPoints == initial_hit_points - 5
    print("test_throg_resistance passed")


def test_throg_ai_attack_type():
    """Tests that AI chooses valid attack choice."""
    throg = Throg(isPlayer=False)
    for _ in range(10):
        attack_type = throg.ai()
        assert attack_type in [1, 2, 3, 4]
    print("test_throg_ai_attack_type passed")


if __name__ == "__main__":
    pytest.main()
