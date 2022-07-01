import os
import time
from collections import defaultdict

import numpy as np
import pyperclip
from scipy.spatial.transform import Rotation as R
from utility import parse

GT = set([
    tuple([-892,524,684]),
    tuple([-876,649,763]),
    tuple([-838,591,734]),
    tuple([-789,900,-551]),
    tuple([-739,-1745,668]),
    tuple([-706,-3180,-659]),
    tuple([-697,-3072,-689]),
    tuple([-689,845,-530]),
    tuple([-687,-1600,576]),
    tuple([-661,-816,-575]),
    tuple([-654,-3158,-753]),
    tuple([-635,-1737,486]),
    tuple([-631,-672,1502]),
    tuple([-624,-1620,1868]),
    tuple([-620,-3212,371]),
    tuple([-618,-824,-621]),
    tuple([-612,-1695,1788]),
    tuple([-601,-1648,-643]),
    tuple([-584,868,-557]),
    tuple([-537,-823,-458]),
    tuple([-532,-1715,1894]),
    tuple([-518,-1681,-600]),
    tuple([-499,-1607,-770]),
    tuple([-485,-357,347]),
    tuple([-470,-3283,303]),
    tuple([-456,-621,1527]),
    tuple([-447,-329,318]),
    tuple([-430,-3130,366]),
    tuple([-413,-627,1469]),
    tuple([-345,-311,381]),
    tuple([-36,-1284,1171]),
    tuple([-27,-1108,-65]),
    tuple([7,-33,-71]),
    tuple([12,-2351,-103]),
    tuple([26,-1119,1091]),
    tuple([346,-2985,342]),
    tuple([366,-3059,397]),
    tuple([377,-2827,367]),
    tuple([390,-675,-793]),
    tuple([396,-1931,-563]),
    tuple([404,-588,-901]),
    tuple([408,-1815,803]),
    tuple([423,-701,434]),
    tuple([432,-2009,850]),
    tuple([443,580,662]),
    tuple([455,729,728]),
    tuple([456,-540,1869]),
    tuple([459,-707,401]),
    tuple([465,-695,1988]),
    tuple([474,580,667]),
    tuple([496,-1584,1900]),
    tuple([497,-1838,-617]),
    tuple([527,-524,1933]),
    tuple([528,-643,409]),
    tuple([534,-1912,768]),
    tuple([544,-627,-890]),
    tuple([553,345,-567]),
    tuple([564,392,-477]),
    tuple([568,-2007,-577]),
    tuple([605,-1665,1952]),
    tuple([612,-1593,1893]),
    tuple([630,319,-379]),
    tuple([686,-3108,-505]),
    tuple([776,-3184,-501]),
    tuple([846,-3110,-434]),
    tuple([1135,-1161,1235]),
    tuple([1243,-1093,1063]),
    tuple([1660,-552,429]),
    tuple([1693,-557,386]),
    tuple([1735,-437,1738]),
    tuple([1749,-1800,1813]),
    tuple([1772,-405,1572]),
    tuple([1776,-675,371]),
    tuple([1779,-442,1789]),
    tuple([1780,-1548,337]),
    tuple([1786,-1538,337]),
    tuple([1847,-1591,415]),
    tuple([1889,-1729,1762]),
    tuple([1994,-1805,1792]),
]
)



