"""Dictionary microservice, with funcations to add values and search.

Program prompts user to point to a csv based list of items. Program then imports
the list into memory. Once in memory, user can add values via a text based command file.
Program returns boolien variables based on command

Commands:
    search:<value> : command written to command file to search dictionary for <value>
    add:<value> : Command written to command file to add <value> to the dictionary
    delete:<value>

Returns:
    results:<bool> : Response written to command file based on command passed
                     True for when value found during searche or added to dictionary
                     False for when values not found during search


"""
import csv
import os
import time

def SetDict():
    """ Prompts user for local path to CSV list to populate dictionary

    Function takes path for CSV list opens the file and imports each value
    strips and lowers each before adding ot the dictionary. Once done the 
    dict is returned 

    Args:
        None
    
    Returns:
        new_dict :: dictionary based on CSV provided at console prompt

    """

    new_dict = {}
    while len(new_dict) == 0:
        #Local path to CSV text file with entires on new lines.
        print("Please enter the path for a CSV formated dictionary to load:")        
        dict_path = str(input())
    
        if os.path.isfile(dict_path): # check if valid path
            try:
                print("Trying to open file")
                dict_csv = csv.reader(open(dict_path, "r"))
        
            except: 
                print("There was an error while trying to opening the file.")
        
            for row in dict_csv: 
                key = row[0].lower()
            
                if key not in new_dict:
                    item = row[0].strip().lower()
                    new_dict[item] = True
                    print(key + " was added ")
            
                else:
                    print(key + " was already in the dictionary.")
                    continue
    
        else:
            print("The path does not seem to be valid.")
    
    return new_dict


def SetCommandFile():
    """Function sets the location of the command text file

    Args:
        None

    Returns:
        command_file_path :: Command file path

    """
    command_file_path = None
    while command_file_path is None:
        print("Please enter the path for command_file.txt:") 
        command_file_path = str(input())
    
        if os.path.isfile(command_file_path) is False:
            print("The path seems to be invalid or command_file.txt does not exist in this location.")
            command_file_path = None

    return command_file_path


def DictLookUpService(command_path, dictionary):
    """Main loop for conducting dictionary search
    
    Opens command files, reads command and then calls relevent
    function based on command

    Args:
        command_path :: path to command file
        dictionary :: dictionary based list of items 

    Returns:
        None
    
    """
    while True:
        time.sleep(2)

        command_file = open(command_path, "r")
        command_input = command_file.readline()
        command_file.close()
        command_input_list= command_input.split(sep=":", maxsplit=1)
        command = command_input_list[0].strip().lower()
    
        if command == "search":
            SearchDict(command_input_list, dictionary)
        elif command == "add":
            AddDict(command_input_list, dictionary)
        elif command == "delete":
            DeleteDict(command_input_list, dictionary)
        else:
            continue


def SearchDict(command_list, dictionary):
    """Dictionary search function 
    
    Reads value from command phrase, then searches dictionary.
    if values is found writes true to command file.

    Args:
        command_path :: path to command file
        dictionary :: dictionary based list of items 

    Returns:
        None
    
    """

    try:
        search_key = command_list[1].strip().lower()
        print("Searching for " + str(search_key))
            
        if search_key in dictionary:
            search_response = True
           
        else:
            search_response = False

        command_file = open(command_file_path, "w")
        command_file.write("result:" + str(search_response))
        command_file.close()
        
    except:
        print("There was an issue while searching for the item. Item may have been undefined.")
        search_response = False
        
    finally:
        command_file = open(command_file_path, "w")
        command_file.write("result:" + str(search_response))
        command_file.close()


def AddDict(command_list, dictionary):
    """Dictionary add item function 
    
    Reads value from command phrase, then checks if value is already in
    dictionary. If value is not found, value is added and True is wrote  
    to command file.

    Args:
        command_path :: path to command file
        dictionary :: dictionary based list of items 

    Returns:
        None
    
    """

    try:
        add_key = command_list[1].strip().lower()
        print("Trying to add " + str(add_key) + " to the dictionary.")
          
        if add_key in dictionary:
            print(str(add_key) + " is already in the dictionary.")
            
        elif len(add_key) == 0:
            print("Please enter an item to add.")
            
        else:
            gluten_dict[add_key] = True
            print(str(add_key) + " was added successfully.")

    except:
        print("There was an issue while adding the item. Item may have been undefined.")

    finally:
        command_file = open(command_file_path, "w")
        command_file.write("result:True")
        command_file.close()


def DeleteDict(command_list, dictionary):
    """Dictionary delete item function 
    
    Reads value from command phrase, then checks if value is in dictionary.
    If value is found the value is deleted and True is wrote to command file.

    Args:
        command_path :: path to command file
        dictionary :: dictionary based list of items 

    Returns:
        None
    
    """

    try:
        delete_key = command_list[1].strip().lower()
        print("trying to delete " + str(delete_key) + " from the dictionary.")

        if delete_key in dictionary:
            del dictionary[delete_key]
        else:
            print("Item was not found in dictionary.")
    
    except:
        print("There was an issue with the delete command.")
    
    finally:
        command_file = open(command_file_path, "w")
        command_file.write("result:True")
        command_file.close()


if __name__ == '__main__':
    gluten_dict = SetDict()
    command_file_path = SetCommandFile()
    DictLookUpService(command_file_path, gluten_dict)