#  https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    width=len(bin(number))-2
    for i in range(1,number+1):
        decimal=str(i).rjust(width)
        octal=oct(i)[2:].rjust(width)
        hexadecimal=hex(i)[2:].upper().rjust(width)
        binary=bin(i)[2:].rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")
        
        
if _name_ == '_main_':
    n = int(input())
