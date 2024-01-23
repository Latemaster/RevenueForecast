import pandas as pd
from datetime import datetime

# Read the CSV file into a DataFrame
load_file = input("file name:")
listing_data = pd.read_csv(load_file)

monhtly_cost = float(input("Cost estimate:"))


# Filter rows where "Revenue" is not equal to 0
filtered_data = listing_data[listing_data["Revenue"] != 0]

# Drop unnecessary columns from the filtered DataFrame
filtered_data.drop(columns=['Units', 'No. Booked', 'No. Blocked', 'Blocked Units', 'Bookable Units'], inplace=True)

# Reset the index of the filtered DataFrame
filtered_data.reset_index(drop=True, inplace=True)

# Print the filtered DataFrame
#save_file = input("save to file:")
print(filtered_data)

total_revenue = filtered_data["Revenue"].sum()
avg_revenue = filtered_data["Revenue"].mean()

print(total_revenue, avg_revenue)
season_succes = [0, 0, 0, 0]
season_count = [0, 0, 0, 0]

today = datetime.now()

cur_year = today.year
cur_month = today.month

month_num = {
    "Jan": 0, 
    "Feb": 1,
    "Mar": 2,
    "Apr": 3, 
    "May": 4, 
    "Jun": 5,
    "Jul": 6,
    "Aug": 7,
    "Sep": 8,
    "Oct": 9,
    "Nov": 10,
    "Dec": 11
}

monthly_revenue = {
"Jan": 0, 
    "Feb": 0,
    "Mar": 0,
    "Apr": 0, 
    "May": 0, 
    "Jun": 0,
    "Jul": 0,
    "Aug": 0,
    "Sep": 0,
    "Oct": 0,
    "Nov": 0,
    "Dec": 0}

month_count = [0,0,0,0,0,0,0,0,0,0,0,0]

for datapoint in filtered_data.itertuples():   
    if cur_year > datapoint.Year or (cur_year == datapoint.Year and cur_month >= month_num[datapoint.Month]):
        monthly_revenue[datapoint.Month] += datapoint.Revenue
        month_count[month_num[datapoint.Month]] += 1
        if datapoint.Month == "Dec" or datapoint.Month == "Jan" or datapoint.Month == "Feb":
            season_count[0] += 1
            season_succes[0] += datapoint.Revenue
        elif datapoint.Month == "Mar" or datapoint.Month == "Apr" or datapoint.Month == "May":
            season_count[0] += 1
            season_succes[1] += datapoint.Revenue
        elif datapoint.Month == "Jun" or datapoint.Month == "Jul" or datapoint.Month == "Aug":
            season_count[0] += 1
            season_succes[2] += datapoint.Revenue
        elif datapoint.Month == "Sep" or datapoint.Month == "Oct" or datapoint.Month == "Nov":
            season_count[0] += 1
            season_succes[3] += datapoint.Revenue
        print(datapoint.Month)

  
Average_monthly_revenue_season = [0, 0, 0, 0]


yearly_profit_forecast = {"conservative": 0, "normal": 0, "Positive": 0 }

for i in range(len(season_succes)):
    if season_count[i] > 0:
        Average_monthly_revenue_season[i] = round(season_succes[i]/season_count[i])

for key in monthly_revenue:
    if month_count[month_num[key]-1] > 0:
        monthly_revenue[key] =  monthly_revenue[key]/month_count[month_num[key]-1]
        yearly_profit_forecast["conservative"] += (monthly_revenue[key]*0.8 - monhtly_cost)
        yearly_profit_forecast["normal"] += (monthly_revenue[key] - monhtly_cost)
        yearly_profit_forecast["Positive"] += (monthly_revenue[key]*1.2 - monhtly_cost)

print("Average Monthly Revenue:", monthly_revenue)

print(yearly_profit_forecast)