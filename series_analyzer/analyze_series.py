import os
import sys
import carball
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
from carball.analysis.utils.pandas_manager import PandasManager
import matplotlib.pyplot as plt
import numpy as np



def analyze_series(series_path):
    print(f"Processing replays in {series_path}!")

    game_num = 0
    games = []

    for file in os.listdir(series_path):
        game_num = game_num + 1
        if game_num > 1:
            continue
        extension = os.path.splitext(file)
        
        if extension[1] == ".replay":
            game_path = f'{series_path}\game{game_num}'
            game_path_exists = os.path.exists(game_path)


            if not game_path_exists:
                #os.mkdir(f'{SERIES_PATH}\game{game_num}')
                _json = carball.decompile_replay(f'{series_path}\{file}',)
                game = Game()
                game.initialize(loaded_json=_json)
                analysis = carball.analyze_replay_file(f'{series_path}\{file}')
                # with open(pts_path, 'wb') as f:
                #     analysis.write_proto_out_to_file(file=f)

                gameInfo = {}

                gameInfo["path"] = game_path
                gameInfo["analysis"] = analysis

                games.append(gameInfo)
                
    return games

if __name__ == "main":
    analyze_series()


# for file in os.listdir(SERIES_PATH):
#     game_num = game_num + 1
#     extension = os.path.splitext(file)    
#     if extension[1] == ".replay":
#         game_path = f'{SERIES_PATH}\game{game_num}'
#         pts_path = f'{game_path}\game{game_num}.pts'

#         game_path_exists = os.path.exists(game_path)
#         ptb_exists = os.path.exists(pts_path)
#         if not game_path_exists:
#            # os.mkdir(f'{SERIES_PATH}\game{game_num}')
#             _json = carball.decompile_replay(f'{SERIES_PATH}\{file}',)
#             game = Game()
#             game.initialize(loaded_json=_json)
#             analysis = carball.analyze_replay_file(f'{SERIES_PATH}\{file}')
#             # with open(pts_path, 'wb') as f:
#             #     analysis.write_proto_out_to_file(file=f)
#             games.append(analysis)
            
# for file in os.listdir(SERIES_PATH):
#     game_num = game_num + 1
#     extension = os.path.splitext(file)

#     if extension[1] == ".replay":
#         game_path = f'{SERIES_PATH}\game{game_num}'
#         pts_path = f'{game_path}\game{game_num}.pts'
        
        
#         game_path_exists = os.path.exists(game_path)
#         ptb_exists = os.path.exists(pts_path)

#         if ptb_exists:
#             pts_file = open(pts_path, 'rb')
#             game = ProtobufManager.read_proto_out_from_file(pts_file)
#             analysis = AnalysisManager(game)
#             analysis.create_analysis()
#             games.append(analysis)
#             continue
#         else:
#             if not game_path_exists:
#                 os.mkdir(f'{SERIES_PATH}\game{game_num}')
#             _json = carball.decompile_replay(f'{SERIES_PATH}\{file}',)
#             balls_game = Game()
#             balls_game.initialize(loaded_json=_json)
#             analysis = carball.analyze_replay_file(f'{SERIES_PATH}\{file}')
#             with open(pts_path, 'wb') as f:
#                 analysis.write_proto_out_to_file(file=f)
#             games.append(analysis)

            
