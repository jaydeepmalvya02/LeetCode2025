def canBeValid(s,locked):
    if len(s) % 2 == 1:
        return False
    openBracket = []
    unlocked = []

    for i in range(len(s)):
        if locked[i] == '0':
            unlocked.append(i)
        elif s[i] == '(':
            openBracket.append(i)
        elif s[i] == ")":
            if openBracket:
                openBracket.pop()
            elif unlocked:
                unlocked.pop()
            else:
                return False
    while openBracket and unlocked and openBracket[-1] < unlocked[-1]:
        openBracket.pop()
        unlocked.pop()
    if openBracket:
        return False
    return True


s="())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
locked="100011110110011011010111100111011101111110000101001101001111"
x=canBeValid(s,locked)
print(x)