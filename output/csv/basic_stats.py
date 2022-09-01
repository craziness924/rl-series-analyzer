import os
import csv
import json

from series_analyzer.series import Series
from series_analyzer.crazy_game import CrazyGame

from google.protobuf.json_format import _Printer

game_schema = ["Player", "Goals", "Assists", "Points (g+a)", "Saves", "Shots", "Shot%", "Demos", "Demoed"]
series_schema = ["Player", "Games", "Goals", "Assists", "Points (g+a)", "Saves", "Shots", "Shot%", "Demos", "Demoed"]

class BasicStats():
    @staticmethod
    def get_debug_filename():
        return ("protobuf.json")
    @staticmethod
    def get_output_name():
        return "basic_stats.csv"

    @staticmethod
    def output_csv(series: Series, save_points: bool) -> None:
        series_stats = []
        for game in series.games:
            js = _Printer()._MessageToJsonObject(game.analysis.protobuf_game)

            if (save_points):
                with open(f"{game.path}\\{BasicStats.get_debug_filename()}", mode="w") as f:
                    json.dump(js, f)

            BasicStats.write_game_csv(protobuf_json=js, path=game.path)
    
    @staticmethod
    def write_game_csv(protobuf_json: dict, path: str):
        with open(file=f"{path}\\{BasicStats.get_output_name()}", mode="w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow(game_schema)
                

