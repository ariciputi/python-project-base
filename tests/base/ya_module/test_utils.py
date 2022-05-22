# pylint: disable = too-few-public-methods, missing-docstring, no-self-use

from base.ya_module.utils import dummy_sum


class TestDummySum:
    def test_dummy_sum(self):
        assert dummy_sum(1, 2) == 3
