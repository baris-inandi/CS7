"""
Define a Clock class that has instance variables __hours and __minutes.
Your definition should include a constructor that takes two integer arguments
(a time expresed as the hour and minute) using 24-hour "military time".
For example, now = Clock(15, 10). The constructor should ensure that the
2 arguments are valid: the first should be an integer between 1 and 23;
the second should be an integer between 0 and 59.

Your class should also define the method __str__(self) to output a clock
value in AM/PM format. For example, the command print(now) will output
The time is 3:10 PM.
"""


class Clock:
    def __init__(self, hours, minutes):
        if hours < 0 or hours > 23:
            raise ValueError("Hours must be between 0 and 23")
        if minutes < 0 or minutes > 59:
            raise ValueError("Minutes must be between 0 and 59")
        self.__hours = hours
        self.__minutes = minutes

    def to_am_pm(self):
        am_pm = "AM"
        hours = self.__hours
        if self.__hours == 0:
            hours, am_pm = 12, "AM"
        elif self.__hours == 12:
            hours, am_pm = 12, "PM"
        elif self.__hours > 12:
            hours, am_pm = self.__hours - 12, "PM"
        return hours, am_pm

    def __str__(self):
        hours, am_pm = self.to_am_pm()
        return f"The time is {hours}:{self.__minutes:02d} {am_pm}"


def main():
    for i in range(0, 24):
        print(f"{i:<4}", Clock(i, 0).to_am_pm())


if __name__ == "__main__":
    main()
