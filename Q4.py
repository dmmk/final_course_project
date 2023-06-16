#https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/


from ast import literal_eval
import sys

class MiniMax:
    # print utility value of root node (assuming it is max)
    # print names of all nodes visited during search
    def __init__(self, game_tree):
        self.game_tree = game_tree  # GameTree
        self.root = game_tree.root  # GameNode
        self.currentNode = None     # GameNode
        self.successors = []        # List of GameNodes
        return

    def minimax(self, node):
        # first, find the max value
        best_val = self.max_value(node) # should be root node of tree

        # second, find the node which HAS that max value
        #  –> means we need to propagate the values back up the
        #      tree as part of our minimax algorithm
        successors = self.getSuccessors(node)
        print ("MiniMax:  Utility Value of Root Node: = " + str(best_val))
        # find the node with our best move
        best_move = None
        for elem in successors:   # —> Need to propagate values up tree for this to work
            if elem.value == best_val:
                best_move = elem
                break

        # return that best value that we've found
        return best_move


    def max_value(self, node):
        print ("MiniMax–>MAX: Visited Node :: " + node.Name)
        if self.isTerminal(node):
            return self.getUtility(node)

        infinity = float('inf')
        max_value = -infinity

        successors_states = self.getSuccessors(node)
        for state in successors_states:
            max_value = max(max_value, self.min_value(state))
        return max_value

    def min_value(self, node):
        print ("MiniMax–>MIN: Visited Node :: " + node.Name)
        if self.isTerminal(node):
            return self.getUtility(node)

        infinity = float('inf')
        min_value = infinity

        successor_states = self.getSuccessors(node)
        for state in successor_states:
            min_value = min(min_value, self.max_value(state))
        return min_value

    #                     #
    #   UTILITY METHODS   #
    #                     #

    # successor states in a game tree are the child nodes…
    def getSuccessors(self, node):
        assert node is not None
        return node.children

    # return true if the node has NO children (successor states)
    # return false if the node has children (successor states)
    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0

    def getUtility(self, node):
        assert node is not None
        return node.value



def parse_data_as_list(fname):
    with open(fname, "r") as f:
        data_as_string = f.read()
        print (data_as_string)
        data_list = literal_eval(data_as_string)
    return data_list


class GameNode:
    def __init__(self, name, value=0, parent=None):
        self.Name = name      # a char
        self.value = value    # an int
        self.parent = parent  # a node reference
        self.children = []    # a list of nodes

    def addChild(self, childNode):
        self.children.append(childNode)

class GameTree:
    def __init__(self):
        self.root = None

    def build_tree(self, data_list):
        """
        :param data_list: Take data in list format
        :return: Parse a tree from it
        """
        self.root = GameNode(data_list.pop(0))
        for elem in data_list:
            self.parse_subtree(elem, self.root)
            print(elem)

    def parse_subtree(self, data_list, parent):
        # base case
        if type(data_list) is tuple:
            # make connections
            leaf_node = GameNode(data_list[0])
            leaf_node.parent = parent
            parent.addChild(leaf_node)
            # if we're at a leaf, set the value
            if len(data_list) == 2:
                leaf_node.value = data_list[1]
            return

        # recursive case
        tree_node = GameNode(data_list.pop(0))
        # make connections
        tree_node.parent = parent
        parent.addChild(tree_node)
        for elem in data_list:
            self.parse_subtree(elem, tree_node)

        # return from entire method if base case and recursive case both done running
        return


def main():
    filename = sys.argv[1]
    #print ("hello world! " + filename)
    data_list = parse_data_as_list(filename)
    data_tree = GameTree()
    data_tree.build_tree(data_list)
    #print(data_tree)
    #print(data_tree.root)
    minimax = MiniMax(data_tree)
    minimax.minimax(data_tree.root)

if __name__ == "__main__":
    main()

