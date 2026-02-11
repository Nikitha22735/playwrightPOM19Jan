from utils.jsonReading import jsonData
from utils.csvReading import csvData, writeCSVData
import csv
import os

def test_grabData():
    print(jsonData("testData\\credentials.json"))
    

def test_grabCSVData():
    print(csvData("testData\\credentails.csv"))

    data = csvData("testData\\credentails.csv")
    print(data[1]["username"])




def test_writeCSVData():
    headers = ["username","password","age"]
    data12 = {'username': 'test3@gmail.com', 'password': 'Admin1@123', 'age': '20'}
    path = "testData\\credentails.csv"
    writeCSVData(headers,data12,path)



def test_grabFromCommandLine():
    usernameValue= os.getenv("username")
    passwordValue = os.getenv("password")
    print(usernameValue)
    print(passwordValue)
   


