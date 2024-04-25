areaOfATriangle = lambda base, height: base * height

# if else shorthand
triangle_area = areaOfATriangle(base=4, height=6)

print("It's huge") if triangle_area > 36 else print("It's small")