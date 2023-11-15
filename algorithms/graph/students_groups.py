"""
A classroom consists of N students, whose friendships can be represented
in an adjacency list.
For example, the following descibes a situation where 0
is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}

Each student can be placed in a friend group,
which can be defined as the transitive closure of that
student's friendship relations.
In other words, this is the smallest set such that no student
in the group has any friends outside this group.
For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
"""
from typing import Dict, List, Set, Tuple


def solution(adj_list: Dict[int, List[int]]) -> Tuple[List[Set[int]], int]:
    """
    :param adj_list: dict
    :return: int
    """

    def dfs(student: int):
        group = set()
        queue = [student]

        while queue:
            elem = queue.pop()
            if elem in visited:
                continue
            group.add(elem)

            for neighbour in adj_list[elem]:
                if neighbour not in group:
                    queue.append(neighbour)
            visited.add(elem)
        return group

    groups = []
    students = set(adj_list.keys())
    visited = set()

    for student in students:
        if student not in visited:
            group = dfs(student)
            groups.append(group)
            visited.add(student)
    return groups, len(groups)


if __name__ == "__main__":
    adj_list = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}

    print(solution(adj_list))
