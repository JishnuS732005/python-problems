#  https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

if _name_ == '_main_':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    result=hash(t)
    print(result)
