import csv

data = [
    ["Target", "Feature1", "Feature2"],
    [25, 8, 10],
    [30, 12, 15],
    [22, 6, 8],
    [35, 15, 18],
    [28, 10, 12]
]

new_data = [
    ["Feature1", "Feature2"],
    [9, 11],
    [13, 17],
    [15, 20],
    [12, 15],
    [18, 22]
]

csv_file_path = 'C:\\Temp\\data.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

new_data_path = 'C:\\Temp\\newdata.csv'

with open(new_data_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_data)

print(f"CSV файлы созданы: {csv_file_path} и {new_data_path}")
