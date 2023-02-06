import math

with open("DATA11.txt", "r") as f:
    # read the lines from the file and store them in a list
    lines = f.readlines()
    # initialize an empty list to store the results
    results = []
    # iterate over the lines in groups of 3
    for i in range(0, len(lines), 3):
        # set the total cost to the first cell in the list
        total_cost = int(lines[i])

        # order the second line found into a list
        percentages = list(map(float, lines[i + 1].strip().split()))

        # for loop to put each of the 4 floats into a list
        for j in range(len(percentages)):
            if j == 0:
                y1 = percentages[j]
            elif j == 1:
                y2 = percentages[j]
            elif j == 2:
                y3 = percentages[j]
            else:
                y4 = percentages[j]

        # n is the number of students
        n = int(lines[i + 2])

        # calculate the funds and append the result to the list
        y1 = y1 * n
        y2 = y2 * n
        y3 = y3 * n
        y4 = y4 * n

        # calculate which grade of students has the most so I can
        # add all the "extra" students to the end of the one with the most.
        if y1 > y2 and y1 > y3 and y1 > y4:
            # finds the extra decimal
            # ex. 307.15 - 307 = 0.15
            y2_floor = y2 - math.floor(y2)
            y3_floor = y3 - math.floor(y3)
            y4_floor = y4 - math.floor(y4)

            # calculate floor total by add ing up all the decimals
            floor_total = y2_floor + y3_floor + y4_floor

            # add the floor total to the most amount of students
            y1 = y1 + floor_total

        # if y2 has the most students
        elif y2 > y1 and y2 > y3 and y2 > y4:
            y1_floor = y1 - math.floor(y1)
            y3_floor = y3 - math.floor(y3)
            y4_floor = y4 - math.floor(y4)

            floor_total = y1_floor + y3_floor + y4_floor
            y2 = y2 + floor_total

        # if y3 has the most students
        elif y3 > y1 and y3 > y2 and y3 > y4:
            y1_floor = y1 - math.floor(y1)
            y2_floor = y2 - math.floor(y2)
            y4_floor = y4 - math.floor(y4)

            floor_total = y1_floor + y2_floor + y4_floor
            y3 = y3 + floor_total

        # if y4 has the most students
        elif y4 > y1 and y4 > y2 and y4 > y3:
            y1_floor = y1 - math.floor(y1)
            y2_floor = y2 - math.floor(y2)
            y3_floor = y3 - math.floor(y3)

            floor_total = y1_floor + y2_floor + y3_floor
            y4 = y4 + floor_total

        # calculate the money each student is going to give
        # if there is still a decimal number it floors
        y1 = math.ceil(y1) * 12
        y2 = math.ceil(y2) * 10
        y3 = math.ceil(y3) * 7
        y4 = math.ceil(y4) * 5

        # add up the total money
        money = y1 + y2 + y3 + y4

        # divide the money we raise by 2, we can only use 50%
        money /= 2

        # if the total money is greater than or equal to the total cost
        # print no if they don't need to raise more funds
        # print yes if they do need to raise more funds
        if money >= total_cost:
            print("NO")
        else:
            print("YES")
