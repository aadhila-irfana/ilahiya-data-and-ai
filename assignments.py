def average(*numbers):
    return sum(numbers) / len(numbers)
count= int(input("how many numbers you want to enter:"))
nums =[]
for i in range(count):
    num=float(input(f"enter number{i+1}:"))
    nums.append(num)
print("average=",average(*nums))
    