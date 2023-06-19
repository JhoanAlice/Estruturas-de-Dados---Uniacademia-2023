import time

def read_file(filename):
    with open(filename, 'r') as file:
        content = [int(x) for x in file.read().split()]
    return content

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time
