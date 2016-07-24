import math
class DepthFirstSearch:
    def _init_(self):
        seen_states = []


    def get_anagrams(self, word):
        print dfs(word)

    def dfs(self, word):
        new_states = get_states(self, word)
        for elem in new_states:
            if new_states == []:
                return
            else:
                return dfs(self, new_states)

    def get_states(self, state):
        '''Ok. so what do these states look like? Well what do you start with?
        The first letter. Lets start there. Then we can do a depth first'''


    def hash_indicies(self, indices):
        out = 0
        for i in range(len(indices)):
            out += indices[i] * math.pow(10, len(indices) - i - 1)
        return out




