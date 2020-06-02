NAME=0
COPIES=1
YEAR=2
GENRE=3
COMPANY=4



def open_file(file_name):
    with open(file_name) as f:
        my_list=[line.split("\t")for line in f]
    return my_list
    
def count_games(file_name):
    lists=open_file(file_name)
    return len(lists)

def decide(file_name, year):
    lists=open_file(file_name)
    for item in lists:
        if int(item[2])==year:
            return True
    return False

def get_latest(file_name):
    lists=open_file(file_name)
    latest_year=int(lists[NAME][YEAR])
    game=""
    for item in lists:
        current_year=int(item[YEAR])
        if current_year>latest_year:
            latest_year=current_year
            game=item[NAME]
    return game

def count_by_genre(file_name, genre):
    lists=open_file(file_name)
    count=0
    for item in lists:
        if item[GENRE]==genre:
            count+=1
    return count

def get_line_number_by_title(file_name, title):
    lists=open_file(file_name)
    counter=0
    for item in lists:
        counter+=1
        if item[NAME]==title:
            return counter
    raise ValueError("Not Found")

def sorting(x):
    for i in range (0,len(x)-1):
        for j in range(0,len(x)-i-1):
            if x[j]>x[j+1]:
                temp=x[j]
                x[j]=x[j+1]
                x[j+1]=temp
    return x

def sort_abc(file_name):
    lists=open_file(file_name)
    my_list=[]
    for item in lists:
            my_list.append(item[0])
    return sorting(my_list)

def get_genres(file_name):
    lists=open_file(file_name)
    new_list=[]
    my_list=[]
    for item in lists:
        my_list.append(item[3])
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
    return sorting(new_list)

def when_was_top_sold_fps(file_name):
    lists=open_file(file_name)
    copies=0
    for items in lists:
        sold_copies=float(items[1])
        if items[3]=="First-person shooter" and sold_copies>copies:
            copies=sold_copies
            year=items[2]
    if year:
        return year
    else:
        raise ValueError("Error")