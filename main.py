import time
from multiprocessing import Pool, cpu_count

def factorize(number):
    return _factorize(number)

def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        result = pool.starmap(_factorize, [(num,) for num in numbers])
    return result

def _factorize(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def main():
    start_time = time.time()
    result_parallel = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time.time()

    print("Parallel Execution Time:", end_time - start_time)
    print("Results (Parallel):", result_parallel)

if __name__ == '__main__':
    main()
