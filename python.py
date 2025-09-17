import pandas as pd
import re

# Replace with your actual file path
input_file = 'PhoneDec.csv'
df = pd.read_csv(input_file)

def remove_country_code(phone):
    phone = str(phone).strip()
    return re.sub(r'^91[ ]*', '', phone)

df['Phone Number'] = df['Phone Number'].apply(remove_country_code)
df.to_csv('PhoneNumbers-No91.csv', index=False)