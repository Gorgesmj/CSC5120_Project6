
import mock
import builtins
import project6 as battleSim

"I don't have the attack choice in my battle sim "


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
