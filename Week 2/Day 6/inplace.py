import random


def randomnumber(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(list_nums):
    # Shuffle the input in place
    if len(list_nums) <= 1:
        return list_nums

    l = len(list_nums) - 1

    for x in range(0, l):
        randomnum = randomnumber(x, l)
        if randomnum != x:
            list_nums[x], list_nums[randomnum] = list_nums[randomnum], list_nums[x]


print('--------------')
sample_list = [1, 2, 3, 4, 5,-1,-2,-3,-4,-5]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [-10,10,-20,20,-30,30,-40,40,-50,50]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [1, 2, 3, 4, 5,6,7,8,9,10]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [1, 2, 3, 4, 5,0,0,0,0,0]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

print('--------------')
sample_list = [1, 2, 3, 4, 5,-3,-5,-6,-7,-9]
print('Sample list:', sample_list)
print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

