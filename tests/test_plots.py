from series_analyzer.series import Series
import os

from output.output_list import OutputList
from util.point import Point

def test_plots(args):
    if (args.season):
        raise TypeError("Seasons are unsupported by plot tester.")
        
    mpl_outputs = OutputList.get_plotting_outputs()

    for plot in mpl_outputs:
        filename = plot.get_debug_filename()

        series_files = os.scandir(args.series)
        point_files = []
        
        series_data = []
        data = []

        for i, file in enumerate(series_files, 1):
            if file.is_file():
                continue

            point_filename = f"{file.path}\\{filename}"

            if not os.path.exists(point_filename):
                continue
            
            with open(point_filename, mode="r") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    point_data = line.split(" ")
                    point = Point(float(point_data[0]), float(point_data[1]), point_data[2], point_data[3], point_data[4])

                    data.append(point)
                    series_data.append(point)

            series = Series(args.series)
            if len(data) > 0:
                plt = plot._create_plot(data=data, series=series, game_num=i)
                plt.show()
                
        if len(series_data) > 0:
            plt = plot._create_plot(data=series_data, series=series)
            plt.show()