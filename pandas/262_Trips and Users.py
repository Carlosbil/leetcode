import pandas as pd
"""
trips: trip_id, client_id, driver_id, city_id, status, request_at
id is the primary key (column with unique values) for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').

users: users_id, banned, role
users_id is the primary key (column with unique values) for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM (category) type of ('Yes', 'No')
"""
def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # remove trips that are not .between('2013-10-01','2013-10-03')
    trips = trips[trips['request_at'].between('2013-10-01','2013-10-03')]
    # merge both dataframe saving employee, dept
    trips_with_user_info = pd.merge(trips, users, left_on='client_id', right_on='users_id')
    trips_with_driver_info = pd.merge(trips, users, left_on='driver_id', right_on='users_id')

    # no banned trips
    unbanned_trips = trips_with_user_info[trips_with_user_info['banned'] == 'No']
    unbanned_trips_with_driver = trips_with_driver_info[trips_with_driver_info['banned'] == 'No']

    # no banned trips (merge unbaned trips with unbanned driver, only keep trips with unbanned driver)
    unbanned_trips = pd.merge(unbanned_trips, unbanned_trips_with_driver, left_on='request_at', right_on='request_at')

    # assumem that cancelled_by_driver and cancelled_by_client are the same
    unbanned_trips['cancelled'] = unbanned_trips['status_x'] != 'completed'

    # group by day and calculate the mean
    daily_cancellation_rates = unbanned_trips.groupby('request_at')['cancelled'].agg(['mean']).reset_index()

    # rename columns
    daily_cancellation_rates.columns = ['Day', 'Cancellation Rate']
    daily_cancellation_rates['Cancellation Rate'] = daily_cancellation_rates['Cancellation Rate'].round(2)

    # if day is not 
    return daily_cancellation_rates
