import os
import matplotlib.pyplot as plt
import numpy as np
import datetime

import carball
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager

from series_analyzer.crazy_game import CrazyGame
from series_analyzer.crazy_game import ReplayInfo

DEBUG_MODE = False

class Series():
    def __init__(self, series_path):
        if series_path is None:
            Exception("No series path found when creating series object!")

        split = str.split(series_path, "\\")
        self.name = split[len(split) - 1]

        self.series_path = series_path
        self.games: list[CrazyGame] = []
        self.parsed_replays = []
        # self.extra_stats = None

    def analyze_series(self):
        """
        DEBUG CONFIG, ONLY ANALYZES 1
        """
        print(f"Processing series at {self.series_path}!")

        series_files = os.scandir(self.series_path)

        self._parse_replays(series_files)

        if len(self.parsed_replays) == 0:
            print(f"No replays found for series at {self.series_path}")

        for i, replay in enumerate(self.parsed_replays, 1):
            if i > 1 and DEBUG_MODE:
                continue
            game_path = f'{self.series_path}\game{i}'
            game_path_exists = os.path.exists(game_path)

            # later when multiple files exist for analysis, we could check that each one exists and make them exist if they don't
            if not game_path_exists: 
                os.mkdir(game_path)

            # _json = carball.decompile_replay(f'{series_path}\{file}')

            analysis = AnalysisManager(game=replay.game)
            analysis.create_analysis(calculate_intensive_events=False)

            f = open(f"{game_path}\\output.json", mode="w")
            analysis.write_json_out_to_file(f)
            
            # with open(pts_path, 'wb') as f:
            #     analysis.write_proto_out_to_file(file=f)

            game = CrazyGame()
            game.path = game_path
            game.analysis = analysis
            game.replay_info = replay

            self.games.append(game)

    def  _parse_replays(self, files):
        for file in files:
            extension = os.path.splitext(file.name)
            
            replayInfo = {}

            if extension[1] == ".replay":
                _json = carball.decompile_replay(replay_path=file.path)
                
                game = Game()
                game.initialize(loaded_json=_json)

                replay_info = ReplayInfo(_json, game, game.datetime)

                self.parsed_replays.append(replay_info)
            if DEBUG_MODE:
                break
        self.parsed_replays.sort(key=self._replay_sort)

    def _replay_sort(self, x):
        return x.start_time


            
