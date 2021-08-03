def can_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        memo[target] = True
        return True

    for word in word_bank:
        if target.startswith(word) and len(word) <= len(target):
            result = can_construct(target[len(word) :], word_bank, memo)
            memo[target] = result
            if result:
                return True

    memo[target] = False
    return False


if __name__ == "__main__":
    target = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    word_bank = ["e", "ee", "eeee", "eeeeee", "eeeeeeee", "eeeeeeeeee"]
    import time

    start = time.time()
    print(can_construct(target, word_bank))
    end = time.time()
    print(end - start)
