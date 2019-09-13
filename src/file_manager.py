import csv

def get_data_from_file(file_path):
    file = open(file_path, "r")
    table = {} 
    for line in file.readlines():
        table_elements = line.split(",")
        id = int(table_elements[0].strip())
        data = table_elements[1].strip()
        table[id] = data
    file.close()
    return table

def save_data_to_file(file_path, data):
    file = open(file_path, "w")
    csv_writer = csv.writer(file)
    for id, row_elements in data.items():
        csv_writer.writerow([id, row_elements])
    file.close()
