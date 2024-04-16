# Класс для создания узла бинарного дерева
import matplotlib.pyplot as plt
from graphviz import Digraph

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Класс для создания бинарного дерева
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Метод для добавления узла в дерево
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    # Вспомогательный метод для рекурсивного добавления узла в дерево
    def _insert(self, key, node):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    # Метод для поиска узла в дереве
    def search(self, key):
        return self._search(key, self.root)

    # Вспомогательный метод для рекурсивного поиска узла в дереве
    def _search(self, key, node):
        if node is None or node.val == key:
            return node
        elif key < node.val:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    # Метод для удаления узла из дерева
    def delete(self, key):
        self.root = self._delete(key, self.root)

    # Вспомогательный метод для рекурсивного удаления узла из дерева
    def _delete(self, key, node):
        if node is None:
            return node
        elif key < node.val:
            node.left = self._delete(key, node.left)
        elif key > node.val:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.val = min_node.val
                node.right = self._delete(min_node.val, node.right)
        return node

    # Метод для поиска минимального узла в дереве
    def find_min(self):
        return self._find_min(self.root)

    # Вспомогательный метод для рекурсивного поиска минимального узла в дереве
    def _find_min(self, node):
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)

    # Метод для поиска максимального узла в дереве
    def find_max(self):
        return self._find_max(self.root)

    # Вспомогательный метод для рекурсивного поиска максимального узла в дереве
    def _find_max(self, node):
        if node.right is None:
            return node
        else:
            return self._find_max(node.right)

    def visualize(self):
        dot = Digraph()
        if self.root:
            self._visualize(self.root, dot)
        dot.render('binary_tree', format='png', cleanup=True)
        img = plt.imread('binary_tree.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    # Вспомогательный метод для рекурсивной визуализации бинарного дерева
    def _visualize(self, node, dot):
        if node.left:
            dot.node(str(node.left.val))
            dot.edge(str(node.val), str(node.left.val))
            self._visualize(node.left, dot)
        if node.right:
            dot.node(str(node.right.val))
            dot.edge(str(node.val), str(node.right.val))
            self._visualize(node.right, dot)
