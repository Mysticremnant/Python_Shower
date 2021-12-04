"""
Name: Steven Zhang
Final project
Behold, the smart shower!
"""
# Failed attempt at managing user input.
# USERLOG = {}
# USERLOG_2 = []
# # I will allow manual input of shower users and time spent in shower.
# def add_user():
#     user = input("Enter name of shower user:")
#     faucet_use = float(input("Enter time spent in shower here:"))
#     record = [user, faucet_use]
#     return record
# Class shower initiated.
class shower:
    # This rate is in gallons/minute.
    shower_rate = 2.1
    # Two variables for the person and the time in shower.
    def __init__(self, people, time):
        self._people = people
        self._time = time
    # Get the current name.
    def get_people(self):
        return self._people
    # Get current time.
    def get_time(self):
        return self._time
    # Set new name.
    def set_people(self):
        self._people = input("Enter new name here:")
        return self._people
    # Set new time.
    def set_time(self):
        self._time = float(input("Enter new time here:"))
        return self._time
    # Calculate water usage.
    def water_usage(self):
        # self._time really doesn't want to be read as a number here.
        washwater = shower.shower_rate * float(self._time)
        return washwater
    # See how much water person used in a shower.
    def water_goal(self, benchmark=10):
        benchmark = input("Enter goal amount of water used per shower(in gallons):")
    # Since this function requires my other function to work, this is also broken.
        wastewater = shower.water_usage - benchmark
        if wastewater > 0:
            return False
        else:
            return True
        
def main():
    port_1 =shower.get_people("Loopy")
    port_2=shower.get_time(3)
    port_3=shower.set_people("Nobody")
    port_4=shower.set_time(6)
    port_5=shower.water_usage(9)
    port_6=shower.water_goal("Rodney", 12)
    print(port_1)
    print(port_2)
    print(port_3)
    print(port_4)
    print(port_5)
    print(port_6)


if __name__ == "__main__":
    main()

# Acknowledgements/Citations
# https://blog.constellation.com/2016/07/05/average-shower-length-flowchart/ for shower information.