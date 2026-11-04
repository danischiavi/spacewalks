import matplotlib.pyplot as plt
import pandas as pd

# ==============================
# Utility functions
# ==============================

# Read in and parse a json file. Formattinf data and float cols and dropping records with missing data
def read_json_to_dataframe(json_file):
    df = pd.read_json(json_file, convert_dates=['date'], encoding='ascii')
    df['eva'] = df['eva'].astype(float)
    df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return(df)    

# writes out the csv
def write_dataframe_to_csv(df, csv_file):
    df.to_csv(csv_file, index=False, encoding='utf-8')
    return f"file save to {csv_file}"

# Modify input data. Make a copy. Modify the copy. Return the copy. 
def add_duration_hours(df):
    df_copy = df.copy()
    df_copy["duration_hours"] = df_copy["duration"].apply(text_to_duration)
    return df_copy

# if input == 10:00 , output should be 10.00
def text_to_duration(duration): 
    hours, minutes = duration.split(":")
    duration = int(hours) + int(minutes)/60  
    return duration


# Plot the cumulative
def plot_cumulative_time_in_space(df, png_file):
    df.sort_values('date', inplace=True)
    df = add_duration_hours(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(png_file)
    plt.show()


# =============================
# Main logit 
# ================================

# Define the data
# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./data/eva-data.json', 'r', encoding='ascii')
output_file = open('./data/eva-data.csv', 'w', encoding='utf-8')
graph_file = './results/cumulative_eva_graph.png'


# read in and parse 
eva_df = read_json_to_dataframe(json_file = input_file)

# save data
write_dataframe_to_csv(df = eva_df, csv_file = output_file)

# plot 
plot_cumulative_time_in_space(df = eva_df, png_file= graph_file)



# if __name__ == "__main__":

#     input_file = './eva-data.json'
#     output_file = './eva-data.csv'
#     graph_file = './cumulative_eva_graph.png'
#     main(input_file, output_file, graph_file)
