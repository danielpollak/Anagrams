import queue
import unittest
import Search.BreadthFirstSearch as Breadth


class BfsTest(unittest.TestCase):
    def setUp(self):
        self.Br = Breadth.BreadthFirstSearch()
        self.Br.set_word("Hello")

        self.comp = queue.Queue

    def test_get_word(self):
        self.assertEqual("Hello", self.Br.get_word())

    def test_test_class(self):
        self.assertEqual("Hello", self.Br.get_word())

    def test_hash_indices(self):
        self.assertEqual(self.Br.hash_indices([2, 3, 5, 6, 4]), "_\"_#_%_&_$")

    def test_get_remaining_letters(self):
        # case when there are no remaining letters
        self.assertEqual(self.Br.get_remaining_letters("Hello"), [])
        self.assertEqual(self.Br.get_remaining_letters("oelHl"), [])
        self.assertEqual(self.Br.get_remaining_letters("olleH"), [])

        # case when there are some remaining letters
        self.assertEqual(self.Br.get_remaining_letters("lHeo"), ["l"])
        self.assertEqual(self.Br.get_remaining_letters("Helo"), ["l"])
        self.assertEqual(self.Br.get_remaining_letters("Hel"), ["l", "o"])
        self.assertEqual(self.Br.get_remaining_letters("leH"), ["l", "o"])
        self.assertEqual(self.Br.get_remaining_letters("eH"), ["l", "l", "o"])
        self.assertEqual(self.Br.get_remaining_letters("ol"), ["H", "e", "l"])

        # case when all letters are remaining
        ans = self.Br.get_remaining_letters("")
        self.assertEqual(ans, ''.join(["H", "e", "l", "l", "o"]))

    def test_get_states(self):
        q = self.Br.get_states("ol")
        self.assertEqual(list(q.queue).sort(), ["olH", "ole", "oll"].sort())

        o = self.Br.get_states("")          # HELLO
        self.assertEqual(list(o.queue), ["H", "e", "l", "o"])
        o = self.Br.get_states("H")
        self.assertEqual(list(o.queue), ["He",                       "Hl",                                   "Ho"])
                                #         |         \                  |            \           \                    |               \
        o = self.list_states(o)  # o = self.Br.get_states(list(o.queue))             |           |
        self.assertEqual(list(o.queue).sort(), ["Hel",         "Heo",       "Hle",          "Hlo",     "Hll",              "Hoe",           "Hol"].sort())
                                        #  \                \               \              \       \                    \                \
        o = self.list_states(o)#|          |               |               |       \                       |                |
                                        #  \/               \/              \/              \/       \                      \/               \/
        self.assertEqual(list(o.queue).sort(), ["Hell", "Helo",   "Heol"     "Hleo", "Hlel",  "Hlol", "Hloe","Hllo","Hlle"         "Hoel",     "Holl", "Hole"].sort())
        #o = self.list_states(list(o.queue))
                                        # "Hell", "Helo",    "Heol"     "Hleo", "Hlel",   "Hlol", "Hloe"          "Hoel",       "Holl", "Hole"
        #self.assertEqual(list(o.queue), ["Hello", "Helol",   "Heoll"    "Hleo", "Hlelo", "Hlole", "Hloel"         "Hoell",      "Holle","Holel"])

    def list_states(self, o):
        out_queue = queue.Queue()
        for q in list(o.queue):
            for elem in list(self.Br.get_states(q).queue):
                out_queue.put(elem)
        return out_queue

if __name__ == '__main__':
    unittest.main()
