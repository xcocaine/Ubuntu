import random
import os
H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

text1 = B+"""
                                                                                 
,--.  ,--. """+F+'Author: '+W+'B3@v3r'+B+""" ,--.   ,--.        ,--.                                
|  '--'  |,--.,--.,--,--, |  |   `--' ,---.,-'  '-. ,---. ,--,--,  ,---. ,--.--. 
|  .--.  ||  ||  ||      \|  |   ,--.(  .-''-.  .-'| .-. :|      \| .-. :|  .--' 
|  |  |  |'  ''  '|  ||  ||  '--.|  |.-'  `) |  |  \   --.|  ||  |\   --.|  |    
`--'  `--' `----' `--''--'`-----'`--'`----'  `--'   `----'`--''--' `----'`--'    

"""+E
text2 = G+"""
  _   _             _     _     _                       
 | | | |_   _ _ __ | |   (_)___| |_ ___ _ __   ___ _ __ 
 | |_| | | | | '_ \| |   | / __| __/ _ \ '_ \ / _ \ '__|
 |  _  | |_| | | | | |___| \__ \ ||  __/ | | |  __/ |   
 |_| |_|\__,_|_| |_|_____|_|___/\__\___|_| |_|\___|_|   
                                                        
 """+E
text3 = F+"""
                      __ _     _                       
  /\  /\_   _ _ __   / /(_)___| |_ ___ _ __   ___ _ __ 
 / /_/ / | | | '_ \ / / | / __| __/ _ \ '_ \ / _ \ '__|
/ __  /| |_| | | | / /__| \__ \ ||  __/ | | |  __/ |   
\/ /_/  \__,_|_| |_\____/_|___/\__\___|_| |_|\___|_|   
                                                       
"""+E
text4 = O+"""
 __    __                      __        __              __                                             
/  |  /  |                    /  |      /  |            /  |                                            
$$ |  $$ | __    __  _______  $$ |      $$/   _______  _$$ |_     ______   _______    ______    ______  
$$ |__$$ |/  |  /  |/       \ $$ |      /  | /       |/ $$   |   /      \ /       \  /      \  /      \ 
$$    $$ |$$ |  $$ |$$$$$$$  |$$ |      $$ |/$$$$$$$/ $$$$$$/   /$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |$$      \   $$ | __ $$    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ |  $$ |$$ \__$$ |$$ |  $$ |$$ |_____ $$ | $$$$$$  |  $$ |/  |$$$$$$$$/ $$ |  $$ |$$$$$$$$/ $$ |      
$$ |  $$ |$$    $$/ $$ |  $$ |$$       |$$ |/     $$/   $$  $$/ $$       |$$ |  $$ |$$       |$$ |      
$$/   $$/  $$$$$$/  $$/   $$/ $$$$$$$$/ $$/ $$$$$$$/     $$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       
                                                                                                        
                                                                                                                                                                                                                                                                                     
"""+E
text5 = W+"""
   __ __             __    _      __                     
  / // /__ __ ___   / /   (_)___ / /_ ___  ___  ___  ____
 / _  // // // _ \ / /__ / /(_-</ __// -_)/ _ \/ -_)/ __/
/_//_/ \_,_//_//_//____//_//___/\__/ \__//_//_/\__//_/   
                                                         
"""+E

ran = random.randrange(1,6)

if ran == 1:
	print(text1)
elif ran == 2:
	print(text2)
elif ran == 3:
	print(text3)
elif ran == 4:
	print(text4)
elif ran == 5:
	print(text5)