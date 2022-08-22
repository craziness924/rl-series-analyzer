import os
import matplotlib.pyplot as plt
import numpy as np
import datetime

import carball
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager

from series_analyzer.crazy_game import CrazyGame
from series_analyzer.crazy_game import ReplayInfo

import multiprocessing
from multiprocessing import Process

DEBUG_MODE = False

class FileInfo():
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

class Series():
    def __init__(self, series_path):
        if series_path is None:
            Exception("No series path found when creating series object!")

        split = str.split(series_path, "\\")
        self.name = split[len(split) - 1]

        self.series_path = series_path
        self.games: list[CrazyGame] = []
        self.parsed_replays = []
        self.extra_stats = None

    def analyze_series(self):
        """
        Debug config. Only analyzes first game if DEBUG_MODE is True
        """
        print(f"Processing series at {self.series_path}!")

        series_files = os.scandir(self.series_path)
        
        file_list = []
        for file in series_files:
            file_list.append(FileInfo(file.name, file.path))

        game_pool = multiprocessing.Pool()

        for result in game_pool.map(self._parse_replays, file_list, chunksize=1):
            self.parsed_replays.append(result)

        self.parsed_replays.sort(key=self._replay_sort)

        if len(self.parsed_replays) == 0:
            print(f"No replays found for series at {self.series_path}")

        task_infos = []

        for i, replay in enumerate(self.parsed_replays, 1):
            if i > 1 and DEBUG_MODE:
                continue
            task_info = {}

            game_path = f'{self.series_path}\game{i}'
            
            task_info["game_path"] = game_path
            task_info["replay"] = replay

            task_infos.append(task_info)

            game_path_exists = os.path.exists(game_path)

            if not game_path_exists: 
                os.mkdir(game_path)

        analysis_pool = multiprocessing.Pool()

        for result in analysis_pool.map(self._create_game_from_replay, task_infos, chunksize=1):
            self.games.append(result)
        pass

        # for i, replay in enumerate(self.parsed_replays, 1):
        #     if i > 1 and DEBUG_MODE:
        #         continue

        #     p = Process(target=self._create_game_from_replay, args=[replay, game_path, analysis_queue])
        #     p.start()

        #     analysis_processes.append(p)

        # for process in processes:
        #     process.join()

        # for game in analysis_queue.get():
        #     self.games.append(game)
        # pass

    def _create_game_from_replay(self, task_info):
        replay: ReplayInfo = task_info["replay"]

        analysis = AnalysisManager(game=replay.game)
        analysis.create_analysis(calculate_intensive_events=False)

        game = CrazyGame()
        game.path = task_info["game_path"]
        game.analysis = analysis
        game.replay_info = replay

        return game

    def  _parse_replays(self, file_info: FileInfo):
       # for file in files:
            extension = os.path.splitext(file_info.name)
            
            replayInfo = {}

            if extension[1] == ".replay":
                _json = carball.decompile_replay(replay_path=file_info.path)

                game = Game()
                game.initialize(loaded_json=_json)

                replay_info = ReplayInfo(_json, game, game.datetime)

                return replay_info
        

    def _replay_sort(self, x):
        return x.start_time


            
