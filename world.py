import pygame as pg

class World():
    def __init__(self, data, map_image):
        self.paths = []
        self.level_data = data
        self.image = map_image

    def process_data(self):
        for layer in self.level_data["layers"]:
            if layer["name"] == "path":
                for obj in layer["objects"]:
                    paths_data = obj["polyline"]
                    self.process_paths(paths_data)

    def process_paths(self, data):
        for point in data:
            temp_x = point.get("x") + 125
            temp_y = point.get("y") 
            self.paths.append((temp_x, temp_y))
            print(self.paths)

    def draw(self, screen):
        screen.blit(self.image, (0, 0))