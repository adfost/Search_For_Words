

This program (written in Python 3) finds words from a dictionary that are anagrams of a given word. After being given a word, it checks every word in the dictionary to see if it is an anagram. In order to do this, the program first checks whether the words are the same length. If they are not, they cannot be anagrams, so the function returns False. If are the same length, the program initializes a Python dict for the two words being compared, in which each letter is a key, and the values count the number of occurrences of the key. The program then loops through the words, counting the occurrences of each key. If these dictionaries match at the end of the counting, the words are counted as anagrams. This function to check whether two words are anagrams is run to compare the inputted word with each of the words in the dictionary, and the words for which the function returns true are stored in an array, which is then sorted to be in alphabetical order.

1. The program has an online asymptotic complexity of O(N (M + log N)), where N is the length of the dictionary and M is the length of the longest word because it does constant time operations for each pair of items in a list of length N and length M, and afterwards, in the case where the list of results is long, a sort operation must be done, adding N log N to the worst case complexity (the sort is Timsort, a sort that has worst case O(N log N).
The offline asymptotic complexity is O(N), where O(N) is the length of the dictionary, because of the load operation.

2. The memory consumption is O(NM) because the dictionary must be stored, whose size is NM.

3. I would try a compression scheme for the dictionary. Since characters in words can only be letters or the apostrophe, we only need codes for a limited number of ASCII symbols.