scanner_match = {0: {24: {'rotation': 13, 'translation': (26.0, 1163.0, -170.0)}}, 1: {15: {'rotation': 8, 'translation': (-158.0, -32.0, -1300.0)}}, 2: {18: {'rotation': 2, 'translation': (10.0, 110.0, 1119.0)}}, 3: {6: {'rotation': 19, 'translation': (1290.0, 46.0, 21.0)}}, 4: {11: {'rotation': 1, 'translation': (155.0, -134.0, -1274.0)}}, 5: {13: {'rotation': 5, 'translation': (-101.0, 1133.0, -33.0)}}, 6: {3: {'rotation': 3, 'translation': (46.0, -1290.0, -21.0)}}, 7: {18: {'rotation': 14, 'translation': (-6.0, -1045.0, -38.0)}}, 8: {12: {'rotation': 10, 'translation': (-64.0, -132.0, 1285.0)}}, 9: {6: {'rotation': 8, 'translation': (99.0, -1212.0, 116.0)}}, 10: {15: {'rotation': 19, 'translation': (1104.0, -101.0, -75.0)}}, 11: {4: {'rotation': 11, 'translation': (-155.0, 1274.0, -134.0)}}, 12: {4: {'rotation': 7, 'translation': (-14.0, -1225.0, -115.0)}}, 13: {5: {'rotation': 21, 'translation': (-1133.0, 33.0, 101.0)}}, 14: {25: {'rotation': 9, 'translation': (1172.0, -148.0, 70.0)}}, 15: {1: {'rotation': 8, 'translation': (-158.0, 32.0, -1300.0)}}, 16: {29: {'rotation': 14, 'translation': (1.0, -1364.0, 31.0)}}, 17: {9: {'rotation': 2, 'translation': (1227.0, 100.0, 51.0)}}, 18: {2: {'rotation': 18, 'translation': (1119.0, -110.0, -10.0)}}, 19: {3: {'rotation': 14, 'translation': (-31.0, -12.0, -1159.0)}}, 20: {3: {'rotation': 9, 'translation': (1338.0, -145.0, 47.0)}}, 21: {13: {'rotation': 7, 'translation': (-7.0, -1083.0, -174.0)}}, 22: {33: {'rotation': 21, 'translation': (172.0, -106.0, 1221.0)}}, 23: {10: {'rotation': 6, 'translation': (-1374.0, -87.0, 147.0)}}, 24: {0: {'rotation': 13, 'translation': (1163.0, 26.0, -170.0)}}, 25: {14: {'rotation': 23, 'translation': (70.0, 1172.0, 148.0)}}, 26: {15: {'rotation': 17, 'translation': (-145.0, 1243.0, -77.0)}}, 27: {0: {'rotation': 17, 'translation': (-1254.0, 90.0, -158.0)}}, 28: {14: {'rotation': 1, 'translation': (-1113.0, -28.0, 34.0)}}, 29: {16: {'rotation': 14, 'translation': (1364.0, -1.0, 31.0)}}, 30: {12: {'rotation': 23, 'translation': (-56.0, -1336.0, -39.0)}}, 31: {24: {'rotation': 22, 'translation': (1219.0, 17.0, -142.0)}}, 32: {1: {'rotation': 9, 'translation': (1039.0, -70.0, -13.0)}}, 33: {16: {'rotation': 11, 'translation': (-16.0, -129.0, -1289.0)}}, 34: {6: {'rotation': 14, 'translation': (-1255.0, -73.0, 100.0)}}, 35: {6: {'rotation': 20, 'translation': (-59.0, -6.0, -1125.0)}}}

# ROTATIONS = [
#     R.from_euler('zyx', [  0,  0,  0], degrees=True), #  I
#     R.from_euler('zyx', [  0,  0, 90], degrees=True), #  x
#     R.from_euler('zyx', [  0, 90,  0], degrees=True), #  y
#     R.from_euler('zyx', [ 90,  0,  0], degrees=True), #  z
#     R.from_euler('zyx', [  0,  0,180], degrees=True), #  xx
#     R.from_euler('zyx', [  0, 90, 90], degrees=True), #  xy
#     R.from_euler('zyx', [ 90,  0, 90], degrees=True), #  xz
#     R.from_euler('zxy', [  0, 90, 90], degrees=True), #  yx
#     R.from_euler('zyx', [  0,180,  0], degrees=True), #  yy
#     R.from_euler('yzx', [ 90, 90,  0], degrees=True), #  zy
#     R.from_euler('zyx', [180,  0,  0], degrees=True), #  zz
#     R.from_euler('zyx', [  0,  0,270], degrees=True), #  xxx
#     R.from_euler('zyx', [  0, 90,180], degrees=True), #  xxy
#     R.from_euler('zyx', [ 90,  0,180], degrees=True), #  xxz
#     R.from_euler('zyx', [ 90,180,  0], degrees=True), #  yyz
#     R.from_euler('zyx', [  0,180, 90], degrees=True), #  xyy
#     R.from_euler('zyx', [180,  0, 90], degrees=True), #  xzz
#     R.from_euler('zxy', [  0, 90,180], degrees=True), #  yxx
#     R.from_euler('zyx', [  0,270,  0], degrees=True), #  yyy
#     R.from_euler('zyx', [270,  0,  0], degrees=True), #  zzz
#     R.from_euler('zyx', [  0, 90,270], degrees=True), #  xxxy
#     R.from_euler('zyx', [ 90,180, 90], degrees=True), #  xyyz
#     R.from_euler('yzx', [ 90,180, 90], degrees=True), #  xzzy
#     R.from_euler('zyx', [  0,270, 90], degrees=True), #  xyyy
# ]

