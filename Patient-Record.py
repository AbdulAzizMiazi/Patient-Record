## Patients' Recode Keeping System:
import json
info_needed = ("Name", "Sex", "Age", "Height", "Weight", "Doctor")
store_data = {}

def bmi(height, weight):
    return round((weight / height**2), 2)

def patienct_details(name = "", sex = "", age = 0, height = 0, weight = 0, doctor = ""):
    height *= 0.3048
    patient = {
        "name"  : name.upper(),
        "sex"   : sex.lower(),
        "age"   : age,
        "height": round(height, 1),
        "weight": weight,
        "doctor": doctor.upper(),
        "bmi"   : bmi(height, weight)
    }
    store_data[name] = patient
    return patient

def take_record():
    patient = []

    for i in range(len(info_needed)):
        if info_needed[i] == "Age":
            patient.append(int(input(f'Patient {info_needed[i]}\t: ')))
        elif info_needed[i] == "Weight":
            patient.append(float(input(f'Patient {info_needed[i]}\t: ')))
        elif info_needed[i] == "Height":
            patient.append(float(input(f'{info_needed[i]} (feets)\t: ')))
        else:
            patient.append(input(f'Patient {info_needed[i]}\t: '))

    return patienct_details(*patient)


while True:
    info = take_record()
    print(info, "\n")
    ans = input("Wanna Continue? (y / n): ")

    if ans == "n" or ans == "N":
        with open("Patient_records.txt", "r") as file_read:
            file_data_in_str = file_read.read()  ## Data in JSON/string formate
            file_data = json.loads(file_data_in_str)  ## data in dictionary formate
            file_read.close()
            with open("Patient_records.txt", "w") as file:
                for patient in [*store_data]:  ## margin both dicttionaries together
                    file_data[patient] = store_data[patient]

                file_data_in_json = json.dumps(file_data)
                file.write(file_data_in_json)

        break
