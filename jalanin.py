import os
import time
import subprocess

VM_UUID = "{3a9cbd66-88f2-43d2-88a9-aebc492c64ba}"

# Memulai VirtualBox Headless
subprocess.Popen(["C:/Program Files/Oracle/VirtualBox/VBoxHeadless.exe", "--comment", "Windows 10 Ghost Spectre", "--startvm", VM_UUID], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

# Menunggu sebentar untuk memastikan VM telah dimulai
time.sleep(30)

# Mengirimkan kunci ke virtual mesin (spasi)
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "39", "b9"])
time.sleep(1)

# Mengirimkan password karakter per karakter
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "1e", "9e"])
time.sleep(1)
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "20", "a0"])
time.sleep(1)
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "32", "b2"])
time.sleep(1)
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "17", "97"])
time.sleep(1)
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "31", "b1"])
time.sleep(1)

# Menekan tombol "Enter"
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "1c", "9c"])
