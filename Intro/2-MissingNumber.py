n = int(input())

line = input()
items = list(map(int, line.split(" ")))
items.sort()

for num in range(1, n + 1):
    if num == n:
        print(num)
        break

    if items[num - 1] != num:
        print(num)
        break




