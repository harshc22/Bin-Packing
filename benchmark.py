import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.baseline import FiniteBins
from macpacking.algorithms.online import BestFit, FirstFit, NextFit, TerribleFit, WorstFit
from macpacking.algorithms.offline import BestFitDecreasing, FirstFitDecreasing,WorstFitDecreasing 
from macpacking.reader import BinppReader


# We consider:
#   - 500 objects (N4)
#   - bin capacity of 120 (C2)
#   - and weight in the [20,100] interval (W2)
CASES = './_datasets/binpp/N4C2W2'


def main():
    '''Example of benchmark code'''
    cases = list_case_files(CASES)
    run_bench(cases)


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def run_bench(cases: list[str]): #benchmarks the given algorithm
    runner = pyperf.Runner()
    for case in cases:
        name = basename(case)
        data = BinppReader(case).offline()
        binpacker = FiniteBins()
        runner.bench_func(name, binpacker, data)

