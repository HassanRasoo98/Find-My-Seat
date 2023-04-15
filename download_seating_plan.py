from utilities import download_element, setup_driver

def download_pdf(url, usr, pas, time_url=''):
    '''
        this function serves to download the seating plan pdf and time table of examsfrom the slate
        website url provided it uses selenium to navigate to the website, to enter login credentials,
        and to download the seating plan pdf in project folder

        args:
            url: url to seating plan pdf presented on slate
            usr: username of slate id
            pas: password of slate id
            time_url: url of time table schedule of examination, works if user sets time = True

        returns: nothing
    '''

    slate_login = False # no need to login again if already logged in once
    if url != '' :
        driver = setup_driver()
        print('[DOWNLOADING SEATING PLAN]    Please Wait...!')
        download_element(driver, url, usr, pas, slate_login)
        print('[DOWNLOADING SEATING PLAN]    COMPLETE!')
        slate_login = True

    if time_url != '':
        driver = setup_driver()
        print('[DOWNLOADING EXAM SCHEDULE]    Please Wait...!')
        download_element(driver, time_url, usr, pas, slate_login)
        print('[DOWNLADING EXAM SCHEDULE]    COMPLETE!')