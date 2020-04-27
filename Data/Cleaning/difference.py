import pandas as pd

complete_csv = "./all_details.csv"
location_csv = "./output.csv"
output_csv = "./remaining.csv"

complete_df = pd.read_csv(complete_csv)

location_df = pd.read_csv(location_csv, header=None)

location_df.rename(columns={0: "ImageFileName"}, inplace=True)

final_df = complete_df[~complete_df["ImageFileName"].isin(list(location_df["ImageFileName"]))]

final_df.to_csv(output_csv, header=False,index=False)
