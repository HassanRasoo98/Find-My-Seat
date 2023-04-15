import os

from utilities import get_user_info, end_screen, get_filename
from GmailAPI import connect
from download_seating_plan import download_pdf
from pdf_extract2 import extract_pdf_data

def main():
  name, roll_number, usr, pas, n, time = get_user_info()
  url, url2 = connect(n, time) # connect to GMAIL api and fetch slate url
  # print(url, url2, sep='\n\n')

  # function to download seating plan pdf and final exam schedule if user asked for it
  download_pdf(url, usr, pas, url2)

  doc = get_filename('.pdf')
  print('[EXTRACTING PDF]    Please Wait!', end = '\n\n')
  extract_pdf_data(doc, name, roll_number, time)
  print('[EXTRACTING PDF]    Complete!')

  end_screen()

if __name__ == '__main__':
    main()