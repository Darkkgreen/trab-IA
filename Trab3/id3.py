from __future__ import division
import csv
import math

# data structure for tree nodes in ID3
class Node(object):
    entropy = 0
    gain = 0
    attributes = {}
    num_classes = 0

    def __init__(self, data, num):
        self.data = data
        self.children = []
        self.num_classes = num

    def add_child(self, obj):
        self.children.append(obj)

    def print_dataset(self):
        print self.data

    def calc_gain(self):
        gain += 0

    def calc_entropy_root(self):
        num_total = 0
        for i in self.attributes:
            num_total += self.attributes[i]

        print self.attributes[i]
        for i in self.attributes:
            aux = self.attributes[i]/num_total
            self.entropy += -(aux)*(math.log(aux)/math.log(2))
        print self.entropy


    def calc_entropy(self):
        num_total = 0
        for i in self.attributes:
            num_total += self.attributes[i]

        print self.attributes[i]
        for i in range (1..self.num_classes):
            aux = self.attributes[i]/num_total
            self.entropy += -(aux)*(math.log(aux)/math.log(2))
        print self.entropy



    # attribute's column, and the dataset
    def summarize_examples(self, attribute):
        for i in self.data:
            if i[attribute] in self.attributes:
                self.attributes[i[attribute]] += 1
            else:
                self.attributes[i[attribute]] = 1
        print self.attributes


def data_init():
    data = []
    with open('example.data', 'rb') as csvfile:
        csv_data = csv.reader(csvfile)
        for row in csv_data:
            data.append(row)
    return data


def main():
    dataset = data_init()
    num_attributes = len(dataset[0]) - 1
    node_result = Node(dataset, 2)

    node_result.summarize_examples(num_attributes)
    node_result.calc_entropy_root()
    nodes = []

    for i in range(0, len(dataset[0])-1):
        # calculate the entropy for others entries
        aux = Node(dataset, 2)




if __name__ == "__main__":
    main()


