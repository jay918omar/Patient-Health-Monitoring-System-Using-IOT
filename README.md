# Patient-Health-Monitoring-System-Using-IOT
My team has created a project under "IOT Fundamentals" course that is using ThingSpeak, IFTTT, ArduinoUNO, Twitter and Flask (to show the data on a created webpage using JSON).

Methodologu ---

Here in this project, we will make an IoT based Health Monitoring System which records the patient body temperature, movement and the distance from the other patients. After 
sensing these readings from the sensors controlled by arduino, we send it to the our own created ThingSpeak channel to visualize it in different field graphs & for any further. 
We read those values in ThingSpeak and do MATLAB analysis to develop the conditions according to the status of the patient suggested by the readings from the patients. When these 
conditions are met, MATLAB analysis will throw a patient’s status and write it in the ThingSpeak channel itself. Then we are using this status from the MATLAB analysis to make 
tweet in Twitter with help of React app in ThingSpeak. After making tweet, we are using those tweets to send an email to the doctor about the status of patient with the help of 
IFTTT.

