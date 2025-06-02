import random
# The goal of this project is to develop a sorting algorithm using Machine Learning
# that finds the optimal combination of swaps to sort datasets as quick as possible
train_iters = 10


def main():
    print("Generating lists")
    lst, sorted_list = generateList(10)
    sorted_list = prep_lst(sorted_list)

    print("Training model...")
    model = train(lst, sorted_list)
    print("Training finished successfully")

    print("Begin sorting")
    #sorted_list = mysort(model, lst)
    print("Sorting completed")

    print("Adjusted list:")
    #print(sorted_list)

    
def generateList(size):
    res = []
    for i in range(0,size):
        res += [i]
    res_sorted = res[:]
    random.shuffle(res)
    return res, res_sorted

def train(lst, sorted_list):
    S = set()
    for i in range(train_iters):
        random.shuffle(lst)
        temp = lst[:]
        ops = get_ops(lst, sorted_list)
        hash_val = my_hash(temp)
        to_add = trainedList(hash_val, ops)
        print(to_add)
        S.add(to_add)
    return S

def mysort(model, lst):
    closest = find_matching_list(lst)
    for op in closest[1]:
        perform_swap(op,lst)
    return lst

def get_ops(lst, sorted_list):
    last_list = lst[:]
    swap_list = generate_swap_list(lst)
    lst, swaps = best_move(lst,sorted_list,swap_list)

    while (lst != last_list):
        last_list = lst
        lst, next_swap = best_move(lst,sorted_list,swap_list)
        swaps += next_swap
    return swaps

def loss_func(lst,sorted_list):
    loss = 0
    for i in range(len(lst)):
        loss += distance(i,lst,sorted_list)**2
    return loss

def distance(elm_idx, lst, sorted_list):
    if(str(lst[elm_idx]) in sorted_list):
        return abs(sorted_list[str(lst[elm_idx])] - elm_idx)
    return len(lst)

def prep_lst(lst):
    sorted_list = {}
    #generate_swap_list(lst)
    for i in range(len(lst)):
        sorted_list[str(lst[i])] = i
    return sorted_list

def best_move(lst,sorted_list,swap_list):
    iters = len(lst)*(len(lst)-1)/2
    best_list = lst[:]
    min_loss = loss_func(lst,sorted_list)
    swaps = []

    for i in range(iters):
        test_list = swap(swap_list,lst,i)
        loss = loss_func(test_list,sorted_list)

        if(loss < min_loss):
            best_list = test_list
            min_loss = loss
            swaps = [swap_list[i]]
    return best_list, swaps

def swap(swap_list,lst,i):
    test_list = lst[:]
    temp = test_list[swap_list[i][0]]
    test_list[swap_list[i][0]] = test_list[swap_list[i][1]]
    test_list[swap_list[i][1]] = temp
    return test_list

def generate_swap_list(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i):
            res += [[i,j]]
    return res

def my_hash(lst):
    primes = generate_prime(len(lst))
    res = 0
    for idx in range(len(primes)):
        res += lst[idx]*primes[idx]
    return res

def generate_prime(num_primes):
    num = 1
    primes = [2]
    j = 3
    while(num < num_primes):
        if(check_prime(j)):
            primes += [j]
            num += 1
        j += 2
    return primes

def check_prime(num):
    for i in range(3,num,2):
        if (num % i == 0): return False
    return True

class trainedList:
    hash_val = 0
    ops = []
    def __init__(self, hash_val, ops):
        self.hash_val = hash_val
        self.ops = ops
    def __str__(self):
        return str([self.hash_val, self.ops])

def find_matching_list(lst):
    pass

def perform_swap(lst):
    pass

#d = {}
#d['1'] = 0
#d['2'] = 1
#d['3'] = 2
#lst = [3,2,0]
#print(loss_func(lst,d))
main()