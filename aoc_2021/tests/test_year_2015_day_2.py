from year_2015_day_2.solution import first_task, second_task


def test_first_task():
    assert first_task(["2x3x4"]) == 58
    assert first_task(["1x1x10"]) == 43


def test_second_task():
    assert second_task(["2x3x4"]) == 34
    assert second_task(["1x1x10"]) == 14
