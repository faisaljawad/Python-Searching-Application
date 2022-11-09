import pandas as pd

"""
This function (search_data) will take the 'name' of file/entity as input and read its corresponding .json file.
The .json file is read into a Dataframe and then all its column values are converted to string in order to normalize the data into 
generic datatype. If we do not convert this, we will have to make separate matching condition for numbers and strings.
We also validate if the selected column and its value exists in the dataframe then we proceed with our further processing.

Note: The code is tested with negative cases like when the values are incorrectly entered
"""
def search_data(name):
    # appending '.json' to fetch the file by the name it is receiving from the parent function
    df = pd.read_json(name + ".json")
    # converting dataframe values to string because we need to normalize the datatypes of all the values to perform generic searching
    df = df.applymap(str)
    column = input("Enter the search field name: ")
    if column in df:
        data = input("Enter the value you want to search in the field: ")
        result_df = df.loc[df[column] == data]
        if not result_df.empty:
            for column in result_df:
                print("{0:20} {1}".format(column, result_df[column].values[0]))
        else:
            print("\nSearching {0} for {1} with a value of {2} \nNo result found".format(name, column, data))
    else:
        print("Column '{0}' not found in data".format(column))

"""
This function (print_columns) will print the columns of provided dataframe
"""
def print_columns(df, name):
    print("*****************************************************")
    print("Search '{0}' with:".format(name))
    for column in df.columns:
        print(column)
    print("*****************************************************\n")

"""
This function (view_search_fields) will return the list of all possible columns that a user can search for in each dataframe
"""
def view_search_fields():
    users_df = pd.read_json('users.json')
    organizations_df = pd.read_json('organizations.json')
    tickets_df = pd.read_json('tickets.json')
    print_columns(users_df, 'Users')
    print_columns(organizations_df, 'Organizations')
    print_columns(tickets_df, 'Tickets')

"""
This function (print_main_menu) will print the main menu of the program that will drive the whole command line application
It can be exited anytime by selecting the 'Q' option
"""
def print_main_menu():
    print("\n*****************************************************")
    print("Welcome to my Searching System")
    print("Press 1: Search")
    print("Press 2: View a List of Searchable Fields")
    print("Press Q: Exit")
    selection = input("Enter your selection: ")
    if selection == 'quit' or selection == 'Quit' or selection == 'Q' or selection == 'q':
        print("Exiting...")
        exit()
    else:
        if selection.isnumeric():
            selection = int(selection)
            if selection == 1:
                print("Select:\n 1) Users \n 2) Organizations \n 3) Tickets\n")
                selection_step_2 = input("Enter your selection: ")
                if selection_step_2.isnumeric():
                    selection_step_2 = int(selection_step_2)
                    if (selection_step_2 == 1):
                        search_data('users')
                    elif (selection_step_2 == 2):
                        search_data('organizations')
                    elif (selection_step_2 == 3):
                        search_data('tickets')
                else:
                    print("You have entered invalid selection.\n")    
            elif selection == 2:
                view_search_fields()
            else:
                print("You have entered invalid selection.\n")
        else:
            print("You have entered invalid selection.\n")

"""
This function (main) will keep running infinitely until the user selects to quit the application from command line
"""
def main():
    while (True):
        print_main_menu()


main()
