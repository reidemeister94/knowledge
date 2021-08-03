def can_construct(target, word_bank, memo={}):
    if len(target) == 0:
        memo[target] = True
        return True

    for word in word_bank:
        if target.startswith(word) and len(word) <= len(target):
            if target[len(word) :] in memo:
                result = memo[target[len(word) :]]
            else:
                result = can_construct(target[len(word) :], word_bank, memo)
                memo[target] = result
            if result:
                return True

    return False


if __name__ == "__main__":
    target = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    word_bank = ["e", "ee", "eeee", "eeeeee", "eeeeeeee", "eeeeeeeeee"]
    print(can_construct(target, word_bank))