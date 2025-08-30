class Date:
    def __init__(self,day=1,month=1,year=2024):
        if(day > 0 and day <= 31):
            self.__day = day
        else:
            print("Invalid value for day")
        if(month > 0 and month <13):
            self.__month = month
        else:
            print("Invalid value for month")
        if(year > 0 and year <= 2024):
            self.__year = year
        else:
            print("Invalid value for Year")

    def __str__(self):
        return f"{self.__day}\{self.__month}\{self.__year}"