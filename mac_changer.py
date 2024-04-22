import subprocess

print("""
  __  __                  ____ _                                 
 |  \/  | __ _  ___      / ___| |__   __ _ _ __   __ _  ___ _ __ 
 | |\/| |/ _` |/ __|____| |   | '_ \ / _` | '_ \ / _` |/ _ \ '__|
 | |  | | (_| | (_|_____| |___| | | | (_| | | | | (_| |  __/ |   
 |_|  |_|\__,_|\___|     \____|_| |_|\__,_|_| |_|\__, |\___|_|   
                                                 |___/           
""")

print("\n")

print("Author : Jevaa kharthik N")
print("Contact : jevaakharthik@gmail.com")
mac_address = input("Enter mac address to change : ")

subprocess.call("sudo ifconfig en0 down", shell=True)
subprocess.call("sudo ifconfig en0 hw ether {}".format(mac_address), shell=True)
subprocess.call("sudo ifconfig en0 up", shell=True)
