import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# خواندن فایل اکسل
df = pd.read_excel('path_to_excel_file.xlsx')

# استخراج ستون زمان
time_column = 'Month' # نام ستون زمان در فایل اکسل
time = df[time_column]

# استخراج داده‌ها
data_columns = ['CO', 'O3', 'SO2', 'PM10', 'PM2.5', 'AQI'] # نام ستون‌های داده در فایل اکسل

# تعیین نقاط اشتراک بیشترین و کمترین مقدار
min_values = df[data_columns].min()
max_values = df[data_columns].max()

# رسم نمودار با نشان دادن نقاط اشتراک
fig, ax = plt.subplots(figsize=(10, 6))
for column in data_columns:
    data = df[column]
    ax.plot(time, data, marker='o', linestyle='-', label=column)
    ax.annotate(f"Min: {min_values[column]}", xy=(time.iloc[data.idxmin()], min_values[column]), xytext=(time.iloc[data.idxmin()], min_values[column]-10), arrowprops=dict(facecolor='black', arrowstyle='->'))
    ax.annotate(f"Max: {max_values[column]}", xy=(time.iloc[data.idxmax()], max_values[column]), xytext=(time.iloc[data.idxmax()], max_values[column]+10), arrowprops=dict(facecolor='black', arrowstyle='->'))
ax.set_xlabel('Time')
ax.set_ylabel('Data')
ax.legend()
plt.show()