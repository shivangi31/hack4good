class UtilService:
    def __init__(self):
        pass

    @staticmethod
    def pinCodeParser(path):
        location = {}
        f = open(path)
        for line in f:
            words = line.split()
            location[words[1]] = (words[-3],words[-2])
        return location
