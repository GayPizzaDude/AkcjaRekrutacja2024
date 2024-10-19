import pandas
from classes import *


def prepare_data(data_from_xlsx: list or object):
    return data_from_xlsx[4:]


def divide_datetime(serialized_string: str):

    """
    Divides input string into two strings classified as date and time. Removes parenthesis from time
    :param serialized_string: String with date and time given in xlsx file.
    :return: Tuple with two values: date and time.
    """

    output_tuple = (serialized_string[:10], serialized_string[11:][1:-1])
    return output_tuple


def interpret_meetings(data_list: list):
    meetings = []

    for meeting_id in range(1, len(data_list[0])):
        datetime = DateTime(divide_datetime(data[0][meeting_id]))

        meetings.append(Meeting(datetime))

    return meetings


dataframe = pandas.read_excel(r'./InputFiles/strawpoll-w4nWWRYrlnA-3c200498-8d5b-11ef-9651-3e6875717338.xlsx')
data = dataframe.values.tolist()
data = prepare_data(data)

for x in data:
    print(x)

meetings_list = interpret_meetings(data)


print(meetings_list[0].get_date().get_date())
print(meetings_list[0].get_date().get_time())
