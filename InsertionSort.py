import timeit
import numpy as np


def insertion_sort(n):
    array = np.random.randint(500, size=n)
    start_time = timeit.default_timer()

    # PART I AND H: COMMENT LINE 6 and uncomment this section
    # array = []
    # for i in range(0, n):
    #     array.append(i)
    ################

    for i in range(1, len(array)):

        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    print(timeit.default_timer() - start_time)
    return timeit.default_timer() - start_time
