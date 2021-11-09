import math

rows = int(input("Enter the number of rows in your table:\n"))
table = []
class getratio(object):
    def __init__(self, table):
        for i in range(rows):
            self.currentrow = []
            self.x = int(input("Enter the x value:\n"))
            self.y = int(input("Enter the y value:\n"))
            self.currentrow.append(self.x)
            self.currentrow.append(self.y)
            table.append(self.currentrow)
    def findratio(self, table):
        self.norows = 0
        for novals in table:
            self.norows+=1
        