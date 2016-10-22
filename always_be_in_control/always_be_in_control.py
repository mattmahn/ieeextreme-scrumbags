#!/bin/env python


a2_set = [0, 0, 1.880, 1.023, .729, .577, .483, .419, .373, .337, .308]


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        process_test_case()


def process_test_case():
    line = [int(x) for x in input().split()]
    num_data_points = line[0]
    subgroup_size = line[1]

    ranges = []
    averages = []

    index = 2
    for _ in range(int(num_data_points / subgroup_size)):
        subgroup_index = 0
        subgroup_average = 0
        subgroup_smallest = line[index]
        subgroup_largest = line[index]
        while subgroup_index < subgroup_size and index <= num_data_points + 1:
            subgroup_average += line[index]
            if line[index] < subgroup_smallest:
                subgroup_smallest = line[index]
            if line[index] > subgroup_largest:
                subgroup_largest = line[index]
            subgroup_index += 1
            index += 1

        ranges.append(subgroup_largest - subgroup_smallest)
        subgroup_average /= subgroup_index
        # print('subgroup avg:', subgroup_average)
        averages.append(subgroup_average)

    range_avg = sum(ranges) / len(ranges)
    x_avg = sum(averages) / len(averages)

    ucl = x_avg + (a2_set[subgroup_size] * range_avg)
    lcl = x_avg - (a2_set[subgroup_size] * range_avg)

    sigma = (ucl - x_avg) / 3

    last_5_points = []
    points_above = []
    points_below = []

    out_of_control = False

    for point in line[2:]:
        if point > ucl or point < lcl:
            # print('Out of Control')
            out_of_control = True
            break

        if point > x_avg:
            points_above.append(point)
            if len(points_above) >= 8:
                # print('Out of Control')
                out_of_control = True
                break
            del points_below[:]

            if point > x_avg + 2*sigma:
                prev_points_2_sig_over = 0
                for p in last_5_points[3:]:
                    if p > x_avg + 2*sigma:
                        prev_points_2_sig_over += 1
                if prev_points_2_sig_over >= 1:
                    # print('Out of Control')
                    out_of_control = True
                    break
            if point > x_avg + sigma:
                prev_points_1_sig_over = 0
                for p in last_5_points[1:]:
                    if p > x_avg + sigma:
                        prev_points_1_sig_over += 1
                if prev_points_1_sig_over >= 3:
                    # print('Out of Control')
                    out_of_control = True
                    break
        elif point < x_avg:
            points_below.append(point)
            if len(points_below) >= 8:
                # print('Out of Control')
                out_of_control = True
                break
            del points_above[:]

            if point < x_avg - 2*sigma:
                prev_points_2_sig_under = 0
                for p in last_5_points[3:]:
                    if p < x_avg - 2*sigma:
                        prev_points_2_sig_under += 1
                if prev_points_2_sig_under >= 1:
                    # print('Out of Control')
                    out_of_control = True
                    break
            if point < x_avg - sigma:
                prev_points_1_sig_under = 0
                for p in last_5_points[1:]:
                    if p < x_avg - sigma:
                        prev_points_1_sig_under += 1
                if prev_points_1_sig_under >= 3:
                    # print('Out of Control')
                    out_of_control = True
                    break

        last_5_points.append(point)
        if len(last_5_points) > 5:
            last_5_points.pop(0)

    if out_of_control:
        print('Out of Control')
    else:
        print('In Control')


main()
