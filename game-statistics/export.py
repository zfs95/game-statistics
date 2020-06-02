import reports
# Export functions
saved_list=[]
saved_list.append(reports.count_games("game_stat.txt"))

the_year=input("Choose a year. ")
if reports.decide("game_stat.txt",the_year)==True:
    saved_list.append(True)
else:
    saved_list.append(False)

saved_list.append(reports.get_latest("game_stat.txt"))

what_genre=input("Choose a genre: ")
saved_list.append(reports.count_by_genre("game_stat.txt",what_genre))

what_title=input("Choose a titel: ")
saved_list.append(reports.get_line_number_by_title("game_stat.txt",what_title))

saved_list.append(reports.sort_abc("game_stat.txt"))

saved_list.append(reports.get_genres("game_stat.txt"))

saved_list.append(reports.when_was_top_sold_fps("game_stat.txt"))

def file_write(file_name,a_list):
    with open(file_name,"w") as f:
        for item in a_list:
            f.write("%s\n" % item)

file_write("new_text.txt",saved_list)