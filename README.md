# RHAB
The Rose State High Altitude Ballon project started in the fall of 2016 as an idea from professor Bill Richards. This idea was simple, we put a raspberry pi with a senseHAT in a box, attach it to a weather balloon, and launch it. This idea expanded, I was the project lead for the payload, or the box itself. Throughout the semester my team came up with other ideas for this payload. It ended up having a Eagle Flight Computer with a radio bug, a raspberry pi 3 with a senseHAT and a camera module all in a 3d printed case, and having 4 cameras in total; 1 pi camera, 2 cannon cameras, 1 sony action camera. Overall the flight was a success and we are already planning for RHAB 2 with better features.

Flight statistics
- Highest altitude: 101,834 feet
- Distance traveled: 39.8 miles from launch site
- Lowest Temperature: -11 Degrees Farenheit
- Flight duration: 4 hours 30 minutes

Hardware
 - Eagle Flight Computer
   - Had an unlocked GPS so it could operate over 65,000 feet
   - The computer also had a temperature module which we placed outside the payload to measure the outside temperature.
   - The radio bug attached to it was a HAM radio trasnmitter
      - The bug would transmit packets which included speed of the payload, alitude, GPS cordinates, and temperature

  - Raspberry pi 3
    - Connected to it was four buttons, a senseHAT, and a camera
    - We powered the pi with a 4000 Mah external battery pack

  - Cannon 
    - These cameras did not have the funtionality to take pictures at intervals
    - Professor Richards found the CHDK (CannonHackersDevelopmentKit) which allowed the cameras to run cutsom scripts
    - We then wrote a simple script to take a picture every minute
    - sadly the cannon cameras died only 2 hours into the flight.
    
Software
  - massterScript.py
    - Written to take the input from the different sensors on the sense HAT
    - Writes all the measurments to a log file

  - cameraIGuess.py
    - Written to take video the first 30 minutes of the flight
    - After the video ends it will start taking pictures, one every 30 seconds

  - masterBut.py
    - Waits for in input from one of the buttons that is connected to the pi
    - Once that button is pressed it will launch masterScript.py

  - cameraBut.py
    - Similar to masterBut.py but it launches cameriaIGuess.py
