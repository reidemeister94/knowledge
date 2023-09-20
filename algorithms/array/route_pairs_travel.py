import operator


def routePairs(maxTravelDist, forwardRouteList, returnRouteList):
    valid_pairs = [[]]
    min_diff = float("inf")
    forwardRouteList = sorted(forwardRouteList, key=operator.itemgetter(1))
    print(forwardRouteList)
    print(returnRouteList)
    for id_route_return, distance_return in returnRouteList:
        print(id_route_return, distance_return)
        idx_left = 0
        idx_right = len(forwardRouteList)
        distance_difference = maxTravelDist - distance_return
        while idx_left < idx_right:
            idx_mid = (idx_left + idx_right) // 2
            if forwardRouteList[idx_mid][1] <= distance_difference:
                idx_left = idx_mid + 1
            else:
                idx_right = idx_mid
            print(forwardRouteList[idx_left - 1][1])
        current_difference = maxTravelDist - (
            distance_return + forwardRouteList[idx_left - 1][1]
        )
        if current_difference < min_diff and current_difference > 0:
            min_diff = current_difference
            valid_pairs = [[forwardRouteList[idx_left - 1][0], id_route_return]]
        elif current_difference == min_diff:
            valid_pairs.append([forwardRouteList[idx_left - 1][0], id_route_return])
        print(current_difference)
        print(min_diff)
        print(valid_pairs)
        print("=" * 75)
    return valid_pairs


f = [[1, 10], [2, 20], [3, 30], [4, 40]]
r = [[1, 10], [2, 20], [3, 30], [4, 40]]
t = 5

# f = [[1, 2000], [2, 4000], [3, 6000]]
# r = [[1, 2000]]
# t = 7000

# f = [[1, 8], [2, 15], [3, 9]]
# r = [[1, 8], [2, 11], [3, 12]]
# t = 20

print(routePairs(t, f, r))
