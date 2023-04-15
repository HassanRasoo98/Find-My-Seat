'''helper functions for the smooth running of the program'''
import os
import time
import easygui_qt as easy
from selenium import webdriver
from selenium.webdriver.common.by import By

from FrontEnd import get_details, get_username_password, get_time, get_n
from saved_data import file_already_exists

def save_user_info(name, roll_number):
  fhandle = open('user_details.txt', 'w')
  fhandle.write(name + ' ' + roll_number)
  fhandle.close()  

def get_user_info():
  if file_already_exists('user_details.txt'):
    # read from this file instead of getting user input again
    msg = 'Do you want to use previous input details (name, roll#). If you select No then you will have to enter these details again!'
    prev_details = easy.get_yes_or_no(title='Use previous details?', message=msg)
    if prev_details:
      # read from file
      fhandle = open('user_details.txt', 'r')
      a = fhandle.readline().split()
      name = a[:-1]
      roll_number = a[-1]
      usr, pas = get_username_password()
      time = get_time()
      n = get_n()
      
    else:
      # get new details
      name, roll_number, usr, pas, n, time = get_details()
      save_user_info(name, roll_number)

  else:
    name, roll_number, usr, pas, n, time = get_details()
    save_user_info(name, roll_number)

  return name, roll_number, usr, pas, n, time

def generate_url(temp: list, alpha=7, beta=3, gamma=1):
  '''alpha beta and gamma are names of hyper(hardcoded parameters)'''
  temp = temp.split()
  # truncate the list upto where attachments is
  a = temp.index('Attachments:') + alpha # a bit of hard coding here
  temp = temp[a:][:beta] # this is where the url is

  # this for loop will remove redundant '=' sign from the desired url of the seating plan pdf
  for j in range(len(temp)):
    if '=' in temp[j]:
        temp[j] = temp[j][:len(temp[j])-gamma]

  url = ''.join(temp)
  url = url[1:len(url)-1]
  return url
  
def download_wait(directory, timeout, nfiles=None):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.
    timeout : int
        How many seconds to wait until timing out.
    nfiles : int, defaults to None
        If provided, also wait for the expected number of files.

    """
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True

        seconds += 1
    return seconds

def download_element(driver, url, usr, pas, login=False):
    # go to the designated url
    driver.get(url)

    # if not login: # no need to login again if already logged in one time
    # find and enter login credentials of slate website
    username = driver.find_element(By.ID, "eid")
    password = driver.find_element(By.ID, "pw")

    username.send_keys(usr)
    password.send_keys(pas)

    driver.find_element(By.ID, 'submit').click()
    download_wait(os.path.abspath(os.path.curdir), 5, 1)
    driver.quit()

    # if login:
    #    driver.quit()
    

def end_screen():
   msg = '''
      PLEASE FIND YOUR RESULTS ON THE TERMINAL SCREEN.
      Thank You for using this program. Did you find it satisfactory? Did you enjoy using it?
      Did you face any issues? Kindly submit your feedback to me at hassanrasool1057@gmail.com
      Stay Blessed!
   '''
   easy.show_text(title='The End', text=msg)

def setup_driver():
  # the profile object is setup with random stuff from the internet
  # basically it is a configuration to download pdf files from the web
  # the profile object is then sent to the webdriver object
  profile = webdriver.FirefoxProfile()
  profile.set_preference("browser.download.folderList", 2)
  profile.set_preference("browser.download.manager.showWhenStarting", False)
  profile.set_preference("browser.download.dir", os.path.abspath(os.path.curdir))
  profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

  profile.set_preference("pdfjs.disabled", True)

  driver = webdriver.Firefox(firefox_profile=profile)
  return driver

def get_filename(extension: str):
  doc = None
  for subdir, dirs, files in os.walk('./'):
    for file in files:
      if file.endswith(extension):
        doc = file # the name of the downloaded pdf file
        break

  return doc