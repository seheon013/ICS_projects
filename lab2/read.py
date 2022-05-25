from pathlib import Path 
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    with open(file,'r') as csvfile:
        csvdata = csv.reader(csvfile)
        output_data = []
        for i,a in enumerate(csvdata):
            if i == 0 and a[0] != "City": 
                raise ValueError
            elif i == 0 and a[1] != "Team Name":
                raise ValueError
            elif i == 0 and a[2] != "Sport":
                raise ValueError   
                
            if len(a) != 3:
                raise ValueError
            if a[0] == '' or a[1] == '' or a[2] == '':
                raise ValueError
            if i > 0:
                output_data.append(tuple(a))
        return output_data
    

def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """

    p = Path("C:\\Users\\wlstn\\Downloads\\122937758").glob("*.csv")

    file_count = 0
    unique_teams = []
    
    team_list = []
    report = open("report.txt","w")
    error = open("error_log.txt", "w")
    for files in p:
        try:
            input_file = readFile(files)
            file_count += 1
            unique_teams.append(input_file)
        except ValueError:

            error.write(str(files)+"\n")
            continue

    outputs = []
    new_outputs = []
    for teams in unique_teams:
        for i in teams:
            
            clubs = SportClub(i[0], i[1], i[2], 0)
            team_list.append(i[1])
            if clubs.getName() not in outputs:
                new_outputs.append(clubs)
                outputs.append(clubs.getName())
    
    for teams in new_outputs:
        teams.count = team_list.count(teams.name)           

    report.writelines("Number of files read: " + str(file_count) + "\n")
    report.writelines("Number of lines read: " + str(len(team_list))+"\n")
    
    return new_outputs

