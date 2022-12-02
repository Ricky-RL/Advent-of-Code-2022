
currentCalories = 0
maxCalories = 0


calList = [0,0,0]

with open("data.txt") as file:
  for line in file:
    if line.strip():
      currentCalories += int(line)
    else:
      for i in range(3):
        if(currentCalories > calList[i]):
          calList[i] = currentCalories
          break;

      currentCalories = 0

print('maxCalories List:', calList)
print('total cal count:', sum(calList))
