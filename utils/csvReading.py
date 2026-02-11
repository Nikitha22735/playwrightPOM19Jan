import csv

def csvData(path):
    values = []
    with open(path) as data:
        data1 = csv.DictReader(data)
        for rows in data1:
            values.append(rows)

    return values


def writeCSVData(headers,data12,path):
    # headers = ["username","password","age"]
    # data12 = {'username': 'test3@gmail.com', 'password': 'Admin1@123', 'age': '20'}
    with open(path, mode='a',newline="") as data:
        writer = csv.DictWriter(data, fieldnames=headers)
        writer.writerow(data12)