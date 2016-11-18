# Export functions
# For exporting the reports into a single export file.
# By running this program Judy will get a single text file with all the answers she needs

import reports

file_name = "game_stat.txt"
genre = "First-person shooter"
title = "Counter-Strike"

def export_reports(file_name):
    save_file = open("answers_for_judy.txt", "w")
    save_file.write("1. How many games are in the file?")
    save_file.write("\n")
    save_file.write(str(reports.count_games(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("2. Is there a game from a given year(2000)?")
    save_file.write("\n")
    save_file.write(str(reports.decide(file_name, 2000)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("3. Which was the latest game?")
    save_file.write("\n")
    save_file.write(str(reports.get_latest(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("4. How many games do we have by genre?")
    save_file.write("\n")
    save_file.write(str(reports.count_by_genre(file_name, genre)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("5. What is the line number of the given game (by title)?")
    save_file.write("\n")
    save_file.write(str(reports.get_line_number_by_title(file_name, title)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("6. What are the genres?")
    save_file.write("\n")
    save_file.write(str(reports.get_genres(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("7. What is the release date of the top sold \"First-person shooter\" game?")
    save_file.write("\n")
    save_file.write(str(reports.when_was_top_sold_fps(file_name)))
    save_file.write("\n")

    save_file.write("\n")
    save_file.write("8. What is the alphabetical ordered list of the titles?")
    save_file.write("\n")
    save_file.write(str(reports.sort_abc(file_name)))
    save_file.write("\n")

    save_file.close()

export_reports("game_stat.txt")