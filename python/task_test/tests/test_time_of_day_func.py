from python.task_test.func import time_of_day
import pytest
from freezegun import freeze_time


@freeze_time("2022-04-24 08:00:00")
@pytest.mark.parametrize('day_time', ["morning"])
def test_time_of_day_good(day_time):
    assert time_of_day() == day_time


@freeze_time('2022-04-24 08:00:00')
@pytest.mark.parametrize('time', ["night",
                                  'afternoon'])
def test_time_of_day_bad(time):
    with pytest.raises(AssertionError):
        assert time_of_day() == time
