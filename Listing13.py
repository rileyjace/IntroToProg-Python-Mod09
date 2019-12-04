# -------------------------------------------------------------------------------------------------------------------- #

# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who, When, What):
# JRiley 12.3.2019 Added Pseudo Code to start Assignment 09
# JRiley 12.3.2019 Updated code to complete Assignment 09

# -------------------------------------------------------------------------------------------------------------------- #

# TODO: Import Modules (Done)
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script ------------------------------------------------------------------------------------------------ #

lstEmployeeTable = []
lstFileData = []
Txt = "EmployeeData.txt"

# TODO: Add Data Code to the Main Body (Done)

# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file(Txt)
for row in lstFileData:
    lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

# Show user a menu of options
while True:
    Eio.print_menu_items()
    strOption = Eio.input_menu_options()

    if strOption == "1":
        # Show user current data in the list of employee objects
        Eio.print_current_list_items(lstEmployeeTable)

    elif strOption == "2":
        # Let user add data to the list of employee objects
        lstEmployeeTable.append(Eio.input_employee_data())

    elif strOption == "3":
        # Let user save current data to file
        Fp.save_data_to_file(Txt, lstEmployeeTable)

    elif strOption == "4":
        print("You have exited the program!")
        break
        #Exit the Program

# Main Body of Script ------------------------------------------------------------------------------------------------ #