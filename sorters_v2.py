from collections import defaultdict
import heapq
import time

def insertion_sort(arr, left, right):
    """
    Basic Insertion Sort Implementation
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    """
    Perform merging operation as done in merge sort
    """
    # Create temporary arrays
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i, j, k = 0, 0, left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def tim_sort(arr):
    """
    Pure Python implementation of Tim Sort (for benchmarking)
    """
    min_run = 32
    n = len(arr)

    # Step 1: Sort small chunks with insertion sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge runs in a bottom-up manner
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:  # If there's something to merge
                merge(arr, left, mid, right)
        size *= 2
    
    return arr


def avisort(lst):
  """
  My custom sorting algorithm
  """
  mx = max(lst)
  mn = min(lst)
  elms = len(lst)

  new_idx_map = {}
  for n in lst:
    k = int(((n - mn) / mx) * elms)
    if k in new_idx_map:
      new_idx_map[k].append(n)
    else:
      new_idx_map[k] = [n]
  
  result = []
  for v in range(elms + 1):
    if v in new_idx_map:
      result.extend(sorted(new_idx_map[v]))

  return result


# CUSTOM AVISORT ALGORITHM
def avisort2(lst):
  """
  Version 2 of my custom sorting algorithm (unfinished due to bug)
  """
  mx = max(lst)
  mn = min(lst)
  elms = len(lst)

  shift = [(0, 0) for _ in range(elms)]
  result = [None for _ in range(elms)]
  for n in lst:
    k = int(((n - mn) / mx) * elms)
    l, r = shift[k]
  
  result = []
  for v in range(elms + 1):
    if v in new_idx_map:
      result.extend(sorted(new_idx_map[v]))

  return result


def avisort3(lst, alpha = 0.001):
    """
    Version 3 of my custom sorting algorithm
    """
    mx = max(lst)
    mn = min(lst)
    elms = len(lst)

    buckets = defaultdict(list)
    for n in lst:
       k = int(((n - mn) / mx) * alpha * elms)
       buckets[k].append(n)

    result = []
    for v in range(elms + 1):
        if v in buckets:
            result.extend(sorted(buckets[v]))
    
    return result
   

def avisort4(lst, alpha = 0.001):
    """
    Version 4 of my custom sorting algorithm (current fastest)
    """
    mx = max(lst)
    mn = min(lst)
    elms = len(lst)

    buckets = defaultdict(list)
    tmp_val = alpha * elms / mx
    for n in lst:
       k = int((n - mn) * tmp_val)
       buckets[k].append(n)

    result = []
    for v in range(elms + 1):
        if v in buckets:
            result.extend(sorted(buckets[v]))
    
    return result


def hashing_bucket_sort(arr, num_buckets=10):
    """
    ChatGPT generated hashed bucket sort for benchmarking
    """
    # Step 1: Create buckets
    buckets = defaultdict(list)
    for value in arr:
        # Use a hash function to assign to buckets
        bucket_idx = hash(value) % num_buckets
        buckets[bucket_idx].append(value)

    # Step 2: Sort each bucket
    sorted_buckets = []
    for bucket_idx in sorted(buckets.keys()):
        sorted_buckets.append(sorted(buckets[bucket_idx]))  # Using Python's built-in sort

    # Step 3: Merge each bucket
    result = merge_sorted_buckets(sorted_buckets)
    return result

def merge_sorted_buckets(sorted_buckets):
    """
    ChatGPT generated merging fucntion for hashed bucket sort
    """
    # Use a priority queue (heap) to efficiently merge multiple sorted lists
    heap = []
    for i, bucket in enumerate(sorted_buckets):
        if bucket:  # Check if the bucket is non-empty
            # Push the first element of each bucket into the heap
            heapq.heappush(heap, (bucket[0], i, 0))  # (value, bucket index, element index)

    result = []
    while heap:
        value, bucket_idx, elem_idx = heapq.heappop(heap)
        result.append(value)
        # If there's another element in the same bucket, push it to the heap
        if elem_idx + 1 < len(sorted_buckets[bucket_idx]):
            next_value = sorted_buckets[bucket_idx][elem_idx + 1]
            heapq.heappush(heap, (next_value, bucket_idx, elem_idx + 1))

    return result