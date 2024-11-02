class Availability:

    """
    Container with all possible meetings presented as list of boolean values.
    True value corresponds with date marked on strawpoll.
    Input is automatically analyzed from "-" and 1 into boolean values.
    """

    dates = []

    def __init__(self, dates):
        self.dates = dates

        self.analyze_input()

    # GETTERS / SETTERS

    def get_data(self):
        return self.dates

    def get_day_data(self, day):
        pass

    # Private Methods

    def analyze_input(self):

        """
        Analyzes input and transforms dates property into a list of boolean values.
        """

        temp_list = []

        for date in self.dates:
            if date == '-':
                temp_list.append(False)

            if date == 1:
                temp_list.append(True)

        self.dates = temp_list


class Recruiter:

    """
    Contains every data connected with recruiter:
    name - name of recruiter,
    availability - Availability object with marked dates from strawpoll
    dates_number - sum of carried out meeting
    email - email of recruiter
    affiliation - affiliation to the committee. Automatically analyzed and stored in list
    faculty - faculty of recruiter

    Conversion into dictionary data type has been implemented as to_dict() method. It is required when object
    needs to be saved as json format.

    Only dates_number property has getter and setter. Other properties cannot be accessed.
    """

    name = ''
    availability = ''
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

        self.analyze_affiliation()

    # GETTERS / SETTERS

    def get_dates_number(self):
        return self.dates_number

    def set_dates_number(self, dates_number_value: int):
        self.dates_number = dates_number_value

    # Private Methods

    def analyze_affiliation(self):

        """
        Analyzes affiliation given as an input. Converts raw input into a list with discrete values.
        """

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

    # Public Methods

    def to_dict(self):

        """
        Converts all properties into a dictionary. All keys are properties names presented as strings pointing to
        exact values of properties.
        Availability is returned as list.
        :return: Dictionary with all properties.
        """

        return {
            'name': self.name,
            'availability': self.availability.get_data(),
            'dates_number': self.dates_number,
            'email': self.email,
            'affiliation': self.affiliation,
            'faculty': self.faculty
        }


class Candidate:

    """
    Contains all information about candidate:
    name - name of candidate,
    availability - Availability object with data from strawpoll.
    meeting_occurred - boolean value pointing to the fact, if candidate has already been on meeting
    email - candidate's email
    preferred_affiliation - committees checked on candidates google form
    phone_number - candidate's phone number
    faculty - candidate's faculty
    specific_info - additional information left by candidate in google form

    Preferred affiliation to the committee is automatically analyzed and converted from raw string into a list
    with discrete values.

    Properties getters and setters are not implemented.

    Conversion into dictionary data type has been implemented as to_dict() method. It is required when object
    needs to be saved as json format.
    """

    name = ''
    availability = ''
    meeting_occurred = False

    email = ''
    preferred_affiliation = None

    phone_number = ''
    faculty = ''
    specific_info = ''

    def __init__(self, name: str, availability: Availability, meeting_occurred: bool, email: str,
                 preferred_affiliation: str, phone_number: str, faculty: str, specific_info: str):

        self.name = name
        self.availability = availability
        self.meeting_occurred = meeting_occurred
        self.email = email
        self.preferred_affiliation = preferred_affiliation
        self.phone_number = phone_number
        self.faculty = faculty
        self.specific_info = specific_info

        self.analyze_affiliation()

    # Private Methods

    def analyze_affiliation(self):

        """
        Analyzes affiliation. Converts raw string given as an input into a list with specific values.
        """

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

    # Public Methods

    def to_dict(self):

        """
        Converts all properties into a dictionary. All keys are properties names presented as strings pointing to
        exact values of properties.
        Availability is returned as list.
        :return: Dictionary with all properties.
        """

        return {
            'name': self.name,
            'availability': self.availability.get_data(),
            'meeting_occurred': self.meeting_occurred,
            'email': self.email,
            'preferred_affiliation': self.preferred_affiliation,
            'phone_number': self.phone_number,
            'faculty': self.faculty,
            'specific_info': self.specific_info
        }


class DateTime:

    """
    Storage for date of meeting. Consists of a day and time.

    Double constructor has been implemented:
    1 passed value - raw data given as a string. Automatically strapped into a day and time.
    2 passed values - two strings saved as properties.

    All properties are saved and returned as strings.

    Save frame:
    "YYYY-MM_DD HH-MM - HH-MM"
    """

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

    # GETTERS / SETTERS

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

    """
    Contains all information about recruitment meeting.
    date - DateTime object specific to every occurred meeting
    candidateID - NEEDS TO BE IMPLEMENTED - database optimization
    recruiterID - NEEDS TO BE IMPLEMENTED - database optimization
    meeting_occurred - boolean value corresponding to fact, if meeting has already occurred

    Candidate and Recruiter objects are not saved in Meeting object. ID values of candidate and recruiters are used
    instead. It is required for faster database lookups.
    """

    date = None

    candidateID = None
    recruiterID = []

    meeting_occurred = False

    def __init__(self, datetime: DateTime):
        self.date = datetime

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
            'candidateID': self.candidateID,
            'recruiterID': self.recruiterID,
            'meeting_occurred': self.meeting_occurred
        }
