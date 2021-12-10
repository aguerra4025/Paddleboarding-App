# Programmer: Arlety Guerra
# Description: This is a tracking app for paddle-boarding enthusiasts who
# would like to document their trips.
# The app will help record and determine patterns and create budgeting
# opportunities.
# Resources and information was gathered from w3schools.com.

import datetime

print("Welcome to Paddle Specs, "
      "your very own personalized paddling experience tracker."
      "\nMy name is Lilo and I will be assisting you "
      "in keeping up with your adventures."
      "\nEnough about me.")
name = input("What is your name? ")
print("Hello,", name + "!")

while True:  # try/except loop prevents program from crashing if input is incorrect
    try:
        age = int(input("So that we can better communicate, I need to know your age. How old are you? "))
        if 0 < age < 120:
            break
    except ValueError:  # displays error message and repeats input request
        print("I'm sorry. That doesn't seem right. Let's try again!")

minor_message = str("Oops! O.o That's awkward. "
                    "Paddle Specs doesn't have the technology "
                    "it needs to help your age category quite yet."
                    "\nMake sure to always stay safe out "
                    "in the water and that you are always accompanied by a "
                    "responsible adult. Hope to see you back in the near "
                    "future.\nGoodbye! ^-^")
google_fact = str("Fun fact: You're older than Google!!! Don't take it to "
                  "heart, "
                  "though. You're still younger than me... \nunless you were "
                  "born before 1936, then you're older than "
                  "the modern computer a.k.a. me. "
                  "Awkward... Anyways! ")

while age in range(0, 18):  # prints minor message if user < 18 yrs old
    print(minor_message)
    exit()  # closes the program if restricted age is inputted
