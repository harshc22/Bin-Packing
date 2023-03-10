from macpacking.algorithms import offline, online, baseline

capacity=100
weights=[61, 62, 69, 83, 97, 13, 61, 88, 44, 72, 43, 66, 79, 97, 20, 23, 83, 62, 37, 100, 15, 70, 40, 8, 18, 44, 50, 67, 63, 17, 13, 37, 43, 14, 76, 8, 12, 97, 51, 30, 93, 39, 93, 92, 76, 75, 71, 99, 92, 19]
def test_baseline():
    base=baseline.BenMaier
    solution=base._process(base,capacity,weights)
    assert solution==[[100], [99], [97], [97], [97], [93], [93], [92, 8], [92, 8], [88, 12], [83, 17], [83, 15], [79, 20], [76, 23], [76, 19], [75, 18], [72, 13, 13], [71], [70, 30], [69], [67], [66], [63, 37], [62, 37], [62], [61, 39], [61], [51, 44], [50, 44], [43, 43, 14], [40]]

def test_online_NextFit():
    base=online.NextFit
    solution=base._process(base,capacity,weights)
    assert solution==[[61], [62], [69], [83], [97], [13, 61], [88], [44], [72], [43], [66], [79], [97], [20, 23], [83], [62, 37], [100], [15, 70], [40, 8, 18], [44, 50], [67], [63, 17, 13], [37, 43, 14], [76, 8, 12], [97], [51, 30], [93], [39], [93], [92], [76], [75], [71], [99], [92], [19]]

def test_online_TerribleFit():
    base=online.TerribleFit
    solution=base._process(base,capacity,weights)
    assert solution==[[61], [62], [69], [83], [97], [13], [61], [88], [44], [72], [43], [66], [79], [97], [20], [23], [83], [62], [37], [100], [15], [70], [40], [8], [18], [44], [50], [67], [63], [17], [13], [37], [43], [14], [76], [8], [12], [97], [51], [30], [93], [39], [93], [92], [76], [75], [71], [99], [92], [19]]

def test_online_FirstFit():
    base=online.FirstFit
    solution=base._process(base,capacity,weights)
    assert solution ==  [[13, 20], [61, 23, 15], [62, 8, 18], [69, 17], [83], [97, 37], [61, 8], [88, 43, 13], [44, 14, 12], [72, 30], [66, 19], [79], [97], [83, 37], [62], [100], [70, 44], [40, 43], [50], [67], [63], [76], [97, 39], [51], [93], [93], [92], [76], [75], [71], [99], [92]]


def test_online_BestFit():
    base=online.BestFit
    solution=base._process(base,capacity,weights)
    assert solution ==[[], [61, 37], [62, 17, 13], [69, 13], [83], [97], [61, 8], [88, 43, 12], [44, 23], [72], [66, 20], [79], [97, 15], [83, 37], [62], [100, 18, 8], [70, 44, 14], [40, 43], [50, 30], [67], [63, 19], [76], [97, 39], [51], [93], [93], [92], [76], [75], [71], [99], [92]]


def test_online_WorstFit():
    base=online.WorstFit
    solution=base._process(base,capacity,weights)
    assert solution == [[13], [61, 23], [62, 8], [69], [83], [97, 20], [61], [88, 43], [44], [72, 15], [66], [79], [97], [83, 37], [62], [100, 12], [70, 8, 18, 13], [40, 50], [44, 14], [67, 17], [63, 43], [37], [76], [97, 30], [51], [93, 19], [39], [93], [92], [76], [75], [71], [99], [92]]
 
def test_offline_NextFit():
    base=offline.NextFit
    solution=base._process(base,capacity,weights)
    assert solution==[[100], [99], [97], [97], [97], [93], [93], [92], [92], [88], [83], [83], [79], [76], [76], [75], [72], [71], [70], [69], [67], [66], [63], [62], [62], [61], [61], [51], [50, 44], [44, 43], [43, 40], [39, 37], [37, 30, 23], [20, 19, 18, 17, 15], [14, 13, 13, 12, 8, 8]]

def test_offline_FirstFitDecreasing():
    base=offline.FirstFitDecreasing
    solution=base._process(base,capacity,weights)
    assert solution == [[], [100], [99], [97], [97], [97], [93], [93, 8], [92, 8], [92, 12], [88, 17], [83, 15], [83, 20], [79, 23], [76, 19], [76, 18], [75, 14, 13], [72, 13], [71, 30], [70], [69], [67], [66, 37], [63, 37], [62], [62, 39], [61], [61, 44], [51, 44], [50, 43], [43], [40]]

def test_offline_BestFitDecreasing():
    base=offline.BestFitDecreasing
    solution=base._process(base,capacity,weights)
    assert solution == [[], [100], [99], [97], [97], [97], [93], [93], [92], [92, 8], [88, 15], [83, 14], [83, 20], [79, 23], [76, 18], [76, 17], [75, 13, 12], [72, 8], [71], [70, 30], [69], [67], [66], [63, 37], [62, 37], [62], [61], [61, 44], [51, 44], [50, 43, 13], [43, 39, 19], [40]]

def test_offline_WorstFitDecreasing():
    base=offline.WorstFitDecreasing
    solution=base._process(base,capacity,weights)
    assert solution == [[], [100], [99], [97], [97], [97], [93], [93], [92], [92], [88], [83], [83, 8], [79, 12], [76, 8], [76, 13], [75, 13], [72, 14], [71, 15], [70, 17], [69, 18], [67, 19], [66, 20], [63, 30], [62, 23], [62, 37], [61, 37], [61, 44], [51, 44], [50, 43], [43, 39], [40]]