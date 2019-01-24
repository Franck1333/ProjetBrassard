# Projet Brassard
  
This software has been develloped to build a connected Armband by using a Raspberry Pi + Python (w/Tkinter) and a Awesome 4inch display by Pimoroni.

For the people who love to walk in the Nature, you will be able to get useful details about the environement where you are by Using an USB GPS and some API with an Internet USB Modem, plus Weather forecast with the GPS coordinates and ISS position in real time and more...

In this project, you will be able to interact to the software with a Tkinter graphic user interface.
  
## Getting Started  
  
To get a copy of the project , you can go on the GitHub's webpage of the project and click on the green button to download as a .ZIP file. However , if you're using a prompt console on an Unix machine use this line :

```
git clone https://github.com/Franck1333/ProjetBrassard.git
```
  
### Prerequisites  
  
To use the project , you will need some Hardware :
  
```  
A Raspberry Pi (Last Version is better)
A USB G.P.S (Ublox-7) -->  http://amzn.eu/aG9vR3t
A USB 2G/3G/EDGE Modem (Huawei E3531) --> https://amzn.to/2T8SXWa
A Micro S.D card (8 Gb Minimum)
A Display like the Pimoroni 4inch HyperPixel Display --> https://bit.ly/2FVOy5j
* A 3D Printed case for your device --> https://bit.ly/2Cyd9ti *
```  
  And you will also need some libraries and softwares :

```
- Python version 2
	- Python Libraries:
		-os
		-sys
		-datetime
		-time
		-Tkinter
		-ttk
		-serial
		-unicodedata
		-requests
		-json
		-geopy
		-unicodecode
		-urllib
		-pyowm
		-urllib2
		-PIL
		-cStringIO
		-random
		-io
		-commands
		-unirest
		
-Software needed:
	- Raspbian (The Latest version is better)
	- The Virtual Keyboard #1 "**FLORENCE**"
		Command Line: sudo apt-get install florence && sudo apt-get install at-spi2-core
	-The Virtual Keyboard #2 "Matchbox"
		Command Line: sudo apt-get install matchbox-keyboard
```

Now especially for the *Pimoroni HyperPixel 4* in our case :

```
	- The Github page : https://github.com/pimoroni/hyperpixel4
	- The command line Setup (need to be install) : https://get.pimoroni.com/hyperpixel4 | bash 
```
  
### Downloading/Installing - EASY WAY !!!  
To get and downloaded the files , use this line : 
```
git clone https://github.com/Franck1333/ProjetBrassard.git
```
- When the project is Downloaded , check your "pi" folder , and you will see the folder "ProjetBrassard"
When you did it , you will have to launch the file called "setup.py" to install the dependencies neccessary for the project with this command line : 

```
  sudo python setup.py install
```

### This commmand line must be executed anyway to install the Virtual Keyboard  *Florence* : 

#### The  *Florence's* Software :
```
  sudo apt-get install florence && sudo apt-get install at-spi2-core
```

### This commmand line must be executed anyway to install the  *Pimoroni Hyperpixel 4* : 

#### The  *Pimoroni HyperPixel 4's* Software :

```
  https://get.pimoroni.com/hyperpixel4 | bash
```

## Run
#### First Way to run the project :
To run the project , you can run the small script file called "Start.sh" in the main folder ; it's will launch the project in the background.

#### Second Way to run the project :
To run the project ; if you want to see the console activities , you can launch the file called "BrassardMain.py"  into the Command Line Prompt with "sudo python BrassardMain.py" in the main folder.

#### The Last Way to run the project :
To run the Project with a G.I.U ; if you want the project run automatically when system start-up ; Go to launch a Prompt and type:

```
>>>sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
>>@/home/pi/ProjetBrassard/Start.sh
```

## Running the tests  
  
That's how to test features:

    sudo python file.py

## The Folders and Files

In this project we've got three folders

#### Folders
```
Example 	: 	Any help or example that I used for the project
Extra 		: 	Various (Not-main) programs and some (ideas) features that maybe will be developped in the future
GPS 		:	Main features use the GPS USB STICK or in realtion with GPS data
```
#### Files in "/ProjetBrassard/Extra/"
 - MISC and Future features
```
 - Deezer_Recherche.py : This extra feature allows you to search an Artist,song or an Album on Deezer.com via your prompt.
 - Deezer_top_chart.py : This extra feature allows you to get the Top10 on Deezer.com.
 - Deezer_top_chart_suggest.py : This extra feature allows you to get a single song randomly of the Top10 on Deezer.com.
 - Infos_Hardware.py : This feature allows you to get useful data about the Hardware on board.
 - food_suggest.py : This extra feature allows you to get a random recipe from many recipes websites. 
 - nettoyage_du_cache.py : This useful feature allows you to clean up your folder of the Python cache files.
```
 - Folder inside
 ```
 - ChatPython : This is an attempt to integrate a chat into the project with Tkinter
 ```

#### Files in "/ProjetBrassard/GPS/"
- GPS data
```
- Boussole.py : Get Compass data by using the "Recuperation_Determination.py" file's data.
- GPSoI.py : Get the location of the user's IP Adress.
- Meteo.py : Get the Weather's data by using *pyown API* and the "Recuperation_Determination.py" file's data.
- Recuperation_Determination.py : Get information come from the GPS USB stick and determinate the location.
- ISS_locate.py : Get data about the ISS location in real time and the forecast of the next visible passage of the I.S.S in the sky above your head.
- Map_YANDEX.py : Get a map in the JPG format about your location and the ISS location in real time.
- emergency_number.py : Get the emergencies Numbers from where your IP adress is located in the world.
- nettoyage_du_cache.py : This useful feature allows you to clean up your folder of the Python cache files.
```
 - Folders inside
 ```
 - Divers : Some files that help me to try few ideas
 - MAP_downloads : Here will be downloaded the .JPG map by Yandex Services 
 ```

## Authors

-   **Franck ROCHAT**  -  _Initial work_  -  [Franck ROCHAT](https://github.com/Franck1333)  Thank You !  :heart:
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIyMzIwMzM2NSw3NDM1NjU0MDEsLTIyOD
MyNDIxMSwxMjU2MTU4MTIxLDE3NDkyODYwOTYsMTk2OTcwMjk2
LC0xNDQ3NDc2NTE2LDIwODYyNTI4NDgsLTQ5Mzk3NjA1NF19
-->
