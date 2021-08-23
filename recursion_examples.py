"""
Recursion Example 1: Counting backward by 2
Here we have a function named backwardsby2, which prints numbers in reverse order using steps of 2
starting with an initial number. The breaking condition is if the number is less than or equal to zero.
In that case, we simply print Zero! If that condition is not met, the function calls itself using the
current number – 2. We also initialize a list and add a smiley emoji equal to the current number. 
That way, as the counting backward happens, a corresponding number of emoji smiles will appear for
each iteration. I think you’ll agree, this is an important feature of this recursion example.
"""

def backwardsby2(num):
    if num <= 0:
        print('Zero!')
        return
    else:
        emojismiles = []
        for i in range(0, num):
            emojismiles += '😃'
        print(num, ' '.join(emojismiles))
        backwardsby2(num - 2)


backwardsby2(9)

"""
Recursion Example 2: Tower of Hanoi
The Tower Of Hanoi is an ancient puzzle said to have originated in India or Vietnam. It involves moving
various sized rings or disks around on three poles. The goal in this puzzle is to move all of the rings
on one pole to another while keeping the order of the rings intact. You must follow the rules of the 
puzzle however, and this is that only one right can be moved at a time, and no ring may be placed on 
top of a smaller sized ring. This puzzle can be solved using recursion in Python, so let’s see that 
in action!
"""

def towerOfHanoi(numrings, from_pole, to_pole, aux_pole):
    if numrings == 1:
        print('Move ring 1 from', from_pole, 'pole to', to_pole, 'pole')
        return
    towerOfHanoi(numrings - 1, from_pole, aux_pole, to_pole)
    print('Move ring', numrings, 'from', from_pole, 'pole to', to_pole, 'pole')
    towerOfHanoi(numrings - 1, aux_pole, to_pole, from_pole)


numrings = 2
towerOfHanoi(numrings, 'Left', 'Right', 'Middle')


