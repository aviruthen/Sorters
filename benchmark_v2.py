import time
from list_generators import *
from sorters import *


def run_time_comparison(sorting_fn1, sorting_fn2, lst_gen_fn, n_elms, max_value, iters, verbose=False):
  lsts = []
  for _ in range(iters):
    lsts.append(lst_gen_fn(n_elms, max_value))

  total_time = 0
  for i, lst in enumerate(lsts):
    start_time = time.time()
    new_lst = sorting_fn1(lst)
    finish_time = time.time() - start_time
    if not sorted(lst) == new_lst:
      print('ERROR, FIRST LIST NOT CORRECTLY SORTED!')
      import sys
      sys.exit()
    if verbose:
      print(f'Time for Run {i + 1}: {finish_time}')
    total_time += finish_time

  print(f'Average Time for First Algorithm (elements: {n_elms}, max_value: {max_value}): {total_time / iters}')

  total_time = 0
  for i, lst in enumerate(lsts):
    start_time = time.time()
    new_lst = sorting_fn2(lst)
    finish_time = time.time() - start_time
    if verbose:
      print(f'Time for Run {i + 1}: {finish_time}')
    if not sorted(lst) == new_lst:
      print('ERROR, SECOND LIST NOT CORRECTLY SORTED!')
      import sys
      sys.exit()
    total_time += finish_time

  print(f'Average Time for Second Algorithm (elements: {n_elms}, max_value: {max_value}): {total_time / iters}')


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
    


def test(lst):
  new_lst = [None]*len(lst)
  for n in lst:
    new_lst[n] = n
  return new_lst

n_elms = 100000
max_value = 100000
iters = 5
verbose = False

# print(gen_list_skew(n_elms, max_value))

run_time_comparison(merge_sorted_buckets, avisort4, gen_list_uniform, n_elms, max_value, iters=iters, verbose=False)
# run_time_trial(avisort3, gen_list_uniform, n_elms, max_value, iters=iters, verbose=False)

# lst = gen_list_uniform_ints(n_elms, max_value)
# avisort(lst)