ROTATIONS = set([
    R.from_euler('zyx', [  0,  0,  0], degrees=True), #  I
    R.from_euler('zyx', [  0,  0, 90], degrees=True), #  x
    R.from_euler('zyx', [  0, 90,  0], degrees=True), #  y
    R.from_euler('zyx', [ 90,  0,  0], degrees=True), #  z
    R.from_euler('zyx', [  0,  0,180], degrees=True), #  xx
    R.from_euler('zyx', [  0, 90, 90], degrees=True), #  xy
    R.from_euler('zyx', [ 90,  0, 90], degrees=True), #  xz
    R.from_euler('zxy', [  0, 90, 90], degrees=True), #  yx
    R.from_euler('zyx', [  0,180,  0], degrees=True), #  yy
    R.from_euler('yzx', [ 90, 90,  0], degrees=True), #  zy
    R.from_euler('zyx', [180,  0,  0], degrees=True), #  zz
    R.from_euler('zyx', [  0,  0,270], degrees=True), #  xxx
    R.from_euler('zyx', [  0, 90,180], degrees=True), #  xxy
    R.from_euler('zyx', [ 90,  0,180], degrees=True), #  xxz
    R.from_euler('zyx', [ 90,180,  0], degrees=True), #  yyz
    R.from_euler('zyx', [  0,180, 90], degrees=True), #  xyy
    R.from_euler('zyx', [180,  0, 90], degrees=True), #  xzz
    R.from_euler('zxy', [  0, 90,180], degrees=True), #  yxx
    R.from_euler('zyx', [  0,270,  0], degrees=True), #  yyy
    R.from_euler('zyx', [270,  0,  0], degrees=True), #  zzz
    R.from_euler('zyx', [  0, 90,270], degrees=True), #  xxxy
    R.from_euler('zyx', [ 90,180, 90], degrees=True), #  xyyz
    R.from_euler('yzx', [ 90,180, 90], degrees=True), #  xzzy
    R.from_euler('zyx', [  0,270, 90], degrees=True), #  xyyy
])