while True:
    try:
        year_born = int(input("Just to verify that I interpret the correct "
                              "information, what year were you born? "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")

if year_born + age == datetime.datetime.now().year - 1:
    print("Oops! There seems to be an error in my calculations. I "
          "apologize for the inconvenience. Please call our support team at "
          "1-(800)555-5367 and we will assist you immediately. "
          "Thank you for your understanding.")
    exit()  # need work on getting exact age; yr is not specific enough
elif year_born + age == datetime.datetime.now().year:
    print()
else:
    year_born = int(input("Mmm... That doesn't seem right. Please try again. "
                          "On what year were you born? "))
    while year_born + age != datetime.datetime.now().year:
        year_born = int(input("Mmm... That doesn't seem right. Please try again. "
                              "On what year were you born? "))
if year_born < 1998:
    print(google_fact)
print()

print("Let's begin with today's adventure, shall we?")
adventure_title = input("How would you like to name today's adventure? "
                        "\nThis is how it will be recorded on your file. ")
date = input("On what date did this adventure take place? ")
while True:
    try:
        start_time = float(input("At what time did you head out into the water? "
                                 "\nPlease enter the time in the format hh.mm in military time. "))
        break
    except ValueError:
        start_time = input("I'm sorry. That doesn't seem right. Let's try again! Remember "
                           "that military time is a 24 hour time system.")
if 00.00 <= start_time <= 11.59:  # range check
    standard_start_time = start_time, "AM"
elif 12.00 <= start_time <= 23.59:
    standard_start_time = start_time - 12, "PM"
else:
    standard_start_time = start_time
while 00.00 > start_time > 23.59:
    start_time = input("I'm sorry. That doesn't seem right. Let's try again! Remember "
                       "that military time is a 24 hour time system.")
print()
location_name = input("What is the name of the body of water "
                      "where you paddled on this date? ")
water_body_type = input("What type of body of water is this? "
                        "Is it a beach, lagoon, river, spring, etc.? ")
print()
full_location_name = location_name + " " + water_body_type
f = open(water_body_type, "a+")  # adds to file if exists, creates file if it doesn't exist
print("Sounds great! A new adventure log has been opened for you."
      "\nThe entry is titled", adventure_title + " " + date + " " + str(standard_start_time),
      "and is stored on the file for", water_body_type + ".")
f.write(adventure_title + " " + date + " " + str(standard_start_time))
print()
distance = input("How many miles did you travel on today's trip? ")
f.write(str(print("\n", "Trip summary:", name, "traveled", distance, "miles during the", adventure_title,
                  "trip on", date + ".")))
print()
weather = input("In one word, describe the weather. ")
tide = input("Was it high or low tide when the paddling trip first started? ")
water_clarity = input("Was visibility through the water clear or opaque? ")
wind_direction = input("Were there onshore or offshore winds? ")

f.write(str(print("\n", "Conditions: ", "The", weather, "weather,", wind_direction, "winds, and", tide,
                  "tide contributed greatly to the", water_clarity, "water visibility.")))
# writes conditions to file
print()


def mileage():  # calculates gas price for trip
    total_gas_cost = miles_traveled / miles_per_gallon * gas_price_per_gallon
    f.write(str(print("Mileage: ", "According to my calculations, the total price for gas for this trip"
                      " is ~$", format(total_gas_cost, '.2f') + ".", sep='')))
    return


print("Now that we are familiar with the quality of your trip, "
      "let's record the cost of the trip for budgeting and future reference.")
print("Let's begin with travel costs.")
while True:
    try:
        gas_price_per_gallon = float(input("How much is the price of a gallon of gas "
                                           "in your region in American dollars? "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")
while True:
    try:
        miles_per_gallon = float(input("How many miles does your vehicle travel "
                                       "per gallon of gas consumed? "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")
while True:
    try:
        miles_traveled = float(input("How many miles did you travel in total "
                                     "to and from the paddling location? "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")
# divide the number of miles traveled by the miles the vehicle travels
# per gallon, then multiply by the price of gas
mileage()
print()
# parking cost
print("Another cost that should be taken into account is parking.")
while True:
    try:
        price_per_vehicle = float(input("How much was the flat rate per vehicle "
                                        "to enter the park area? "
                                        "If there was none, enter 0. "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")
while True:
    try:
        price_per_person = float(input("How much was the entrance cost per person "
                                       "to enter the park? If there was none, "
                                       "enter 0. "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")
while True:
    try:
        num_of_people = int(input("How many individuals did you pay "
                                  "the entrance fee for (including yourself)? "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")
while True:
    try:
        price_of_parking_per_HR = float(input("How much was the price of parking per "
                                              "hour per vehicle? If there was none, "
                                              "enter 0. "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")
while True:
    try:
        time_parked = float(input("Roughly, how many hours were you parked "
                                  "at this location? "))
        break
    except ValueError:
        print("I'm sorry. That doesn't seem right. Let's try again!")

total_park_per_person = price_per_person * num_of_people
# 2 types of parking were grouped separately
# and united in the final operation due to multiplication
total_park_per_HR = price_of_parking_per_HR * time_parked
total_parking_cost = price_per_vehicle + total_park_per_person + \
                     total_park_per_HR
f.write(str(print("\n", "Parking & Admission Costs: ", "The total price of parking/admission for a ", time_parked,
                  " hour trip to ", full_location_name, " costs ~$",
                  format(total_parking_cost, '.2f') + ".", sep='')))
print()
notes = input("If you would like to add any notes about today's trip, please do so here. ")
f.write(str(print("\n", "Notes: ", notes)))
print()
sign_log = input("If you would like to complete today's log, please print your initials. ")
date_time = str(datetime.datetime.now())
f.write(str(print("\n", sign_log + " " + date_time)))
print()

close_file = input("Please type in the word close if you could like to close the file. ")

if close_file == "close":
    print("Your file has been saved. See you soon!")
    f.close()
while close_file != "close":
    close_file = input("I'm sorry. I don't think I got that. "
                       "\nPlease type in the word close if you would like me to close the file. ")
    if close_file == "close":
        print("Your file has been saved. See you soon!")
        break
    f.close()
print("<3" * 6)
# multiplying a string repeats it by the number by which it is multiplied
