#recursion:

predict_next([10, 13, 16, 21, 30, 45])
    pd = [3, 3, 5, 9, 15]
    return 45 + predict_next([3, 3, 5, 9, 15])
        pd = [0, 2, 4, 6]
        return 15 + predict_next([0, 2, 4, 6])
            pd = [2, 2, 2]
            return 6 + predict_next([2, 2, 2])
                pd = [0, 0]
                #YESSS
                return 0

def predict_next(num):
    pd = pairwise_diff(num)
    if < every value of pd is 0 + num[-1] SEE BELOW>
        return num[-1] + predict_next(pd)


# boolean values all-function to check for 0!!!!! 

innocent = [0, -1, 2, 0, 3]
def all_zero(num):
    for n in num:
        if n != 0:
            return False
    return True