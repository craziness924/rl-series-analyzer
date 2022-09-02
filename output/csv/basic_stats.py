import os
import csv
import json

import pandas as pd

from series_analyzer.series import Series
from series_analyzer.crazy_game import CrazyGame

from google.protobuf.json_format import _Printer

game_schema = ["Player", "Goals", "Assists", "Points (g+a)", "Saves", "Shots", "Shot%", "Demos", "Demoed"]
series_schema = ["Player", "Games", "Goals", "Assists", "Points (g+a)", "Saves", "Shots", "Shot%", "Demos", "Demoed"]

class BasicStats():
    @staticmethod
    def get_debug_filename():
        return ("output.json")
    @staticmethod
    def get_output_name():
        return "basic_stats.csv"

    @staticmethod
    def output_csv(series: Series, save_points: bool) -> None:
        #TODO: append all game DFs to series DF

        series_df = pd.DataFrame(columns=series_schema)

        # series_stats = [] 
        for i, game in enumerate(series.games, 1):
            js = _Printer()._MessageToJsonObject(game.analysis.protobuf_game)
            df = BasicStats.generate_game_dataframe(js, game)

            if i == 1:
                series_df = df.copy(True)
            else:
                series_df = df.add(series_df, fill_value=0.0)

            df.to_csv(f"{game.path}\\{BasicStats.get_output_name()}")
        
        series_df = BasicStats.calculate_shot_pct(series_df)
        series_df.to_csv(f"{series.series_path}\\{BasicStats.get_output_name()}")

    @staticmethod
    def generate_game_dataframe(protobuf_json, game: CrazyGame = None) -> pd.DataFrame:
        df = pd.DataFrame(columns=game_schema)

        for player in protobuf_json["players"]:
            player_id = player["id"]["id"]

            player_name = player.get("name", 0)
            player_goals = player.get("goals", 0)
            player_assists = player.get("assists", 0)
            player_saves = player.get("saves", 0)
            player_shots = player.get("shots", 0)

            player_demos = 0
            player_demoed = 0

            try:
                demoStats = player["stats"]["demoStats"]

                for key, item in demoStats.items():
                    if key == "numDemosInflicted":
                        player_demos += item
                    elif key == "numDemosTaken":
                        player_demoed += item
                    else:
                        print("Unknown key in demoStats!")
            except KeyError:
                pass

            df.loc[len(df.index)] = [player_name, player_goals, player_assists, player_goals + player_assists, player_saves,
                                    player_shots, 0.0, player_demos, player_demoed]

        df.set_index("Player", inplace=True)
        
        df = BasicStats.calculate_shot_pct(df=df)

        return df

    # this function is necessary because we need to recalculate the shot pct for the series df
    @staticmethod
    def calculate_shot_pct(df: pd.DataFrame) -> pd.DataFrame:
        """
        Returns a dataframe with the shot percentage of each player.
        """
        for player in df.index:
            player_df = df.loc[player]

            player_shots = player_df.loc["Shots"]
            player_goals = player_df.loc["Goals"]
        
            if player_shots == 0:
                shot_pct = 0
            else:
                shot_pct = (player_goals / player_shots) * 100

            df["Shot%"][player] = shot_pct

        return df
                        

