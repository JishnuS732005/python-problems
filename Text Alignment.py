#  https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print(((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)).center(thickness*2))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(2*(thickness-i-1)+1)).center(thickness*2)).rjust(thickness*6))