import re
from datetime import date

with open('examdates.txt','r') as f:
    for line in f:
        mystr = re.findall(r"\d{1,2}[-|\/]\d{1,2}[-|\/]\d{2,4}",line)
        examname = re.findall(r"^\w*",line)
        if(len(mystr) > 0 and len(examname) > 0):            
            arraydate=re.split(r"[-|\/]", mystr[0])
            dateholder=date(int(arraydate[2]), int(arraydate[1]), int(arraydate[0]))
            difference = dateholder-date.today()
            print(examname[0],dateholder,' ',int(difference.days/7), "weeks &",difference.days%7,"days\n")          


