import timeit
import numpy as np


def selection_sort(n):
    array = np.random.randint(500, size=n)
    start_time = timeit.default_timer()

    # PART I AND H: COMMENT LINE 6 and uncomment this section
    # array = []
    # for i in range(0, n):
    #     array.append(i)
    ################

    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
    print(timeit.default_timer() - start_time)
    return timeit.default_timer() - start_time
