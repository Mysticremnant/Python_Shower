https://github.com/Mysticremnant/Python_Shower is my Github link.

The class represented here is a shower that tracks how much water is used from various users. 
The expected inputs would have been the name of the user and their total time in the shower.
Outputs would have included the current person and time taken, the amount of water they used in the shower, the ability to adjust the amount of water the shower uses, and checks to see if users meet a particular benchmark.

shower_rate reperesents the shower's usage of 2.1 gallons per minute.
self._person stores the name of the person.
self.time stores the amount of time in the shower.
I had a lot of trouble with getting these private data variables to read properly; they unfortunately caused a lot of issues and I ran out of time to fix them.
get_people is simple; it asks for a name and returns it.
get_time is similar; it asks for a user's time and returns it.
set_people asks for an input. This input will become the current name in the program. The program will then return it.
set_time asks for an input. This input will become the current time in the program. The program will then return it.
water_usage asks for the time given by the user. It then multiplies the time by the current shower_rate and returns the amount of water used in gallons.
Water_goal asks for an amount of water in gallons and compares it to the current user's water_usage. It then returns True if benchmark was met, or False if water_usage exceeds the benchmark.

The demo program implements various names and times.
To run the demo program, initalize the file and watch the errors pop up.
