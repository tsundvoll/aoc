from day_2.solution import first_task, second_task


def test_first_task():
    ex = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    assert first_task(ex) == 150

def test_second_task():
    ex = ("""forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2""").splitlines()
    assert second_task(ex) == 900
