
# # Introduction
#
# Program for casinos --> automate the game night selector based on the player's availability to get the most people through the door and send them E-vites accordingly .
#
#
# Create an empty list called `gamers`. This will be your list of people who are attending game night.

gamers = []

# Now we want to create a function that will update this list and add a new gamer to the this `gamers` list. Each `gamer` should be a dictionary with the following keys:

def add_gamer(gamer,gamers_list):
    foundname = False
    foundavailibility = False
    for key in gamer.keys():
        if key == "name":
            foundname = True
        elif key == "availability":
            foundavailibility = True
    if foundname == True and foundavailibility == True:
        gamers_list.append(gamer)

# Next we want to add our first gamers!
kimberly = {'name':'KimberlyWarner@gmail.com','availability': ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly , gamers)
add_gamer({'name':'themahajan99@yahoo.com','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'pmahajan1973@yahoo.com','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'mahajanvedant99@gmail.com','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'ThomasNelson@gmail.com','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'JoyceSellers@gmail.com','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'MichelleReyes@gmail.com','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'StephenAdams@gmail.com','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'JoanneLynn@gmail.com', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'LatashaBryan@gmail.com','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'CrystalBrewer@gmail.com','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'JamesBarnesJr.@gmail.com','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'MichelTrujillo@gmail.com','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Finding the perfect availability
#
# Now that we have a list of all of the people interested in game night, we want to be able to calculate which nights would have the most participation. First we need to create a frequency table which correlates each day of the week with gamer availability.

def build_daily_frequency_table():
    days =["Monday", "Tuesday", "Wednesday", "Thursday",
                         "Friday", "Saturday", "Sunday"]
    dict = {}
    for day in days:
        dict[day] = 0
    return dict

count_availability = build_daily_frequency_table()

# Next we need to count the number of people every night.

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

# Now let's use these tools to find the best night to run Abruptly Goblins!

calculate_availability(gamers, count_availability)

# Lastly we need a way to pick the day with the most available people to attend so that we can schedule game night on that night.

def find_best_night(availability_table):
    max = float("-inf")
    max_key = ""
    for key,val in availability_table.items():
        if val > max:
            max = val
            max_key = key
    return max_key

# Now let's find the best day to host game night.

game_night = find_best_night(count_availability)

# And let's make a list of all of the people who are available that night.

def available_on_night(gamers_list,day):
    availableppl = []
    for dicts in gamers_list:
        for key,val in dicts.items():
            if key == "availability":
                for items in val:
                    if items ==  day:
                        res = next(iter(dicts))
                        if dicts[res] not in availableppl:
                            availableppl.append(dicts[res])
    return availableppl

attending_game_night = available_on_night(gamers,game_night)

# Generating an E-mail for the Participants

form_email = """
Dear {name},

You are invited to the "{game}" night on {day_of_week}

"""

def contactlist(gamers_who_can_attend):
    contacts = []
    for gamer in gamers_who_can_attend:
            contacts.append(gamer)
    return contacts

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer, day_of_week = day, game = game))

#-------------------------------------------------- EMAIL GENERATION---------------------------------------------------------#

from subprocess import call

class CallPy(object):

    def __init__(self, path = '/Users/vedantmahajan/PycharmProjects/Evites/mailing.py'):
        self.path = path

    def call_python_file(self):
        call(["Python3" , "{}".format(self.path)])

if __name__ == "__main__":
    c = CallPy()
    c.call_python_file()

#------------------------------------------------------------------------------------------------------------------------------#

send_email(attending_game_night, game_night, "Poker")

#  use your currently written methods to have a second game night of the week with second highest availability day.

unable_to_attend_best_night = []

for dicts in gamers:
    for key,val in dicts.items():
        if key == "name":
            if dicts[key] not in attending_game_night:
                res = list(dicts)[-1]
                unable_to_attend_best_night.append({'name': dicts[key] ,'availability': dicts[res] })

count_sec_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, count_sec_availability)

second_night = find_best_night(count_sec_availability)

# Let's send out an email to everyone who coudnt make to the game the first time

available_second_game_night = available_on_night(unable_to_attend_best_night, second_night)
send_email(available_second_game_night, second_night, "Poker")
