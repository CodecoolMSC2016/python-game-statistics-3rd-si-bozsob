# Report functions
import csv
import operator

#How many games are in the file? output: a number
def count_games(file_name):
    with open(file_name, "r") as my_file:
        count = 0
        for line in my_file:
            count += 1
    return count
    

#Is there a game from a given year? output: boolean
def decide(file_name, year):
    with open(file_name, "r") as my_file:
        if str(year) in my_file.read():
            return True
        else:
            return False


#Which was the latest game? output: a title (string)
#(if there is more than one, then return the first from the file)
def get_latest(file_name):
    my_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            my_list.append(line.strip().split("\t"))
    my_list = sorted(my_list, key = operator.itemgetter(2))
    return my_list[-1][0]
    

#How many games do we have by genre? output: a number
def count_by_genre(file_name, genre):
    genre_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            genre_list.append(line.strip().split("\t"))
    sum_genre = sum(line.count(genre) for line in genre_list) 
    return sum_genre


#What is the line number of the given game (by title)? output: a number
#if there is no game found, then raises ValueError exception
def get_line_number_by_title(file_name, title):
    my_list = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            my_list.append(line.strip().split("\t"))
        for index, line in enumerate(my_list, 1):
            if title in line:
                return index


#What are the genres? output: a list of the genres (without duplicates, in alphabetical order)
def get_genres(file_name):
    genres = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            temp_list = line.strip().split("\t")
            if temp_list[3] not in genres:
                genres.append(temp_list[3])
            else:
                continue
    genres = sorted(genres, key = str.lower)
    return genres


#What is the release date of the top sold "First-person shooter" game?
#output: year of the release, as integer
#(if there is no game with genre "First-person shooter" then raises ValueError exception
def when_was_top_sold_fps(file_name):
    fps = "First-person shooter"
    fps_game = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            temp_list = line.strip().split("\t")   
            if temp_list[3] == fps:
                temp_list[1] = float(temp_list[1])
                fps_game.append(temp_list)
                
    fps_game = sorted(fps_game, key = operator.itemgetter(1))
    return int(fps_game[-1][2])                


#What is the alphabetical ordered list of the titles? output: a list of strings
def sort_abc(file_name):
    games = []
    with open(file_name, "r") as my_file:
        for line in my_file:
            temp_list = line.strip().split("\t")
            games.append(temp_list[0])
        games = sorted(games, key = str.lower)
    return games