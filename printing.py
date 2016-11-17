#for printing the output of the report functions

import reports

file_name = "game_stat.txt"
print(reports.count_games(file_name))
print(reports.decide(file_name, 2000))
print(reports.get_latest(file_name))
print(reports.count_by_genre(file_name, "First-person shooter"))
print(reports.get_line_number_by_title(file_name, "Counter-Strike"))
print(reports.get_genres(file_name))
print(reports.when_was_top_sold_fps(file_name))

#print(reports.sort_abc(file_name)) 
for i in reports.sort_abc(file_name):
    print(i)

 