PAIRS = [
    # [1, 0, 0] Forward
    # 1
    [
        [1, 0, 0],  # Forward
        [0, 1, 0],  # Left
    ],
    # 2
    [
        [1, 0, 0],  # Forward
        [0, -1, 0],  # Right
    ],
    # 3
    [
        [1, 0, 0],  # Forward
        [0, 0, 1],  # Up
    ],
    # 4
    [
        [1, 0, 0],  # Forward
        [0, 0, -1],  # Down
    ],


    # [0, 1, 0] Left
    # 1
    [
        [0, 1, 0],  # Left
        [-1, 0, 0],  # Backward
    ],
    # 2
    [
        [0, 1, 0],  # Left
        [1, 0, 0],  # Forward
    ],
    # 3
    [
        [0, 1, 0],  # Left
        [0, 0, 1],  # Up
    ],
    # 4
    [
        [0, 1, 0],  # Left
        [0, 0, -1],  # Down
    ],

    # [-1, 0, 0] Backward
    # 1
    [
        [-1, 0, 0],  # Backward
        [0, -1, 0],  # Right
    ],
    # 2
    [
        [-1, 0, 0],  # Backward
        [0, 1, 0],  # Left
    ],
    # 3
    [
        [-1, 0, 0],  # Backward
        [0, 0, 1],  # Up
    ],
    # 4
    [
        [-1, 0, 0],  # Backward
        [0, 0, -1],  # Down
    ],

    # [0, -1, 0] Right
    # 1
    [
        [0, -1, 0],  # Right
        [1, 0, 0],  # Forward
    ],
    # 2
    [
        [0, -1, 0],  # Right
        [-1, 0, 0],  # Backward
    ],
    # 3
    [
        [0, -1, 0],  # Right
        [0, 0, 1],  # Up
    ],
    # 4
    [
        [0, -1, 0],  # Right
        [0, 0, -1],  # Down
    ],

    # [0, 0, 1] Up
    # 1
    [
        [0, 0, 1],  # Up
        [0, 1, 0],  # Left
    ],
    # 2
    [
        [0, 0, 1],  # Up
        [1, 0, 0],  # Forward
    ],
    # 3
    [
        [0, 0, 1],  # Up
        [0, -1, 0],  # Right
    ],
    # 4
    [
        [0, 0, 1],  # Up
        [-1, 0, 0],  # Backward
    ],

    # [0, 0, -1] Down
    # 1
    [
        [0, 0, -1],  # Down
        [0, 1, 0],  # Left
    ],
    # 2
    [
        [0, 0, -1],  # Down
        [1, 0, 0],  # Forward
    ],
    # 3
    [
        [0, 0, -1],  # Down
        [0, -1, 0],  # Right
    ],
    # 4
    [
        [0, 0, -1],  # Down
        [-1, 0, 0],  # Backward
    ],
]

ROTATIONS_2 = []
for pair in PAIRS:
    ROTATIONS_2.append(
        R.from_matrix(
            [
                pair[0],
                pair[1],
                np.cross(pair[0], pair[1])
            ]
        )
    )
# ROTATIONS_2 = np.array(ROTATIONS_2)





