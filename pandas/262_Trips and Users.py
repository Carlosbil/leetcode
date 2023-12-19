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
    # Filter trips for the specified date range
    trips = trips[trips['request_at'].between('2013-10-01', '2013-10-03')]

    # Merge the trips with user information for clients
    trips_with_users = pd.merge(trips, users, left_on='client_id', right_on='users_id')

    # Merge the trips with user information for drivers
    trips_with_users = pd.merge(trips_with_users, users, left_on='driver_id', right_on='users_id', suffixes=('_client', '_driver'))

    # Filter out trips where either the client or the driver is banned
    unbanned_trips = trips_with_users[(trips_with_users['banned_client'] == 'No') & (trips_with_users['banned_driver'] == 'No')]

    # Mark trips as cancelled if their status is not 'completed'
    unbanned_trips['cancelled'] = unbanned_trips['status'] != 'completed'

    # Group by request date and calculate the mean cancellation rate
    daily_cancellation_rates = unbanned_trips.groupby('request_at')['cancelled'].mean().reset_index()

    # Rename columns and round the cancellation rate to two decimal places
    daily_cancellation_rates.columns = ['Day', 'Cancellation Rate']
    daily_cancellation_rates['Cancellation Rate'] = daily_cancellation_rates['Cancellation Rate'].round(2)

    return daily_cancellation_rates
