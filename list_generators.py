import random

def gen_list_uniform(n_elms, max_value):
  return [random.randint(0, max_value) + random.random() for _ in range(n_elms)]

def gen_list_uniform_ints(n_elms, max_value):
  return [random.randint(0, max_value) for _ in range(n_elms)]

def gen_list_ints(n_elms, max_value):
    lst = list(range(n_elms))
    random.shuffle(lst)
    return lst

def gen_list_skew(n_elms, max_value=None):
  lst = [i**2 for i in range(n_elms)]
  random.shuffle(lst)
  return lst

