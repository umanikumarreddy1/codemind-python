import math
ab=int(input())
bc=int(input())
hyp=math.sqrt(ab*ab+bc*bc)
hyp=hyp/2.0
ab=ab/2.0
angle=round(math.degrees(math.acos(ab/hyp)))
print(angle)