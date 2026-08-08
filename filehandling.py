#FILE HANDLING(process of creating, opening, reading, writing, and updating files)
#FILE (where data is stored permanently)


#open() [used to open or create a file]
#mode read, write, append, Create New File 
#syntax [file = open("filename", "mode")]

#read
file = open("filehandling(practice).py", "r")
print(file.read())
file.close()


#write
file = open("filehandling(practice).py", "w")
print(file.write('hlo'))
file.close()


#Append Mode(a)
file = open("filehandling(practice).py","a")
file.write("\nAI")
file.close()



#Create Mode ("x") create new file
file = open("OOP.py","x")
file.close()



#readline() Reads ONE line.
file = open("filehandling(practice).py","r")
print(file.readline())


#readlines() Reads ALL lines
file = open("filehandling(practice).py","r")
print(file.readlines())



#writelines() Writes multiple lines

file = open("filehandling(practice).py","w")
lines = [
    "Python\n",
    "Java\n",
    "AI"
]
file.writelines(lines)
file.close()


#with open() opens a file and automatically closes it
with open("filehandling(practice).py", "r") as file:
    print(file.read())



#file pointer(cursor)current position where Python is reading or writing in a file

with open("filehandling(practice).py", "r") as file:
    print(file.tell())
    file.read(2)
    print(file.tell())



#Binary Files (store data as bytes instead of readable text e.g images, videos, audio, and PDFs)


#rb Mode
'''with open("eyes.jpg", "rb") as file:
     data = file.read()
 print(type(data))'''



#wb Mode #b tells  binary file


''' with open("eyes.jpg", "rb") as file:
      data = file.read()'''


#writerow()writes one row to a CSV file
#CSV FILES(Comma Separated Values)

'''import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#acssesing individual values
        print(row[0], row[1])'''



#WRITING A CSV FILE
'''import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ali", 20, "Lahore"])
    writer.writerow(["Memona", 18, "Okara"])'''




#Writing Multiple Rows

'''import csv
rows = [
    ["Name", "Age"],
    ["Ali", 20],
    ["Sara", 19],
    ["Memona", 18]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)'''




#JSON FILES (JavaScript Object Notation) store and exchange structured data


'''import json
student = {
    "name": "Memona",
    "age": 18,
    "city": "Okara"
}
with open("student.json", "w") as file:
    json.dump(student, file)'''



#dump() saves Python data into a JSON file

#load() reading JSON file


'''import json
with open("student.json", "r") as file:
    data = json.load(file)
print(data)
print(student["name"])#accsesing json 
print(student["city"])'''



'''| CSV                    | JSON                        |
   | ---------------------- | --------------------------- |
   | Table (rows & columns) | Key-value structure         |
   | Good for Excel         | Good for APIs & web apps    |
   | Uses commas            | Uses `{}` and `[]`          |
   | Best for datasets      | Best for structured objects |
   |easier                  | longer with nested data     |
   |Excel, AI datasets      | APIs, websites, apps        |
   |can't store list,dict   | can store list,dict         |'''


