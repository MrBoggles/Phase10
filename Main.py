import random

colors = ['Blue', 'Yellow', 'Green', 'Red']
numbers = [str(x) for x in range(0, 13)]
numbers.append('W')
duplicate = ['a', 'b']


class card:
    def __init__(self, color, value, dup):
        self.color = color
        self.value = value
        self.duplicate = dup

deck = []

def makedeck():
    global deck
    deck = []
    for i in colors:
        for j in numbers:
            for k in duplicate:
                deck.append(card(i, j, k))
    for i in range(0, 4):
        deck.append(card('Blue', 'Skip', 'a'))


def drawhand(x):
    return random.sample(deck, x)


def find1set(hand, n): #finds if there is 1 set of size n
    nums = {'W': 0, 'Skip': 0}
    for i in range(0, 13):
        nums[str(i)] = 0
    for i in hand:
        nums[i.value] += 1
    del nums['Skip']
    
    for i in range(0, 13):
        if nums[str(i)] + nums['W'] >= n:
            return True
    return False



def findsets(hand, x, n): #finds if there are at least x sets of size n
    nums = {'W': 0, 'Skip': 0}
    for i in range(0, 13):
        nums[str(i)] = 0
    for i in hand:
        nums[i.value] += 1
    del nums['Skip']
    print(nums)
    print('---------')
    potentialsets = {}
    wilds = nums['W']
    for i in nums:
        if nums[i] >= n - wilds:
            potentialsets[i] = n - nums[i]
    print(potentialsets)

    

makedeck()
repeats = 10000
count = 0

#findsets(drawhand(10), 1, 3)


for i in range(0, repeats):
    if find1set(drawhand(10), 5):
        count += 1

print(count / repeats)

