#  https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    return s.swapcase()

if _name_ == '_main_':
    s = input()
    result = swap_case(s)
    print(result)
