from dice import Die
def test_roll():
    d6 = Die(6)
    value = d6.roll()
    assert (value>0 and value<=6)
    assert value==d6.get_current_value()

