# Driver Safety Awareness project

System name: Safe Driver Coaching System

* Develop a basic prototype
    * learn more about the subject of safe driving, sensors, data processing, machine learning
    * to find out if its possible to develop a cost effective solution
    * to demonstrate its capabilities
* If this first step succeeds, try to interest parties to actually develop and use such systems
* If not then I have lost nothing and learned a lot.

Use case:
* Promote safe driving habits
* Improve safe driving behaviour
* Help to prevent car accidents
* Lower costs for society

Possible business cases:
* Car lease (safety as a service, reduce accidents)
* Insurance (reduce accidents)
* Road service organization (safety for its members)

Description:

The "Driver Coach" will help the driver of a car to improve its safety by providing feedback just like any regular coach. 
The system is based on a camera and sensors that monitors the driver's behaviour during a road trip.

When a driver enters the car he/she is automatically recognized.
During the trip the system continuously determines the actual driving situation (parked, cruising, braking, turning) and evaluates the drivers activity and behaviour.
It provides an audible warning when the driver gets tired and requires a break.
It immediately alerts the driver when a dangerous situation occurs, such as texting while driving. 

After each trip the system sends a summary to the driver's smartphone for quick review. When at home specific situations can be reviewed in depth with the Driving Coach App. The App will show snapshots or short video with detailed data and advise for improvement.

The collected data is kept on the device under full control of the driver and can be deleted when required. Data can be shared anonymously for specific applications such as a safe driver leader board  where drivers can compare themselves with other drivers.

![image](doc/driver-monitoring.jpg )

Monitor driver behavior:
  * Good driving habits
    * Wearing seat belt
    * Active driving posture
    * Hands on the steering wheel
    * Looking to the general driving direction
    * Checking for traffic from all directions
    * Left/right/rear mirror checking
   * Abstain from distractions
     * Mobile phone usage (handheld, call, texting)
     * Operating the radio / airco
     * Talking to passengers
     * Eating or drinking
     * Other (looking for something, singing)
   * Driver physics
     * Body, arm and hand position
     * Head pose (rotation, looking direction)
     * Driver drowsiness
       * Eye blinking/closed
       * Head bobbing
       * Mouth yawning
  
  
 Tools and technology
 
 * Driver Sensors
    * Face location (is there a driver)
    * Driver recognition (who is driving)
    * Head Pose estimation (looking direction)
    * Face landmarks (eyes, mouth)
    * Hand location (on steering wheel)
    * Image classification of dangerous situations
 * Vehicle sensors
    * Acceleration (left/right turn, breaking)
    * Vehicle speed
 * Tools
    * Python, OpenCV (CV2), Dlib, fast.ai
    * Python-video-annotator [code](https://github.com/chan0park/video-annotation-tool) / [documentation](https://pythonvideoannotator.readthedocs.io/en/master/index.html)
    * UAH DriveSet Reader [git](https://github.com/Tauvic/uah_driveset_reader)
 * Datasets
    * Eyeblink8 [dataset](https://www.blinkingmatters.com/research)
    * Columbia Gaze DataSet [link](https://www.cs.columbia.edu/CAVE/databases/columbia_gaze/)
 * Example solutions
   * Futurebridge [link](https://www.futurebridge.com/blog/driver-monitoring-from-essential-safety-to-passenger-wellness/)
 * Example code:
    * Learn Open CV Examples [code](https://github.com/spmallick/dlib)
    * Aontoine Lame GazeTracking [code](https://github.com/antoinelame/GazeTracking)
    * CNN Human face detector [model](http://arunponnusamy.com/files/mmod_human_face_detector.dat)
    
    Selecting the best face detection method:
    Source: Face Detection – OpenCV, Dlib and Deep Learning ( C++ / Python ) [link](https://www.learnopencv.com/face-detection-opencv-dlib-and-deep-learning-c-python/)
    ![face-detection](doc/face-detection-comparison.jpg)