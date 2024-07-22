#  https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

def create_door_mat(N,M):
    for i in range(1,N,2):
        pattern=(".|."*i).center(M,"-")
        print(pattern)
        
    welcome_line="WELCOME".center(M,"-")
    print(welcome_line)
    
    for i in range(N-2,0,-2):
        pattern=(".|."*i).center(M,"-")
        print(pattern)
        
N,M = map(int,input().split()) 
create_door_mat(N,M)
