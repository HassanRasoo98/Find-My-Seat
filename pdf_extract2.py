from pypdf import PdfReader
from timings import get_time
# !pip install pypdf

def get_room(text):
    count = 0
    temp = None
    for entry in text:
        if 'Room' in entry:
            count += 1
            temp = entry
            
    if count > 1:
        print('(Note that registered section may appear wrong. Kindly Ignore it)')
    return temp

def helper(text, roll_number):
    find = None
    room = None
    for student in text.split('\n'):
        if roll_number in student: #or name in student:
            find = student
            room = get_room(text.split('\n'))
            return find, room

def show_data(find, room, display_time = False):
    find = find.split()

    roll = find[0]
    seat = find[-1]
    # this check is important becuase in serial numbers < 10, there appears to be no gap
    # between the roll number of the student and the serial number.
    if len(roll) == 2:
        roll = find[1]
    else:
        roll = roll[1:]

    name = find[1:]
    name = name[:-1]
    name = ' '.join(name)

    time = get_time(room)
    if display_time:
        print(room, time)
        print(name, roll, seat, sep = '\t')
    else:
        print(room)
        print(name, roll, seat, sep = '\t')

    print()

# get pdf page having name of the student
# and show results
def extract_pdf_data(doc, name, roll_number, time: bool):
    reader = PdfReader(doc)
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text = page.extract_text()
        if roll_number in text:# or name in text:
            find, room = helper(text, roll_number)
            show_data(find, room, time)