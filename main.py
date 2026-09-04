"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
    return ra + rb

def longest_run(mylist, key): #iterative version
    current = 0
    max = 0
    for num in mylist:
        if num == key:
            current += 1
        else:
            if current > max:
                max = current
            current = 0
        if current > max:
            max = current
    return max


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    if len(mylist) == 0:
        return Result(0, 0, 0, True)
    if len(mylist) == 1:
        if (mylist[0] == key):
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    middle = len(mylist) // 2 
    left_res = longest_run_recursive(mylist[:middle], key)
    right_res = longest_run_recursive(mylist[middle:], key)
    cross = left_res.right_size + right_res.left_size
    long = max(left_res.longest_size, right_res.longest_size, cross)
    if left_res.is_entire_range:
        left_res.left_size += right_res.left_size
    if right_res.is_entire_range:
        right_res.right_size += left_res.right_size
    entire = len(mylist) == long
    return Result(left_res.left_size, right_res.right_size, long, entire)