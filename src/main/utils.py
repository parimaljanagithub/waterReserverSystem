import datetime 
import calendar

# date format has to be yyyy-mm-dd HH MM SS in python = '%Y-%m-%d %H:%M:%S'


#class CustomDateUtils:
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    # This method return datetime object from a input string
def getDateFromString( input_date):
        date_time_obj = datetime.datetime.strptime(input_date, DATE_FORMAT)
        return date_time_obj

    # This method return start day of the month from input date
    #input type must be in datetime format
def getStartDayOfTheMonth( input_date):
        date_time_obj = input_date #getDateFromString(input_date)
        first_day_of_month = date_time_obj.replace(day=1)
        print('start day of month = ',first_day_of_month)
        return first_day_of_month

    #we calculate the first day of the next month from a given date, then we subtract 1 day from this date 
    # and we get the date of the last day of the month.
    #input type must be in datetime format
def getEndDayOfTheMonth(input_date):
        date_time_obj = input_date #getDateFromString(input_date)
        first_day_of_month = getStartDayOfTheMonth(date_time_obj)
        days_in_month = calendar.monthrange(first_day_of_month.year, first_day_of_month.month)[1]
        next_month =first_day_of_month + datetime.timedelta(days=days_in_month)
        end_date_of_month = next_month - datetime.timedelta(days=1)
        return end_date_of_month





