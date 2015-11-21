#-*- coding: utf-8 -*-

'''
一个数据改变，其他的也跟着改变
'''

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self,observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self,observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self.data = 0

    def setData(self,data):
        self.data = data
        self.notify()

    def getData(self):
        return self.data


class HexViewer:                #十进制
    def update(self, subject):
        print 'HexViewer:Subject %s has data 0x%x' % (subject.name,subject.getData())


class DecimalViewer:             #十六进制
    def update(self, subject):
        print 'DecimalViewer:Subject %s has data %d' % (subject.name,subject.getData())

def main():
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)
    print "Setting Data 1 = 10"
    data1.setData(10)
    print "Setting Data 2 = 15"
    data2.setData(15)
    print "Setting Data 1 = 3"
    data1.setData(3)
    print "Setting Data 2 = 5"
    data2.setData(5)
    print "Detach HexViewer from data1 and data2."
    data1.detach(view2)
    data2.detach(view2)
    print "Setting Data 1 = 10"
    data1.setData(10)
    print "Setting Data 2 = 15"
    data2.setData(15)

if __name__ == '__main__':
    main()
