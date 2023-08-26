import openpyxl

def sum_excel_file(excel_file):
    sum=0
    try:
        workbook=openpyxl.load_workbook(excel_file)
        sheet=workbook.active
        for i in sheet.iter_rows():
            for j in i:
                if  j.value is not None and isinstance(j.value,(int,float)):
                    sum+=j.value
    except Exception as error:
        print(error)
    else:
        print("Общая сумма составляет:",sum)
    finally:
        workbook.close()


sum_excel_file(input("Введите имя файла: "))