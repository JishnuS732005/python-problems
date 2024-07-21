#  https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if _name_ == '_main_':
    n = int(input())
    arr = list(map(int, input().split()))
    unique_scores=list(set(arr))
    unique_scores.sort()
    runner_up_scores=unique_scores[-2]
    print(runner_up_scores)
