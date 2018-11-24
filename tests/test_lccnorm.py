import lccnorm
import pytest


def test_no_normalization():
    assert lccnorm.normalize('n78890351') == 'n78890351'


def test_normalization():
    assert lccnorm.normalize('n78-890351') == 'n78890351'
    assert lccnorm.normalize('n78-89035') == 'n78089035'
    assert lccnorm.normalize('n 78890351 ') == 'n78890351'
    assert lccnorm.normalize(' 85000002 ') == '85000002'
    assert lccnorm.normalize('85-2 ') == '85000002'
    assert lccnorm.normalize('2001-000002') == '2001000002'
    assert lccnorm.normalize('75-425165//r75') == '75425165'
    assert lccnorm.normalize(' 79139101 /AC/r932') == '79139101'


def test_detect_error():
    # Too many characters to the right of the hyphen
    with pytest.raises(lccnorm.lccnorm.InvalidLccnError):
        lccnorm.normalize('n78-8903510')

    # Non-numeric character to the right of the hyphen
    with pytest.raises(lccnorm.lccnorm.InvalidLccnError):
        lccnorm.normalize('n78-890351a')
    

def test_valid():
    # 8 digits
    assert lccnorm.is_valid('79139101')is True
    
    # 1 alphabetic character + 8 digits
    assert lccnorm.is_valid('n78890351')is True

    # 2 alphabetic characters + 8 digits
    assert lccnorm.is_valid('gm71005810')is True

    # 2 digits + 8 digits
    assert lccnorm.is_valid('2001000002')is True

    # 1 alphabetic character + 2 alphabetic characters + 8 digits
    assert lccnorm.is_valid('agr14000102')is True

    # 1 alphabetic character + 2 digits + 8 digits
    assert lccnorm.is_valid('a2002003456')is True
      
    # 2 alphabetic characters + 10 digits
    assert lccnorm.is_valid('mm2002084896')is True


def test_invalid():
    # not enough characters
    assert lccnorm.is_valid('7913910')is False
    
    # 1 character prefix, but not a letter
    assert lccnorm.is_valid('078890351')is False
    
    # 2 character prefix, mixed letter and number
    assert lccnorm.is_valid('a078890351')is False
    
    # 3 character prefix, doesn't start with a letter
    assert lccnorm.is_valid('4gr14000102')is False
    
    # 3 character prefix, 2nd & 3rd characters mixed letter and number
    assert lccnorm.is_valid('ag414000102')is False
    
    # 1 alphabetic character + 11 digits
    assert lccnorm.is_valid('m02002084896')is False    
