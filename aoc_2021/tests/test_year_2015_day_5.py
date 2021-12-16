from year_2015_day_5.solution import first_task, second_task


def test_first_task():
    assert first_task(["ugknbfddgicrmopn"]) == 1
    assert first_task(["aaa"]) == 1
    assert first_task(["jchzalrnumimnmhp"]) == 0
    assert first_task(["haegwjzuvuyypxyu"]) == 0
    assert first_task(["dvszwmarrgswjxmb"]) == 0


def test_second_task():
    assert second_task(["qjhvhtzxzqqjkmpb"]) == 1
    assert second_task(["xxyxx"]) == 1
    assert second_task(["uurcxstgmygtbstg"]) == 0
    assert second_task(["ieodomkazucvgmuy"]) == 0
