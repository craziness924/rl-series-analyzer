import os
import matplotlib.pyplot as plt
import numpy as np
import datetime

import carball
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager

from stats.stats.stat_manager import StatsManager
from stats.events.event_manager import EventManager

from series_analyzer.game_info import GameInfo


class Series():
    def __init__(self, series_path):
        if series_path is None:
            Exception("No series path found when creating series object!")
        self.series_path = series_path
        self.games = []
        self.parsed_replays = []
        self.stats_manager = StatsManager()
        self.event_manager = EventManager()

    def analyze_series(self):
        print(f"Processing series at {self.series_path}!")

        series_files = os.scandir(self.series_path)

        self._parse_replays(series_files)

        if len(self.parsed_replays) == 0:
            print(f"No replays found for series at {self.series_path}")

        for i, replay in enumerate(self.parsed_replays, 1):
            game_path = f'{self.series_path}\game{i}'
            game_path_exists = os.path.exists(game_path)


            # later when multiple files exist for analysis, we could check that each one exists and make them exist if they don't
            if not game_path_exists: 
                #os.mkdir(f'{SERIES_PATH}\game{game_num}')
            # _json = carball.decompile_replay(f'{series_path}\{file}')

                analysis = AnalysisManager(game=replay["game"])
                analysis.create_analysis(calculate_intensive_events=True)
                
                # with open(pts_path, 'wb') as f:
                #     analysis.write_proto_out_to_file(file=f)

                gameInfo = GameInfo()

                gameInfo.path = game_path
                gameInfo.analysis = analysis

                self.games.append(gameInfo)

    def  _parse_replays(self, files):
        for file in files:
            extension = os.path.splitext(file.name)
            
            replayInfo = {}

            if extension[1] == ".replay":
                _json = carball.decompile_replay(replay_path=file.path)

                game = Game()
                game.initialize(loaded_json=_json)

                replayInfo["data"] = _json
                replayInfo["game"] = game
                replayInfo["startTime"] = game.datetime

                self.parsed_replays.append(replayInfo)
        self.parsed_replays.sort(key=self._replay_sort)

    def _replay_sort(self, x):
        return x["startTime"]


            
