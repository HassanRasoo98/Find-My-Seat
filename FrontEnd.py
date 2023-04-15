import easygui_qt as easy
import datetime

from saved_data import file_already_exists

def helper():
    msg = 'Note: You are about to get a lot of dialog boxes asking you for a lot of inputs. Do you need a complete walkthrough for each input?'
    need_help = easy.get_yes_or_no(title='Need help?', message=msg)

    if need_help:
        easy.show_file(file_name='help.txt', title = 'Help')

def get_time():
    time = easy.get_yes_or_no(message='Do you want to display Time of exam along with room and seat no.?')
    return time

def get_n():
    n = easy.get_int(message='How many emails you want to search for Seating Plan Email?', default_value=10)
    return n

def get_username_password():
    if file_already_exists('login_info.txt'):
        # return id pass from this file
        fhandle = open('login_info.txt', 'r')
        all = fhandle.readline().split()
        # print(all, type(all))
        usr = all[0]
        pas = all[1]

        # print('username : {}, password : {}'.format(usr, pas))
        return usr, pas

    reply = easy.get_username_password(title='Slate Login Credentials')

    usr = reply['User name']
    pas = reply['Password']

    save = easy.get_yes_or_no(title='Save?', message='Do you want to save your login credentials to avoid logging in again in the future?')
    if save:
        # create a file and save id pass
        fhandle = open('login_info.txt', 'w')
        fhandle.write(usr + ' ' + pas)
        fhandle.close()

    return usr, pas

def get_details():
    name = easy.get_string(message="Enter your name", title='Name', default_response="Hassan Rasool")
    today = datetime.date.today()
    year = today.year
    batch = easy.get_integer("Enter Batch", default_value=20, min_=year%100 - 7, max_=year%100)

    # 4 digit roll number
    number = easy.get_string('Enter 4 digit Roll Number: ', default_response='0767')
    while len(number) != 4 or not number.isnumeric():
        number = easy.get_string('Error! Enter 4 digit Roll Number: ', default_response='0767')    

    roll_number = str(batch) + 'I-' + number    
    
    helper()

    time = get_time()
    
    n = get_n()
    usr, pas = get_username_password()

#     connect = easy.get_yes_or_no('Connect to Gmail API?')
#     if connect:
#         usr, pas = get_username_password()
#     else:
#         easy.show_message(message='Navigate to folder containing seating Plan Pdf')
#         path = easy.get_directory_name(title='Select Folder Containing Seating Plan pdf')

#         # implement a simple check here
#         doc = None
#         for subdir, dirs, files in os.walk(path):
#             for file in files:
#                 if file.endswith('.pdf'):
#                     doc = file # the name of the downloaded pdf file
#                     break
#         if doc is None:
#             # error finding file take input again.
#             easy.show_text(title='Error', text='Error finding file specified. Connect to Gmail Api or Select Folder Again')
#             get_pdf()

    return name, roll_number, usr, pas, n, time