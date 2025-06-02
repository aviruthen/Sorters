import random as r
import time as t

MAX_VALUE = 10000
ELMS = 100000
SHIFT_VAL = 1/ELMS

#################### RANDOM LIST GENERATORS ###############################

def gen_list_uniform():
  lst = []
  for i in range(ELMS):
      lst += [r.randint(0, MAX_VALUE) + r.random()]
  return lst

def gen_list_uniform_ints():
  lst = []
  for i in range(ELMS):
      lst += [r.randint(0, MAX_VALUE)]
  return lst

def gen_list_ints():
  lst = []
  for i in range(ELMS):
    lst += [i]
  r.shuffle(lst)
  return lst

def gen_list_skew():
  lst = []
  for i in range(ELMS):
    lst += [i**2]
  r.shuffle(lst)
      #lst += [(r.randint(0, MAX_VALUE) + r.random())**2]

  #print(lst)
  return lst


################ SORTING ALGORITHMS (MULTIPLE VERSIONS) ######################

def get_min_max(lst):
  min = lst[0]
  max = lst[0]
  for e in lst:
     if e < min:
        min = e
     elif e > max:
        max = e
  return min, max

def ins_sort(lst):
  #print(lst)
  #print(len(lst))
  for i in range(1, ELMS):
    j = i
    while j > 0 and lst[j-1] > lst[j]:
        lst[j], lst[j-1] = lst[j-1], lst[j]
        j -= 1
  return lst

def sort_list(lst):
  min, max = get_min_max(lst)

  hmap = {}
  shift_lst = [0]*ELMS
  for e in lst:
    x = int((e - min)/max * (ELMS-1))
    hmap[ELMS*x + shift_lst[x]] = e
    shift_lst[x] += 1
  #print(shift_lst)
  #i = 0 
  #for elm in shift_lst:
    #if elm > 0.01: i += 1
  #print(i)
 #sorted_lst = [None]*ELMS
 # for i in hmap:
  #  if sorted_lst[hmap[i]] is None:
  #     sorted_lst[hmap[i]] = i
  #  else

  #print(lst)
  sorted_lst = [None]*ELMS
  index = 0
  #print(hmap)
  for i in range(0,ELMS*ELMS,ELMS):
    #print("i: " + str(i))
    #print("index: " + str(index))
    try: 
      sorted_lst[index] = hmap[i]
      index += 1

      loop = True
      num_loops = 1
      while loop:
        try:
          sorted_lst[index] = hmap[i+num_loops]
          index += 1
          num_loops += 1
        except Exception:
          loop = False
    
    except Exception:
      pass
  #print(index)
  #print(sorted_lst)
  sorted_lst = ins_sort(sorted_lst)

  return sorted_lst

  
def sort_list_power(lst):
  a = t.time()
  min, max = get_min_max(lst)
  print("Finding Min-Max: " + str(t.time() - a))
  a = t.time()

  hmap = {}
  shift_lst = [0]*ELMS
  for e in lst:
    x = int((e - min)/max * (ELMS-1))
    hmap[ELMS*x + shift_lst[x]] = e
    shift_lst[x] += 1

  print("Make HashMap: " + str(t.time() - a))
  a = t.time()

  sorted_lst = [None]*ELMS
  index = 0
  for i in range(0,ELMS*ELMS,ELMS):
    try: 
      sorted_lst[index] = hmap[i]

      index += 1
      loop = True
      num_loops = 1
      while loop:
        try:
          sorted_lst[index] = hmap[i+num_loops]
          j = index
          #INSERTION SORT HERE
          while j > 0 and sorted_lst[j-1] > sorted_lst[j]:
            sorted_lst[j], sorted_lst[j-1] = sorted_lst[j-1], sorted_lst[j]
            j -= 1
          
          index += 1
          num_loops += 1
        except Exception:
          loop = False
    
    except Exception:
      pass
  
  print("Sort List: " + str(t.time() - a))

  return sorted_lst


def sort_list_power2(lst):
  a = t.time()
  min, max = get_min_max(lst)
  print("Finding Min-Max: " + str(t.time() - a))
  a = t.time()

  hmap = {}
  shift_lst = [0]*ELMS
  for e in lst:
    x = int((e - min)/max * (ELMS-1))
    hmap[ELMS*x + shift_lst[x]] = e
    shift_lst[x] += 1

  print("Make HashMap: " + str(t.time() - a))
  a = t.time()

  sorted_lst = [None]*ELMS
  index = 0
  for i in range(0,ELMS*ELMS,ELMS):
    try: 
      sorted_lst[index] = hmap[i]

      index += 1
      loop = shift_lst[i]
      for k in range(loop):
        try:
          sorted_lst[index] = hmap[i+k]
          j = index
          #INSERTION SORT HERE
          while j > 0 and sorted_lst[j-1] > sorted_lst[j]:
            sorted_lst[j], sorted_lst[j-1] = sorted_lst[j-1], sorted_lst[j]
            j -= 1
          
          index += 1
        except Exception:
          loop = False
    
    except Exception:
      pass
  
  print("Sort List: " + str(t.time() - a))

  return sorted_lst


