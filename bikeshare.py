import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze - like " chicago, new york city, and washington"
        (str) month - name of the month to filter by, or "all" to apply no month filter at all
        (str) day - name of the day of week to filter by, or "all" to apply no day filter at all
    """
    print('Hello Welocome! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for chicago, new york city, or washington. Type city name, like- chicago.?")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("You have just entered invalid input. Please enter a valid input, like - chicago, new_york_city or washington")

    # get user input for month (all, january, february, march, april, may, and  june)

    while True:
        month = input("Would you like to filter by month? If yes, type month name from within january through june, else type 'all'")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("You entered invalid input. Please, enter a valid input, like - january, february, march, april, may, june")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to filter by day? If yes, type day name within monday through sunday, else type 'all'")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("You enetered invalid input. Please enter a valid input, like monday, tuesday, wednesday, thursday,...")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is ", df['month'].mode()[0], "\n")

    # display the most common day of week
    print("The most common day of week  is ", df['day_of_week'].mode()[0], "\n")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")

    # display most commonly used end station
    print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # display mean travel time
    print("The total mean time is", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != 'washington':
        # Display counts of gender
        gender = df.groupby(['Gender'])['Gender'].count()
        print(gender)
        # Display earliest, most recent, and most common year of birth
        most_recent_yob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        earliest_yob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        most_common_yob = df['Birth Year'].mode()[0]
        print("The earliest year of birth is ", earliest_yob, "\n")
        print("The most recent year of birth is ", most_recent_yob, "\n")
        print("The most common year of birth is ", most_common_yob , "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
