# Driver Safety Awareness project

System name: Safe Driver Coaching System

## Why we all should have a personal driving coach
<img align="right" width="300" src="https://github.com/Tauvic/DriverAwareness/blob/master/doc/distracted.jpg"/>

Of all car accidents 94 percent are caused by driver error and 57 percent by distracted driving.
A system that helps the driver to focus its attention on driving can reduce injuries and damages.
My objective is to develop an affordable personal driving coach that will help the driver.
Therefore I have open sourced my code and hope companies and organisations will step in and take over.

## How can we make driving safer? 
Its so easy to get distracted. The "Driver Coach" is a system that will help the driver of a car to improve its safety by providing feedback just like any regular coach. 
The system is based on a camera and sensors that monitor the driver's behaviour during a road trip.

|Use case|Business case|
|----------|-----------|
|* Promote safe driving habits|* Car lease (safety as a service, reduce car accidents)
| * Improve safe driving behaviour|* Insurance (reduce car accidents)
| * Help to prevent car accidents|* Road service organizations (safety for its members)
| * Make Driver Monitoring systems available for low cost|* Driving school (feedback)
| * Lower costs for society|

My plan is to develop a demo to verify its feasibility, then a prototype to further investigate requirements.


### Following a step by step approach

Developing a driver monitoring system is not a trivial task, and there are several ways to get there. 
The easiest is of course just to buy such a system from a reliable supplier or develop one using a toolkit. 
But this may be expensive or not suit your needs. And how do you get the expertise to choose the right solution?
I decided to try to develop one myself to see how far I can come. Its an interesting project.

* Develop a basic prototype
    * learn more about the subject of safe driving, sensors, data processing, machine learning
    * build a proof of concept based on a simple system such as laptop / webcam / smartphone
    * find out if its possible to develop the POC into a cost effective solution
    * demonstrate its capabilities
* If this first step succeeds, try to interest parties to actually further develop and use such systems
* If not then I have lost nothing and learned a lot.

## How the system works

<img align="right" width="300" src="https://github.com/Tauvic/DriverAwareness/blob/master/doc/driver-monitoring.jpg">
When a driver enters the car he/she is automatically recognized.
During the trip the system continuously determines the actual driving situation (parked, cruising, braking, turning) and evaluates the drivers activity and behaviour.
It provides an audible warning when the driver gets tired and requires a break.
It immediately alerts the driver when a dangerous situation occurs, such as texting while driving. 



After each trip the system sends a summary to the driver's smartphone for quick review. 
When at home specific situations can be reviewed in depth with the Driving Coach App. 
The App will show snapshots or short video with detailed data and advise for improvement.

The collected data is kept on the device under full control of the driver and can be deleted when required. Data can be shared anonymously for specific applications such as a safe driver leader board  where drivers can compare themselves with other drivers.

## Monitoring driver behavior

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
  
  
![img](doc/drivers_statefarm.png)  


 ## Challenges
 
 * System design
     * Specifications (domain knowledge
     * Determine actual driving state based on sensor data
     * Combine driving state with driver activity and evaluate its behavior (scoring)
 * System limitations (processing power, battery consumption, operating system)
 * Physical conditions
    * Lighting conditions
    * Vibrations
    * Mounting (where, how, car types)
 * Calibration & Testing (test data)
 * Legal issues
 
 
## Tools and technology
 
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
    * StateFarm Distracted Driver dataset [link](https://www.kaggle.com/c/state-farm-distracted-driver-detection)
    * Eyeblink8 [dataset](https://www.blinkingmatters.com/research)
    * Columbia Gaze DataSet [link](https://www.cs.columbia.edu/CAVE/databases/columbia_gaze/)
    * DMD - Driving Monitoring Dataset [link](https://dmd.vicomtech.org/)
 * Example solutions
   * Futurebridge [link](https://www.futurebridge.com/blog/driver-monitoring-from-essential-safety-to-passenger-wellness/)
 * Example code:
    * Learn Open CV Examples [code](https://github.com/spmallick/dlib)
    * Brain4Cars technical research [website](http://brain4cars.com/)
    * Ground AI Real-Time Driver State Monitoring
                Using a CNN Based Spatio-Temporal Approach*
[link](https://www.groundai.com/project/real-time-driver-state-monitoring-using-a-cnn-based-spatio-temporal-approach/1)
    * Gaurav Shadev Drowsiness Detection [github](https://github.com/Gauravsahadev/Drowsiness-detection-and-alert-system-DDAS-)
    * Aontoine Lame GazeTracking [code](https://github.com/antoinelame/GazeTracking)
    * CNN Human face detector [model](http://arunponnusamy.com/files/mmod_human_face_detector.dat)
    
    Selecting the best face detection method:
    Source: Face Detection – OpenCV, Dlib and Deep Learning ( C++ / Python ) [link](https://www.learnopencv.com/face-detection-opencv-dlib-and-deep-learning-c-python/)
    ![face-detection](doc/face-detection-comparison.jpg)