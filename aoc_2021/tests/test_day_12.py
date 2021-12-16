import pytest
from day_12.solution import first_task, second_task

# @pytest.mark.parametrize(
#     "input, expected_output",
#     [
#         (
#             """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""",
#             10
#         ),
#         (
#             """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc""",
#             19
#         ),
#         (
#             """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW""",
#             226
#         ),
#     ]
# )
# def test_first_task(input, expected_output):
#     ex = list(map(lambda l: l.strip(), input.splitlines()))
#     assert first_task(ex) == expected_output


# @pytest.mark.parametrize(
#     "input, expected_output",
#     [
#         (
#             """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""",
#             36
#         ),
#         (
#             """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc""",
#             103
#         ),
#         (
#             """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW""",
#             3509
#         ),
#     ]
# )
def test_second_task_small():
    input="""start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    expected_output = 36
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output

    input="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
    expected_output = 103
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output

    input="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
    expected_output = 3509
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
