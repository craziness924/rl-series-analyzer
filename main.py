import argparse
import sys
import os

from tests.test_plots import test_plots
from series_analyzer.series import Series
from season_analyzer.season import Season

from stats.events.event_manager import EventManager
from output.output_manager import OutputManager

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

    output_manager = OutputManager()
    if (args.series):
        series = Series(args.series)
        series.analyze_series()
        series = EventManager.calculate_events(series)
        output_manager.output_for_series(series, args.save_points)
    elif (args.season):
        season = Season(args.season)
        season.analyze_season()

        event_manager = EventManager()
        for i, week in enumerate(season.weeks):
            if week["series"]:
                week["series"] = EventManager.calculate_events(week["series"])
                if (args.no_output):
                    continue
                output_manager.output_for_series(series, args.save_points)
                pass          
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="RL Series Analyzer", description="Analyzes series of series, and series and then outputs stats.")

    parser.add_argument("--series", type=str, required=False, help="The path to the series to analyze. Optional.")
    parser.add_argument("--season", type=str, required=False, help="The path to the season to analyze. Optional.")
    parser.add_argument("--test_plots", required=False, action="store_true", help="Uses saved points from previous analysis, shows plots, then exits.")
    parser.add_argument("--save_points", required=False, action="store_true", help="Saves points when making plots.")
    parser.add_argument("-no_output", required=False, action="store_true", help="Pass this argument to prevent any output from the program.")

    args = parser.parse_args()

    if (not args.series) and (not args.season):
        print("No path entered. Exiting...")
        exit(1)
    elif (args.series) and (args.season):
        print("Cannot process a series and season at the same time. Exiting...")
        exit(1)
    
    if (args.test_plots):
        test_plots(args)
    else:
        main(args)
