import pandas as pd
from tabulate import tabulate


def search_data(name):
    # appending '.json' to fetch the file by the name it is receiving from the parent function
    df = pd.read_json(name + ".json")
    # converting dataframe values to string because we need to normalize the datatypes of all the values to perform generic searching
    df = df.applymap(str)
    column = input("Enter the search field name: ")
    if column in df:
        data = input("Enter the value you want to search in the field: ")
        # print(df.loc[df[column] == data] + '\n')
        result_df = df.loc[df[column] == data]
        print(tabulate(result_df, headers='keys',
              tablefmt='psql', showindex=False))
    else:
        print("Column '{0}' not found in data".format(column))


def print_columns(df, name):
    print("*****************************************************")
    print("Search '{0}' with:".format(name))
    for column in df.columns:
        print(column)
    print("*****************************************************\n")


def view_search_fields():
    users_df = pd.read_json('users.json')
    organizations_df = pd.read_json('organizations.json')
    tickets_df = pd.read_json('tickets.json')
    print_columns(users_df, 'Users')
    print_columns(organizations_df, 'Organizations')
    print_columns(tickets_df, 'Tickets')


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
        selection = int(selection)
        if selection == 1:
            print("Select:\n 1) Users \n 2) Organizations \n 3) Tickets\n")
            selection_step_2 = input("Enter your selection: ")
            selection_step_2 = int(selection_step_2)
            if (selection_step_2 == 1):
                search_data('users')
            elif (selection_step_2 == 2):
                search_data('organizations')
            elif (selection_step_2 == 3):
                search_data('tickets')
        elif selection == 2:
            view_search_fields()
        else:
            print("You have entered invalid selection.\n")


def main():
    while (True):
        print_main_menu()


main()
