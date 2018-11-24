import lccnorm
import pytest


def test_no_normalization():
    assert lccnorm.normalize('n78890351') == 'n78890351'
