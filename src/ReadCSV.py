import csv
import json
from datetime import datetime, date


class Personnel:

    def __init__(self):
        pass
    
    def make_json(self, csvFilePath, jsonFilePath):
        
        # create a dictionary
        data = {}
        student_list = []
        teacher_list = []
        
        # Open a csv reader called DictReader
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            
            # Convert each row into a dictionary 
            # and add it to data
            for rows in csvReader:
                if rows['category'] == "student":
                    student_list.append(rows['id'])
                else:
                    teacher_list.append(rows['id'])
                    
                # Assuming a column named 'No' to
                # be the primary key
                key = rows['id']
                data[key] = rows

        # with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        #     jsonf.write(json.dumps(data, indent=4))
            
        # print("Students List = " , student_list)
        # print("Teachers List = " , teacher_list)
        return student_list, teacher_list




    def required_data(self, csvFilePath, jsonFilePath):

        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            data2 = {}

            for rows in csvReader:

                key = rows['id']
                fullname = rows['firstname'] + " " + rows['lastname']

                dob = rows['dob']
                today = date.today()

                POSSIBLE_DATE_FORMATS = ['%m/%d/%Y', '%m-%d-%Y']
                
                for date_format in POSSIBLE_DATE_FORMATS :
                    try:
                        parsed_date = datetime.strptime(dob, date_format) # try to get the date
                        break # if correct format, don't test any other formats
                    except ValueError:
                        pass # if incorrect format, keep trying other formats

                age = today.year - parsed_date.year - ((today.month, today.day) < (parsed_date.month, parsed_date.day))

                sex = rows['gender']
                if sex == "m":
                    gender = "Male"
                else:
                    gender = "Female"

                aadhar_number = rows['aadhar_number']
                city = rows['city']
                contact_number = rows['contact_number']
                category = rows['category']

                data2[key] = {"Id": key, "category": category, "fullname": fullname, "gender": gender, "dob": dob, "age": age, "aadhar": aadhar_number, "city": city, "contact_number": contact_number}

        # with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        #     jsonf.write(json.dumps(data2, indent=4))
             
        return data2

# csvFilePath = 'resource/master-data2.csv'
# jsonFilePath = 'result/Parent_Class.json'
# jsonFilePath2 = r'result/Original.json'
# object1 = Personnel()

# object1.make_json(csvFilePath, jsonFilePath2)

# object1.required_data(csvFilePath, jsonFilePath)

    


    




