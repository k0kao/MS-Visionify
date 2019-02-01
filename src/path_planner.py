# -*- coding:utf-8 -*-
import terrain_analyzer

class PathPlanner:
    def __init__(self):
        self.map_grid = []
        self.map_width = 0
        self.map_height = 0

    def generate_map_grid(self, platforms, oneway_platforms, width, height):
        """
        Generates a map grid from input parameters
        :param platforms: list of terrain_analyzer Platform object
        :param oneway_platforms: list of terrain_analyzer Platform object, oneway
        :param width: width of map
        :param height: height of map
        :return: map_grid: list of lists representing map where each element is 1 if platform, 0 if empty.
        """