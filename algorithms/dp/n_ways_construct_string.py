def n_ways_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word) and len(word) <= len(target):
            result = n_ways_construct(target[len(word) :], word_bank, memo)
            total_count += result

    memo[target] = total_count
    return total_count


if __name__ == "__main__":
    target = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    word_bank = ["e", "ee", "eeee", "eeeeee", "eeeeeeee", "eeeeeeeeee"]
    t = "enterapotentpot"
    w_b = ["a", "p", "ent", "enter", "ot", "o", "t"]
    print(n_ways_construct(t, w_b))
