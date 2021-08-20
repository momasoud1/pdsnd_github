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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('enter a valid city: chicago,new york city,washington\n').lower()
    while (city not in ['chicago','new york city','washington']):
        city = input('Please enter a valid city: chicago,new york city,washington\n')
        if city not in  ['chicago','new york city','washington']:
            print ('Re enter the right selection\nfrom chicago,new york city,washington ' )
    print(f'you have selected {city.title()}')

    # get user input for month (all, january, february, ... , june)
    month_format={'january': 1, 'february': 2, 'march': 3,'april': 4, 'may': 5, 'june': 6, 'all' : 7}
    month= input('enter a valid month : january,february,.....,june Or set all for all months\n').lower()
    while month not in month_format.keys():
        month = input('Please enter a valid month like : january , february ,...\n')
        if month not in month_format.keys():
            print('Re enter the right selection')
    print(f'you have selected {month.title()}')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('enter a valid day : saturday,sunday,monday,tuesday,wednesday,thursday,friday,all\n').lower()
    while (day not in ['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']):
        day=input('Please enter a valid day like : sunday,monday , tuesday ,...,all\n' )
        if day not in ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']:
            print('Re enter the right selection\nsaturday,sunday,monday,tuesday,wednesday,thursday,friday,all')
    print(f'you have selected {day.title()}')

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
    # load city from city_data and set it in dataframe
    df= pd.read_csv(CITY_DATA[city])
    # convert start time column to date time
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #from start time column extract month and day columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
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
    popular_month=df['month'].mode()[0]
    print(f'The most common month : {popular_month} ')

    # display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print(f'The most common day : {popular_day}')

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print(f'The most common hour : {popular_hour}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_staion=df['Start Station'].mode()[0]
    print(f'The most common start station : {popular_start_staion}')

    # display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print(f'The most common end station : {popular_end_station}')

    # display most frequent combination of start station and end station trip
    popular_start_end_station=(df['Start Station'] +''+df['End Station']).mode().values[0]
    print(f'The most frequent combination of start station and end station trip : {popular_start_end_station} ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print(f'The total travel time : {total_travel_time/60} minutes')

    # display mean travel time
    mean_travel_time= round(df['Trip Duration'].mean())
    print(f'The average travel time : {mean_travel_time/60} minutes')



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type=df['User Type'].value_counts()
    print(f'The Counts of user types : {count_user_type}')

    # Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print(f'The counts of gender : {counts_of_gender}')
    except:
        print('Gender : No data found to display')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print( f'The earliest birth year :{earliest_year_of_birth}\nThe newest birth year : {most_recent_year_of_birth}\nThe most common birth year :{most_common_year_of_birth}')
    except:
        print('Birth year : No data found to display')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   #display 5 rows of the raw data

def show_raw_data(df):
    """" Displaying 5 rows of the raw data for more information """
    user_entry = input('\n would you like to see first 5 rows of the data\n please enter yes or no\n').lower()
    if user_entry in ('yes', 'YES', 'y', 'Y'):
        i=0
        while True:
            print(df.iloc[i:i + 5])
            i += 5
            addetional_inquiry = input('would you like to see more data ? please enter yes or no\n').lower()
            if addetional_inquiry in ('yes', 'YES', 'y', 'Y','ye','YE'):
                continue
            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        df= load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

