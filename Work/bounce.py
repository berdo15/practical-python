# bounce.py
#
# Exercise 1.5

height = 100
bounce_height = 3/5
bounce_number = 0

while bounce_number < 10:
    height = height*bounce_height
    print(round(height, 4))
    bounce_number += 1

# testchange