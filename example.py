from datetime import datetime
import pandas as pd

date_time_str = '2018-06-29 08:15:27'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

dictionary = {
    'A': ['1', '2', '3'],
    'B': ['4', '5', '6'],
    'C': ['10', '20', '30'],
    'D': ['40', '50', '60']
}

data_frame = pd.DataFrame(dictionary)
data_frame = data_frame[['A', 'D']]

print(data_frame)