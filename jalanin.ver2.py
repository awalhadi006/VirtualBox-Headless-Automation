import os
import time
import subprocess

VM_UUID = "{3a9cbd66-88f2-43d2-88a9-aebc492c64ba}"
password = "admin"


# Mendefinisikan fungsi `scancode_table`
def scancode_table():
  return {
   "error": 0x00,  # Error code
  "esc": 0x01,
  "1": 0x02,
  "2": 0x03,
  "3": 0x04,
  "4": 0x05,
  "5": 0x06,
  "6": 0x07,
  "7": 0x08,
  "8": 0x09,
  "9": 0x0a,
  "0": 0x0b,
  "-": 0x0c,
  "=": 0x0d,
  "backspace": 0x0e,
  "tab": 0x0f,
  "q": 0x10,
  "w": 0x11,
  "e": 0x12,
  "r": 0x13,
  "t": 0x14,
  "y": 0x15,
  "u": 0x16,
  "i": 0x17,
  "o": 0x18,
  "p": 0x19,
  "[": 0x1a,
  "]": 0x1b,
  "enter": 0x1c,
  "lctrl": 0x1d,
  "a": 0x1e,
  "s": 0x1f,
  "d": 0x20,
  "f": 0x21,
  "g": 0x22,
  "h": 0x23,
  "j": 0x24,
  "k": 0x25,
  "l": 0x26,
  ";": 0x27,
  "'": 0x28,
  "`": 0x29,
  "lShift": 0x2a,
  "\\": 0x2b,
  "z": 0x2c,
  "x": 0x2d,
  "c": 0x2e,
  "v": 0x2f,
  "b": 0x30,
  "n": 0x31,
  "m": 0x32,
  ",": 0x33,
  ".": 0x34,
  "/": 0x35,
  "rShift": 0x36,
  "lAlt": 0x38,
  "space": 0x39,
  "capsLock": 0x3a,
  "f1": 0x3b,
  "f2": 0x3c,
  "f3": 0x3d,
  "f4": 0x3e,
  "f5": 0x3f,
  "f6": 0x40,
  "f7": 0x41,
  "f8": 0x42,
  "f9": 0x43,
  "f10": 0x44,
  "numLock": 0x45,
  "scrollLock": 0x46,
  "kp7": 0x47,
  "kp8": 0x48,
  "kp9": 0x49,
  "-": 0x4a,
  "kp4": 0x4b,
  "kp5": 0x4c,
  "kp6": 0x4d,
  "+": 0x4e,
  "kp1": 0x4f,
  "kp2": 0x50,
  "kp3": 0x51,
  "enter": 0x52,
  "kpEnter": 0x52,
  "rctrl": 0x53,
  "kpDel": 0x53,
  "/": 0x54,
  "sysrq": 0x55,
  "alt-print": 0x57,
  "home": 0x58,
  "up": 0x59,
  "pageUp": 0x5a,
  "-": 0x5b,
  "left": 0x5c,
  "center": 0x5d,
  "right": 0x5e,
  "+": 0x5f,
  "end": 0x60,
  "down": 0x61,
  "pageDown": 0x62,
  "insert": 0x63,
  "delete": 0x64,
  "lWin": 0x65,
  "rWin": 0x66,
  "menu": 0x67,
  "f11": 0x75,
  "f12": 0x76,
  }

def key_release_scancode(scancode):
    return hex(scancode | 0x80)[2:].zfill(2)  # Set bit ke-7 untuk menandakan key release


# Memulai VirtualBox Headless
subprocess.Popen(["C:/Program Files/Oracle/VirtualBox/VBoxHeadless.exe", "--comment", "Windows 10 Ghost Spectre", "--startvm", VM_UUID], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

# Menunggu sebentar untuk memastikan VM telah dimulai
time.sleep(17)

# Mengirimkan kunci ke virtual mesin (spasi)
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "39", "b9"])
time.sleep(1)

# Mengirimkan password secara otomatis
password_value = password
for char in password_value:
  scancode = scancode_table().get(char.lower(), None)
  if scancode is None:
    raise ValueError(f"Karakter '{char}' tidak ditemukan dalam tabel scancode.")
  subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", hex(scancode)[2:].zfill(2), key_release_scancode(scancode)])
  time.sleep(1)

# Menekan tombol "Enter"
subprocess.run(["C:/Program Files/Oracle/VirtualBox/VBoxManage.exe", "controlvm", VM_UUID, "keyboardputscancode", "1c", "9c"])
