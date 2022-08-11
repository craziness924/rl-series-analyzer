import argparse
import sys
import os

import series_analyzer.analyze_series as series_analyzer
from output.output import write_game_stats_to_csv


DEBUG_MODE = True

def analyze_season(season_path):
    season = [{}]
    weeks = []

    for file in os.scandir(season_path):
        absolutePath = file.path
        fileStats = file.stat()

        creationTime = fileStats.st_ctime
        
        if file.is_dir():
            fileInfo = {}

            fileInfo["path"] = absolutePath
            fileInfo["creationTime"] = creationTime
            fileInfo["file"] = file
            
            weeks.append(fileInfo)
        else:
            continue

    for week in weeks:
        games = series_analyzer.analyze_series(week.path)


def main(args):
    if DEBUG_MODE:
        series_path = args.series or f'{os.getcwd()}\\Test\\IGL 2022 Winter Week 4' 
    else:
        arglen = len(sys.argv)
        isSingleReplay = os.path.isfile(sys.argv[1]) and arglen == 2
        if  (isSingleReplay) or (os.path.isdir(sys.argv[1])):
            series_path = sys.argv[1]
        else:
            print("Exiting! Please put replays together in a folder before attempting to process together.") # sus
            sys.exit(1)

    if (args.series or False):
        games = series_analyzer.analyze_series(series_path)
    elif (args.season or DEBUG_MODE):
        args.season = "C:\\Users\\JD\\Documents\\Esports\\RL Seasons\\MOSEF Fall 2021 Season"
        season = analyze_season(args.season)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="RL Series Analyzer", description="Analyzes series of series and outputs stats.")

    parser.add_argument("--series", type=str, required=False, help="The path to the series to analyze. Optional.")
    parser.add_argument("--season", type=str, required=False, help="The path to the season to analyze. Optional.")

    args = parser.parse_args()

    if (not args.series) and (not args.season) and (not DEBUG_MODE):
        print("No path entered. Exiting...")
        exit(1)

    main(args)
