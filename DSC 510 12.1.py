# Purpose: To create a program which will tell the user the weather based on city or zip code entered
# Assignment Number: 12.1
# Name: Zachary DeNoto

# imports json and requests
import requests

# function that uses an input from user to see if zip code or city was entered
def get_area(user_input):

    # sees if zip code was entered, returns zip code
    if len(user_input) == 5 and user_input.isdigit():
        zip = user_input
        return zip

    # sees if number was entered for zip code but incorrectly typed in, lets user try again to input zip, city, or exit
    elif len(user_input) != 5 and user_input.isdigit():
        return get_area(input('You have entered an invalid zip code. Please enter a valid zip code, enter a city instead or type exit to exit the program: '))

    # sees if user wants to exit, if so will end program
    elif user_input.upper() == 'EXIT':
        end_program()

    # if the input is a the city (not numbers) and returns city
    else:
        city = user_input
        return city

# function to determine if connection to openweathermap.com works or not
def connection(url):

    # try statement to connect to the api, prints message and exits if there is a problem
    try:

        # uses requests to GET the information back from the url
        response = requests.request('GET', url)

        # prints message to user that connection was successful if connection is successful
        if response.status_code == 200:
            print('\nYour connection was successful!')

        # prints message to user that connection was not successful if connection is not successful
        else:
            print('\nYour connection was not successful.')

    # prints message if there is a problem with the connection and exits
    except:
        print('There was a problem with the website. Please try again at a later time. Sorry for the inconvenience.')
        exit()

# function that takes the url of the openweathermap website and displays the weather in a nice format for the user
def display_weather(url):

    # gets the data from the url and saves it as variable
    response = requests.request('GET', url)

    # formats the data into json format
    dict = response.json()

    # sifts through the json format data to get the location name, weather description, temperatures
    for k, v in dict.items():
        if k == 'name':
            name= v
        elif k == 'weather':
            for x,y in v[0].items():
                if x == 'description':
                    descrip = y
        elif k == 'main':
            for x, y in v.items():
                if x == 'temp':
                    temp = y
                elif x == 'temp_min':
                    min_temp = y
                elif x == 'temp_max':
                    max_temp = y
                else:
                    pass
        else:
            pass

    # prints the weather in a nice format for the user based on the data
    print('\nWeather in {}\n---------------------\nCurrent Weather: {}\nCurrent Temperature: {}°F '\
          '\nMax Temperature: {}°F \nMin Temperature: {}°F'.format(name,descrip,round(temp),round(max_temp),round(min_temp)))

# ends the program by displaying a message to the user and exiting
def end_program():
    print('\nThank you for user the weather program. Come back soon!')
    exit()

# prints a welcome message to the user
def intro():
    print('Welcome to the Weather Forecast Program!\n')

# main function to loop and allow the user to enter a zip or city to get the weather
def main():

    # calls intro to display welcome message to user
    intro()

    # variable to keep loop going
    keep_going = True

    # while loop to allow the user to keep seeing the weather
    while keep_going:

        # asks the user for input and saves value as variable
        user_input = input('\nPlease type in a zip code or city. Type in exit to end program: ')

        # users input is checked to see if they are trying to exit
        if user_input.upper() =='EXIT':
            end_program()

        # sets variable area to return value from get_area function using users input as the parameter
        area = get_area(user_input)

        # try statement to set the url based on area user input, displays if connection was successful or not and displays weather in nice format
        try:
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Imperial&appid=b113d0d8b55fc09fcee342931907c51a'.format(area)
            connection(url)
            display_weather(url)

        # if the user enters in a city that cannot be found, displays message to user and allows them to try again or exit
        except:
            print('You have entered in invalid city. Pleases enter a valid city, zip code or instead type exit to exit the program: ')


# calls the main function
main()