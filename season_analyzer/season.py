import os

from series_analyzer.series import Series


class Season():
    def __init__(self, season_path):
        if season_path is None:
            Exception("No season path found when creating season object!")
        self.path = season_path
        self.weeks = []


    def analyze_season(self):
        for file in os.scandir(self.path):
            absolute_path = file.path
            file_stats = file.stat()

            creation_time = file_stats.st_ctime
            
            if file.is_dir():
                fileInfo = {}

                fileInfo["path"] = absolute_path
                fileInfo["creationTime"] = creation_time
                fileInfo["file"] = file
                
                self.weeks.append(fileInfo)
            else:
                continue

        for i, week in enumerate(self.weeks, 0):
            week_info = {}

            series = Series(week["path"])
            series.analyze_series()

            self.weeks[i]["series"] = series

            pass