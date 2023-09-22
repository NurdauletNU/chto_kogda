import datetime
import  json
import openpyxl



class Worker:
    additional_bonus=1.15


    def __init__(self,name,posotion,salary,personal_register,date_device):
        self.name=name
        self.position=posotion
        self.salary=salary
        self.personal_register:bool=personal_register
        self.date_device: datetime.datetime=date_device



