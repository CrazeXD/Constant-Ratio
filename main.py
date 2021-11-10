import sys
import time

rows = int(input("Enter the number of rows in your table:\n"))
if rows == 0:
    sys.exit()
elif rows == 1:
    sys.exit()
table = []
class getratio(object):
    def __init__(self, rows, table):
        self.rows = rows
        self.table = table
        for i in range(rows):
            self.currentrow = []
            self.x = int(input("Enter the x value:\n"))
            self.y = int(input("Enter the y value:\n"))
            self.currentrow.append(self.x)
            self.currentrow.append(self.y)
            table.append(self.currentrow)
    def findratios(self):
        self.changes = []
        for a in range(self.rows):
            if a>=1:
                self.ychangecurrentrow = table[a][1]/table[a-1][1]
                self.xchangecurrentrow = table[a][0]-table[a-1][0]
                self.currentrowratio = self.ychangecurrentrow/self.xchangecurrentrow
                self.changes.append(self.currentrowratio)
    def checkratio(self, list):
        for x in list:
            if x==list[0]:
                pass
            else:
                return False
        return True
if __name__ == '__main__':
    obj = getratio(rows, table)
    obj.findratios()
    a = obj.checkratio(obj.changes)
    if a:
        print(f"Common Ratio = {obj.changes[0]}")
    else:
        print('No constant ratio')
        time.sleep(10)
        sys.exit()