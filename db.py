import os
from classes import *
import pandas
import json


class DataBase:

    data_base_path = './DataBase/'
    input_files_path = './InputFiles/'

    def __init__(self):
        pass

    def create(self, name):
        with open(self.data_base_path + name + '.json', 'w') as file:
            pass

    def initiate_data_base(self):

        if not os.path.exists('./DataBase'):
            os.mkdir('./DataBase')

        self.create('Meetings')
        self.create('Candidates')
        self.create('Recruiters')

    def populate_meetings(self):
        file_data = self.open_xlsx('Candidates.xlsx')
        meetings_list = self.interpret_meetings(file_data)

        #meetings_to_save = self.serialize_meeting(meetings_list)

        self.save_meetings(meetings_list)

    def populate_candidates(self):

        candidates_info = self.open_xlsx('Candidates-info.xlsx')
        candidates_availability = self.open_xlsx('Candidates.xlsx')

        candidates_list = self.interpret_candidates(candidates_info, candidates_availability)

        #candidates_to_save = self.serialize_candidate(candidates_list)

        self.save_candidates(candidates_list)

    def populate_recruiters(self):

        recruiters_info = self.open_xlsx('Recruiters-info.xlsx')
        recruiters_availability = self.open_xlsx('Recruiters.xlsx')

        recruiters_list = self.interpret_recruiters(recruiters_info, recruiters_availability)

        #recruiters_to_save = self.serialize_recruiter(recruiters_list)

        self.save_recruiters(recruiters_list)

    # --------- STATIC METHODS ---------- #

    def open_xlsx(self, file_name: str):

        """
        Opens xlsx file and saves data in list.
        :param file_name: Name of file
        :return: List with file data.
        """

        file_path = self.input_files_path + file_name

        file_dataframe = pandas.read_excel(file_path)
        file_data = file_dataframe.values.tolist()
        file_data = self.prepare_data(file_data)

        return file_data

    def prepare_data(self, data_from_xlsx: list or object):

        """
        Strips data from header.
        :param data_from_xlsx: List with data from xlsx file.
        :return: List of striped data.
        """

        return data_from_xlsx[4:]

    def interpret_candidates(self, candidates_info: list, candidates_availability: list):

        candidates_list = []

        # space stripping
        for x in range(len(candidates_info)):
            candidates_info[x][1] = candidates_info[x][1].replace(' ', '')
            candidates_info[x][2] = candidates_info[x][2].replace(' ', '')

        names_info = [(x[1] + ' ' + x[2]).lower() for x in candidates_info]

        names_availability = [x[0].lower() for x in candidates_availability]
        names_availability = [x.strip() for x in names_availability]

        # first iteration through availability
        for x in range(len(names_availability)):

            # second iteration through info
            for y in range(len(names_info)):

                if names_availability[x] == names_info[y]:
                    temp_availability = Availability(candidates_availability[x][1:])

                    temp_candidate = Candidate(names_availability[x], temp_availability, False, candidates_info[y][3],
                                               candidates_info[y][6], candidates_info[y][4], candidates_info[y][5],
                                               candidates_info[y][7])

                    candidates_list.append(temp_candidate)

        return candidates_list

    def interpret_recruiters(self, recruiters_info: list, recruiters_availability: list):

        recruiters_list = []

        # space stripping
        for x in range(len(recruiters_info)):
            recruiters_info[x][1] = recruiters_info[x][1].replace(' ', '')
            recruiters_info[x][2] = recruiters_info[x][2].replace(' ', '')

        names_info = [(x[1] + ' ' + x[2]).lower() for x in recruiters_info]

        names_availability = [x[0].lower() for x in recruiters_availability]
        names_availability = [x.strip() for x in names_availability]

        # first iteration through availability
        for x in range(len(names_availability)):

            # second iteration through info
            for y in range(len(names_info)):

                if names_availability[x] == names_info[y]:
                    temp_availability = Availability(recruiters_availability[x][1:])

                    temp_candidate = Recruiter(names_availability[x], temp_availability, recruiters_info[y][3],
                                               recruiters_info[y][5], recruiters_info[y][4])

                    recruiters_list.append(temp_candidate)

        return recruiters_list

    def divide_datetime(self, serialized_string: str):

        """
        Divides input string into two strings classified as date and time. Removes parenthesis from time
        :param serialized_string: String with date and time given in xlsx file.
        :return: Tuple with two values: date and time.
        """

        output_tuple = (serialized_string[:10], serialized_string[11:][1:-1])
        return output_tuple

    def interpret_meetings(self, data_list: list):

        """
        Created list of meetings populated with Meeting objects.
        :param data_list: List with striped data from xlsx file.
        :return: List of Meeting objects.
        """

        meetings = []

        for meeting_id in range(1, len(data_list[0])):
            datetime = DateTime(self.divide_datetime(data_list[0][meeting_id]))

            meetings.append(Meeting(datetime))

        return meetings

    def serialize_meeting(self, meetings_list: list):

        serialized_list = []

        for meeting in meetings_list:
            serialized_meeting = meeting.get_date() + '\t' + meeting.get_time() + '\t'

            serialized_list.append(serialized_meeting)

        return serialized_list

    def save_meetings(self, serialized_list: list):

        serialized_list = [x.to_dict() for x in serialized_list]

        with open(self.data_base_path + "Meetings.json", 'a', encoding="utf-8") as file:
            json.dump(serialized_list, file, indent=2)

        print(len(serialized_list))


    def serialize_candidate(self, candidates_list: list):

        serialized_list = []

        for candidate in candidates_list:

            serialized_candidate = candidate.name + '\t' + str(candidate.availability.get_data()) + '\t' + \
                                   str(candidate.meeting_occured) + '\t' + candidate.email + '\t' + \
                                   candidate.preferred_affiliation + '\t' + str(candidate.phone_number) + '\t' + \
                                   candidate.faculty + '\t' + str(candidate.specific_info) + '\t'

            serialized_list.append(serialized_candidate)

        return serialized_list

    def save_candidates(self, serialized_list: list):

        serialized_list = [x.to_dict() for x in serialized_list]

        with open(self.data_base_path + "Candidates.json", 'a', encoding="utf-8") as file:
            json.dump(serialized_list, file, indent=2)

    def serialize_recruiter(self, recruiters_list: list):

        serialized_list = []

        for recruiter in recruiters_list:

            serialized_recruiter = recruiter.name + '\t' + str(recruiter.availability.get_data()) + '\t' + \
                                   str(recruiter.dates_number) + '\t' + recruiter.email + '\t' + \
                                   recruiter.affiliation + '\t' + recruiter.faculty + '\t'

            serialized_list.append(serialized_recruiter)

        return serialized_list

    def save_recruiters(self, serialized_list: list):

        serialized_list = [x.to_dict() for x in serialized_list]

        with open(self.data_base_path + 'Recruiters.json', 'w', encoding='utf-8') as file:
            json.dump(serialized_list, file, indent=2)
