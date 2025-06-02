from sort_try import sort_try
import numpy as np
import random
import time


def gen_list_uniform(n_elms, max_value):
  return [random.randint(0, max_value) + random.random() for _ in range(n_elms)]

def run_time_trial(sorting_fn, lst_gen_fn, n_elms, max_value, iters, verbose=False):
  lsts = []
  for _ in range(iters):
    lsts.append(lst_gen_fn(n_elms, max_value))

  alphas = [0.00001, 0.00002, 0.00005, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05]
  best_time = 1000000
  best_alpha = 0.01
  for alpha in alphas:
    total_time = 0
    for i, lst in enumerate(lsts):
      start_time = time.time()
      new_lst = sorting_fn(lst, alpha=alpha)
      finish_time = time.time() - start_time
      if not sorted(lst) == new_lst:
        print('ERROR, FIRST LIST NOT CORRECTLY SORTED!')
        import sys
        sys.exit()
      if verbose:
        print(f'Time for Run {i + 1}: {finish_time}')
      total_time += finish_time
    
    if total_time < best_time:
      best_alpha = alpha
      best_time = total_time
    
    print(f'{alpha}, {total_time}')
  
  print(f'Best Run has alpha = {best_alpha} with Time: {best_time}')


n_elms = 100000
max_value = 100000
iters = 5

# run_time_trial(sort_try, gen_list_uniform, n_elms, max_value, iters=iters, verbose=False)


# arr = [4, 2, 5, 3, 1, 2.5]
# print(sort_try(arr, alpha=0.001))  # Output: 10


# PREVIOUS BAD IMPLEMENTATIONS:

# import numpy as np
# cimport numpy as cnp
# from collections import defaultdict
# from libc.string cimport memcpy

# def sort_try (list input_list, double alpha):
#     cdef cnp.ndarray[double, ndim=1] arr = np.array(input_list, dtype=np.float64)
#     return _sort_try(arr, alpha)


# cdef cnp.ndarray[double, ndim=1] result
# cdef double* dest_ptr
# cdef double* src_ptr
# cdef cnp.ndarray[double, ndim=1] bucket

# Sort each list and accumulate lists in memory using pointer approach
# PARALLELIZE HERE? Can sort each bucket individually, then add to result?
# result = np.empty(elms, dtype=np.float64)
# dest_ptr = <double*>result.data
# idx = 0
# for k in range(elms + 1):  # Process buckets in sorted order
#     bucket = np.sort(np.array(buckets[k], dtype=np.float64))
#     src_ptr = <double*>bucket.data
#     memcpy(dest_ptr + idx, src_ptr, bucket.size * sizeof(double))
#     idx += bucket.size

# return result.tolist()



# Maybe good idea to track sizes of each bucket earlier and then speed up
# This computation? Can avoid needing the new variable bucket in memory!
# cdef double[:] bucket
# cdef int idx = 0
# for key in buckets:
    # bucket = np.sort(np.array(buckets[key], dtype=np.float64))
    # result[idx:idx + bucket.shape[0]] = bucket
    # idx = idx + bucket.shape[0]



# cdef (double, double, int) cython_min(double[:] arr):
#    cdef int i
#    cdef double min_val = arr[0]
#    cdef double max_val = arr[0]
#    
#    for i in range(1, arr.shape[0]):
#        if arr[i] < min_val:
#            min_val = arr[i]
#        if arr[i] > max_val:
#            max_val = arr[i]
#    return min_val, max_val, arr.shape[0]