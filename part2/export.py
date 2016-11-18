# Export functions

import reports

file_name = "game_stat.txt"
title = "Age of Empires"

def export_reports(file_name):
    save_file = open("reports.txt", "w")
    save_file.write("1. What is the title of the most played game?")
    save_file.write("\n")
    save_file.write(str(reports.get_most_played(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("2. How many copies have been sold total?")
    save_file.write("\n")
    save_file.write(str(reports.sum_sold(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("3. What is the average selling?")
    save_file.write("\n")
    save_file.write(str(reports.get_selling_avg(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("4. How many characters long is the longest title?")
    save_file.write("\n")
    save_file.write(str(reports.count_longest_title(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("5. What is the average of the release dates?")
    save_file.write("\n")
    save_file.write(str(reports.get_date_avg(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("6. What properties has a game?")
    save_file.write("\n")
    save_file.write(str(reports.get_game(file_name, title)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("7. How many games are there grouped by genre?")
    save_file.write("\n")
    save_file.write(str(reports.count_grouped_by_genre(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("8. What is the date ordered list of the games?")
    save_file.write("\n")
    save_file.write(str(reports.get_date_ordered(file_name)))
    save_file.write("\n")

    save_file.close()

export_reports("game_stat.txt")