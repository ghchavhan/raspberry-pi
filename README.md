# Raspberry-pi
Just an approach to learn Raspberry pi and its applications in day to day engineering life


Accessing Raspberry Pi from Putty and Xming

1. Start Xming

2.Start putty   
3. Assign static Address of Pi in Putty : (current add 192.168.0.8 )    
4.  in dropdown menu of SSH enable X11.     
5. Click Open 
6. for Login screen     
enter id as :pi
password: raspberry    
7. after successful login , for starting session enter :lxsession [enter]    
8. once the raspbian GUi is open fo to shell andchange the user to super user      
       Type : su
Password: a [current pass]

9.  TO access “interfaces” file from shell type:     
	sudo nano /etc/network/interfaces

change the ip (if you want to change the static ip of the Pi) like 192.168.0….     
to save and exit type : control^x     ->  y   ->  enter to accept the changes.     

To reboot the board type : reboot [Enter]     

...................................................................................................................................


General commands for shell:   
sudo raspi-config       :   for accessing Raspberry pi configurations     

First we should check for these two commands:     
1.	sudo apt-get update && sudo apt-get upgrade : for updating and upgrading the os       
2.	man      : for help command       
3.	cd: change directory        
4.	ls : LIST OF FILE  
5.	pwd: current home directory  
6.	mv : to move file   
7.	help: for help  
8.	cp : copy  
9.	sudo passwd : you can change the password of super user (hurrey…)  
10.	clear; to clear the terminal screen  
11.	exit: to exit the directory or terminal  
12.	reboot: or rebooting the system.  
13.	mkdir : to create directory  
14.	sudo nano …… : for editing a file ( like configuration file)   
15.	sudo apt-get install [software / update name]  : for installing  software or libraries or updates.  
16.	sudo apt-get update && sudo apt-get upgrade: for updating and upgrading the os .  
17.	to edit interfaces file   
first copy the original file for backup  
  cp /etc/network/interfaces /etc/network/interfaces_backup  

now edit it by using “nano” command  
sudo nano /etc/network/interfaces  
18.	for software installations  
sudo apt-get install scrot    ;    example for installing scrot software  
sudo apt-get install pistore  ;;   

...........................................................................................................................


Accessing Raspberry pi camera:  

1. shell: raspi-config  
Enable camera , and reboot/ finish.  

A. for capturing image: raspistill –o image.jpeg    will capture image and save it as image.jpeg in pi directory   

B. for capturing video: raspivid –d                   for demo capturing video.  

.................................................................................................................................

Changing Ip address of raspberry pi  

>> Sudo nano /etc/network/interfaces  
Then edit it as   
Iface eth0 inet static  
address 10.xx.xx.xx  
netmask 255.0.0.0  
gateway 10.xx.xx.xx  

then Contrl+x      Press Y to save the file  
and to restart the network services use following command  
 sudo service networking restart  


................................................................................................................................

changing keyboard layouts from default “gb”  to “US”  
sudo nano /etc/default/keyboard  

and change “gb” to “us”  

ctrl+O to save and  
ctrl+x  to exit   


....................................................................................................................................


