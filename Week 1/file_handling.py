# file handling
with open("sample.txt", mode="r") as f:
    # print(f.readlines())
    print(f.read().upper())

# write user input in file
with open("sample.txt", mode="a") as f:
    user_input=""
    while(user_input!="STOP"):
        f.write(user_input + "\n")
        user_input = input("enter input: ")

# read csv
import csv
with open("data.csv", mode='r') as f:
    reader = csv.DictReader(f)
    next(reader)
    for row in reader:
        print(row)

# Write Using DictWriter
with open('data.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'ema', 'age': 18})