def sort_list_power3(lst):
  a = t.time()
  min, max = get_min_max(lst)
  print("Finding Min-Max: " + str(t.time() - a))
  a = t.time()

  hmap = {}
  for e in lst:
    x = int((e - min)/max * (ELMS-1))
    try:
      hmap[x].append(e)
      j = len(hmap[x]) - 1
      #INSERTION SORT HERE
      while j > 0 and hmap[x][j-1] > hmap[x][j]:
        hmap[x][j], hmap[x][j-1] = hmap[x][j-1], hmap[x][j]
        j -= 1
    except:
      hmap[x] = [e]
  print("Make HashMap: " + str(t.time() - a))

  res = []
  for i in range(ELMS):
    try:
      res += hmap[i]
    except:
      pass


  #Attempt 2: sorting hmap keys, going through buckets that way
  # key_lst = list(hmap.keys())
  # key_lst.sort()
  # for k in key_lst:
  #   #try:
  #   #print(hmap[k])
  #   res += hmap[k]
    #except:
      #pass
  print("Sort List: " + str(t.time() - a))
  return res

def sort_list_power4(lst):
  a = t.time()
  min, max = get_min_max(lst)
  print("Finding Min-Max: " + str(t.time() - a))
  a = t.time()

  buck_sizes = [0 for _ in range(ELMS)]

  for elm in lst:
    buck_sizes[int((elm - min)/max * (ELMS-1))] += 1
  
  # Convert bucket sizes into bucket start indices
  size = buck_sizes[0]
  buck_sizes[0] = 0
  for i in range(1, len(buck_sizes)):
    size_temp = buck_sizes[i]
    buck_sizes[i] = buck_sizes[i-1] + size
    size = size_temp
  
  # Create the new roughly sorted list
  res = lst[:]
  for elm in lst:
    x = int((elm - min)/max * (ELMS-1))
    res[buck_sizes[x]] = elm
    buck_sizes[x] += 1
  
  print('Sorting List: ' + str(t.time() - a))

  a = t.time()
  res = ins_sort(res)
  print('Insertion Sort: ' + str(t.time() - a))

  return res

def sort_list_power5(lst):
  a = t.time()
  min, max = get_min_max(lst)
  print("Finding Min-Max: " + str(t.time() - a))
  a = t.time()

  buck_sizes = [0] * ELMS

  for elm in lst:
    buck_sizes[int((elm - min)/max * (ELMS-1))] += 1
  
  # Convert bucket sizes into bucket start indices
  size = buck_sizes[0]
  buck_sizes[0] = 0

  for i in range(1, len(buck_sizes)):
    size_temp = buck_sizes[i]
    buck_sizes[i] = buck_sizes[i-1] + size
    size = size_temp
  
  print(lst)
  prev_idx = 0
  moved_list = [False]*ELMS
  for i in range(ELMS):
    if not moved_list[i]:
      moved_list[i] = True
      x = int((elm - min)/max * (ELMS-1))
      elm, lst[buck_sizes[x]] = lst[buck_sizes[x]], elm
      prev_idx = buck_sizes[x]
      buck_sizes[x] += 1
      
      while prev_idx != i:
        moved_list[prev_idx] = True
        x = int((elm - min)/max * (ELMS-1))
        prev_idx = buck_sizes[x]
        print(buck_sizes)
        elm, lst[buck_sizes[x]] = lst[buck_sizes[x]], elm
        
        buck_sizes[x] += 1
        
        #print(moved_list)

  return lst

    



