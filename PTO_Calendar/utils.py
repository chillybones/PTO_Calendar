from datetime import datetime
import calendar

class Calendar:
    start_date = datetime.now()

    '''Allow to sepcify which date to start the calender with'''
    def __init__(self, start_date):
        if start_date is not None:
            self.startDate = start_date

    def make_calendar(self, year, month):
        calendar.setfirstweekday(firstweekday=6)
        cal = calendar.monthcalendar(year, month)
        return cal





