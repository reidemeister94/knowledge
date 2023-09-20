def all_ways_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return [[]]

    ways = []

    for word in word_bank:
        if target.startswith(word):
            new_target = target[len(word) :]
            target_ways = all_ways_construct(new_target, word_bank, memo)
            target_ways = [way + [word] for way in target_ways]
            if target_ways:
                ways.extend(target_ways)

    memo[target] = ways
    return ways


if __name__ == "__main__":
    target = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    word_bank = ["e", "ee", "eeee", "eeeeee", "eeeeeeee", "eeeeeeeeee"]
    t = "enterapotentpot"
    w_b = ["a", "p", "ent", "enter", "ot", "o", "t"]
    print(all_ways_construct(target, word_bank))
