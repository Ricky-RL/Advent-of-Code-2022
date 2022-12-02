
currentCalories = 0
maxCalories = 0

with open("data.txt") as file:
  for line in file:
    if line.strip():
      currentCalories += int(line)
    else:
      if(currentCalories > maxCalories):
         maxCalories = currentCalories
  
      currentCalories = 0

print('maxCalories :', maxCalories)

