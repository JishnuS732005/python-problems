#  https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if _name_ == '_main_':
    my_list=[]
    N = int(input().strip())
    for _ in range(N):
        command=input().strip().split()
        if command[0]=="insert":
            my_list.insert(int(command[1]),int(command[2]))
        elif command[0]=="print":
            print(my_list)
        elif command[0]=="remove":
            my_list.remove(int(command[1]))
        elif command[0]=="append":
            my_list.append(int(command[1]))
        elif command[0]=="sort":
            my_list.sort()
        elif command[0]=="pop":
            my_list.pop()
        elif command[0]=="reverse":
            my_list.reverse()