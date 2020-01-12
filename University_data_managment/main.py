from pyexcel_ods import get_data
from pyexcel_ods import save_data
import collections
result = dict()

academics_files = ["Data1.ods","Data2.ods","Data3.ods","Data4.ods"]

academics = [get_data("./Data_Task/"+i)["Sheet1"] for i in academics_files]

for i in academics:
    for j in i[3:]:
        try:
            if(j[0] not in result):
                result[j[0]] = 0
            term_point = 0
            trem_subject = 0
            for k in range(1,len(j),1):
                if(i[2][k]=="Physics" or i[2][k]=="Math"):
                    term_point += j[k]
                    trem_subject += 1
                term_point += j[k]
                trem_subject += 1
            result[j[0]]+=(((term_point/trem_subject)/len(academics))*0.4)
        except:
            pass


interview = get_data("./Data_Task/Interview.ods")["Sheet1"]

for i in interview[3:]:
    try:
        if(i[0] not in result):
            result[i[0]] = 0
        temp_point=0
        for j in i[1:]:
            temp_point+=j
        result[i[0]]+=((temp_point*2)*0.3)
    except:
        pass

IELTS = get_data("./Data_Task/IELTS.ods")["Sheet1"]

for i in IELTS[3:]:
    try:
        if(i[0] not in result):
            result[i[0]] = 0
        temp_point=0
        for j in i[1:]:
            temp_point+=j
        result[i[0]]+=((temp_point*100/36)*0.3)
    except:
        pass

result=[[k,v] for k, v in sorted(result.items(), key=lambda item: item[1],reverse=True)]
result={"Sheet1":result}
print(result)

result_data = collections.OrderedDict()
result_data.update(result)
save_data("result.ods", result_data)