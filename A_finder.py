import os
import glob

FINAL_DICT = {}


def get_anime_list(file_name):
    '''(str) -> NoneType
    Gets anime list from the given CSV and saves it into a dict.'''
    anime_list = []
    csv_open = open(str(file_name), 'r')
    csv_list = csv_open.readlines()
    # Loops thought all the items in the file as a list.
    for each_list in csv_list:
        get_list = (each_list.split(',')[1])
        anime_list.append(get_list)
    # saves the databse in the dict with user as a key and data as anime_list.
    FINAL_DICT[file_name.replace('.csv', '')] = anime_list
    # Removes the title from the final dict.
    FINAL_DICT[file_name.replace('.csv', '')].remove('series_title')
    csv_open.close()


def check_anime_list(anime_name):
    '''(str) -> list of str
    Checks the final_dict and finds username and returns a list of username
    where users have watched the anime'''
    user_list = []
    txt_open = open('database.txt', 'r')
    text_dict = eval(txt_open.read())
    # Loop thought all the user and anime they watch. Loop is True iff the
    # provided anime_name matches a str.
    for each_user in text_dict:
        temp_dict = []
        for each in text_dict[each_user]:
            temp_dict.append(each.replace('"', ''))
        for each_l in temp_dict:
            if (str(anime_name) == str(each_l)):
                user_list.append(each_user)
    return user_list

if (__name__ == "__main__"):
    # Lists all the file in the database directory.
    file_list = glob.glob('*.csv')
    # Loops thought all the user and gets their dict.
    for each_name in file_list:
        get_anime_list(each_name)
    # Saves all the information/ Database into a directory.
    fx = open('database.txt', 'w')
    fx.write(str(FINAL_DICT))
    fx.close()
    get_anime_list = input('Which anime you want to search: ')
    user_watched = check_anime_list(get_anime_list)
    print(user_watched)
