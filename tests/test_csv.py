import os
import json

from IPython.display import display

import pandas as pd

from output.output_list import OutputList

def test_csv(args):
    if (args.season):
        raise TypeError("Seasons are unsupported by csv tester.")
    csv_outputs = OutputList.get_csv_outputs()

    series_df = pd.DataFrame()
    
    for csv in csv_outputs:
        filename = csv.get_debug_filename()

        series_files = os.scandir(args.series)

        for i, file in enumerate(series_files, 1):
            if file.is_file():
                continue

            

            json_file_name = f"{file.path}\\{filename}"
            js = json.load(open(json_file_name, mode="r"))

            df = csv.generate_game_dataframe(js)

            if i == 1:
                series_df = df.copy(True)
            else:
                series_df = df.add(series_df, fill_value=0.0)

            display(df)
            # df.to_csv(f"{file.path}\\{csv.get_output_name()}")
        series_df = csv.calculate_shot_pct(series_df)
        display(series_df)


