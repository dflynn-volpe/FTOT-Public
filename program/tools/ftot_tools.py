
import os
import lxml_upgrade_tool
import run_upgrade_tool
import scenario_compare_tool
import input_csv_templates_tool


header = "\n\
 _______  _______  _______  _______    _______  _______  _______  ___      _______\n\
|       ||       ||       ||       |  |       ||       ||       ||   |    |       |\n\
|    ___||_     _||   _   ||_     _|  |_     _||   _   ||   _   ||   |    |  _____|\n\
|   |___   |   |  |  | |  |  |   |      |   |  |  | |  ||  | |  ||   |    | |_____ \n\
|    ___|  |   |  |  |_|  |  |   |      |   |  |  |_|  ||  |_|  ||   |___ |_____  |\n\
|   |      |   |  |       |  |   |      |   |  |       ||       ||       | _____| |\n\
|___|      |___|  |_______|  |___|      |___|  |_______||_______||_______||_______|\n"



def xml_tool():
    print "You called xml_tool()"
    xml_file_location = lxml_upgrade_tool.repl()

def bat_tool():
    print "You called bat_tool()"
    run_upgrade_tool.run_bat_upgrade_tool()
    raw_input("Press [Enter] to continue...")

def compare_tool():
    print "You called compare_tool()"
    scenario_compare_tool.run_scenario_comparison_tool()
    raw_input("Press [Enter] to continue...")

def gridded_data_tool():
    print "You called gridded_data_tool()"
    # gridded_data_tool
    raw_input("Press [Enter] to continue...")

def csv_tool():
    print "You called csv_tool()"
    input_csv_templates_tool.run_input_csv_templates_tool()
    # generate_template_csv_files()
    raw_input("Press [Enter] to continue...")

def pdb():
    print "You called pdb()"
    import pdb; pdb.set_trace()
    raw_input("Press [Enter] to continue...")

menuItems = [
    { "xml_tool": xml_tool},
    { "bat_tool": bat_tool},
    { "scenario_compare_tool": compare_tool},
    { "aggregate_gridded_data": gridded_data_tool},
    { "generate_template_csv_files": csv_tool},
    { "breakpoint": pdb},
    { "exit": exit},
]

def main():
    while True:
        os.system('cls')
        print (header)
        print ('version 0.1\n')
        print ('select an option below to activate a tool')
        print ('-----------------------------------------')
        for item in menuItems:
            print("[" + str(menuItems.index(item)) + "] " + item.keys()[0])
        choice = raw_input(">> ")
        try:
            if int(choice) < 0 : raise ValueError
            # Call the matching function
            menuItems[int(choice)].values()[0]()
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
