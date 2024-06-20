
from math_lib import moyenne

def test_moyenne():

    input1 = [1, 1, 1]
    result = moyenne(input1)

    assert result == 1

    input2 = [1, 2, 3]
    result = moyenne(input2)

    assert result == 2