#  https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    count=0
    sub_len=len(sub_string)
    for i in range(len(string)-sub_len+1):
        if string[i:i +sub_len]==sub_string:
              count += 1 
    return count

if _name_ == '_main_':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
