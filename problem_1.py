#Calculate Special Bonus leetcode 1873

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    result= []  
    for i in range(len(employees)): 
        e_id = employees['employee_id'][i]
        name = employees['name'][i]
        if (e_id %2 !=0) and (name[0] != 'M'):
            result.append([e_id, employees['salary'][i]])
        else:
            result.append([e_id,0])
            
    return pd.DataFrame(result,columns=['employee_id', 'bonus']).sort_values(by =['employee_id'])

#Another method
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    for i in range(len(employees)): 
        e_id = employees['employee_id'][i]
        name = employees['name'][i]
        if (e_id %2 ==0) or (name[0] == 'M'):
            employees['salary'][i]= 0
    
    df = employees[['employee_id','salary']]
    df = df.sort_values(by=['employee_id'])
    return df.rename(columns= {'salary':'bonus'})

#apply method

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x : x['salary'] if x['employee_id'] % 2 and not x['name'].startswith('M') else 0, axis =1)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')