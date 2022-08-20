from output.output_list import OutputList

from series_analyzer.series import Series

class OutputManager():
    @staticmethod
    def output_for_series(series: Series):
        csv_outputs = OutputList.get_csv_outputs()
        mpl_outputs = OutputList.get_plotting_outputs()

        for output in mpl_outputs:
            output.output_plot(series)