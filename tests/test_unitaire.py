from TTT.exemples import super_additionneur


def test_super_additionneur():

    assert super_additionneur(1, 1) == 2
    assert super_additionneur(3, 5) == 8
    assert super_additionneur(1, -1) == 0
    assert super_additionneur(2.5, 5.) == 7.5
    assert super_additionneur("1", "1") == 2
