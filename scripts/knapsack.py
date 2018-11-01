#!/usr/bin/env python3

#from progress.bar import Bar
import numpy as np

def solve(weight, benefit, W):
    n = len(benefit)
    B = [[0]*(W+1)for i in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            bi = benefit[i-1]
            wi = weight[i-1]
            dw = w - wi

            if (wi <= w):
                if (bi+B[i-1][dw] > B[i-1][w]):
                    B[i][w] = bi + B[i-1][dw]
                else:
                    B[i][w] = B[i-1][w]
            
            if (wi > w):
                B[i][w] = B[i-1][w]

    return B


def capacity(B):
    n = len(B)-1
    K = len(B[0])-1
    return B[n][K]

def indices(B,w):
    n = len(B)
    k = len(B[0])-1
    idx = []

#    print(B)
    iteration = 0
    for i in range(n-1,0,-1):
        if (B[i][k] != B[i-1][k]):
#            print("iteration {}: n={}, k={}".format(iteration,i,k))
            k = k - w[i]+1
            idx.append(i)
            iteration += 1

    return idx[::-1]


if __name__=="__main__":
    weight = [2,3,4]
    benefit = [3,4,5]
    W = 5

    # results
    B = solve(weight, benefit, W)
    print("length B = {}".format(len(B)))
    print("length W = {}".format(len(B[0])))
    Max = capacity(B)
    idx = indices(B,weight)
    print("The benefit constrained by Wmax={}, Benefit={}".format(W, Max))
    print("")
    print("The solution consists of:")
    for i in range(len(idx)):
        for j in range(len(weight)):
            if (j-1) == (idx[i]-1):
                print("cell[{}]: weight={}, benefit={}".format(j-1, weight[idx[i]-1], benefit[idx[i]-1]))
