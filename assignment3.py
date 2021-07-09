# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:33:28 2020

@author: Wong Jun Kang
@StudentID: 29801036
"""
class Node:
    """
    The Node class for the trie. 
    """
    def __init__(self, size=26):
        """
        The constructor of Node class.
        @arguments              :   size, the size of the link list.
                                    size=26 by default
                                    
        @precondition           :   size must be greater than 0
        
        @postcondition          :   A node containng a link list of specified
                                    size will be created. (26 by default)
                                    
        @time compleity         :   Best and worst case O(1)
        
        @space complexity       :   O(S), where S is the size of the link list
        
        @aux-space complexity   :   O(1)
        """
        # 26 alphabets
        self.link = [None] * size
        self.count = 0
        self.child_count = 0
        self.terminal = False
        self.value = None
    
  
class Trie:
    """
    Class that allow user to construct A Trie Data Structure containing keys
    of type string that are within a-z (non-capital letters).
    """
    def __init__(self, text):
        """
        The constructor of Trie class.
        
        @arguments              :   text,a list of Strings containing non-capital
                                    letters from a-z.
                                    
        @precondition           :   text, must only contain String characters
                                    within a-z(non-capital letters).
                                    
        @postcondition          :   A Trie containing all the elements in text
                                    will be constructed.
                                    
        @time compleity         :   Best and worst case O(T), where:
                                    T is the total character over all strings
                                    in the list.
                                    
        @space complexity       :   O(T), where:
                                    T is the total character over all strings
                                    in the list.
                                    
        @aux-space complexity   :   O(1)
        """
        self.root = Node()
        # insert all elements in the text into the trie
        for item in text:
            # add item at the terminal
            self[item] = item 
            
    
    def __setitem__(self, key, value):
        """
        Gven a key and a value, this function will set the value at the terminal
        of the key. If the path doesnt yet exist, create the nodes(paths).
        
        @arguments              :   key, a key to add value at.
                                    value, the value to be added
                                    
        @precondition           :   key, must only contain characters
                                    within a-z(non-capital letters).
                                    
        @postcondition          :   The specified value will be added at the 
                                    terminal of the key, if it already exists 
                                    (duplicate),self.count will be incremented.
                                    
        @time compleity         :   Best and worst case O(n), where:
                                    n is the length of the key
                                    
        @space complexity       :   O(n), where:
                                    n is the length of the key
                                    
        @aux-space complexity   :   O(1)
        """
        # start from root
        current = self.root
        current.child_count += 1
        # loop through each characters in the key
        for char in key:
            # "a" starts at 0
            index = ord(char) - 97
            # if node doesn't exists at link[index] (path not exists)
            if current.link[index] is None:
                current.link[index] = Node()
                
            current = current.link[index]
            current.child_count+= 1
            
        current.terminal = True
        current.value = value # add value at terminal
        current.count +=1
    

    def __contains__(self, key):
        """
        Given a key, this function will check whether the key exists in the Trie.
        Returning True, if the key exists in the Trie, otherwise False.
        
        @arguments              :   key, a key to be checked.
        
        @precondition           :   key, must only contain characters
                                    within a-z(non-capital letters).
                                    
        @postcondition          :   If the key exists, True will be returned
                                    else, False.
                                    
        @time compleity         :   Best and worst case O(n), where:
                                    n is the length of the key
                                    
        @space complexity       :   O(n), where:
                                    n is the length of the key
                                    
        @aux-space complexity   :   O(1)
        
        @return                 :   True, if the key exists, otherwise False.
        """
        # start from root
        current = self.root
        # loop through each characters in the key
        for char in key:
            # terminal "$" starts at 0 and "a" starts at 1
            index = ord(char) - 97
            # if node doesn't exists at link[index] (path not exists)
            if current.link[index] is None:
                return False

            current = current.link[index]   
        return current.terminal
        

    def string_freq(self, query_str):
        """
        Given a String,  string_freq returns an integer, which is the number of 
        elements of the text which are exactly query_string.
        
        @arguments              :   query_str, a string to be checked for 
                                    occurences
                                    
        @precondition           :   query_str, must only contain characters
                                    within a-z(non-capital letters).
                                    
        @postcondition          :   An integer will be returned based on the number
                                    of occurences of query_str in the Trie/text.
                                    
        @time compleity         :   Best and worst case O(q), where:
                                    q is the length of the query_str
        @space complexity       :   O(q), where:
                                    q is the length of the query_str
                                    
        @aux-space complexity   :   O(1)
        
        @return                 :   current.count, the number of occurences of 
                                    query_str in the Trie
        """
        # start from root
        current = self.root
        # loop through each characters in query_str
        for char in query_str:
            # "a" starts at 0
            index = ord(char) - 97
            # if node doesn't exists at link[index] (path not exists)
            if current.link[index] is None:
                return 0
            current = current.link[index]
        
        return current.count
    
    
    def prefix_freq(self, query_str):
        """
        Given a String,  prefix_freq returns an integer, which is the number of 
        words in the text that have the string as a prefix.
        
        @arguments              :   query_str, a string to be checked for 
                                    the number of words in the text that have
                                    the string as a prefix
                                    
        @precondition           :   query_str, must only contain characters
                                    within a-z(non-capital letters).
                                    
        @postcondition          :   An integer will be returned based on the 
                                    number of words in the text that have the
                                    string as a prefix
                                    
        @time compleity         :   Best and worst case O(q), where:
                                    q is the length of the query_str
                                    
        @space complexity       :   O(q), where:
                                    q is the length of the query_str
                                    
        @aux-space complexity   :   O(1)
        @return                 :   current.child_count, the number of words in
                                    the text that have the string as a prefix.
        """
        # start from root
        current = self.root
            
        # loop through each characters in query_str
        for char in query_str:
            # "a" starts at 0
            index = ord(char) - 97
            # if node doesn't exists at link[index] (path not exists)
            if current.link[index] is None:
                return 0
            current = current.link[index]  
            # If it's not terminal, child_count will be 0, since count is only 
            # incremented at terminal.
        return current.child_count 
    
    

    def traverse(self, start_node, rtn):
        """
        Given a starting node, the function will traverse and append all the 
        value at the terminal of its children node(All terminated string, under
        the branches of start node) at rtn. 
        
        @arguments              :   start_node, the node to start the traverse from
        
        @precondition           :   start_node, must be a Node type object.
        
        @postcondition          :   rtn will be append with a new associated 
                                    String for each terminal node encountered.
                                    
        @time complexity         :  Best and worst case O(k), where:
                                    k is the total amount of nodes under 
                                    the start_node.
                                    
        @space complexity       :   O(w), where w is output sensitive.
                                    w is the total amount of terminated string
                                    appended by traverse into rtn.
                                    
        @aux-space complexity   :   O(m), where m is deepest node, from start_node
                                    caused by recursion depth.
                                    
        @return                 :   self.traverse_aux(start_node, rtn).
        """
        return self.traverse_aux(start_node, rtn)
                    
    def traverse_aux(self, cur_node, rtn):
        """
        The auxlilary function of traverse.
        The functions traverse through the Trie from the cur_node and appends a
        the associated value/string value for each terminated string into rtn.
        
        @arguments              :   cur_node, the node to traverse from
        
        @precondition           :   cur_node, must be a Node type object.
        
        @postcondition          :   rtn will be append with a new associated 
                                    String for each terminal node encountered.
                                    
        @time complexity         :  Best and worst case O(k), where:
                                    k is the total amount of nodes under 
                                    the start_node.
                                    
        @space complexity       :   O(w), where w is output sensitive.
                                    w is the total amount of terminated string
                                    appended by traverse into rtn.
                                    
        @aux-space complexity   :   O(m), where m is deepest node, from cur_node
                                    caused by recursion depth
        """
        # if current_node has a $.
        if cur_node is not None:
            if cur_node.terminal:
                # loop through count to append duplicates.
                for i in range(cur_node.count):
                    rtn.append(cur_node.value)  
            # loop through all characters in the node.
            for next_node in cur_node.link: 
                self.traverse_aux(next_node, rtn)
 

    def wildcard_prefix_freq(self, query_str):
        """
        Given a string containing a single wildcard '?' this function will return
        a list of strings in the text that have the string as a prefix.
        
        @arguments              :   query_str, a wildcard prefix to be specify
        
        @precondition           :   query_str must only contain string type character
                                    query_str must and will only contain exactly one '?'
                                    
        @postcondition          :   rtn will be append with a new associated 
                                    String for each terminal node encountered.
                                    
        @time complexity         :  Best and worst case O(q+S), where:
                                    q is the length of query_str
                                    S if the total number of characters in all
                                    strings of the text
                                    
        @space complexity       :   O(q+S) where 
                                    q is the length of the query string
                                    S is the total number of characters in 
                                    all strings of the text (inclusive of duplicates) 
                                    which have a prefix matching query_str
                                    
        @aux-space complexity   :   O(k+q), where
                                    k is the longest string in text which
                                    have a prefix matching query_str.
                                    q is the length of the query string.
                                    (recursion depth)
                                    
        @return:                    self.wildcard_prefix_freq_aux(self.root, query_str, 0)
        """
        return self.wildcard_prefix_freq_aux(self.root, query_str, 0, [])

    def wildcard_prefix_freq_aux(self, current, query_str, n, rtn):
        """
        The auxilary function of wildcard_prefix_freq.
        
        @arguments              :   current, the current node
                                    query_str, a wildcard prefix to be specify
                                    n, a counter indicating index of current characters
                                    
        @precondition           :   query_str must only contain string type character
                                    query_str must and will only contain exactly one '?'
                                    
        @postcondition          :   rtn will be append with a new associated 
                                    String for each terminal node encountered.
                                    
        @time complexity         :  Best and worst case O(q+S), where:
                                    q is the length of query_str
                                    S if the total number of characters in all
                                    strings of the text(inclusive of duplicates) 
                                    which have a prefix matching query_str
                                    
        @space complexity       :   O(q+S) where 
                                    q is the length of the query string
                                    S is the total number of characters in 
                                    all strings of the text (inclusive of duplicates) 
                                    which have a prefix matching query_str
                                    
        @aux-space complexity   :   O(k+q), where
                                    k is the longest string in text which
                                    have a prefix matching query_str.
                                    q is the length of the query string.
                                    (recursion depth)
                                    
        @return                 :   rtn, list containing all strings of the text 
                                    (inclusive of duplicates) which have a prefix 
                                    matching query_str
        """
        if current is not None:
            # if reached last character 
            if len(query_str) == n:
                self.traverse(current, rtn)
            # if current character is '?'
            elif query_str[n] == '?':
                # Recurse for all children nodes.
                for node in current.link:
                    self.wildcard_prefix_freq_aux(node, query_str, n+1, rtn)
            else: # if current character is not '?'
                index = ord(query_str[n]) - 97
                next_node = current.link[index]
                self.wildcard_prefix_freq_aux(next_node, query_str, n+1, rtn)
        
        return rtn








