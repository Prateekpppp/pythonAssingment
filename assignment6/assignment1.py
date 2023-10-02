import os
import json

dir = os.getcwd()
lst = []
with open(dir+'/assignment6/employees.json') as file:
    data = json.load(file)
for key in data:
    # print(data[key])
    lst.append(data[key])
    
print(lst)

stateDict = {
    'state1':'city1',
    'state2':'city2',
    'state3':'city3',
    'state4':'city4',
    'state5':'city5',
    'state6':'city6',
    'state7':'city7',
}
save_data = open(dir+'/assignment6/save_json.json','w')
json.dump(stateDict,save_data)            
save_data.close()
