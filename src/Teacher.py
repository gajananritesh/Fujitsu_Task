import csv
import json
from datetime import datetime, date
from ReadCSV import Personnel

class Teacher(Personnel):
    def required_data_teacher(self, csvFilePath):
        
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            data4 = {}

            for rows in csvReader:
                
                key = rows['id']
                if rows['category'] == "teacher":
                    emp_no = rows['emp_no']
                    class_teacher = rows['class_teacher_of']
                    doj = rows['doj']
                    previous_school = rows['previous_school']
                    post = rows['post']

                    try:
                        salary = int(rows['salary'])
                    except ValueError:
                        pass
                    
                    today = date.today()
                    POSSIBLE_DATE_FORMATS = ['%m/%d/%Y', '%m-%d-%Y']
                    
                    for date_format in POSSIBLE_DATE_FORMATS :
                        try:
                            parsed_date = datetime.strptime(doj, date_format)
                            break 
                        except ValueError:
                            pass

                    age_y = (today.year - parsed_date.year)
                    age_m = (today.month - parsed_date.month)

                    if age_m < 0:
                        age_y = age_y - 1
                        age_m = age_m + 12

                    service_period = str(age_y) + " years " + str(age_m) + " months "

                    subject_teaches = rows['subject_teaches']

                    data4[key] = {"emp_no": emp_no, "class_teacher": class_teacher, "doj": doj, "post": post, "salary": salary, "service_period": service_period, "previous_school": previous_school, "subject_teaches": subject_teaches}
            # print(data4)
        return data4


    def teacher_task(self):

        csvFilePath = r'resource/master-data2.csv'
        jsonFilePath = r'result/Parent_Class.json'
        object3 = Teacher()
        dict5 = object3.required_data(csvFilePath, jsonFilePath)

        object4 = Teacher()
        object4.required_data_teacher(csvFilePath)
        dict6 = object4.required_data_teacher(csvFilePath)

        jsonFilePath6 = r'result/Original.json'
        list0 = object4.make_json(csvFilePath, jsonFilePath6)
        list2 = list0[1]

        dict7 = {}

        for y in list2:
            dict5[y].update(dict6[y])
            dict7[y] = dict5[y]
        
        # Open a json writer, and use the json.dumps(), # function to dump data
        jsonFilePath7 = r'result/' + 'Teacher_Record_' + datetime.now().strftime("%Y%m%d") + '.json'
        with open(jsonFilePath7, 'w', encoding='utf-8') as jsonf:
                    jsonf.write(json.dumps(dict7, indent=4))


obj2 = Teacher()
obj2.teacher_task()
   