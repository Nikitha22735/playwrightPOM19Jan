from utils.jsonReading import jsonData
from utils.csvReading import csvData, writeCSVData
import csv
import os
import pytest

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


from dotenv import load_dotenv
@pytest.mark.data()
def test_grabFromEnvFile():
    env = os.getenv("env")
    print(env)
    load_dotenv(env)
    url = os.getenv("AmazonURL")
    usname = os.getenv("username")
    pwValue = os.getenv("pw")

    print("url",url)
   


