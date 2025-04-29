import pytest
from p import pr

def tpr():
    assert pr(2) == True

    assert pr(19) == True

    assert pr(23) == True

    assert pr(29) == True

    assert pr(37) == True

    assert pr(41) == True

    assert pr(43) == True

    assert pr(47) == True

    assert pr(53) == True

    assert pr(59) == True


    assert pr(103) == True

    assert pr(105) == False

   
    assert pr(-2) == False

    assert pr(-5) == False

    assert pr(-7) == False

    assert pr(-10) == False


    assert pr(0) == False

    assert pr(1) == False

    assert pr(4) == False

    assert pr(6) == False

    assert pr(8) == False

    assert pr(9) == False

    assert pr(10) == False

    assert pr(12) == False

    assert pr(14) == False

    assert pr(15) == False
