# Following Assistant Robot
This project is aimed toward building a Raspberry Pi robot which utilizes machine learning to follow a leader object based on its color.


## How to run:
1) Follow the instructions in section 5 “Hardware Implementation” of our report to build the same robot we used.
2) Make sure to have a separate power supply for the motors and the Raspberry Pi.
3) To run the Raspberry Pi server you have to make sure you are running Raspbian OS on your RPI.
4) Install socket/OpenCV/python3 if you have any missing libraries (everything is installed by default on Raspbian OS).
5) Run the file called “MOTOR.py” on your Raspberry Pi. This is the main code for the server and FAR’s following algorithm.
- Note that you have to configure the IP address and the port of the socket according to your Raspberry Pi (You can refer to the comments in the code to find the instructions regarding this).

## The repository includes:
- Presentation File "Docs/Team3_Presentation"
- Source Code Files in the Directory "Source Code"
- Manual for Running the Code "Docs/Team3_Manual"
- Report and Design Document "Docs/Team3_Report"
