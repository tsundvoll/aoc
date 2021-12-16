from year_2015_day_3.solution import first_task, second_task


def test_first_task():
    assert first_task(">") == 2
    assert first_task("^>v<") == 4
    assert first_task("^v^v^v^v^v") == 2


def test_second_task():
    assert second_task("^v") == 3
    assert second_task("^>v<") == 3
    assert second_task("^v^v^v^v^v") == 11
