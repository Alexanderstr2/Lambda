# Imports
import requests
import json
import csv


#Global Varibles
rentFasterURL = "https://www.rentfaster.ca/api/map.json?e=undefined&beds=&baths=&type=&price_range_adv%5Bfrom%5D=&price_range_adv%5Bto%5D=&area="
csvFilePath = '/Users/alexanderstratmoen/Documents'
csvFileName = 'datafile'

longLeft = '50.90397819717543'
longRight = '51.18725531061486'
latLeft = '-114.3877763892578'
latRight = '-113.72722341074217'




# Settings Menu
def settings():
    global rentFasterURL
    global longLeft
    global longRight
    global latLeft
    global latRight
    global csvFilePath
    global csvFileName

    # loop

    while True:
        print("Settings")
        print("----------------------------------------------")
        print("Enter option #:")
        print("1) Specify area to pull from")
        print("2) Edit CSV File Path")
        print("3) Advanced")
        print("4) Exit")
        setting_in = input()
        if setting_in == '1':
            print("To change bounding box for listings enter bounds for Longitude and Latitude:")
            longLeft = input("Enter Longitude Left Bound: ")
            longRight = input("Enter Longitude Right Bound: ")
            latLeft = input("Enter Latitude Left Bound: ")
            latRight = input("Enter Latitude Right Bound: ")

        elif setting_in == '2':
            csvFilePath = input("Enter Path: ")
            csvFileName = input("Enter File Name: ")

        elif setting_in == '3':
            while True:
                print("Advanced Settings")
                print("----------------------------------------------")
                print("Enter option #:")
                print("1) Change Rent Faster URl")
                print("2) Exit")
                setting_adv_in = input()
                if setting_adv_in == '1':
                    if input("Danger, this can break program, are you sure you want to proceed? (Y/N): ") == 'Y':
                        print("Current URL: " + rentFasterURL)
                        rentFasterURL = input("Enter new URL: ")

                elif setting_adv_in == '2':
                    break
                else:
                    print("Invalid Input")

        elif setting_in == '4':
            return
        else:
            print("Invalid Input")
# Scrape
def webScrape():
    global rentFasterURL
    global longLeft
    global longRight
    global latLeft
    global latRight
    global csvFilePath
    global csvFileName

    print("Pulling site JSON...")
    site = requests.get(rentFasterURL + longRight + '%2C' + latRight + '%2C' + longLeft + '%2C' + latLeft)

    print("Parsing...")
    parse = json.loads(site.text)
    listings = parse['listings']

    # Adding Riding Validation soon


    # Cleaning Data

    for listing in listings:
        listing.pop("availability", None)
        listing.pop("ref_id", None)
        listing.pop("id", None)
        listing.pop("userId", None)
        listing.pop("phone", None)
        listing.pop("phone_2", None)
        listing.pop("email", None)
        listing.pop("rented", None)
        listing.pop("a", None)
        listing.pop("v", None)
        listing.pop("f", None)
        listing.pop("s", None)
        listing.pop("title", None)
        listing.pop("marker", None)
        listing.pop("link", None)
        listing.pop("thumb2", None)
        listing.pop("preferred_contact", None)
        listing.pop("price", None)
        listing.pop("price2", None)
        listing.pop("beds", None)
        listing.pop("beds2", None)
        listing.pop("sq_feet", None)
        listing.pop("sq_feet2", None)
        listing.pop("cats", None)
        listing.pop("dogs", None)
        listing.pop("utilities_included", None)
        listing.pop("baths", None)
        listing.pop(" ", None)

    # File Writing

    print("Writing File...")
    path = csvFilePath + '/' + csvFileName + '.csv'
    print("Data Path: "+path)
    data_file = open(path, 'w')

    csv_writer = csv.writer(data_file)
    count = 0

    for listing in listings:
        if count == 0:
            # Writing headers
            header = ['address', 'city', 'community', 'latitude', 'longitude', 'type']
            csv_writer.writerow(header)
            count += 1

        # Writing data
        csv_writer.writerow(listing.values())

    data_file.close()

# Main Menu

print("Disclaimer:")
print("----------------------------------------------")
print("Only webscrape with premission from the website owner. Running this script and/or program may violate terms and conditions of websites,"
          "code is provided for educational purposes only. The uses takes al responsibility over ensuring their use of this tool complies with website terms"
          " and all applicable laws and regulations.")
print("----------------------------------------------")
while True:
    print("Lambda Version 0.1")
    print("----------------------------------------------")
    print("Enter option #:")
    print("1) Settings")
    print("2) Scape")
    print("3) Exit")
    main_in = input()
    if main_in == '1':
        settings()
    elif main_in == '2':
        webScrape()
    elif main_in == '3':
        break
    else:
        print("Invalid Input")
