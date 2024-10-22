import pandas
from classes import *
import json


def open_xlsx(file_name: str):
    """
    Opens xlsx file and saves data in list.
    :param file_name: Name of file
    :return: List with file data.
    """

    file_path = './InputFiles/' + file_name

    file_dataframe = pandas.read_excel(file_path)
    file_data = file_dataframe.values.tolist()
    file_data = prepare_data(file_data)

    return file_data


def prepare_data(data_from_xlsx: list or object):
    """
    Strips data from header.
    :param data_from_xlsx: List with data from xlsx file.
    :return: List of striped data.
    """

    return data_from_xlsx[4:]


data_info = open_xlsx("Recruiters-info.xlsx")

# space stripping
for x in range(len(data_info)):
    data_info[x][1] = data_info[x][1].replace(' ', '')
    data_info[x][2] = data_info[x][2].replace(' ', '')

for x in data_info:
    print(x)

# list of names created from info file
names_info = [(x[1] + ' ' + x[2]).lower() for x in data_info]


for x in names_info:
    print(x)



data = open_xlsx("Recruiters.xlsx")

print()

for x in data:
    print(x)

# list of names created form availability file
names = [x[0].lower() for x in data]
names = [x.strip() for x in names]

for x in names:
    print(x)



recruiters_list = []

# first iteration through availability
for x in range(len(names)):

    # second iteration through info
    for y in range(len(names_info)):

        if names[x] == names_info[y]:

            temp_availability = Availability(data[x][1:])

            temp_candidate = Recruiter(names[x], temp_availability, data_info[y][3], data_info[y][5], data_info[y][4])

            recruiters_list.append(temp_candidate)

print(len(recruiters_list))
print(len(names))

print(recruiters_list[0].get())
print('\n\n\n\n')

print(json.dumps(recruiters_list[0].to_dict(), indent=2))

with open('test.json', 'w') as file:
    pass


if not __name__ == '__main__':
    pass
