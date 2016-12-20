from __future__ import division
import csv
import math

global _class
_class = ["negative","positive"]

class NodeDecision(object):
    def __init__(self, decision):
        self.decision = decision

    def run(self):
        #print "Decisao: ",self.decision
        print self.decision

    def navigation(self, path):
        self.run()

# data structure for tree nodes in ID3
class Node(object):

    def run(self):
        #print "Decisao num",self.num_att
        return

    def create_edges(self):
        for i in self.entropy:
            if(self.entropy[i] == 0.0):
                # entropia == a 0
                #remoev dados desnecessarios
                self.children[i] = NodeDecision(self.data2[i][-1][-1])
                del self.data2[i]
            else:
                # entropia != de 0
                self.children[i] = id3(self.data2[i], self.entropy[i], _class)


    def __init__(self, data, classes, num_att):
        self.data = data
        self.children = {}
        self.attributes = {}

        self.num_att = num_att
        self.data2 = {}

        if num_att == -1:
            self.classes = classes
        else:
            self.classes = ["x","b","o"]
    def get_decision(self):
        return num_att

    def get_data2(self):
        return self.data2

    def add_child(self, obj, string):
        self.children[string] = obj
    def show_childs(self):
        for i in self.children:
            self.children.run()

    def sumarize_data(self):
        self.total = 0
        for i in self.data:
            if i[self.num_att] in self.classes:
                if i[self.num_att] in self.attributes:
                    self.attributes[i[self.num_att]] += 1
                else:
                    self.attributes[i[self.num_att]] = 1
                self.total += 1

    def set_root_entropy(self, entropy):
        self.root_entropy = entropy

    def entropy_root(self):
        self.entropy = 0
        for i in self.classes:
            aux = self.attributes[i]/self.total
            self.entropy += -(aux) * (math.log(aux)/math.log(2))

    def entropy(self):
        # i need to identfy these attributes
        attributes = {}

        # ISSO DAQUI VAI DAR PAU
        for i in self.data:
            if i[self.num_att] not in attributes:
                attributes[i[self.num_att]] = [i]
                self.data2[i[self.num_att]] = [i]
            else:
                attributes[i[self.num_att]].append(i)
                self.data2[i[self.num_att]].append(i)

        self.entropy = {}
        for i in self.classes:
            if i in attributes:
                self.entropy[i] = 0
                used = 0
                total  = 0
                for i2 in attributes[i]:
                    if i2[len(i2)-1] == _class[1]:
                        used+= 1
                        total += 1
                    else:
                        total += 1
                aux = used/total

                entropia1 = 0
                if aux != 0:
                    entropia1 = -(aux) * (math.log(aux)/math.log(2))
                aux = (total-used)/total

                entropia2 = 0
                if aux != 0:
                    entropia2 = -(aux) * (math.log(aux)/math.log(2))
                self.entropy[i] += entropia1 + entropia2

    def calculate_gain(self):
        attributes = {}
        total = 0
        for i in self.data:
            total +=1
            if i[self.num_att] not in attributes:
                attributes[i[self.num_att]] = 1
            else:
                attributes[i[self.num_att]] += 1

        aux = 0
        for i in self.classes:
            if i in self.entropy:
                aux += self.entropy[i] * (attributes[i]/total)
        return self.root_entropy - aux


    def get_entropy(self):
        return self.entropy

    def navigation(self, path):
        self.run()
        if self.num_att == -1:
            self.children['begin'].navigation(path)
        else:
            self.children[path[self.num_att]].navigation(path)


def check_data(data):
    num = len(data[0]) -1
    attr = {}
    for i in data:
        if(i[num] in attr):
            attr[i[num]] += 1
        else:
            attr[i[num]] = 1
    return attr

def data_init():
    data = []
    with open('tic.data', 'rb') as csvfile:
        csv_data = csv.reader(csvfile)
        for row in csv_data:
            data.append(row)
    return data

def id3(examples, entropy, classes):
    attr = check_data(examples)
    if(len(attr) >= 0):
        gain = []
        for i in range(0, len(examples[0])-1 ):
            aux = Node(examples, _class, i)
            aux.set_root_entropy(entropy)
            aux.sumarize_data()
            aux.entropy()
            gain.append([aux.calculate_gain(), len(aux.get_entropy()),aux])
        gain = sorted(gain, key = lambda x: (x[0], x[1]))
        gain = gain[-1][-1]
        #root.add_child(gain, gain.get_decision)
        #root = gain
    gain.create_edges()


    return gain

def printM(matrix):
    for i in matrix:
        print i

def main():
    data = data_init()
    root = Node(data, _class, -1)
    root.sumarize_data()
    root.entropy_root()
    root.add_child(id3(data, root.get_entropy(),_class), "begin")
    input = raw_input()
    input = input.split(",")
    while(input != "0"):
        root.navigation(input)
        input = raw_input()
        if(input == "0"):
            return
        input = input.split(",")


if __name__ == "__main__":
    main()


