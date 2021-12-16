import pytest
from day_16.solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("""D2FE28""", 6),
        ("""38006F45291200""", 1 + 6 + 2),
        ("""EE00D40C823060""", 7 + 2 + 4 + 1),
        ("""8A004A801A8002F478""", 16),
        ("""620080001611562C8802118E34""", 12),
        ("""C0015000016115A2E0802F182340""", 23),
        ("""A0016C880162017C3686B18A3D4780""", 31),
    ]
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))[0]
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("""C200B40A82""", 3),
        ("""04005AC33890""", 54),
        ("""880086C3E88112""", 7),
        ("""CE00C43D881120""", 9),
        ("""D8005AC2A8F0""", 1),
        ("""F600BC2D8F""", 0),
        ("""9C005AC2F8F0""", 0),
        ("""9C0141080250320F1802104A08""", 1),
    ]
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))[0]
    assert second_task(ex) == expected_output
