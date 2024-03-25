import csv
 
f = open('.\grade.csv','r')
rdr = csv.reader(f)
 
for line in rdr:
    print(line)
 
f.close()

f = open('.\write.csv','w', newline='')
wr = csv.writer(f)
wr.writerow([1, 'Alice', 'A', 'Math'])
wr.writerow([2, 'Bob', 'B', 'Science '])
 
f.close()

f = open('.\write.csv','a', newline='')
wr = csv.writer(f)
wr.writerow([3, 'Charlie', 'C', 'English'])

f.close()