def climbstairs(n):
    steps_to_climb = [1,2]
    one, two = 1,1
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one