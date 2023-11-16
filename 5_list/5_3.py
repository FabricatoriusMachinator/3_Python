import random

list_len = random.randrange(5, 100)
rand_list = random.sample(range(100), list_len)
alpha = 0.05

rand_list = sorted(rand_list)

lower_index = round((list_len * alpha)/2)
upper_index = round(list_len*(1-alpha/2))-1

print(f"Lower interval: {rand_list[:lower_index]}")
print(f"Upper interval: {rand_list[upper_index:]}")



