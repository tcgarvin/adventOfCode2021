from collections import defaultdict, Counter
from functools import reduce
from itertools import combinations
import re
from rich import print

def get_puzzle_input():
    puzzle_input = defaultdict(list)
    with open("input.txt") as input_txt:
        current_sensor = None
        for line in input_txt:
            if len(line.strip()) == 0:
                continue

            sensor_match = re.search('scanner ([0-9]+)', line)
            if sensor_match is not None:
                current_sensor = sensor_match.group(1)

            else:
                relative_coordinates = tuple(map(int,line.strip().split(",")))
                puzzle_input[current_sensor].append(relative_coordinates)

    return puzzle_input

def rotate(beacon, rot):
    return (
        beacon[abs(rot[0])-1] * (rot[0] // abs(rot[0])),
        beacon[abs(rot[1])-1] * (rot[1] // abs(rot[1])),
        beacon[abs(rot[2])-1] * (rot[2] // abs(rot[2]))
    )

def all_rotations(beacon):
    # See Explore Rotations to see where this list came from
    results = []
    for rot in ((1, 3, -2), (-3, 1, -2), (-1, -3, -2), (3, -1, -2), (3, -2, 1),
      (2, 3, 1), (-3, 2, 1), (-2, -3, 1), (-2, 1, 3), (-1, -2, 3), (2, -1, 3), 
      (1, 2, 3), (-3, -1, 2), (1, -3, 2), (3, 1, 2), (-1, 3, 2), (-1, 2, -3), 
      (-2, -1, -3), (1, -2, -3), (2, 1, -3), (2, -3, -1), (3, 2, -1), 
      (-2, 3, -1), (-3, -2, -1)):

        results.append((rotate(beacon, rot), rot))
    return results

def solve_part_1(scanner_readings):
    # Assumption:  The 12-sized constellations of beacons are in unique patterns.  If this
    # assumption is false, we'll be in trouble.

    sensor_distances = defaultdict(Counter)
    for scanner_id, beacon_coordinates in scanner_readings.items():
        scanner_distances = sensor_distances[scanner_id]
        for ba, bb in combinations(beacon_coordinates, 2):
            distance = (ba[0] - bb[0]) ** 2 + (ba[1] - bb[1]) ** 2 + (ba[2] - bb[2]) ** 2 
            scanner_distances[distance] += 1
            #if scanner_distances[distance] > 1:
                #print(scanner_id, distance)
            #if distance == 1275089:
                #print(scanner_id, distance)

    paired_scanner_ids = set()
    paired_scanners = []
    for scanner_a, scanner_b in combinations(sensor_distances.keys(), 2):
        distances_a = set(sensor_distances[scanner_a].keys())
        distances_b = set(sensor_distances[scanner_b].keys())
        distances_in_common = distances_a.intersection(distances_b)
        if len(distances_in_common) > 12:
            paired_scanners.append((scanner_a, scanner_b))
            paired_scanner_ids.add(scanner_a)
            paired_scanner_ids.add(scanner_b)
            #if scanner_a == "4" and scanner_b in ("16", "24"):
                #print(distances_in_common)

    #print(paired_scanners)
    assert len(paired_scanner_ids.difference(sensor_distances.keys())) == 0

    normalized_readings = {'0': scanner_readings['0']}
    translations = [(0,0,0)]
    while len(normalized_readings) < len(scanner_readings):
        for scanner_a, scanner_b in paired_scanners:
            if scanner_a in normalized_readings and scanner_b in normalized_readings:
                continue
            if scanner_a not in normalized_readings and scanner_b not in normalized_readings:
                continue

            if scanner_b in normalized_readings:
                scanner_a, scanner_b = scanner_b, scanner_a

            #Normalize Scanner B to Scanner A
            scanner_b_beacons = scanner_readings[scanner_b]
            normalized_beacons = normalized_readings[scanner_a]

            candidate_transformations = Counter()
            for beacon in scanner_b_beacons:
                #print(beacon)
                for norm_beacon in normalized_beacons:
                    #print(beacon, norm_beacon)
                    for transformed_beacon, rot in all_rotations(beacon):
                        needed_translation = (
                            norm_beacon[0] - transformed_beacon[0],
                            norm_beacon[1] - transformed_beacon[1],
                            norm_beacon[2] - transformed_beacon[2]
                        )

                        candidate_transformations[(rot, needed_translation)] += 1

            #print(candidate_transformations.most_common(3))

            (rot, translation), match_strength = candidate_transformations.most_common(1)[0]
            if match_strength < 12:
                #print(scanner_a, scanner_b, "poor match?")
                continue

            translations.append(translation)

            scanner_b_normalized = []
            for beacon in scanner_b_beacons:
                b = rotate(beacon, rot)
                scanner_b_normalized.append((
                    b[0] + translation[0],
                    b[1] + translation[1],
                    b[2] + translation[2]
                ))

            normalized_readings[scanner_b] = scanner_b_normalized

    count = set()
    for s in normalized_readings.values():
        count.update(s)

    return len(count), translations

def solve_part_2(part_2_input):
    largest_manhattan_distance = 0
    for a, b in combinations(part_2_input, 2):
        manhattan_distance = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        largest_manhattan_distance = max(manhattan_distance, largest_manhattan_distance)

    return largest_manhattan_distance

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1, part_2_input = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(part_2_input)
    print(f"Part 2: {answer_2}")