from __future__ import division
import csv
import math

class NodeDecision(object):
    def __init__(self, decision):
        self.decision = decision

    def run(self):
        print "Decisao: ",self.decision

# data structure for tree nodes in ID3
class Node(object):

    def run(self):
        print "Decisao num",num_att

    def create_edges(self):
        print self.entropy
        for i in self.entropy:
            if(self.entropy[i] == 0.0):
                # entropia == a 0
                #remoev dados desnecessarios
                del self.data2[i]
                self.children[i] = NodeDecision(i)
            else:
                # entropia != de 0
                self.children[i] = id3(self.data2[i], self.entropy[i], ["0","1"])


    def __init__(self, data, classes, num_att):
        self.data = data
        self.children = {}
        self.classes = classes
        self.attributes = {}

        self.num_att = num_att
        self.data2 = {}

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
        index_class = len(self.data[0])-1
        for i in self.data:
            if i[index_class] in self.classes:
                if i[index_class] in self.attributes:
                    self.attributes[i[index_class]] += 1
                else:
                    self.attributes[i[index_class]] = 1
                self.total += 1
        print self.attributes

    def set_root_entropy(self, entropy):
        self.root_entropy = entropy

    def entropy_root(self):
        self.entropy = 0
        for i in self.classes:
            aux = self.attributes[i]/self.total
            self.entropy += -(aux) * (math.log(aux)/math.log(2))

        print self.entropy

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

        print attributes

        self.entropy = {}
        for i in self.classes:
            if i in attributes:
                self.entropy[i] = 0
                used = 0
                total  = 0
                print" EHUEHUAEHUAHUEHUAEHU", i
                print attributes
                print" EHUEHUAEHUAHUEHUAEHU"
                for i2 in attributes[i]:
                    if i2[self.num_att] == i2[len(i2)-1]:
                        used+= 1
                        total += 1
                    else:
                        total += 1
                aux = used/total
                print i,":",used,"/",total
                self.entropy[i] += -(aux) * (math.log(aux)/math.log(2))
                aux = (total-used)/total
                if aux != 0:
                    self.entropy[i] += -(aux) * (math.log(aux)/math.log(2))
               # else:
                    # removing unecessary data
                    #self.children[i] = NodeDecision(i)

        print "Entropia:", self.entropy
        print "Data2:", self.data2

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
                print aux, " ", attributes[i], total, self.entropy[i]
        print "Ganho: ", self.root_entropy - aux
        return self.root_entropy - aux


    def get_entropy(self):
        return self.entropy

def check_data(data):
    num = len(data[0]) -1
    attr = {}
    for i in data:
        if(i[num] in attr):
            attr[i[num]] += 1
        else:
            attr[i[num]] = 1

    print attr
    return attr

def data_init():
    data = []
    with open('example.data', 'rb') as csvfile:
        csv_data = csv.reader(csvfile)
        for row in csv_data:
            data.append(row)
    return data

def id3(examples, entropy, classes):
    print "!!!!!!!!!!!!!!!!!!!!!!!!"
    print examples
    print "!!!!!!!!!!!!!!!!!!!!!!!!"
    attr = check_data(examples)
    if(len(attr) > 0):
        gain = []
        for i in range(0, len(examples[0])-1 ):
            aux = Node(examples, classes, i)
            aux.sumarize_data()
            print "EHUHEUH", entropy
            aux.set_root_entropy(entropy)
            aux.entropy()
            gain.append([aux.calculate_gain(),aux])
        print gain
        gain = sorted(gain, key = lambda x: (x[0], x[1]))
        print "ESCOLHI ESSE DAQUI:", gain[len(gain)-1][0]
        gain = gain[len(gain)-1][1]
        #root.add_child(gain, gain.get_decision)
        #root = gain

        gain.create_edges()

        print raw_input('What is your name? ')

    else:
        print "devo retornar uma esoclha aqui"

    return gain


def main():
    data = data_init()
    root = Node(data, ["0", "1"], -1)
    root.sumarize_data()
    root.entropy_root()
    root.add_child(id3(data, root.get_entropy(),["0", "1"]), "begin")
    input = raw_input('What is your name? ') 
    while(input != "0"):
        root.run()
        print "1 - Verificar decision"
        print "heheh"
        print "heheh"
        print "heheh"
        input = raw_input('choose your destiny:') 


if __name__ == "__main__":
    main()


