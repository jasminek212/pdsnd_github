import time
import pandas as pd
import numpy as np

#creates references for different city data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# Gets user input for their choice of city, month, and day 
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to explore data from Chicago, New York City, or Washington? (Input is Case Sensitive) ' ).lower()
        if city in CITY_DATA:
            break
        else:
            print("Sorry, you entered an invalid city. Please choose only from Chicago, New York City, and Washington. ")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to explore data from a specific month from January - June, or all? ').lower()
        if month in ['january','february','march','april','may','june','all']:
            break
        else:
            print("Sorry, you entered an invalid month. Please choose only months from January to June, or enter ALL. ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to explore data from a specific day of the week, or all? ').lower()
        if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            break
        else:
            print("Sorry, you entered an invalid day. Please choose a specific day of the week, or enter ALL. ")

    print('-'*40)
    return city, month, day

# Loads the data needed for the user chosen city
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['DOW'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['DOW'].str.lower() == day]
                                          
    return df

# Calculates time and date specific based on user input
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['January', 'February', 'March', 'April', 'May', 'June']
    # TO DO: display the most common month
    common_month= months[df['Month'].mode()[0] -1]
    print(f"The most common month is {common_month}!")                                   

    # TO DO: display the most common day of week
    common_day= df['DOW'].mode()[0]
    print(f"The most common day is {common_day}!")  

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Hour'].mode()[0]
    if common_start_hour > 12:
        TOD = "PM"
        hour = common_start_hour - 12
    elif common_start_hour < 12:
        TOD = "AM"
        hour = common_start_hour
    else:
        TOD = "PM"
        hour = common_start_hour
        
    print(f"The most common start hour is {hour}{TOD}")
    
    # TO DO: display the least common start hour
    least_start_hour = df['Hour'].value_counts().idxmin()
    if least_start_hour > 12:
        TOD_least = "PM"
        hour_least = least_start_hour - 12
    elif least_start_hour < 12:
        TOD_least = "AM"
        hour_least = least_start_hour
    else:
        TOD_least = "PM"
        hour_least = least_start_hour
        
    print(f"The least common start hour is {hour_least}{TOD_least}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Get station statistics based on user input
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print(f"""The most common start station is "{common_start_station}".""")  

    # TO DO: display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print(f"""The most common end station is "{common_end_station}".""")  

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combo'] = df['Start Station'] + " + " + df['End Station']
    common_combo_station= df['Station Combo'].mode()[0]
    print(f"""The most common combination of start and end stations is "{common_combo_station}".""")  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Get trip duration statistics based on user input
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time= df['Trip Duration'].sum()
    no_of_hours = tot_travel_time // 3600
    no_of_mins = (tot_travel_time % 3600) // 60
    print(f"The total travel time is {no_of_hours} hour(s) and {no_of_mins} minute(s).")  

    # TO DO: display mean travel time
    avg_travel_time= int(df['Trip Duration'].mean())
    no_of_hour = avg_travel_time // 3600
    no_of_min = (avg_travel_time % 3600) // 60
    print(f"The average travel time is approximately {no_of_hour} hour(s) and {no_of_min} minute(s).") 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Prints all statistics gathered based on user input
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_count= df['User Type'].value_counts().to_string()
    print(f"Counts of User Types:\n{type_count}\n")  

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
          gender_count = df['Gender'].value_counts().to_string()
          print(f"Counts of Gender:\n{gender_count}")
    else:
          print('No gender data available')
          

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
          earliest_year = int(df['Birth Year'].min())
          latest_year = int(df['Birth Year'].max())
          common_year = int(df['Birth Year'].mode()[0])
          print(f"\nThe earliest birth year is {earliest_year}")
          print(f"The most recent birth year is {latest_year}")
          print(f"The most common birth year is {common_year}")
    else:
          print("No birth year data is available")
                            
               

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Allows user to choose to run another query 
def display_data(df):
    start = 0
    first_question = True
    
    while True:
        if first_question:        
            user_choice = input("\nDo you want to see 10 rows of raw data? ").lower()
            first_question = False
        else:
            user_choice = input("\nDo you want to see 10 more rows of raw data? ").lower()
            
        if user_choice != 'yes':
            break
            
        print(df.iloc[start:start + 10])
        start += 10
        
        if start >= len(df):
            print("\nNo more data to show.")
            break
# Deploys entire script
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
