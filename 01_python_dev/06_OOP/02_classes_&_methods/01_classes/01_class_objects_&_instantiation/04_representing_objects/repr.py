# # class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
# bham_academy = Location(52.488647, -1.887249)
# print(bham_academy)


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"


bham_academy = Location(52.488647, -1.887249)
print(repr(bham_academy))