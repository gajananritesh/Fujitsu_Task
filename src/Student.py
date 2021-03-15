import csv
import json
from datetime import datetime, date
from ReadCSV import Personnel

class Student(Personnel):
    def __init__(self):
        super().__init__()

    def required_data_student(self, csvFilePath):

        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            data3 = {}    

            for rows in csvReader:
                
                key = rows['id']
                if rows['category'] == "student":
                    roll_number = rows['roll_no']
                    classs = rows['class']
                    total_marks = rows['total_marks']
                    try:
                        secure_percentage = int(rows['sec_percent'])
                    except ValueError:
                        pass

                    stream = rows['hs_stream']
                    
                    if secure_percentage >= 90:
                        grade = "A+"
                    elif secure_percentage >= 80 and secure_percentage <= 89:
                        grade = "A"
                    elif secure_percentage >= 70 and secure_percentage <= 79:
                        grade = "B+"
                    elif secure_percentage >= 60 and secure_percentage <= 69:
                        grade = "B"
                    elif secure_percentage >= 50 and secure_percentage <= 59:
                        grade = "C"
                    else:
                        grade = "D"
                        
                    data3[key] = {"roll_number": roll_number, "classs": classs, "total_marks": total_marks, "stream": stream, "secure_percentage": secure_percentage, "grade": grade}
        # print(data3)

        # Open a json writer, and use the json.dumps(), function to dump data
        return data3    



    def student_task(self):
        csvFilePath = r'resource/master-data2.csv'
        object3 = Student()
        object3.required_data_student(csvFilePath)
        dict2 = object3.required_data_student(csvFilePath)


        jsonFilePath = r'result/Parent_Class.json'
        object2 = Student()
        dict1 = object2.required_data(csvFilePath, jsonFilePath)


        jsonFilePath2 = r'result/Original.json'
        list0 = object2.make_json(csvFilePath, jsonFilePath2)
        list1 = list0[0]

        dict3 = {}

        for x in list1:
            dict1[x].update(dict2[x])
            dict3[x] = dict1[x]


        jsonFilePath4 = r'result/' + 'Student_Record_' + datetime.now().strftime("%Y%m%d") + '.json'
        with open(jsonFilePath4, 'w', encoding='utf-8') as jsonf:
                    jsonf.write(json.dumps(dict3, indent=4))


obj1 = Student()
obj1.student_task() 