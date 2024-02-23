from datetime import datetime

def date_diff(p,f):
     try:
        d1=datetime.strptime(p, "%d/%m/%Y")
        d2=datetime.strptime(f, "%d/%m/%Y")
        diff = abs(d1-d2)
        print(diff)
     except:
            print('Введите верные парамтеры, ожидаются даты в формате dd/mm/yyyy')
     
     
     
     
     
     
date_diff('02/02/2024','01/02/2023')