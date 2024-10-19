import os


class DataBase:

    data_base_path = './DataBase/'
    input_files_path = './InputFies'

    def __init__(self):
        pass

    def create(self, name):
        with open(self.data_base_path + name + '.txt', 'w') as file:
            pass

    def initiate_data_base(self):

        if not os.path.exists('./DataBase'):
            os.mkdir('./DataBase')

        self.create('Meetings')
        self.create('Candidates')
        self.create('Recruiters')

    def populate_meetings(self):
        pass

    def populate_candidates(self):
        pass

    def populate_recruiters(self):
        pass
