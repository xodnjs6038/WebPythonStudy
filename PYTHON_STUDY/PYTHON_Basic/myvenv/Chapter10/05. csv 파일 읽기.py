import csv
file = open("./myvenv/Chapter10/student.csv", "r")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()