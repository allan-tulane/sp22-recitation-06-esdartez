import random, time
import tabulate


def select_random(a):
    return random.choice(a)

def select_first(a):
    return a[0]


def qsort(a, pivot_fn):
    if len(a) <= 1:
        return a
    else:
        p = pivot_fn(a)
        l = list(filter(lambda x: x < p, a))
        r = list(filter(lambda x: x > p, a))
        c = list(filter(lambda x: x==p, a))
        return qsort(l, pivot_fn) + c + qsort(r, pivot_fn)
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    quicksort_fixed_pivot = lambda a: qsort(a, select_first)
    quicksort_random_pivot = lambda a: qsort(a, select_random)
    tim_sort = sorted
    result = []
    for size in sizes:
        mylist = list(range(int(size)))
        random.shuffle(mylist)
        result.append([
            len(mylist),
            #time_search(selection_sort, mylist),
            time_search(quicksort_fixed_pivot, mylist),
            time_search(quicksort_random_pivot, mylist),
            time_search(tim_sort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
