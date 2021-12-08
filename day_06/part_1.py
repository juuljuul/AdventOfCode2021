input = open("input", "r")

for line in input:
    lanternfish_s = line.split(",")

lanternfish = list(map(int, lanternfish_s)    )

#print(lanternfish)

array_new = []
days = 80

for _ in range(0,days):
  for i in lanternfish:
    if i == 0:
      array_new.append(6)
      array_new.append(8)
    else:
      array_new.append(i-1)
  lanternfish = array_new
  array_new = []

print("result: ", len(lanternfish))