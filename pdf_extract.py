from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

def get_seat(temp_page, name, roll_number):
    string = ''
    for element in temp_page:
        if isinstance(element, LTTextContainer):
            string += element.get_text()

    a = string.split('\n')

    seats = []
    for value in a:
        try:
            if 'Seat' in value:
                seats.append(value)
            elif value[0] == 'C' and value[2] == 'R':
                seats.append(value)
        except:
            continue

    ind = a.index('Name of Invigilator:')

    names2 = []
    for i in a[:ind]:
        if not i.isnumeric():
            names2.append(i)

    names = names2[names2.index('sheets')+1:]

    roll_nos = []
    skip_next_iteration = False
    for name in names:
        if skip_next_iteration:
            skip_next_iteration = False
            continue

        if len(name) == 8:
            skip_next_iteration = True

        roll_nos.append(name)
    roll_nos, len(roll_nos)
    roll_numbers = []
    names = []
    for number in roll_nos:
        temp = number.split()
        roll_numbers.append(temp[0])
        try:
            names.append(temp[1] + ' ' +  temp[2])
        except:
            names.append('')
    
    index = roll_numbers.index(roll_number)
    print(roll_numbers)
    return seats[index], roll_numbers[index], names[index]

def extract_pdf_data(doc, name='Ahmed Yaqoob', roll_number='20I-1865'):
    temp_page = None
    print('[FINDING NAME]       Please Wait...')
    for page_layout in extract_pages(doc):
        room = None
        
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                temp = element.get_text()
                temp_element = element

                if 'Room' in temp:
                    room = temp
                if roll_number in temp:
                # if name in temp:
                    # if name found in this page, i want to store this page  
                    temp_page = page_layout
                    seat, roll, name = get_seat(temp_page, name, roll_number)
                    
                    print(room, end = '')
                    print(name, roll, seat, sep= '\n')