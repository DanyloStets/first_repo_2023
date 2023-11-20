import re


class TimeConverter:
    __minute = 0
    __second = 0
    __hours = 0
    __whole_second = 0

    def __init__(self, sec=0, thour=''):
        self.__sec = sec
        self.__thour = thour

    def __str__(self):
        return f"Time is: {self.__hours}:{self.__minute}:{self.__second} and whole second: {self.__whole_second}"

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, new_minute):
        self.__minute = new_minute

    @property
    def hour(self):
        return self.__hours

    @hour.setter
    def hour(self, new_hour):
        self.__hours = new_hour

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, new_second):
        self.__second = new_second

    def convert_sec_to_hour(self):
        if self.__sec <= 0:
            print("Set a positive second")
            exit()
        self.__minute = int(self.__sec / 60)
        self.__hours = int(self.__minute / 60)
        self.__second = int(self.__minute % 60)
        while self.__minute >= 60:
            self.__hours += 1
            self.__minute -= 60

    def convert_thour_to_sec(self):
        hour_re = r"(\s?)(\d+)(\W)(\d+)(\W)(\d+)"
        hour_with_template = re.search(hour_re, hour_with_data)
        if hour_with_template is not None:
            if int(hour_with_template.group(2)) <= 0:
                print("Enter a higher hour!")
                exit()
            elif int(hour_with_template.group(4)) >= 60 or int(hour_with_template.group(4)) < 0:
                print("Enter a minute 1 to 59")
                exit()
            elif int(hour_with_template.group(6)) >= 60 or int(hour_with_template.group(6)) < 0:
                print("Enter a second 1 to 59")
                exit()
            self.__hours = int(hour_with_template.group(2))
            self.__minute = int(hour_with_template.group(4))
            self.__second = int(hour_with_template.group(6))
            self.__minute += self.__hours * 60
            self.__whole_second += self.__minute * 60
            return self.__whole_second


if __name__ == '__main__':
    set_variant_of_hour = int(input(f"Enter a  1 for sec or 0 for hour: "))
    if set_variant_of_hour == 1:
        seconds = int(input(f"Set a seconds: "))
        time_sec = TimeConverter(seconds)
        time_sec.convert_sec_to_hour()
        print(time_sec)
    elif set_variant_of_hour == 0:
        hour_with_data = str(input("Enter a hour with template \"Hour:Minute:Second\": "))
        start_hour_with_data = TimeConverter(thour=hour_with_data)
        print(start_hour_with_data.convert_thour_to_sec())
