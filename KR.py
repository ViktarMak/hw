def card_hide(card):
    return "*" * (len(card) - 4) + card[-4:]


def isPalindrome(string):
    f = str(string)
    if f[::-1].startswith(f):
        return True
    else:
        return False
