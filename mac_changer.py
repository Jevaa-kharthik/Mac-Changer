import subprocess
import re

def change_mac_address(interface, new_mac):
    try:
        # Check if the entered MAC address is valid
        if not re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', new_mac):
            print("Invalid MAC address format. Please enter a valid MAC address.")
            return

        # Bring down the network interface
        subprocess.call(["sudo", "ifconfig", interface, "down"])

        # Change the MAC address
        subprocess.call(["sudo", "ifconfig", interface, "ether", new_mac])

        # Bring the interface back up
        subprocess.call(["sudo", "ifconfig", interface, "up"])

        print(f"MAC address of {interface} changed successfully to {new_mac}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(r"""
      __  __                  ____ _
     |  \/  | __ _  ___      / ___| |__   __ _ _ __   __ _  ___ _ __
     | |\/| |/ _` |/ __|____| |   | '_ \ / _` | '_ \ / _` |/ _ \ '__|
     | |  | | (_| | (_|_____| |___| | | | (_| | | | | (_| |  __/ |
     |_|  |_|\__,_|\___|     \____|_| |_|\__,_|_| |_|\__, |\___|_|
                                                     |___/
        """)
    print("Author : Jevaa kharthik N")
    print("Contact : jevaakharthik@gmail.com")
    while True:
        interface = input("Enter the network interface name (e.g., en0): ")
        if interface.lower() == "quit" or interface.lower() == "exit":
            break
        new_mac = input("Enter the new MAC address: ")
        if new_mac.lower() == "quit" or new_mac.lower() == "exit":
            break
        change_mac_address(interface, new_mac)

