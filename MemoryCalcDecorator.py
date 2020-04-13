from memory_profiler import profile


@profile(precision=4)
def longTime():
    for i in range(1000):
        i * 5


longTime()
