# Write a fucntion that takes a list value as an argument and returns a string all the items separated
# by a comma and a space, with 'and' inserted before the last item. For example, passing
# the previous spam list to function would return
# 'apples, bananas, grapes, and watermelon'
# How to turn list into string?
food = ['apples', 'bananas', 'grapes', 'watermelon']
food = food[0] + ',' ' ' + food[1] + ',' ' ' + food[2] + ',' ' ' +'and '+ food[3]
print(food)
