Number = int(input())
sort_list = []

for i in range(Number):
    sort_list.add(int(input()))

sort_list = list(sort_list)
sort_list.sort()

for j in range(len(sort_list)):
    print(sort_list[j])