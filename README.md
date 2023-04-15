# Find-My-Seat
a simple find my seat command line tool to find seat #, exam hall, exam time of a certain student just by running one command.

Important: YOU NEED FIREFOX TO RUN THIS SHIT OTHER WISE CHANGE THE SELENIUM CODE YOURSELF. I'M TIRED.

Instructions:
1. Open cmd on windows or bash terminal on linux systems.
2. Navigate to the folder containing project.
3. type command "python FindMySeat.py". type in arguments for additional functionality. Also see: Arguments.
4. type in your name and batch and last 4 digits of your roll number. Name does not matter but batch and roll number
	must be correct.
5. wait and see the results.

Note: in cases where two sections are adjusted in the same room, the registered section of the student may appear wrong.
but finding that is not the focus of this program so please ignore it. or better yet maybe help me to fix this lol.

the time functionality is not generalized yet. It is hard coded because I am lazy and I have been working for too long on this project and now I just want to share it ASAP.
may be I will fix it or maybe not.

leave a rating. thanks for using this program.
in case of feedback or review or complaint, kindly write an email to me at hassanrasool1057@gmail.com

To-do:
1. include a parameter time, which, when set to True, also displays the timing of the exam. done.
2. Add arguments functionality. done
3. add references to code snippets taken from the internet.
4. try a different pdf module. done.
5. correct inorrect results. done.
6. correct display of section is cases where there are two sections.
7. Make dialog box to take input argument values instead of command line arguments (use PySimpleGUI). done
8. download final version of the timetable from gmail api. done

Python Modules used for this project:
1. Gmail Api
2. Selenium
3. PdfMiner (discarded)
4. EasyGui
5. PyPdf
6. PyQt5 (even though not explicitly used, this module is used in EasyGui module)
7. Pandas

deployment issues with Gmail Api approve from google first. 

4. Lab Seat Numbers are not catered in this program (implemented not tested).

unsequential thoughts represented as a poem:
"
i keep doing things that don't matter at all.
these types of projects don't have much worth i feel.
but that could because of the envrionment i am setup in
my mind can go only as far as my surroundings allow me to think!
"
