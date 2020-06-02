import reports
# Printing functions

def print_count_games(file_name):
    number_of_games=reports.count_games(file_name)
    print("How many games are in the file ? {}".format(number_of_games))

def print_decide(file_name):
    print("Is there a game from a given year ? ")
    year_input=input("Choose a year: ")
    true_or_false=reports.decide(file_name,year_input)
    print(true_or_false)

def print_latest(file_name):
    latest_game=reports.get_latest(file_name)
    print("Which is the latest game ? {}".format(latest_game))

def print_count_by_genre(file_name):
    print("How many games are in the file by genre ?")
    genre=input("Choose a genre: ")
    games_number_by_genre=reports.count_by_genre(file_name,genre)
    print(games_number_by_genre)

def print_line_number_by_title(file_name):
    print("What is the line number of a given title ? ")
    title=input("Choose a title: ")
    line_number=reports.get_line_number_by_title(file_name,title)
    print(line_number)

def print_sorted_titles(file_name):
    stitle=reports.sort_abc(file_name)
    print("Can you give me the alphabetically ordered list of the titles? {}".format(stitle))

def print_sorted_genres(file_name):
    print("Which genres occur in the data file ?" )
    sortedgen=reports.get_genres(file_name)
    print(sortedgen)

def print_release_date(file_name):
    releasedate=reports.when_was_top_sold_fps(file_name)
    print("What is the release year of the top sold first-person shooter game? {}".format(releasedate))

def main():
    file_name=input("What is the name of the data file ? ")
    if file_name=="game_stat.txt":
        print_count_games(file_name)
        print_decide(file_name)
        print_latest(file_name)
        print_count_by_genre(file_name)
        print_line_number_by_title(file_name)
        print_sorted_titles(file_name)
        print_sorted_genres(file_name)
        print_release_date(file_name)
    else:
        print("file not found")
        main()
main()










    # x=input("What is the name of the data file ?: ")
    # if x="game_stat.txt":
    #     print("1. How many games are in the file?")
    #     print("2. Is there a game from a given year?")
    #     print("3. Which is the latest game?")
    #     print("4. How many games are in the file by genre?")
    #     print("5. What is the line number of a given title?")
    #     print("6. Can you give me the alphabetically ordered list of the titles?")
    #     print("7. Which genres occur in the data file")
    #     print("8. What is the release year of the top sold first-person shooter game?")

