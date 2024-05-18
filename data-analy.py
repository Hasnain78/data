import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

b = pd.read_csv(r'/content/fact_bookings.csv')
d = pd.read_csv(r'/content/dim_date.csv')
t = pd.read_csv(r'/content/fact_aggregated_bookings.csv')
h = pd.read_csv(r'/content/dim_hotels.csv')
r = pd.read_csv(r'/content/dim_rooms.csv')

df = b.merge(h, on='property_id').merge(d, left_on='check_in_date', right_on='date')

total_revenue = df['revenue_realized'].sum()
print(f'Total Revenue: {total_revenue}')

total_bookings = df['booking_id'].count()
print(f'Total Bookings: {total_bookings}')

average_rating = df['ratings_given'].mean()
print(f'Average Rating: {average_rating}')

total_capacity = t['capacity'].sum()
print(f'Total Capacity: {total_capacity}')

total_successful_bookings = t['successful_bookings'].sum()
print(f'Total Successful Bookings: {total_successful_bookings}')

occupancy_percentage = (total_successful_bookings / total_capacity) * 100
print(f'Occupancy Percentage: {occupancy_percentage:.2f}%')

total_cancelled_bookings = df[df['booking_status'] == 'Cancelled']['booking_id'].count()
print(f'Total Cancelled Bookings: {total_cancelled_bookings}')

cancellation_rate = (total_cancelled_bookings / total_bookings) * 100
print(f'Cancellation Rate: {cancellation_rate:.2f}%')

weekly_data = df.groupby('week no').agg({'revenue_realized': 'sum', 'booking_id': 'count'})
weekly_data.plot(y=['revenue_realized', 'booking_id'], kind='line')
plt.title('Trends by Week')
plt.xlabel('Week Number')
plt.ylabel('Values')
plt.show()

plt.pie(df['booking_platform'].value_counts()*100, autopct='%1.2f%%')
plt.title('Booking % by Platform')
plt.ylabel('')
plt.show()