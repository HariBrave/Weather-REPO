# Final Progamming project for Intro to Programming
# Creating a program that connects a user to openweathermap.org
# For making get requests

import requests

# The method fetches the wetaher data and returns the result

def fetch_data(zip=None, city=None):

    # Base url for fetching the weathre

    baseUrl = "http://api.openweathermap.org/data/2.5/weather"

    # api id for the site

    apiid = "007ca4068eadec0dc0bc4c6adfe6f3f5"

    # Check if the suer gave the zip code or the city name

    if zip is not None:

        # us at the end id for usa country , change it as required

        baseUrl += "?zip="+str(zip)+",us"

    else:

        baseUrl += "?q="+str(city)+",us"

    # Finally append the api id

    baseUrl += "&appid="+str(apiid)

    # Make get requetss using requests module

    r = requests.get(baseUrl)

    # Return the response

    return r

# This method shows the result in readbale format,

def showResult(resp):

    # This means request was successfull

    if resp.status_code == 200:

        data= resp.json()

        print(data['name'])

        print(f"""{data['name']} Weather Forecast:

        There will be {data['weather'][0]['description']} with wind speed of {data['wind']['speed']}.

        Visibility will be {data['visibility']}.

        Min. Temp will be {data['main']['temp_min']} and max will be {data['main']['temp_max']}.

        """)

    else:

        print("Request Failed, Try Again Error Code : ",resp.status_code)

# Main method , main drive rcode of teh progra,

def main():

    # Until the user exits, keep running the code

    while True:

        # Show the user choices

        inp =int(input("-----WELCOME TO THE WEATHER MAP-----\nChoose how you want to search\n1. By Zip Code\n2. By City Name\n3. Exit\n"))

        if inp == 1:

            # Ask for zip code

            try:

                queryData=int(input("Enter zip code : "))

                #mak call to fetch fetch_data

                resp= fetch_data(queryData,None)

                showResult(resp)

            except Exception as ex:

                print("Error : ",ex)

        elif inp == 2:

            try:

                queryData = input("Enter city name : ")

                # Make call to fetch fetch_data

                resp= fetch_data(None,queryData)

                showResult(resp)

            except Exception as ex:

                print("Error : ",ex)

        elif inp==3:

            break

        else:

            print("Invalid Choice..\n")




if __name__=="__main__":

    # Call the main function

    main()
