import json


class GatherData():
    def __init__(self):
        self.file = lambda x: open("storage.json", x)
        self.data = json.loads(self.file("r").read())

    def getAll(self):
        return self.data

    def add(self, item):
        self.data.append(item)
        self.file("w").write(self.data)
        print(self.data)
