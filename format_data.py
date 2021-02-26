import json


class GatherData():
    def __init__(self):
        self.file = lambda x: open("storage.json", x)

        self.data = json.loads(self.file("r").read())

    @property
    def updateFile(self):
        return self.file("w").write(json.dumps(self.data))

    def get(self, index=None):
        if index is None:
            return self.data
        else:
            return self.data[index]

    def add(self, item):
        if type(item) is list:
            self.data = [*item, *self.data]
            self.updateFile
            return self.data
        else:
            self.data.append(item)
            self.updateFile
            return self.data

    def remove(self, item):
        self.data.remove(item)
        self.updateFile
        return self.data


# g = GatherData().get(3)

# a = GatherData().add("Welcome!!")

r = GatherData().remove("a")

print(r)
