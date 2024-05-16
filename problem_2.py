# fix names in a table leetcode 1667

#slicing
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users ['name'] .str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by= ['user_id'])

#using Capitalize()

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users ['name'] .str.capitalize()
    return users.sort_values(by= ['user_id'])