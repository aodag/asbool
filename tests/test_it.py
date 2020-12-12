import pytest


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
        with pytest.raises(ValueError) as excinfo:
            converter("TRUE")
        assert "TRUE" in str(excinfo.value)

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


@pytest.mark.parametrize(
    "input, expected",
    [
        ('TRUE', True),
        ('t', True),
        ('y', True),
        ('yes', True),
        (1, True),
        ('FALSE', False),
        ('f', False),
        ('n', False),
        ('no', False),
        (0, False),
    ]
)
def test_asbool(input, expected):
    from asbool import asbool
    result = asbool(input)
    assert result == expected
