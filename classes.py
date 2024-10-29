class Availability:
    """
    lista true/false
    """

    dates = [] #moze zrobic liste list zeby byl jakikolwiek podzial na dni

    def __init__(self, dates):
        self.dates = dates

    def get_data(self):
        return self.dates

    def get_day_data(self, day):
        pass


class Recruiter:

    name = ''
    availability = '' #availability object
    dates_number = 0

    email = ''
    affiliation = None

    faculty = ''

    def __init__(self, name, availability, email, affiliation, faculty):

        self.name = name
        self.availability = availability
        self.email = email
        self.affiliation = affiliation
        self.faculty = faculty

    def get(self):
        temx = [self.name, self.availability.get_data(), self.dates_number, self.email, self.affiliation, self.faculty]
        return temx

    def analyze_affiliation(self):

        affiliation_list = []

        if 'Komisja Kultury i Sportu' in self.affiliation:
            affiliation_list.append('Komisja Kultury i Sportu')

        if 'Komisja Komunikacji i Promocji' in self.affiliation:
            affiliation_list.append('Komisja Komunikacji i Promocji')

        if 'Sekcja Nowych Mediów' in self.affiliation:
            affiliation_list.append('Sekcja Nowych Mediów')

        if 'Zespół Ewaluacji, Formularzy i Rozwoju' in self.affiliation:
            affiliation_list.append('Zespół Ewaluacji, Formularzy i Rozwoju')

        if 'Komisja Rozwoju Struktury Informatycznej' in self.affiliation:
            affiliation_list.append('Komisja Rozwoju Struktury Informatycznej')

        if 'Komisja Współpracy Zewnętrznej i Przedsiębiorczości' in self.affiliation:
            affiliation_list.append('Komisja Współpracy Zewnętrznej i Przedsiębiorczości')

        if 'Komisja Dydaktyki i Jakości Kształcenia' in self.affiliation:
            affiliation_list.append('Komisja Dydaktyki i Jakości Kształcenia')

        self.affiliation = affiliation_list

    def to_dict(self):

        return {
            'name': self.name,
            'availability': self.availability.get_data(),
            'dates_number': self.dates_number,
            'email': self.email,
            'affiliation': self.affiliation,
            'faculty': self.faculty
        }


class Candidate:

    name = ''
    availability = '' #availability object
    meeting_occured = False

    email = ''
    preferred_affiliation = None

    phone_number = ''
    faculty = ''
    specific_info = ''

    def __init__(self, name: str, availability: Availability, meeting_occured: bool, email: str,
                 preferred_affiliation: str, phone_number: str, faculty: str, specific_info: str):

        self.name = name
        self.availability = availability
        self.meeting_occured = meeting_occured
        self.email = email
        self.preferred_affiliation = preferred_affiliation
        self.phone_number = phone_number
        self.faculty = faculty
        self.specific_info = specific_info

    def get(self):
        tempx = [self.name, self.availability.get_data(), self.meeting_occured, self.email, self.preferred_affiliation,
                 self.phone_number, self.faculty, self.specific_info]

        return tempx

    def analyze_affiliation(self):

        affiliation_list = []

        if 'Komisja Kultury i Sportu' in self.preferred_affiliation:
            affiliation_list.append('Komisja Kultury i Sportu')

        if 'Komisja Komunikacji i Promocji' in self.preferred_affiliation:
            affiliation_list.append('Komisja Komunikacji i Promocji')

        if 'Sekcja Nowych Mediów' in self.preferred_affiliation:
            affiliation_list.append('Sekcja Nowych Mediów')

        if 'Zespół Ewaluacji, Formularzy i Rozwoju' in self.preferred_affiliation:
            affiliation_list.append('Zespół Ewaluacji, Formularzy i Rozwoju')

        if 'Komisja Rozwoju Struktury Informatycznej' in self.preferred_affiliation:
            affiliation_list.append('Komisja Rozwoju Struktury Informatycznej')

        if 'Komisja Współpracy Zewnętrznej i Przedsiębiorczości' in self.preferred_affiliation:
            affiliation_list.append('Komisja Współpracy Zewnętrznej i Przedsiębiorczości')

        if 'Komisja Dydaktyki i Jakości Kształcenia' in self.preferred_affiliation:
            affiliation_list.append('Komisja Dydaktyki i Jakości Kształcenia')

        if 'Jeszcze nie wiem' in self.preferred_affiliation:
            affiliation_list.append('Jeszcze nie wiem')

        self.preferred_affiliation = affiliation_list

    def to_dict(self):

        return {
            'name': self.name,
            'availability': self.availability.get_data(),
            'meeting_occured': self.meeting_occured,
            'email': self.email,
            'preferred_affiliation': self.preferred_affiliation,
            'phone_number': self.phone_number,
            'faculty': self.faculty,
            'specific_info': self.specific_info
        }


class DateTime:

    date = ''
    time = ''

    def __init__(self, *args):

        """
        Double constructor
        :param args: Might be tuple with date and time or two arguments which are date and time
        """

        if len(args) == 2:

            self.date = args[0]
            self.time = args[1]

        if len(args) == 1:

            self.date = args[0][0]
            self.time = args[0][1]

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_date_time(self):
        return self.date + ' ' + self.time


class Meeting:

    date = None # DateTime object

    candidateOccupation = None # Candidate object
    candidateID = None

    recruiterOccupation = [] # Recruiters objects
    recruiterID = None

    meeting_occured = False

    def __init__(self, datetime: DateTime):
        self.date = datetime

    def get_candidate(self):
        return self.candidateOccupation

    def get_recruiters(self):
        return self.recruiterOccupation

    def get_datetime(self):
        return self.date.get_date_time()

    def get_date(self):
        return self.date.get_date()

    def get_time(self):
        return self.date.get_time()

    def get_datetime_object(self):
        return self.date

    def to_dict(self):
        return {
            'date': self.date.get_date_time(),
            'candidateOccupation': self.candidateOccupation,
            'candidateID': self.candidateID,
            'recruiterOccupation': self.recruiterOccupation,
            'recruiterID': self.recruiterID,
            'meeting_occured1': self.meeting_occured
        }
