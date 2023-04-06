num_list = []
for _ in range(10):
    x = int(input())
    num_list.append(x%42)

num_set = set(num_list)
print(len(num_set))