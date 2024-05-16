#Patients with a Condition leetcode 1527

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result=[]
    for i in range(len(patients)):
        p_id=patients['patient_id'][i]
        p_name =patients['patient_name'][i]
        conditions=patients['conditions'][i]
        for condition in conditions.split():
            if condition.startswith('DIAB1'):
                result.append([p_id, p_name, conditions])
                break
    return pd.DataFrame(result,columns= ['patient_id', 'patient_name', 'conditions'])

#Shorter method

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df= patients[ (patients['conditions'].str.startswith('DIAB1')) | (patients['conditions'].str.contains(' DIAB1'))]
    
#Another way

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'\bDIAB1', regex= True)]