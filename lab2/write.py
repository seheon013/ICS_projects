import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    
    final_list = []
    list1 = []
    for i in all_clubs:
        list1.append(i.sport)

    new_list = list(set(list1))
    for u in new_list:
        list2 = []
        for j in all_clubs:
            if u == j.sport:
                list2.append(j)
        final_list.append(list2)
    return final_list
        

def sortSport(sport: List[SportClub]) -> List[SportClub]:
    output_list = sorted(sport, key=lambda sportclub: (-sportclub.count, sportclub.name))
    return output_list
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    



def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    # TODO: Complete the function
    with open("survey_database.csv","w") as output_file:
        output_file.write("City,Team Name,Sport,Number of Times Picked\n")
        count = 0
        for i in sorted_sports:
            for j in i:
                if 3 > count >= 0:
                    output_file.write(f'{j.city},{j.name},{j.sport},{str(j.count)}'"\n")
                else:
                    break
                count += 1 
            count = 0
    