def first_task(input):
    # for r in ROTATIONS_2:
    #     print(r.as_euler('zyx', degrees=True))
    #     if r in ROTATIONS:
    #         print(r)
    # print(ROTATIONS_2.intersection(ROTATIONS))

    # for r in ROTATIONS_2:
    #     print(np.round(r.as_euler('zxy', degrees=True)))

    # return

    scanners = []
    beacons = []
    for i, line in enumerate(input):
        if line == '':
            scanners.append(np.array(beacons))
            beacons = []
        elif line[:3] == '---':
            pass
        else:
            x, y, z = map(int, line.split(','))
            beacons.append(np.array([x, y, z]))

    if True:
        scanner_match = defaultdict(lambda: {})
        for scanner_idx in range(len(scanners)):
            print()
            scanner = scanners[scanner_idx]

            for comp_scan_idx in range(len(scanners)):
                if comp_scan_idx == scanner_idx:
                    continue

                compare_scanner = scanners[comp_scan_idx]

                rotation = None
                translation = None
                for r in range(24):
                    diffs = defaultdict(lambda : 0)
                    for beacon_1 in scanner:
                        for beacon_0 in compare_scanner:
                            diff = beacon_0 - np.round(ROTATIONS_2[r].apply(beacon_1))
                            diffs[tuple(diff)] += 1
                    for t, v in diffs.items():
                        if v >= 12:
                            rotation = r
                            translation = t
                            break
                if not rotation is None:
                    print(comp_scan_idx, 'matches', scanner_idx)
                    print(rotation)
                    print(translation)
                    scanner_match[scanner_idx].update(
                        {
                            comp_scan_idx: {
                                'rotation': rotation,
                                'translation': translation,
                            }
                        }
                    )

            if scanner_match[scanner_idx] == {}:
                print(scanner_idx, 'did not find a match')

        # if not rotation is None:
        #     print(comp_scan_idx, 'matches', scanner_idx)
        #     print(rotation)
        #     print(translation)
        #     scanner_match[scanner_idx].update(
        #         {
        #             comp_scan_idx: {
        #                 'rotation': rotation,
        #                 'translation': translation,
        #             }
        #         }
        #     )
        # else:
        #     print(scanner_idx, 'did not find a match')

    # scanner_match_old = {0: {1: {'rotation': 8, 'translation': (68.0, 1246.0, -43.0)}}, 1: {0: {'rotation': 8, 'translation': (68.0, -1246.0, -43.0)}}, 2: {4: {'rotation': 14, 'translation': (168.0, -1125.0, 72.0)}}, 3: {1: {'rotation': 0, 'translation': (160.0, -1134.0, -23.0)}}, 4: {1: {'rotation': 7, 'translation': (88.0, 113.0, -1104.0)}}}
    # print('0', scanner_match[0])
    # print('1', scanner_match[1])
    # print('2', scanner_match[2])
    # print('3', scanner_match[3])
    # print('4', scanner_match[4])
    # scanner_match = {0: {2: {'rotation': 22, 'translation': (-161.0, 1245.0, -28.0)}, 24: {'rotation': 13, 'translation': (26.0, 1163.0, -170.0)}, 27: {'rotation': 11, 'translation': (-1254.0, -158.0, 90.0)}}, 1: {15: {'rotation': 9, 'translation': (-158.0, -32.0, -1300.0)}, 27: {'rotation': 15, 'translation': (1126.0, -145.0, 75.0)}, 32: {'rotation': 23, 'translation': (-13.0, 1039.0, 70.0)}}, 2: {0: {'rotation': 22, 'translation': (-28.0, 1245.0, -161.0)}, 18: {'rotation': 16, 'translation': (10.0, 110.0, 1119.0)}}, 3: {6: {'rotation': 4, 'translation': (1290.0, 46.0, 21.0)}, 19: {'rotation': 5, 'translation': (12.0, 31.0, -1159.0)}, 20: {'rotation': 23, 'translation': (47.0, 1338.0, 145.0)}, 32: {'rotation': 9, 'translation': (115.0, -1242.0, 160.0)}}, 4: {11: {'rotation': 3, 'translation': (155.0, -134.0, -1274.0)}, 12: {'rotation': 21, 'translation': (-115.0, 14.0, -1225.0)}, 27: {'rotation': 10, 'translation': (-176.0, -1168.0, 27.0)}}, 5: {13: {'rotation': 17, 'translation': (-101.0, 1133.0, -33.0)}}, 6: {3: {'rotation': 12, 'translation': (46.0, -1290.0, -21.0)}, 9: {'rotation': 9, 'translation': (99.0, 1212.0, 116.0)}, 34: {'rotation': 5, 'translation': (73.0, 1255.0, 100.0)}, 35: {'rotation': 15, 'translation': (-6.0, -1125.0, 59.0)}}, 7: {18: {'rotation': 5, 'translation': (-6.0, -1045.0, -38.0)}}, 8: {12: {'rotation': 8, 'translation': (-64.0, -132.0, 1285.0)}}, 9: {6: {'rotation': 9, 'translation': (99.0, -1212.0, 116.0)}, 13: {'rotation': 11, 'translation': (31.0, 46.0, -1277.0)}, 17: {'rotation': 20, 'translation': (51.0, -100.0, -1227.0)}, 20: {'rotation': 16, 'translation': (-48.0, 80.0, -1046.0)}}, 10: {15: {'rotation': 4, 'translation': (1104.0, -101.0, -75.0)}, 23: {'rotation': 19, 'translation': (-147.0, -1374.0, -87.0)}}, 11: {4: {'rotation': 2, 'translation': (-155.0, 1274.0, -134.0)}}, 12: {4: {'rotation': 7, 'translation': (-14.0, -1225.0, -115.0)}, 8: {'rotation': 8, 'translation': (-64.0, -132.0, -1285.0)}, 30: {'rotation': 14, 'translation': (-1336.0, 39.0, -56.0)}}, 13: {5: {'rotation': 6, 'translation': (-1133.0, 33.0, 101.0)}, 9: {'rotation': 11, 'translation': (31.0, -1277.0, 46.0)}, 21: {'rotation': 21, 'translation': (-174.0, 7.0, -1083.0)}}, 14: {25: {'rotation': 14, 'translation': (1172.0, -148.0, 70.0)}, 28: {'rotation': 2, 'translation': (1113.0, -34.0, -28.0)}}, 15: {1: {'rotation': 9, 'translation': (-158.0, 32.0, -1300.0)}, 10: {'rotation': 12, 'translation': (-101.0, -1104.0, 75.0)}, 26: {'rotation': 11, 'translation': (-145.0, -77.0, 1243.0)}}, 16: {29: {'rotation': 5, 'translation': (1.0, -1364.0, 31.0)}, 33: {'rotation': 3, 'translation': (16.0, -1289.0, 129.0)}}, 17: {9: {'rotation': 16, 'translation': (1227.0, 100.0, 51.0)}, 34: {'rotation': 7, 'translation': (-1039.0, 127.0, 35.0)}}, 18: {2: {'rotation': 20, 'translation': (1119.0, -110.0, -10.0)}, 7: {'rotation': 5, 'translation': (1045.0, 6.0, -38.0)}, 23: {'rotation': 23, 'translation': (-105.0, 1057.0, -165.0)}}, 19: {3: {'rotation': 5, 'translation': (-31.0, -12.0, -1159.0)}, 35: {'rotation': 6, 'translation': (-83.0, 13.0, 1337.0)}}, 20: {3: {'rotation': 14, 'translation': (1338.0, -145.0, 47.0)}, 9: {'rotation': 20, 'translation': (-1046.0, -80.0, 48.0)}}, 21: {13: {'rotation': 7, 'translation': (-7.0, -1083.0, -174.0)}}, 22: {33: {'rotation': 6, 'translation': (172.0, -106.0, 1221.0)}}, 23: {10: {'rotation': 15, 'translation': (-1374.0, -87.0, 147.0)}, 18: {'rotation': 14, 'translation': (1057.0, 165.0, -105.0)}, 26: {'rotation': 19, 'translation': (-1162.0, -149.0, -30.0)}}, 24: {0: {'rotation': 13, 'translation': (1163.0, 26.0, -170.0)}, 31: {'rotation': 7, 'translation': (-17.0, -142.0, 1219.0)}}, 25: {14: {'rotation': 23, 'translation': (70.0, 1172.0, 148.0)}, 29: {'rotation': 7, 'translation': (48.0, 1117.0, 10.0)}}, 26: {15: {'rotation': 11, 'translation': (-145.0, 1243.0, -77.0)}, 23: {'rotation': 15, 'translation': (-149.0, -30.0, 1162.0)}, 27: {'rotation': 18, 'translation': (-149.0, 1078.0, 62.0)}}, 27: {0: {'rotation': 11, 'translation': (-1254.0, 90.0, -158.0)}, 1: {'rotation': 19, 'translation': (-75.0, 1126.0, -145.0)}, 4: {'rotation': 10, 'translation': (-176.0, -27.0, 1168.0)}, 26: {'rotation': 18, 'translation': (-62.0, 1078.0, 149.0)}}, 28: {14: {'rotation': 3, 'translation': (-1113.0, -28.0, 34.0)}, 29: {'rotation': 5, 'translation': (-66.0, -66.0, -1190.0)}}, 29: {16: {'rotation': 5, 'translation': (1364.0, -1.0, 31.0)}, 25: {'rotation': 21, 'translation': (10.0, -48.0, 1117.0)}, 28: {'rotation': 5, 'translation': (66.0, 66.0, -1190.0)}}, 30: {12: {'rotation': 23, 'translation': (-56.0, -1336.0, -39.0)}}, 31: {24: {'rotation': 21, 'translation': (1219.0, 17.0, -142.0)}}, 32: {1: {'rotation': 14, 'translation': (1039.0, -70.0, -13.0)}, 3: {'rotation': 9, 'translation': (115.0, 1242.0, 160.0)}}, 33: {16: {'rotation': 2, 'translation': (-16.0, -129.0, -1289.0)}, 22: {'rotation': 17, 'translation': (-1221.0, -172.0, 106.0)}}, 34: {6: {'rotation': 5, 'translation': (-1255.0, -73.0, 100.0)}, 17: {'rotation': 21, 'translation': (35.0, 1039.0, 127.0)}}, 35: {6: {'rotation': 19, 'translation': (-59.0, -6.0, -1125.0)}, 19: {'rotation': 17, 'translation': (-1337.0, 83.0, -13.0)}}}
    print(scanner_match)

    # rot = scanner_match[1][0]['rotation']
    # trans = scanner_match[1][0]['translation']
    # for beacon in scanners[1]:
    #     print()
    #     print(beacon)
    #     print(
    #         np.round(ROTATIONS[rot].apply(beacon)) + trans
    #     )

    known_transforms = {
        0: lambda b : b
    }

    print("Known transforms")
    while len(known_transforms.keys()) < len(scanner_match.keys()):
        for key, value in scanner_match.items():
            if key in known_transforms.keys():
                for k, v in value.items():
                    rot = v['rotation']
                    trans = v['translation']
                    transformation = np.eye(4)
                    transformation[:3, :3] = rot
                    transformation[:3, 3] = trans

                    known_transforms[key]

                    transform = lambda b : np.round(
                        ROTATIONS_2[rot].apply(known_transforms[key](b)) + trans
                        )
                    known_transforms[k] = transformation
                    print(k)

    print(known_transforms)

    set_of_beacons = set()
    for scanner_idx in range(len(scanners)):
        for beacon in scanners[scanner_idx]:
            set_of_beacons.add(known_transforms[scanner_idx](beacon))
            break
        break

    print(set_of_beacons)



    return



    set_of_beacons = set()
    print()
    for beacon in scanners[0]:
        set_of_beacons.add(tuple(np.round(beacon).astype('int')))
    print(set_of_beacons)
    print(len(set_of_beacons))

    print()
    print('Transforming')
    for scanner_idx in range(1, len(scanners)):
        print(scanner_idx)
        set_of_beacons_1 = set()
        for beacon in scanners[scanner_idx]:
            # if scanner_idx == 4:
            #     print('here')
            check_idx = scanner_idx
            print(beacon)
            # idx = [a for a in scanner_match[check_idx].keys()][0]
            while True:
                for idx in scanner_match[check_idx].keys():
                    rot = scanner_match[check_idx][idx]['rotation']
                    trans = scanner_match[check_idx][idx]['translation']

                    transformed_beacon = np.round(ROTATIONS_2[rot].apply(beacon) + trans)
                    beacon = transformed_beacon
                    # set_of_beacons.add(tuple(np.round(transformed_beacon).astype('int')))
                    if idx == 0:
                        break
                if idx != 0:
                    check_idx = idx
                else:
                    break

            rot = scanner_match[check_idx][idx]['rotation']
            trans = scanner_match[check_idx][idx]['translation']

            transformed_beacon = np.round(ROTATIONS_2[rot].apply(beacon) + trans)
            set_of_beacons.add(tuple(np.round(transformed_beacon).astype('int')))
            if scanner_idx == 4:
                set_of_beacons_1.add(tuple(np.round(transformed_beacon).astype('int')))
                continue
        # if scanner_idx == 4:
        #     for s in set_of_beacons_1:
        #         print(s)
        #     break

    # for diff, count in diffs.items():
    #     if count == 3:
    #         print(diff)

        # if np.allclose(ROTATIONS[r].apply(M2), goal):
        #     print(r)

    # print(len(set_of_beacons))
    # print("Set")
    # # for b in set_of_beacons:
    #     if b not in GT:
    #         print(b)
    return len(set_of_beacons)


def second_task(input):
    return None


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(str(first_answer))
        pyperclip.paste()

    print('#############################')
    print('The answer to the 1st task is')
    print(first_answer, f'in {first_time} seconds')

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print()
    print('The answer to the 2nd task is')
    print(second_answer, f'in {second_time} seconds')
    print('#############################')


if __name__ == '__main__':
    run_day()
