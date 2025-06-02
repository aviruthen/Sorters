from collections import defaultdict

# sort_try.pyx
def sort_try (list input_list, double alpha):
    return _sort_try(input_list, alpha)

cdef list _sort_try(list arr, double alpha):
    cdef int i
    cdef double value
    cdef double min_val = arr[0]
    cdef double max_val = arr[0]
    cdef int elms = len(arr)
    cdef list result = []
    cdef object buckets
    
    # Compute max and min
    for i in range(1, elms):
        value = arr[i]
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value

    # Fill out dictionary list
    buckets = defaultdict(list)
    cdef double tmp_val = alpha * elms / max_val
    for i in range(0, elms):
        buckets[int((arr[i] - min_val) * tmp_val)].append(arr[i])

    for i in range(elms + 1):
        result.extend(sorted(buckets[i]))
    
    return result














    