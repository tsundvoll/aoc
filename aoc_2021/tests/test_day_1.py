from day_1.solution import first_task, second_task


def test_first_task():
    lists = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    assert first_task(lists) == 7


def test_second_task():
    lists = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    assert second_task(lists) == 5
