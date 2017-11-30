import sys
def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    w1 = word1.lower()
    w2 = word2.lower()
    table1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, '\'': 0}
    table2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, '\'': 0}
    for i in range(0, len(w1)):
        table1[w1[i]] += 1
        table2[w2[i]] += 1
    if table1 == table2:
        return True
    return False
def anagrams(word, dict1):
    result = []
    for w in dict1:
        if is_anagram(word, w):
            result.append(w.lower())
    if result == []:
        print('-')
    else:
        print(*sorted(result))
file = open(sys.argv[1], "r")
dictionary1 = file.read().split('\n')
word = 'word'
while word != '':
    word = input()
    anagrams(word, dictionary1)
