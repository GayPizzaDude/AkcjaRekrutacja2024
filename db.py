import os
from classes import *
import pandas
import json


class DataBase:

    """
    Controls local database. Initiates database, populates files with data placed in InputFolder. All data is saved
    in json files:
    Recruiters.json
    Candidates.json
    Meetings.json

    All files are populated with instances of Recruiter, Candidate, Meeting objects, record ID are implemented for
    faster CRUDE operations.

    No additional constructor functionalities are implemented.

    There are two properties:
    data_base_path - string with path to local database. If given path does not exist, will be created.
    input_files_path - string with path to files with input data. Four files are required:

    Candidates.xlsx - candidates' availability
    Candidates-info.xlsx - candidates' information given in google forms eg: name, email, preferred affiliation
    Recruiters.xlsx - recruiters' availability
    Recruiters-info.xlsx - recruiters' information given in google forms eg: name, email, affiliation
    """

    data_base_path = './DataBase/'
    input_files_path = './InputFiles/'

    def __init__(self):
        pass

    # --------- STATIC METHODS ---------- #

    def create(self, name):

        """
        Creates empty json file with given file name.
        :param name: Name of file
        """

        with open(self.data_base_path + name + '.json', 'w') as file:
            pass

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

        """
        Data mapping based on two files:
        Candidates.xlsx
        Candidates-info.xlsx

        Name of candidate is used as key in mapping. Additional spaces stripping is implemented.
        Two files are searched for the same name, if found Candidate object is filled with data.

        :param candidates_info: Candidates-info.xlsx file content
        :param candidates_availability: Candidates.xlsx file content
        :return: List of Candidate object instances
        """

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

        """
        Data mapping based on two files:
        Recruiters.xlsx
        Recruiters-info.xlsx

        Name of candidate is used as key in mapping. Additional spaces stripping is implemented.
        Two files are searched for the same name, if found Recruiter object is filled with data.

        :param recruiters_info: Recruiters-info.xlsx file content
        :param recruiters_availability: Recruiters.xlsx file content
        :return: List of Recruiter object instances
        """

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

    # DATABASE FILES SAVING METHODS

    def save_meetings(self, serialized_list: list):

        """
        Saves Meeting objects converted to dictionaries respected by json file format
        :param serialized_list: List of strings ready to be saved
        """

        serialized_list = [x.to_dict() for x in serialized_list]

        with open(self.data_base_path + "Meetings.json", 'a', encoding="utf-8") as file:
            json.dump(serialized_list, file, indent=2)

        print(len(serialized_list))

    def save_candidates(self, serialized_list: list):

        """
        Saves Candidate objects converted to dictionaries respected by json file format.
        :param serialized_list: List of strings to be saved
        """

        serialized_list = [x.to_dict() for x in serialized_list]

        with open(self.data_base_path + "Candidates.json", 'a', encoding="utf-8") as file:
            json.dump(serialized_list, file, indent=2)

    def save_recruiters(self, serialized_list: list):

        """
        Saves Recruiter objects converted to dictionaries respected by json file format.
        :param serialized_list: List of strings to be saved
        """

        serialized_list = [x.to_dict() for x in serialized_list]

        with open(self.data_base_path + 'Recruiters.json', 'w', encoding='utf-8') as file:
            json.dump(serialized_list, file, indent=2)


    # ---------- PUBLIC METHODS ------------ #

    def initiate_data_base(self):

        """
        Database initialization. Creates empty Meetings.json, Candidates.json and Recruiters.json files.
        Checks if DataBase folder already exists, if not new folder is created.
        """

        if not os.path.exists('./DataBase'):
            os.mkdir('./DataBase')

        self.create('Meetings')
        self.create('Candidates')
        self.create('Recruiters')

    # DATABASE POPULATION

    def populate_meetings(self):

        """
        Populate Meetings.json file with data given in InputFolder. Uses private methods for data analysis.
        Overwrites existing file.
        """

        file_data = self.open_xlsx('Candidates.xlsx')
        meetings_list = self.interpret_meetings(file_data)

        self.save_meetings(meetings_list)

    def populate_candidates(self):

        """
        Populate Candidates.json file with data given in InputFolder. Uses private methods for data analysis.
        Overwrites existing file.
        """

        candidates_info = self.open_xlsx('Candidates-info.xlsx')
        candidates_availability = self.open_xlsx('Candidates.xlsx')

        candidates_list = self.interpret_candidates(candidates_info, candidates_availability)

        self.save_candidates(candidates_list)

    def populate_recruiters(self):

        """
        Populate Recruiters.json file with data given in InputFolder. Uses private methods for data analysis.
        Overwrites existing file.
        """

        recruiters_info = self.open_xlsx('Recruiters-info.xlsx')
        recruiters_availability = self.open_xlsx('Recruiters.xlsx')

        recruiters_list = self.interpret_recruiters(recruiters_info, recruiters_availability)

        self.save_recruiters(recruiters_list)