import base64
import email
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from utilities import generate_url

def get_messages(service, user_id = 'me'):
  try:
    return service.users().messages().list(userId=user_id).execute()
  except Exception as error:
    print('An error occurred: %s' % error)

def get_mime_message(service, user_id, msg_id):
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()
    # print('Message snippet: %s' % message['snippet'])
    msg_str = base64.urlsafe_b64decode(message['raw'].encode("utf-8")).decode("utf-8")
    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except Exception as error:
    print('An error occurred: %s' % error)

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def connect(n = 10, time = False):
    '''
        the purpose of this function is to connect to gmail api
        then parse emails to find the email containing seating plan
        then parse that email to get slate url and timetable url if time flag is set True

        args: n: number of latest emails to search for seating plan email. default value = 10
              time: bool. download timetable to display timing of exam along with seat no and room
        returns: generated url to pdf file, generated url to timetable if time flag = True
    '''
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
      service = build('gmail', 'v1', credentials=creds)

      print('[PARSING EMAILS]   Please Wait...')

      seating_plan = False
      exam_schedule = False
      url1 = ''
      url2 = ''

      for i in range(n):
        # print(i)
        a = get_messages(service)
        b = a['messages'][i]
        msg_id = b['id']

        gmailMessage = get_mime_message(service, 'me', msg_id)
        try:
           temp = gmailMessage._payload[0].as_string()
        except:
           temp = gmailMessage._payload[0]
        
        # check for seating plan in email
        if seating_plan==False and 'Seating Plan' in temp and 'CS Academic Office' in temp:
           print('[PARSING EMAILS]    Seating Plan Found!')
           url1 = generate_url(temp, 7, 3, 1)
           seating_plan = True

           if time and not exam_schedule:
             continue
           elif not time:
              print('[PARSING EMAILS]    COMPLETE!')

        # check for final time table version in email
        if exam_schedule==False and 'exams schedule' in temp.lower() or 'exam schedule' in temp.lower():
          # print(temp, type(temp))
          print('[PARSING EMAILS]     TimeTable Found!')
          exam_schedule = True

          url2 = generate_url(temp, 9, 3, 1)          
          
        if seating_plan and exam_schedule:
           print('[PARSING EMAILS]    COMPLETE!')
           return url1, url2
        
        # break

      print('Seating plan not found! Try increasing the number of n (number of emails to search)')
      print('You can search last 100 emails for the pdf.')
      return url1, url2

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

