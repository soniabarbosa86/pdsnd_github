import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello & Welcome! Let\'s explore some US bikeshare data!')
    """Prompt the user to enter which of the cities they would like to see and make it case insensetive as well as while loop to handle invalid inputs"""
    city = input('Which city would you like to see? Chicago, New York City or Washington?:').lower()
    while (city not in ['chicago', 'new york city', 'washington']):
                        print('You have selected a city not valid for selection!')
                        city = input('Which city would you like to see? Chicago, New York City or Washington?: ').lower()
    print('Thank you for your input!')



    """Prompt the user to enter which month they want to see or all and using a while loop to handle invalid inputs"""
    month = input('Which month would you like to see?January, February, March, April, May, June or all?: ').lower()
    while (month not in ['january', 'february', 'march', 'april', 'may', 'june']):
                         print('You have selected a month not valid for selection')
                         month = input('Which month would you like to see?January, February, March, April, May, June or all?: ').lower()

    print('Thank you for your input')


    """Prompt the user to enter which day of the week they they want to see and using a while loop to handle invalid inputs"""
    day = input('Which day of the week would you like to see? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?: ').lower()
    while (day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
        print('You have selected a date not valid for selection')
        day = input('Which day of the week would you like to see? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?: ').lower()
    print('Thank you for your input')

    print('-'*40)
    return city, month, day

"""
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """


def load_data(city, month, day):
     df = pd.read_csv(CITY_DATA[city])
     df['Start Time'] = pd.to_datetime(df['Start Time'])
     df['month'] = df['Start Time'].dt.month
     df['day_of_week'] = df['Start Time'].dt.day_name()

     if month != 'all':
         months = ['january', 'february', 'march', 'april', 'may', 'june']
         month = months.index(month) + 1

     df = df[df['month'] == month]

     if day != 'all':
         df = df[df['day_of_week'] == day.title()]

     return df











def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """Extracting month from the Start Time column to create a month column and display which month is most common"""

    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month is:', common_month)

    """Extracting weekday name from the Start Time column to create a weekday column and display which day is most common"""
    df['weekday'] = df['Start Time'].dt.day_name()
    common_day_week = df['weekday'].mode()[0]
    print('Most common day of the week is:', common_day_week)


    """converting the string data to Python date time and extracting the hour from the Start Time column to create an own column. Using .mode function to calculate the most common start hour"""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour is:', common_start_hour)





    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    """Calculating which start station appears most times in the Start Station column"""
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station is: ', most_common_start_station)

    """Calculating which end station appears most times in the End Station column"""
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('Most common end station is: ', most_common_end_station)

    """Grouping the most popular Start and End stations and calulating which combinations are most popular"""
    most_common_combinations = df.groupby(['Start Station', 'End Station']).count()
    print('Most frequent start station and end station: ', most_common_start_station, 'and', most_common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """Calculating the total sum from the Trip Duration column in seconds and converting to days"""
    total_travel_time = df['Trip Duration'].sum()
    conversion = datetime.timedelta(seconds=total_travel_time)
    print('Total Travel Time is: ', conversion)


    """Calculating the mean travel time from the Trip Duration column in seconds and converting to days"""
    mean_travel_time = df['Trip Duration'].mean()
    conversion = datetime.timedelta(seconds=mean_travel_time)
    print('The mean travel time is: ', conversion)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    """Calulating the amount of user types from the User Type column"""
    user_types = df['User Type'].value_counts()
    print('Amount of user types: ', user_types)

    """Calculating the amount of genders from the Gender column and using a try statement to handle any errors. In this case Washington does not have Gender"""
    try:
        print('Amount of genders: ')
        count_genders = df['Gender'].value_counts()
        for count_gender in count_genders.index:
            print(count_gender, ":", count_genders[count_gender])
    except:
        print('Gender data is not available')




    """Display the earliest, recent and most common year of birth from the Birth Year column. Applying a try statement for error handling as the Washington data
    does not include data for Birth Year"""

    try:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mean()

        print('Earliest year of birth is: ', earliest_birth_year)
        print('Most recent birth year is: ',recent_birth_year)
        print('Most common year of birth is: ', common_birth_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print('Gender data is not available')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)



        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        """Prompting the user to answer if they want to see the first 5 rows of data and continue to iterate these promts in order to show additional 5 rows until
        the user says no or there is no more data to show"""
        data_results = input('Would you like to see the first 5 rows of data? Answer yes or no: ').lower()
        start_location = 0
        while data_results == 'yes':
             print(df.iloc[start_location:start_location+5])
             start_location += 5
             data_results = input('Would you like to see additional 5 rows of data? Answer yes or no: ').lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
