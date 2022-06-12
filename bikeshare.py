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
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington)
    while True:
        city = input ('please choose a city from chicago , new york city or washington: ').lower()
        if city not in CITY_DATA:
            print('Invalid input.please enter the correct city from chicago , new york city or washington: '.lower())
        else:
            break
                
    
    # get user input for month (all, january, february, ... , june)
    while True:
        months= ['january','february','march','april','may','june','all']
        month = input ('Please choose a month from (January, February, March, April, May, June) or choose (all)to get results for all months: ').lower()
        if month in months:
            break
        else:
            print('Invalid input.Please enter the correct month from (January, February, March, April, May, June) or choose (all)to get results for all months: '.lower())
            
                
    #  get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
        day = input('Please choose a day or choose (all) to get results for all days: ').lower()
        if day in days:
            break
        else:
            print ('Invalid input,Please choose a day or choose (all) to get results for all days: '.lower())
            
        
   

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
    # loading the data file to a DataFrame
    df  = pd.read_csv(CITY_DATA[city])

    # converting the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting the month, day of week and hour from start time and create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by months
    if month != 'all':
        #use the index of the month to get the month number
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #creating DataFrame
        df = df[df['month'] == month]

    #filter by day 
    if day != 'all':
        #creating DataFrame
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('the most common month is: ', most_common_month)


    #  display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('the most common day of week is: ', most_common_day)


    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('the most common start hour of day is: ', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commo_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', most_commo_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', most_common_end_station)


    # display most frequent combination of start station and end station trip
    most_common_start_end_route = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print ('The most common start-end route is: ', most_common_start_end_route)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    total_travel_time = df['Trip Duration'].sum() / 3600
    print ('the total travel time is: ',total_travel_time,'hours')

    # display mean travel time
    mean_trvael_time = df['Trip Duration'].mean() / 3600
    print ('the mean travel time is: ',mean_trvael_time,'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df['User Type'].value_counts()
    print('The user types are: ' ,user_types)



    #  Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('the count of gender is: ',gender_count)
        


    #  Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print('The earliest year is: ',earliest_year)

        most_recent_year = df['Birth Year'].max()
        print('The most recent year is: ',most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print('The most common year is: ',most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(df):
    """Displays raw data as per user request."""

    
    x = 0
    user_request = input('would you like to see the first 5 rows of data? please enter yes or no: ').lower()
    while True:
        if user_request == 'no':
            break
        print(df[x:x+5])
        user_request = input('would you like to see the next 5 rows of data? please enter yes or no: ').lower()
        x +=5




def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()
         
