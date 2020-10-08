import pandas as pd
data=pd.read_excel('trainingbase50000.xlsx')
print(data.dtypes)
print(data.info)
clear_data=data.dropna()
print(clear_data.dtypes)
print(clear_data.info)
with pd.ExcelWriter('trainingbase50000_clear.xlsx',
                    mode='w') as writer:
    clear_data.to_excel(writer, sheet_name='Training_clear',)
    writer.save()



