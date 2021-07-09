'''
Author  :     Wong Jun Kang
Title   :     Assignment 1  
ID      :     29801036
'''


def stable_counting_sort(num_lst, base, digit):
    """
    This function takes in a number list and perform counting sort based on 
    the magnitude of the number at selected digit position.For example, if 
    digit is 0 (start from right at 0), [129, 456, 783] >> [78"3", 45"6", 12"9"], 
    because it is sorted based on the least significant bit at 0.
    
    @Arguments              :   num_lst, list containing a series of integer numbers.
                                base, int of base to be performed sorting on. 
                                digit, int that sorting will be based on.
                            
    @Precondition           :   Input must be a list of integer.
                                
    @Postcondition          :   Input list must not be altered after the execution of the function.
                                New list order based on digits will be generated.
                                
    @Time complexity        :   Best and Worst case O(n+b), where:
                                n is the size of num_lst.
                                b is the number of possible values (base).
                                
    @Space complexity       :   O(n+b), where:
                                n is the size of num_lst.
                                b is the number of possible values (base)
    
    @Auxiliary complexity   :   O(n+b), where:
                                n is the size of num_lst.
                                b is the number of possible values (base)
                                
    @return                 :   new_lst, a new list containing elements of the
                                input list arranged in ascending order based on
                                selected digit position.
                                maximum, the maximum number in num_lst.       
                    
    """
    # Initialisation
    num, length = 0, len(num_lst)
    position, count = [0] * base, [0] * base
    new_lst, pos_newlst = [None] * length , 0

    
    #Step 1 Generate count array
    #add count for each number encountered on selected digit position.
    for num in num_lst:
        num_at_digit = (num//base**digit) % base    # calculate number on the selected digit position.
        count[num_at_digit] += 1                    # add count for the number on digit
    
    
    #Step 2 Generate initial position array based on previous terms of count
    #array and position array.
    
    # As "0" pos is already initialised as 0. Begin from "1" pos to base.
    for j in range(1, base):
        position[j] = count[j-1] + position[j-1]    # current term is the sum of the previous terms of count and position array.   
    
    
    #Step 3 Generate new list
    #Group number according to num_at_digit, magnitude of number on digit position.
    for num in num_lst:
        num_at_digit = (num//base**digit) % base    # calculate number on the selected digit position.
        pos_newlst = position[num_at_digit]         # position in new list
        new_lst[pos_newlst] = num                   # store number at the position in new list.
        position[num_at_digit] += 1                 # add 1 to position[num] as a new number is added at the position.
        
        
    return new_lst



def maximum(int_lst):
    """
    This function takes in an integer list and return the maximum element in the list.
    @argument           int_lst, list of integer to find maximum on.
    @precondition       input list must be integer
    @postcondition      input list will not be modified
    @time complexity    Best and worst case O(n), where n is the size of the input list (int_lst).
    @space complexity   O(n), where n is the size of the input list (int_lst).
    @aux space          O(1), the algorithm takes constant amount of operation
                        at every iterations.
    @return             maximum, the maxumum number in int_lst.
    
    """
    maximum = 0
    for item in int_lst:
        if item > maximum:
            maximum = item
    return maximum



def radix_sort(num_list, b):
    """
    Function takes in num_list and performs radix sort and produce a new sorted list.
    @Precondition        :  elements of num_list must be of integer type.
    
    @Postcondition       :  A new sorted list will be generated.
                            
    @Arguments           :  num_list, list to be sorted.
                            b, base which list will be sorted on.
                            
    @Time complexity     :  Best case and Worst case, O((n+b)m), where:
                            n is the length of the list.
                            b is the base.
                            m is the number of digits in the largest number in
                            the input list, when represented in base b.
    @Space complexity    :  O(nm), because input is O(nm) where:
                            n is the size of num_list.
                            m is the number of digits in the largest number in
                            the input list, when represented in base b.
    @Aux space complexity:  O(n), where
                            n is the size of num_list.
    @Return              :  lst, a new list containing elements in num_list 
                            arranged in ascending order.
    """
    max_number = maximum(num_list)    # Get the maximum number in num_list.
    i, lst = 0, num_list              # initialise i and num_list into lst
    
    # Loop based on number of digits for specific base.
    while max_number > 0:
        lst = stable_counting_sort(lst, b, i)      # perform counting sort based on digit i,    
        i += 1                                     # increment to perform counting sort on more significant digits.
        max_number //= b                           # Reduce by 1 digit/ base each time.
    return lst



# ANALYSIS

def time_radix_sort():
    """
    Function that time radix radix sort and return a tuple that contains the 
    res of time taken for each bases to perform radix sort on 10000 random
    numbers.
    @argument       None
    @precondition   None
    @postcondition  None
    @return         output, tuple that contains the time taken for each bases 
                    to perform radix sort on a 10000 random numbers.
    
    @Time complexity:       Best case and Worst case, O(1), constant amount of operation at each iteration.
    @Space complexity    :  O(1),constant amount of operation at each iteration.
    @Aux space complexity:  O(1),constant amount of operation at each iteration.
                            n is the length of the list.
    Return:                 output, a list of tuples with base and time used
                            to sort the list.
    """
    # Import library
    import random
    import time

    # Generate test data
    random.seed(100)
    test_data = [random.randint(1,(2**64)-1) for _ in range(100000)]
    # Selected bases
    base_list = [2, 3, 10, 2**16, 2**20, 3123141, 6291461, 2**23, 12582917, 2**24]
    output = []
    
    for base in base_list:
        # time the function only for the sorting itself
        # start timer
        start = time.perf_counter()
        # perform radix_sort
        radix_sort(test_data, base)
        # end timer
        end = time.perf_counter()
        output.append((base ,end-start))
    return output




def plot_graph():
    """
    This function plot a graph based on the generated output of time_radix_sort()
    function.
    @argument           None
    @precondition       None
    @postcondition      None  
    @return             None
    @time complexity    Best and Worst case: O(1), as the number of bases to be tested is in constant amount
                        in time_radix_sort.
    @aux time           O(1)
    """
    # Import Library
    import matplotlib.pyplot as plt
    import numpy
    
    lst_of_tuple = time_radix_sort()
    x, y = [], []
    
    for item in lst_of_tuple:
        x.append(item[0])
        y.append(item[1])
    
    # Scatter plot
    plt.scatter(x,y)
    
    # Plotting best fit line
    mymodel = numpy.poly1d(numpy.polyfit(x, y, 2))
    myline = numpy.linspace(0, 2**24, 15)
    plt.plot(myline, mymodel(myline))
    
    # labelling
    plt.xlabel('Base')
    plt.ylabel('Time/ Second')
    plt.title('Time vs Base')
    plt.show()
    print('Done')
    


def rotation(lst, p):
    """
    This function rotate the string in the list by p character, and output a rotated list.
    @argument   :   lst, list to be rotated
                    p, number of character to be rotated, (-) indicate rotation 
                    to the right, otherwise to the left.
    @precondition:  lst must only contain string type elements.
    @time complexity :  Best and worst case,  O(n), where n is the length
                        
    @space complexity:  Best and worst case, O(n), where n is the sum of all of the string lengths
                        
                        Worst case can also be described as O(nm), where:
                        n is the number of strings.
                        m is the length of the strings. (all same length)
        
                        Or worst case can be described as O(nm), where:
                        n is the number of string.
                        m is the length of the strings. (all same length)
                        
    @aux space complexity : O(nm), where:
                            n is the size of/ space taken by the list.
                            m is the length of the longest string.
                            
    @return     :   rotated_list, A list that is rotated based on p.
                    maximum, the maximum length of string in lst
    
    """
    rotated_lst = []
    maximum = 0
    
    for item in lst:
        # Slice through the list and separate them into prefix and suffix.
        prefix, suffix = item[p % len(item):], item[:p % len(item)]
        rotated_lst.append(prefix + suffix)
        
        # Calculate maximum length of string in the list.
        if len(item) > maximum:
            maximum = len(item)
    
    return rotated_lst, maximum

    
        

    
def stable_counting_sort_string(string_list, to_sort, start):
    """
    This method modifies the input list into a list sorted based on "to_sort", 
    beginning from "start".
    
    @argument           :   string_list, list containing only string  to be sorted.
                            to_sort, the "column" to be sorted
                            start, indicating item from 0 to start are sorted.  
    @precondition       :   string list must only contain string type element.
                            string list must only contain a-z(lowercase).
    @postcondition      :   input list will be modified.
    
    @time complexity    :   Best and worst case, O(n) where:
                            n is the length of the list. 
                            
    @space complexity   :   O(n), where n is the space taken by the string list.
        
    @aux space complexity:  O(n), where n is the size of the input list caused by "unsorted_lst".
                            
    @return             :   lst, sorted list based on to_sort.
                            j, the starting point that indicate o to j are sorted.
    """
    base = 26
    lst, j = string_list, start
    count_array = [0] * (base+1)    # 1 extra space allocated for 0 to create rank list.    
    unsorted_lst = []
    
    for i in range(start, len(lst)):
        item = lst[i]
        # Item with length smaller than the column number, put item into lst
        # Then increase the starting point by 1. 
        if len(item)-1 < to_sort:
            lst[j] = item
            j += 1
        else:
    
    # increase the counter in counter list based on the number of occurence of each item.
            unsorted_lst.append(item)
            character = item[to_sort]
     # -96 instead of -97, as 1 extra space is allocated for 0 in rank array.
            index = ord(character) - 96
            count_array[index] += 1
    
    # create rank array with count_array (Reuse count array)
    for i in range(1, base):
        count_array[i] = count_array[i] + count_array[i-1]

    # sort string based on "character" and store it into "lst".
    for item in unsorted_lst:
        character = item[to_sort]
        index = ord(character) - 97
    
    # add j, because lst[0] to lst[j] has already been occupied.
        to_place = count_array[index] + j
        lst[to_place] = item
        count_array[index] += 1
    
    # Return both lst, and j (indicated sorted)
    return lst, j



def find_rotations(string_list, p):
    """
    This function compare the element from the string list and the rotated_list.
    Then return the matching/ duplicate element in a list.
    @argument       :   string_list, the string list to be rotated and compared
                        p, the number of rotation.
    @precondition   :   string_list must contain only string type element.
                        string_list must not contain duplicate element.
    @postcondition  :   A list of all string in string_list whose p-rotations also exist in string_list
                        is returned
    @complexity     :   Best and worst case, O(n), where n is the sum of all of the string lengths
    
                        Worst case can also be described as O(nm), where:
                        n is the length of the string_list
                        m is the length of the strings. (all same length)
                                              
    @space          :   O(nm), where:
                        n is the length of the string_list
                        m is the length of the longest string.
                         
    @auxiliary      :   O(n), where n is the length of the list
    @return         :   res, matching element from string list and rotated list.
    """
    
    # -p because rotating the 2nd list to left means rotate the 1st list to right.
    # By doing so, we can get the duplicate element in term of original list.
    rotated_list, maximum = rotation(string_list, -p)
    # create a new list based on string list and rotated_list
    
    new_lst = string_list + rotated_list 
    res, start = [], 0
    
    # Perform radix sort with counting sort.
    # Perform operation from 0 to the end.
    # NOTE: item not sorted in ascending order but duplicate element will be grouped together.
    # Sorting start from "start" as lst is already sorted from index "0 to start"
    for i in range(maximum):
        new_lst , start= stable_counting_sort_string(new_lst, i, start)
   
            
    # Loop through the list and check if previous match with current.
    for i in range(1, len(new_lst)):
        previous, current = new_lst[i-1], new_lst[i]
        if current == previous:
            res.append(current)
    
    return res




if __name__ == "__main__": 
    # driver for the test cases
    print("Running test")
    def test_q1():
        # Testing
        lst = [18446744073709551615, 18446744073709551614, 1, 
               11111111111111111111, 2111111111111111111, 311111111111111111]
        
        
        
        # Test sorting
        actual_res01 = radix_sort(lst, 10)
        expected_output01 = [1, 311111111111111111, 2111111111111111111, 
                           11111111111111111111, 18446744073709551614,
                           18446744073709551615]
        
        actual_res02 = radix_sort([1231252156,1231,116236], 4)
        expected_output02 = [1231, 116236, 1231252156]
        
        # Test radix_sort do not modify input list
        lst2 = [18446744073709551615, 18446744073709551614, 1, 
               11111111111111111111, 2111111111111111111, 311111111111111111]
        import random
        
        random.seed('hey we have a gift for u')
        test_data = [random.randint(1,(2**64)-1) for _ in range(100000)]
        sorted_1 = sorted(test_data)
        sorted_2 = radix_sort(test_data, 10)
        

        # Test of empty array, empy array must not return error
        try:
            actual_res03 = radix_sort([], 10)
            expected_output03 = []
        except:
            print('Empty array test failed')
            return
        
        lst4 = []
        expected_output04 = []
        

        if actual_res01 != expected_output01:
            print("failed test1")
        elif actual_res02 != expected_output02:
            print('failed test2')
        elif lst != lst2:
            print('failed test3')
        elif actual_res03 != expected_output03:
            print('failed test4')
        elif sorted_1 != sorted_2:
            print('failed test5')
        elif lst4 != expected_output04:
            print('failed test')
        else:
            print("pass test")
        
        
        
    def test_q2():
        # Not tested as the the output is already generated in pdf.
        time_radix_sort
        plot_graph()
        return
        
        
        
    def test_q3():
        test_lst1 = ["aaa","abc","cab","acb","wxyz","yzwx"]
        test_lst2 = ["abc", "acdds", "bac", "bbb"]
        # Test for positive p
        # Test01
        actual_res01 = find_rotations(test_lst1, 1)
        expected_res01 = ['aaa', 'cab']
        
        # Test02
        actual_res02 = find_rotations(test_lst1, 2)
        expected_res02 = ['aaa', 'abc', 'yzwx', 'wxyz']
        
        # Test for negative p
        # Test03
        actual_res03 = find_rotations(test_lst1, -1)
        expected_res03 = ['aaa', 'abc']
        
        # Test04
        actual_res04 = find_rotations(test_lst1, -2)
        expected_res04 = ['aaa', 'cab', 'yzwx', 'wxyz']
        
        # Test for overbound value (P > length of longest string)
        # Test05
        actual_res05 = find_rotations(test_lst1, 5)
        expected_res05 = ['aaa', 'abc']
        
        # Test06
        actual_res06 = find_rotations(test_lst1, 6)
        expected_res06 = ['aaa', 'cab', 'acb', 'abc', 'yzwx', 'wxyz']
        
        # Test for negative overbound value (-P < -length of longest string)
        # Test07
        actual_res07 = find_rotations(test_lst1, -5)
        expected_res07 = ['aaa', 'cab']
        
        # Test08
        actual_res08 = find_rotations(test_lst1, -6)
        expected_res08 = ['aaa', 'cab', 'acb', 'abc', 'yzwx', 'wxyz']
        
        # Empty lists should be considered as valid input and should not return error message.
        # Test09
        actual_res09 = []
        expected_res09 = []
        
        # Test of empty String
        actual_res10 = find_rotations(test_lst2, 1)
        expected_res10 = ['bbb']
        
        
        def check_task_find_rotations():
            initial = ["aaa", "abc", "cab", "acb", "wxyz", "yzwx"]
            match_list = [["aaa", "cab"],
                          ["aaa", "abc", "yzwx", "wxyz"],
                          ["aaa", "abc", "cab", "acb", ],
                          ["aaa", "cab", "yzwx", "wxyz"],
                          ["aaa", "abc"],
                          ["aaa", "abc", "cab", "acb", "wxyz", "yzwx"],
                          ["aaa", "cab"],
                          ["aaa", "abc", "yzwx", "wxyz"],
                          ["aaa", "abc", "cab", "acb"],
                          ["aaa", "cab", "yzwx", "wxyz"],
                          ["aaa", "abc"]]
            p_list = [integer for integer in range(-5, 6)]
            success_fail_rate = [0, 0]
            
            for p in p_list:
                match_index = p + 5
                duplicate_list = find_rotations(initial, p)
                duplicate_list.sort()
                match_list[match_index].sort()
                if duplicate_list == match_list[match_index]:
                    success_fail_rate[0] += 1
                else:
                    success_fail_rate[1] += 1
                    print("There was a failure case for p =", p)
                    print("Duplicate list: ", duplicate_list)
                    print("Expected list: ", match_list[match_index])
                print("Task 3 Result for p = -5 to p = 5:", success_fail_rate)
        
        #check_task_find_rotations()

                
        actual = [actual_res01, actual_res02, actual_res03, actual_res04,
                  actual_res05, actual_res06, actual_res07, actual_res08,
                  actual_res09, actual_res10]
        
        expected = [expected_res01, expected_res02, expected_res03,
                    expected_res04, expected_res05, expected_res06,
                    expected_res07, expected_res08, expected_res09,
                    expected_res10]
        
        flag = True
        for i in range(len(actual)):
            # If any actual result does not match with the expected result
            if actual[i] != expected[i]:
                # print failed cases
                # set flag to false
                print("test_q3, Test", i+1, "failed.")
                flag = False
        

        # Return the result of test
        if flag == True:
            print("pass test")
        else:
            print("failed test")
            
            
    # run test Q1
    test_q1()
    # test_q2()
    test_q3()
    print("pass all")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    