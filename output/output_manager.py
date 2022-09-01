from output.output_list import OutputList

from series_analyzer.series import Series

class OutputManager():
    @staticmethod
    def output_for_series(series: Series, save_points: bool):
        csv_outputs = OutputList.get_csv_outputs()
        mpl_outputs = OutputList.get_plotting_outputs()

        for plot in mpl_outputs:
            plot.output_plot(series, save_points)

        for csv in csv_outputs:
            csv.output_csv(series, save_points)