from unittest import TestCase
from py.AVLTree import AVLTree, Student, EmptyTreeException
class TestAVLTree(TestCase):
    def test_init(self):
        tree = AVLTree()
        self.assertEqual(tree._length, 0)

    def test_insert(self):
        tree = AVLTree()
        tree.insert(Student('AAa', 2, 3, 4, 5.6))
        tree.insert(Student('AAa', 2, 3, 4, 6.6))
        tree.insert(Student('AAa', 2, 3, 4, 7.6))
        tree.insert(Student('AAa', 2, 3, 4, 8.6))
        tree.insert(Student('AAa', 2, 3, 4, 8.6))
        self.assertEqual(tree._length, 5)

    def test_find_contains(self):
        tree = AVLTree()
        with self.assertRaises(EmptyTreeException):
            tree.find(1)
        tree.insert(Student('AAa', 2, 3, 4, 5.6))
        tree.insert(Student('AAa', 2, 3, 4, 6.6))
        tree.insert(Student('AAa', 2, 3, 4, 7.6))
        tree.insert(Student('AAa', 2, 3, 4, 8.6))
        self.assertEqual(tree.find(5.6).key(), 5.6)
        self.assertEqual(tree.find(5.0), None)

    def test_remove(self):
        tree = AVLTree()
        with self.assertRaises(EmptyTreeException):
            tree.remove(1)
        tree.insert(Student('AAa', 2, 3, 4, 5.6))
        tree.insert(Student('AAa', 2, 3, 4, 6.6))
        tree.insert(Student('AAa', 2, 3, 4, 7.6))
        tree.insert(Student('AAa', 2, 3, 4, 8.6))
        tree.insert(Student('AAa', 2, 3, 4, 8.6))
        self.assertEqual(tree._length, 5)
        tree.remove(8.6)
        self.assertEqual(tree._length, 4)

    def test_is_empty(self):
        tree = AVLTree()
        self.assertEqual(tree.is_empty(), True)

    def test_get_size(self):
        tree = AVLTree()
        self.assertEqual(tree.get_size(), 0)
        tree.insert(Student('AAa', 2, 3, 4, 5.6))
        tree.insert(Student('AAa', 2, 3, 4, 6.6))
        tree.insert(Student('AAa', 2, 3, 4, 7.6))
        tree.insert(Student('AAa', 2, 3, 4, 8.6))
        self.assertEqual(tree.get_size(), 4)

    def test_save_and_loading(self):
        tree = AVLTree()
        tree.insert(Student('AAa', 2, 3, 4, 5.6))
        tree.insert(Student('AAa', 2, 3, 4, 6.6))
        tree.insert(Student('AAa', 2, 3, 4, 7.6))
        tree.insert(Student('AAa', 2, 3, 4, 8.6))
        tree.save('dump.txt')
        tree2 = AVLTree()
        tree2.loading('dump.txt')
        self.assertEqual(tree._root.key(), tree2._root.key())

    def test_str(self):
        tree = AVLTree()
        tree.insert(Student('AAa', 2, 3, 4, 5.6))
        tree.insert(Student('AAa', 2, 3, 4, 6.6))
        tree.insert(Student('AAa', 2, 3, 4, 7.6))
        tree.insert(Student('AAa', 2, 3, 4, 8.6))
        s = """AVLTree
│       ┌── 8.6
│   ┌── 7.6
└── 6.6
    └── 5.6
"""
        self.assertEqual(str(tree), s)