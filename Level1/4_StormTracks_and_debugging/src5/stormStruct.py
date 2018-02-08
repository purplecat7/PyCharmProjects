"""
Structure definition of a storm
"""

class Storm():
    def __init__(self):
        self.stormid = None
        self.pressure = list()
        self.windspeed = list()
        # and this can be extended to keep any information from the data