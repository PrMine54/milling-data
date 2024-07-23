from src.algorithms.algorithm1 import Algorithm1


def test_check_param():
    assert Algorithm1(12, 11).control_parameter() == 2
