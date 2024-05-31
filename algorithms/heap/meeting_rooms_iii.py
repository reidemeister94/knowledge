"""
https://leetcode.com/problems/meeting-rooms-iii/description/
2402.Meeting Rooms III

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi]
means that a meeting will be held during the half-closed time interval [starti, endi).
All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free.
The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original
start time should be given the room.
Return the number of the room that held the most meetings.
If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts
in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts
in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0.
Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2
for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1
for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1.


Constraints:

1 <= n <= 100
1 <= meetings.length <= 105
meetings[i].length == 2
0 <= starti < endi <= 5 * 105
All the values of starti are unique.
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def clean_rooms(start_meet, avail_rooms, end_meets_q, end_meets_map):
        next_end_meet = end_meets_q[0]
        while end_meets_q and next_end_meet <= start_meet:
            heapq.heappop(end_meets_q)
            new_avail_room = heapq.heappop(end_meets_map[next_end_meet])
            heapq.heappush(avail_rooms, new_avail_room)
            if not end_meets_map[next_end_meet]:
                del end_meets_map[next_end_meet]
            next_end_meet = end_meets_q[0] if end_meets_q else None
        return avail_rooms, end_meets_q, end_meets_map

    def most_booked(self, n: int, meetings: List[List[int]]) -> int:
        MAX_ROOM = 101
        avail_rooms = [i for i in range(n)]
        start_meets_q = []
        meets_map = dict()
        end_meets_q = []
        end_meets_map = dict()
        meets_n_map = {i: 0 for i in range(n)}

        for s, e in meetings:
            start_meets_q.append(s)
            meets_map[s] = e

        heapq.heapify(start_meets_q)
        heapq.heapify(avail_rooms)
        heapq.heapify(end_meets_q)

        while start_meets_q:
            start_meet = heapq.heappop(start_meets_q)
            end_meet = meets_map[start_meet]
            if end_meets_q:
                avail_rooms, end_meets_q, end_meets_map = self.clean_rooms(
                    start_meet, avail_rooms, end_meets_q, end_meets_map
                )
            avail_room = avail_rooms[0] if avail_rooms else MAX_ROOM
            if end_meets_q and end_meets_q[0] in end_meets_map:
                next_room_end_meet = end_meets_map[end_meets_q[0]][0]
            else:
                next_room_end_meet = MAX_ROOM

            if avail_room < next_room_end_meet or (
                avail_room != MAX_ROOM
                and avail_room > next_room_end_meet
                and end_meets_q
                and start_meet < end_meets_q[0]
            ):
                # empty room
                heapq.heappop(avail_rooms)
                heapq.heappush(end_meets_q, end_meet)
                if end_meet in end_meets_map:
                    heapq.heappush(end_meets_map[end_meet], avail_room)
                else:
                    end_avail_rooms_q = [avail_room]
                    heapq.heapify(end_avail_rooms_q)
                    end_meets_map[end_meet] = end_avail_rooms_q
                meets_n_map[avail_room] += 1

            else:
                next_end_meet = end_meets_q[0]
                if start_meet < next_end_meet:
                    # need to postpone meet
                    end_meet = end_meet + (next_end_meet - start_meet)
                    meets_map[start_meet] = end_meet
                heapq.heappop(end_meets_q)
                heapq.heappop(end_meets_map[next_end_meet])
                if not end_meets_map[next_end_meet]:
                    del end_meets_map[next_end_meet]
                heapq.heappush(end_meets_q, end_meet)
                if end_meet in end_meets_map:
                    heapq.heappush(end_meets_map[end_meet], next_room_end_meet)
                else:
                    end_avail_rooms_q = [next_room_end_meet]
                    heapq.heapify(end_avail_rooms_q)
                    end_meets_map[end_meet] = end_avail_rooms_q
                meets_n_map[next_room_end_meet] += 1

        meets_n_map_inverted = defaultdict(list)
        for k, v in meets_n_map.items():
            meets_n_map_inverted[v].append(k)
        max_n_meetings = max(meets_n_map.values())
        best_rooms = meets_n_map_inverted[max_n_meetings]
        best_rooms.sort()

        return best_rooms[0]


if __name__ == "__main__":
    n_rooms = 3
    meetings_list = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    sol = Solution()
    print(sol.most_booked(n_rooms, meetings_list))
