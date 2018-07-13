import random

def random7():
    return random.randint(1, 7)

def random5():
    # Implement random5() using random7()
    roll = random7()
    return roll if roll <= 5 else random5()
print('After rolling a 5 sided Die:')
print(random5())