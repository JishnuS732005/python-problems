#  https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

if _name_ == '_main_':
    k = int(input())
    room_numbers=list(map(int,input().split()))
    room_set=set(room_numbers)
    captain_room_number=(sum(room_set)*k-sum(room_numbers)) // (k-1)
    print(captain_room_number)  
