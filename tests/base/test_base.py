# pylint: disable = too-few-public-methods, missing-docstring, no-self-use

from base import main


class TestBase:
    def test_main(self):
        main()
        assert True
