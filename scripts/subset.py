#!/usr/bin/env python3

# use a binary number (represented as string) as a mask
def mask(lst, m):
    # pad number to create a valid selection mask 
    # according to definition in the solution laid out 
    m = m.zfill(len(lst))
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m)))

def subset_sum(lst, target):
    # there are 2^n binary numbers with length of the original list
    for i in range(2**len(lst)):
        # create the pick corresponsing to current number
        pick = mask(lst, bin(i)[2:])
        if sum(pick) == target:
            yield pick


if __name__=="__main__":
    y = list(subset_sum([1,2,3,4,5], 7))
