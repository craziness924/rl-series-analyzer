import argparse
import sys
import os

from series_analyzer.series import Series
from season_analyzer.season import Season

from output.output import write_game_stats_to_csv


DEBUG_MODE = True




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

    if (args.series):
        series = Series(args.series)
        series.analyze_series()
    elif (args.season):
        season = Season(args.season)
        season.analyze_season()
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="RL Series Analyzer", description="Analyzes series of series and outputs stats.")

    parser.add_argument("--series", type=str, required=False, help="The path to the series to analyze. Optional.")
    parser.add_argument("--season", type=str, required=False, help="The path to the season to analyze. Optional.")

    args = parser.parse_args()

    if (not args.series) and (not args.season) and (not DEBUG_MODE):
        print("No path entered. Exiting...")
        exit(1)

    main(args)
