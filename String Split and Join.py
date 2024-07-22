#  https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

def split_and_join(line):
    a = line.split(" ")
    return "-".join(a)

if _name_ == '_main_':
    line = input()
    result = split_and_join(line)
    print(result)
