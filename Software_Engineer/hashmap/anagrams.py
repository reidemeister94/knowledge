def Anagrams(words, n):
    """
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    """
    set_map = {}
    for word in words:
        set_word = tuple(set(word))
        if set_word in set_map:
            set_map[set_word].append(word)
        else:
            set_map[set_word] = [word]
        print(word)
        print(set_map)
        print("=" * 75)

    return list(set_map.values())


n = 5
words = ["act", "god", "cat", "dog", "tac"]

print(Anagrams(words, n))
