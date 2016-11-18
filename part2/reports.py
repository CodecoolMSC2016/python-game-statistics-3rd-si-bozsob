
# Report functions

import operator
import math

# What is the title of the most played game? output: string
# if there is more than one, then return the first from the file
def get_most_played(file_name):
    my_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            temp_list = line.strip().split("\t")
            temp_list[1] = float(temp_list[1])
            my_list.append(temp_list)
        my_list = sorted(my_list, key = operator.itemgetter(1))
    return str(my_list[-1][0])

# How many copies have been sold total? output: number
def sum_sold(file_name):
    my_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            my_list.append(line.strip().split("\t"))
        for line in my_list:
            for index in line:
                line[1] = float(line[1])
        sum_sold = sum(line[1] for line in my_list)
    return float(sum_sold)

# What is the average selling? output: number
def get_selling_avg(file_name):
    my_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            my_list.append(line.strip().split("\t"))
        for line in my_list:
            for index in line:
                line[1] = float(line[1])
        sum_sold = sum(line[1] for line in my_list)
        avg_sold = sum_sold / len(my_list)
    return float(avg_sold)

# How many characters long is the longest title? output: number
def count_longest_title(file_name):
    my_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            temp_list = line.strip().split("\t")
            if temp_list[0] not in my_list:
                my_list.append(temp_list[0])
            else:
                continue
    result = max(my_list, key = len)
    return len(result)

# What is the average of the release dates? output: average year (number)
# the return value must be the rounded up average
def get_date_avg(file_name):
    my_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            temp_list = line.strip().split("\t")
            temp_list[2] = int(temp_list[2])
            if temp_list[2] not in my_list:
                my_list.append(temp_list[2])
            else:
                continue
    avg_date = sum(my_list) / len(my_list)
    avg_date = math.ceil(avg_date)
    return avg_date

# What properties has a game?
# output: a list of all the properties of the game (a list of various type)
def get_game(file_name, title):
    my_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            my_list = line.strip().split("\t")
            my_list[1] = float(my_list[1])
            my_list[2] = int(my_list[2])
            if title == my_list[0]:
                return my_list

# How many games are there grouped by genre?
# output: a dictionary with this structure: { [genre] : [count] }
def count_grouped_by_genre(file_name):
    my_dict = {}
    with open(file_name, "r") as my_file:
        for line in my_file:
            temp_list = line.strip().split("\t")
            if temp_list[3] not in my_dict:
                my_dict.update({temp_list[3]:1})
            else:
                my_dict[temp_list[3]] += 1
        return my_dict
             
# What is the date ordered list of the games? output: list of string
# The secondary ordering rule is the alphabetical ordering of the titles
def get_date_ordered(file_name):
    my_title_list = []
    year = []
    title = []   
    with open(file_name, "r") as my_file:
        for line in my_file:
            temp_list = line.strip().split("\t")
            temp_list[2] = int(temp_list[2])
            year.append(temp_list[2])
            title.append(temp_list[0])
        year_title = list(zip(year, title))
        year_title = sorted(year_title, key = lambda x:(-x[0], x[1]))
        for nested_list in year_title:
            my_title_list.append(nested_list[1])
        return my_title_list