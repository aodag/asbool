import pytest
from testfixtures import ShouldRaise


class TestAsBoolConverter(object):
    @pytest.fixture
    def target(self):
        from asbool.converter import AsBoolConverter
        return AsBoolConverter

    @pytest.mark.parametrize(
        "true_values, false_values, input, expected",
        [
            (['t'], ['f'], 't', True),
            (['t'], ['f'], 'f', False),
            (['true'], ['false'], 'true', True),
            (['true'], ['false'], 'false', False),
            (['true'], ['false'], 'TRUE', True),
            (['true'], ['false'], 'FALSE', False),
            (['t', 'true'], ['f', 'false'], 'true', True),
            (['t', 'true'], ['f', 'false'], 'false', False),
        ],
    )
    def test_call(self, target,
                  true_values, false_values, input, expected):
        converter = target(true_values, false_values)
        result = converter(input)
        assert result == expected

    def test_value_error(self, target):
        converter = target(["t"], ["f"])
        with ShouldRaise(ValueError("TRUE")):
            converter("TRUE")

    @pytest.mark.parametrize(
        "true_values, false_values, input, expected",
        [
            (['t'], ['f'], 0, False),
            (['t'], ['f'], [], False),
            (['t'], ['f'], 1, True),
            (['t'], ['f'], [0], True),
        ],
    )
    def test_non_string(self, target,
                        true_values, false_values, input, expected):
        converter = target(true_values, false_values)
        result = converter(input)
        assert result == expected
