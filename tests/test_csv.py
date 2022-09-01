import os
import json

from output.output_list import OutputList

def test_csv(args):
    if (args.season):
        raise TypeError("Seasons are unsupported by csv tester.")
    csv_outputs = OutputList.get_csv_outputs()

    for csv in csv_outputs:
        filename = csv.get_debug_filename()

        series_files = os.scandir(args.series)

        for i, file in enumerate(series_files, 1):
            if file.is_file():
                continue

            json_file_name = f"{file.path}\\{filename}"
            js = json.load(open(json_file_name, mode="r"))

            csv.write_game_csv(protobuf_json=js, path=f"{file.path}\\{csv.get_output_name}")



