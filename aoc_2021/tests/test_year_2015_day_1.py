from year_2015_day_1.solution import first_task, second_task


def test_first_task():
    assert first_task("(())") ==  0
    assert first_task("(((") ==  3
    assert first_task("))(((((") ==  3
    assert first_task("())") == -1
    assert first_task(")))") == -3

    assert first_task("()()") ==  0
    assert first_task("(()(()(") ==  3
    assert first_task("))(") == -1
    assert first_task(")())())") == -3


def test_second_task():
    assert second_task(")") == 1
    assert second_task("()())") == 5