# Memory conservative version of sorting system
def sort_list_lowmem(lst):
  lst = [6, 2, 0, 10, 1, 3, 0, 9, 3, 7]
  a = t.time()
  min, max = get_min_max(lst)
  print("Finding Min-Max: " + str(t.time() - a))
  a = t.time()

  open_spot = 0
  value = lst[0]
  loops = 0
  print(lst)

  def run_loop(value, open_spot):
    new_loc = int((value - min)/max * (ELMS-1))

    # If the next value maps to the empty spot, place value in empty spot
    # Then go to the next element after the open spot
    if new_loc == open_spot:
      print('Map to empty spot')
      lst[new_loc] = value
      value = lst[(new_loc + 1) % (ELMS - 1)] # Go to next value
      open_spot = (new_loc + 1) % (ELMS - 1)

    # If two values are mapping to the same spot
    elif int((lst[new_loc] - min)/max * (ELMS-1)) == new_loc :
      print('Map to same spot')
      #INSERTION SORT HERE
      while new_loc < ELMS - 1 and value >= lst[new_loc]:
        new_loc += 1
      
      lst[new_loc], value = value, lst[new_loc]
    
    # Perform the usual substitution
    else:
      print('Usual Iteration')
      lst[new_loc], value = value, lst[new_loc]
    # print(lst)
    # print('New loc: ' + str(new_loc), 'Value: ' + str(value), 'Open Spot: ' + str(open_spot))
    # print()

    return value, open_spot

  
  while(loops <= 5):
    loops += 1
    value, open_spot = run_loop(value, open_spot)
    
  print(lst)

  return lst
      # if new_loc + 1 == len(lst):
      #   lst.append(value)
      # value = lst[new_loc + 1]
    


    


  # loops = 0
  # prev_loc = 0
  # prev_val = lst[0]
  # term_steps = 0
  
  # while(loops <= 30):
  #   new_loc = int((prev_val - min)/max * (ELMS-1))
  #   new_val = lst[new_loc]
  #   lst[new_loc] = prev_val
  #   if prev_val == new_val or new_loc == prev_loc:
  #     prev_loc = (prev_loc + 1) % (ELMS - 1)
  #     prev_val = lst[prev_loc]
  #   else:
  #     prev_loc = new_loc
  #     prev_val = new_val

  #   loops += 1
  #   print(lst)
  # print(lst)


    








#################### TESTING DATASETS #######################################

def test_uniform():
  print("\n\nUniform:\n")
  lst = gen_list_uniform()
  lst1 = lst[:]
  lst2 = lst[:]
  lst3 = lst[:]
  now = t.time()
  lst1 = sort_list(lst1)
  my_time = t.time() - now

  now = t.time()
  lst2 = sort_list_power4(lst2)
  my_time_power = t.time() - now

  now = t.time()
  lst3.sort()
  py_time = t.time() - now

  print("Are my list and python list same? " + str(lst1 == lst3))
  print("Are power list and python list same? " + str(lst2 == lst3))
  print("My time: " + str(my_time))
  print("Power time: " + str(my_time_power))
  print("Python time: " + str(py_time))
  print('Ratio: ' + str(my_time / py_time))

def test_ints():
  print("\n\nIntegers:\n")
  lst = gen_list_ints()
  lst1 = lst[:]
  lst2 = lst[:]
  lst3 = lst[:]

  now = t.time()
  lst1 = sort_list(lst1)
  my_time = t.time() - now

  now = t.time()
  lst2 = sort_list_power4(lst2)
  my_time_power = t.time() - now

  now = t.time()
  lst3.sort()
  py_time = t.time() - now

  print("Are my list and python list same? " + str(lst1 == lst3))
  print("Are power list and python list same? " + str(lst2 == lst3))
  print("My time: " + str(my_time))
  print("Power time: " + str(my_time_power))
  print("Python time: " + str(py_time))
  print('Ratio: ' + str(my_time / py_time))

def test_skew():
  print("\nSkewed:\n")
  lst = gen_list_uniform()
  lst1 = lst[:]
  lst2 = lst[:]
  lst3 = lst[:]

  now = t.time()
  lst1 = sort_list(lst1)
  my_time = t.time() - now

  now = t.time()
  lst2 = sort_list_power4(lst2)
  my_time_power = t.time() - now

  now = t.time()
  lst3.sort()
  py_time = t.time() - now

  print("Are my list and python list same? " + str(lst1 == lst3))
  print("Are power list and python list same? " + str(lst2 == lst3))
  print("My time: " + str(my_time))
  print("Power time: " + str(my_time_power))
  print("Python time: " + str(py_time))
  print('Ratio: ' + str(my_time / py_time))







####################### MAIN RUNNER ###########################################

# lst = gen_list_uniform_ints()
# lst1 = lst[:]
# lst2  = lst[:]
# now = t.time()
# lst1 = sort_list_power4(lst)
# my_time = t.time() - now
# now = t.time()
# lst2.sort()
# py_time = t.time() - now

# print("Power time: " + str(my_time))
# print("Python time: " + str(py_time))
# print("Are my list and python list same? " + str(lst1 == lst2))

# now = t.time()
# lst2.sort()
# py_time = t.time() - now
# print(lst == lst2)

# #print(lst)
# #print(lst2)
# print("My time: " + str(my_time))
# print("Python time: " + str(py_time))
# print('Ratio: ' + str(my_time / py_time))


test_uniform()
test_ints()
test_skew()



