"""
Pair every rider wearing a red shirt with a rider wearing a blue shirt to operate a tandem bike. 
Write a function that returns the maximum possibleOR the minimum possible TOTAL SPEED  of ALL TANDEMSbeing ridden.
The indication of max or min speed will be  based on an input param ‘fastest’.
If ‘fastest = true’, then return max total  speed or vice-versa.
"""

red_speeds = [5,5,3,9,2]
blue_speeds = [3,6,7,2,1]
fastest = True
slowest = False

def tandem(red, blue, fastest):
    if fastest:
        combined = red + blue
        combined.sort(reverse=True)
        total = sum(combined[:len(red)])
        print('The fastest speed is {}'.format(total))
        return total
    else:
        red.sort()
        blue.sort()
        total = 0
        for i in range(len(red)):
            if red[i] > blue[i]:
                total += red[i]
            else:
                total += blue[i]
        print('The slowest speed is {}'.format(total))
        return total

tandem(red_speeds, blue_speeds, fastest)
tandem(red_speeds, blue_speeds, slowest)

red_speeds = [5, 5, 3, 9, 2]
blue_speeds = [3, 6, 7, 2, 1]
fastest = True


def tandem_bike(red_speeds, blue_speeds, fastest):
    red_speeds.sort(reverse=True)
    speed = 0

    if fastest:
        blue_speeds.sort(reverse=False)
        for i in range(len(red_speeds)):
            speed += max(red_speeds[i], blue_speeds[i])
    else:
        blue_speeds.sort(reverse=True)
        for i in range(len(red_speeds)):
            speed += max(red_speeds[i], blue_speeds[i])

    return speed


print(tandem_bike(red_speeds, blue_speeds, fastest))
