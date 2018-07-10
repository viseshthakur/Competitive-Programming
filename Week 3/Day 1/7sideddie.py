import random

def random5():
    return random.randint(1, 5)

def random7():
    # Implement random7() using random5()
    var = 5*random5()+random5()-5
    if(var<22):
        return var%7 + 1
    return random7()

print('After rolling a 7 sided die')
print(random7())
