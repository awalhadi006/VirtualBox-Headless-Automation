@echo off
set VM_UUID={3a9cbd66-88f2-43d2-88a9-aebc492c64ba}
set PASSWORD=admin

REM Memulai VirtualBox Headless
start "" /min "C:\Program Files\Oracle\VirtualBox\VBoxHeadless.exe" --comment "Windows 10 Ghost Spectre" --startvm "%VM_UUID%"

REM Menunggu sebentar untuk memastikan VM telah dimulai
timeout /t 30 >nul

REM Mengirimkan kunci ke virtual mesin (spasi)
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm %VM_UUID% keyboardputscancode 39 b9
timeout /t 1 >nul

REM Mengirimkan password karakter per karakter
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm %VM_UUID% keyboardputscancode 1e 9e
timeout /t 1 >nul
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm %VM_UUID% keyboardputscancode 20 a0
timeout /t 1 >nul
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm %VM_UUID% keyboardputscancode 32 b2
timeout /t 1 >nul
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm %VM_UUID% keyboardputscancode 17 97
timeout /t 1 >nul
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm %VM_UUID% keyboardputscancode 31 b1
timeout /t 1 >nul

REM Menekan tombol "Enter"
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm %VM_UUID% keyboardputscancode 1c 9c