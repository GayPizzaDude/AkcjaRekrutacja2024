


class Recruiter:

    name = ''
    availability = '' #availability object

    def __init__(self):
        pass


class Candidate:

    name = ''
    availability = '' #availability object

    def __init__(self):
        pass


class Availability:
    """
    lista true/false
    """

    dates = [] #moze zrobic liste list zeby byl jakikolwiek podzial na dni

    def __init__(self):
        pass

    def getData(self):
        pass


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


class Meeting:

    date = None #DateTime object
    candidateOccupation = None
    recruiterOccupation = []

    def __init__(self, datetime: DateTime):
        self.date = datetime

    def get_candidate(self):
        return self.candidateOccupation

    def get_recruiters(self):
        return self.recruiterOccupation

    def get_date(self):
        return self.date
