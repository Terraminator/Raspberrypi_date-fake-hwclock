# Raspberrypi_date-fake-hwclock
Synchronize your system date with fake-hwclock
<pre>
 __    __  .______    _______       ___   .___________. _______      __    __  ____    __    ____  ______  __        ______     ______  __  ___ 
|  |  |  | |   _  \  |       \     /   \  |           ||   ____|    |  |  |  | \   \  /  \  /   / /      ||  |      /  __  \   /      ||  |/  / 
|  |  |  | |  |_)  | |  .--.  |   /  ^  \ `---|  |----`|  |__       |  |__|  |  \   \/    \/   / |  ,----'|  |     |  |  |  | |  ,----'|  '  /  
|  |  |  | |   ___/  |  |  |  |  /  /_\  \    |  |     |   __|      |   __   |   \            /  |  |     |  |     |  |  |  | |  |     |    <   
|  `--'  | |  |      |  '--'  | /  _____  \   |  |     |  |____     |  |  |  |    \    /\    /   |  `----.|  `----.|  `--'  | |  `----.|  .  \  
 \______/  | _|      |_______/ /__/     \__\  |__|     |_______|____|__|  |__|     \__/  \__/     \______||_______| \______/   \______||__|\__\ 
                                                              |______|                                                                                                                                                                                        
</pre>

### Usage
You can run this script with for example nohup python3 main.py > output.txt to hide the output and write it into output.txt and synchronize your Sytem date with fake-hwclock. You can set your system date with raspi-config or on kali linux with timedatectl.  
To put this script in autostart you can create a cronjob with crontab -e then you select nano by typing 2 and add the line @reboot nohup python3 path_to_main.py > path_to_output.txt .

## Ascii Art  
The Ascii Art is made with: https://patorjk.com/software/taag/
