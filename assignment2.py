# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:37:19 2020

@author: Wong Jun Kang
@studentID: 29801036
@title: FIT2004 Assignment 2.
"""

# Question 1

def longest_oscillation(L):
    
    """
    This function takes in list L and return a tuple containing a number indicating the 
    longest possible oscillation of list L and a list of possible combination of indices that
    build up the longest oscillation. (Implementation: greedy approach).
    This function is implemented optimally.
    
    @argument             : L, Integer list to find the longest oscillation
                            list L can contain duplicates or empty
    @precondition         : List L must only contain Integer
                            duplicates and empty list can be accpted
    @postcondition        : List L will not be modified.
    @time complexity      : Best case O(1), where the input list is empty
                            Worst case O(n), where n is the size of list L
    @space complexity     : O(n), where n is the size of list L
    @aux space complexity : O(n), where n is the size of list L
    @return               : A tuple containing 2 elements 'count' and 'res'
                            count, the sum of longest oscillation
                            res, a possible combination of indexes that 
                            build up the longest oscillation
    """
    if L == None:
        return 0, []
    if len(L) == 0:
        return 0, []
    elif len(L) == 1:
        return 1, [0]
    else:
        res = [0]
        temp = L[0]
        count = 1      # count = 1, because 1st element will always be included.
        k = 1
        # skip duplicate elements at the start
        while L[k-1] == L[k] and k < len(L)-1:
            k += 1
        # direct True indicates upward, direct False indicate downwards.
        direct = L[0] < L[k]
        j = 1
        # start from k, (skipped all duplicate elements)
        for i in range(k, len(L)):
            # if current temp not equal to current element. (duplicate element)
            if L[i] != temp:
                # if current element and temp do not match "direct" upward expected but downward detected or vice versa. 
                if (L[i] > temp and direct == False) or (L[i] < temp and direct == True):
                    res[j-1] = i
               
                # if((L[i] > temp) and direct == True) or (L[i] < temp and direct == False)
                else:
                    direct = not direct             # reverse current direction                   
                    count += 1                      # add new item, hence increment count by 1
                    res.append(i)                   # append current index
                    j += 1
                # replace temp with current if L[i] != temp (not duplicated) 
                temp = L[i]
                
    return count, res


# Question 2

def valid_moves(r, c, matrix):
    """
    This function takes in a position and return the indexes of the adjacent
    elements that are smaller than itself.
    
    @argument             : r, row of matrix, for the valid moves to be calculated
                            c, column of matrix, for the valid moves to be calculated
                            matrix, a matrix of m x n dimension which contain random numbers of integer.            
    @precondition         : index r,c provided must be a valid index for matrix.
                            r and c must only contain integer.
                            matrix must not be empty
    @postcondition        : a list of indices which the element must be smaller than current and
                            are adjacent to current (matrix[r][c])
    @time complexity      : O(1), only a maximum of 8 directions will be looped through
                            hence, the best and worst case time complexity would be a constant 8 or less.
    @space complexity     : O(nm), where:
                            n is the number of rows of matrix M (length of outer matrix)
                            m is the number of columns of matrix M (length of inner matrix)
    @aux space complexity : O(1), always perform a constant (8 times) amount of operations or less,
                            and will always return a list of length 8 or less.
    @return               : possible, a list containing all possible moves that are larger than
                            the element at matrix[r][c] and are adjacent to matrix[r][c]
    """
    width, height = len(matrix[0]) - 1 , len(matrix) - 1
    current = matrix[r][c]
    # all possible directions
    dr = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    possible = []
    # iterate through all adjacent element of current (memo[r][c]).
    for y, x in dr:
        if (r + y >= 0 and r + y<= height)and(c + x >= 0 and c + x <= width):
            temp = matrix[r+y][c+x]
            # append only the element that are smaller than current (reduce space complexity)
            if temp < current:
                possible.append((r+y,c+x))
    return possible

 
def sub_longest_walk(r, c, memo, M):
    """
    This function calculate the longest decreasing walk of matrix M at position
    (r,c) and return the sub optimal solution of position (r,c) into memo[r][c].
    
    @argument             : r, row of matrix M, for the sub_longest_walk to be calculated
                            c, column of matrix M, for the sub_longest_walk to be calculated
                            memo, a matrix of dimension m x n (same dimension as matrix M)
                            to store the sub-optimal solutions.
                            M, a matrix of m x n dimension which contain random numbers of integer.            
    @precondition         : matrix M must only contain integer type elements.
                            matrix memo and M must have same dimension.
                            r and c must only contain integer.
                            M must not be empty
    @postcondition        : the longest walk of matrix[r][c] will be returned at memo[r][c]
    @time complexity      : Best case O(1), 
                            where index is out of bound
                            Worst case O(nm), where:
                            n is the number of rows of matrix M (length of outer matrix)
                            m is the number of columns of matrix M (length of inner matrix)
    @space complexity     : O(nm), where:
                            n is the number of rows of matrix M (length of outer matrix)
                            m is the number of columns of matrix M (length of inner matrix)
    @aux space complexity : O(nm), where:
                            n is the number of rows of matrix M (length of outer matrix)
                            m is the number of columns of matrix M (length of inner matrix)
    @return               : memo[r][c], the optimal solution of longest walk for M[r][c]
    """
    # if out of bound, return 0 as the longest increasing walk
    if(r < 0 or r > len(memo)-1 or c < 0 or c > len(memo[0])-1):
        return 0
    # perform recursion only if memo[r][c] is not None.
    if memo[r][c] == None:
        next_moves = valid_moves(r, c, M)
        max_sub_walk = 1
        # iterate through all possible moves generated by valid_moves function
        for move in next_moves:
            rol, col = move[0], move[1]
            max_sub_walk = max(max_sub_walk, sub_longest_walk(rol, col, memo, M) + 1)
        # longest decreasing walk is returned instead of longest increasing walk for the sub optimal solution,
        # is to ensure, both backtracking of result in the longest_walk and sub_longest_walk can use a same 
        # valid_move function conveniently.
        memo[r][c] = max_sub_walk
            
    return memo[r][c]


def longest_walk(M):
    """
    This function takes in a m x n matrix and calculate the longest increasing 
    walk that can be formed from matrix M and return the count of the longest
    walk and a list of tuple of indices indicating one of the possible walk.
    This function is implemented optimally.
    
    @argument             : M, a matrix of m x n dimension which contain random numbers of integer.
    @precondition         : matrix M must only contain integer type elements.
                            M must be matrix not list, i.e. matrix M must be 2 dimensional e.g. [[1, 2, 3]] not [1,2,3]
    @postcondition        : the longest walk and a tuple containing one of the longest walk will be returned
    @time complexity      : Best case, O(1), where:
                            matrix M is an empty list
                            Worst case, O(nm) where:
                            n is the number of rows of matrix M (length of outer matrix)
                            m is the number of columns of matrix M (length of inner matrix)
    @space complexity     : O(nm), where:
                            n is the number of rows of matrix M (length of outer matrix)
                            m is the number of columns of matrix M (length of inner matrix)
    @aux space complexity : O(nm), where:
                            n is the number of rows of matrix M (length of outer matrix)
                            m is the number of columns of matrix M (length of inner matrix)
    @return               : a tuple containing 2 elements, maximum and res.
                            maximum, the longest increasing walk in matrix M
                            res, a list of indices of one of the longest walk in matrix M
    """
    # Dealing with None
    if M == None:
        return 0, []
    # Dealling with empty list
    if len(M) == 0:
        return 0, []
    # Dealling with empty matrix
    if len(M[0]) == 0:
        return 0, []
    
    row, col = len(M), len(M[0])
    memo = [col * [None] for i in range(row)]
    maximum, val, index  = 0, 0, None
    for i in range(row):
        for j in range(col):
        # calculate sub_longest walk for n x m number of times where n is the number of rows and m is the number of columns.
           val = sub_longest_walk(i, j, memo, M)
           # locate index of maximum/ longest path for backtracking purposes
           if val > maximum:
               maximum, index = val, (i, j)
    
    # backtrack to find one of the possible solution.
    res = [None] * maximum
    r, c = index
    res[-1] = index
    # iterate from largest to smallest
    for k in range(maximum-1, -1, -1):
        possible_moves = valid_moves(r, c, memo)
        for move in possible_moves:
            if memo[move[0]][move[1]] == k:
                # allocate results from the end to start, as the solutions recorded in the 
                # memo are the sub optimals for longest decreasing walk, hence, a reverse is necessary.
                res[k-1] = move
                r, c = move
        
    return maximum, res