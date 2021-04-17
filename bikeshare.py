import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid

    city = ''
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input('Please enter a city from chicago, new york city or washington\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    month = ''
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('specify a month from all, january, february, march, april, may, june\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'saturday', 'sunday', 'all']:
        day = input('specify a day from : monday, tuesday, wednesday, thursday, saturday, sunday or all\n').lower()

    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city.lower()])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    if month.lower() != 'all':
        months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
        df = df[df['month'] == months[month.lower()]]
    if day.lower() != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    freq_month = df['month'].mode()[0]
    print('The most common month is ' + str(freq_month))
    # TO DO: display the most common day of week
    freq_day = df['day'].mode()[0]
    print('The most common day is  ' + freq_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    start_hour = df['hour'].mode()[0]
    print('The most common start hour is  ' + str(start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station used is ' + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station used is ' + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["stations_combination"] = df["Start Station"] + '-' + df["End Station"]
    frequent_combination = df['stations_combination'].mode()[0]
    print('the most common frequent of start station and end station trip is  ' + frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time : ' + str(total_travel_time) + '\n')
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time : ' + str(mean_travel_time) + '\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types :')
    print(user_types)

    # TO DO: Display counts of gender
    if city.lower() == 'chicago' or city.lower() == 'new york city':
        gender_type = df['Gender'].value_counts()
        print('counts of gender :')
        print(gender_type)
    else:
        print(city.lower() + " has no gender data")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city.lower() == 'chicago' or city.lower() == 'new york city':
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print('the earliest year of birth : ' + str(earliest))
        print('the recent year of birth : ' + str(recent))
        print('the most common year of birth  :' + str(common))
    else:
        print(city.lower() + " has no birth date data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    while view_data.lower() not in ['yes','no']:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    else:
        start_loc = 0
        while view_data == 'yes':
            if start_loc == 0:
                print(df.head())
                start_loc += 5
            else:
                print(df.iloc[start_loc:start_loc + 6])
                start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()








def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
