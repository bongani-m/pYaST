import os


# create files for parent function
def mk_parent_folder(parent_folder):
    f = open(parent_folder + '/run_server.py', 'w')
    f.close()


# create files for secondary function
def mk_secordary_folder(secondary_folder):
    f = open(secondary_folder + '/__init__.py', 'w')
    f.close()
    f = open(secondary_folder + '/views.py', 'w')
    f.close()
    static = secondary_folder + '/' + 'static'
    os.mkdir(static)
    templates = secondary_folder + '/' + 'templates'
    os.mkdir(templates)


# setup function create folders
def setup():
    proj_name = raw_input('So what would you like your project to be named?')
    # parent folder creations
    parent_folder = os.getcwd() + '/' + proj_name
    os.mkdir(parent_folder)
    mk_parent_folder(parent_folder)
    # secondary folder creations
    secondary_folder = parent_folder + '/' + proj_name
    os.mkdir(secondary_folder)
    mk_secordary_folder(secondary_folder)


# inro text
print "----------------------------------------------------"
print "     Welcome to pYaST for flask: micro generator    "
print "----------------------------------------------------"
print "\n\n"
print os.getcwd()
response = raw_input('do you want to continue(y/n)')
running = True
while(running):
    if(response[0].lower() == 'y'):
        setup()
        running = False
    elif(response[0].lower() == 'n'):
        running = False
    else:
        response = raw_input("please type in 'y' or 'n'")
print "With great code comes great responsibility"
print " -Wise Old Programmer"
