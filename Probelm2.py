# Time Complexity = O(2(V+E)) = O(V+E) | Space Complexity = O(V+E)

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if prerequisites is None or len(prerequisites) == 0:
            return True
        indeg_arr = [0 for i in range(numCourses)]
        hash_map = {i : [] for i in range(numCourses)}

        # Update indegrees array and hash map
        for pr in prerequisites:          # O(E) edges
            indeg_arr[pr[0]] += 1
            hash_map[pr[1]].append(pr[0])

        queue = deque()
        count = 0
        # add courses to queue with 0 dependent
        for i in range(numCourses):     # O(V) vertices
            if indeg_arr[i] == 0:
                queue.append(i)
                count += 1

        if count == numCourses: return True
        if len(queue) == 0: return False

        # if queue is not empty process courses in queue
        while len(queue) != 0:                # O(V+E)
            curr = queue.popleft()
            dependents = hash_map.get(curr)
            if dependents != None:
                for dependent in dependents:
                    indeg_arr[dependent] -= 1
                    if indeg_arr[dependent] == 0:
                        queue.append(dependent)
                        count += 1
                        if count == numCourses: return True

        return False











