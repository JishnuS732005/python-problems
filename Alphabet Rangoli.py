#  https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(size):
    import string
    
    alphabet=string.ascii_lowercase
    width=4*(size-1)+1
    pattern=[]
    
    for i in range(size):
        letters='-'.join(alphabet[size-1:size-i-1:-1]+alphabet[size-i-1:size])
        pattern.append(letters.center(width,'-'))
        full_pattern=pattern+pattern[-2::-1]
    for row in full_pattern:
        print(row)

if _name_ == '_main_':
    n = int(input())
