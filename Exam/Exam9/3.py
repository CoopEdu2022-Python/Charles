# 2.3  Find the Highest Altitude
# There is a biker going on a road trip.
# The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip at point 0 with altitude equal to 0.
# You are given an integer array gain of length n
# where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.
def largest_altitude(gain: list[int]) -> int:
    highest = 0
    road_list = [0]
    for items in gain:
        highest += items
        road_list.append(highest)
    return max(road_list)


print(largest_altitude([-5,1,5,0,-7]))
print(largest_altitude([-4,-3,-2,-1,4,3,2]))
