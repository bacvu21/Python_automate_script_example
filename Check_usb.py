import win32com.client

def list_usb_ports():
    wmi = win32com.client.GetObject("winmgmts:")
    usb_devices = wmi.ExecQuery("SELECT * FROM Win32_USBHub")
    for device in usb_devices:
        print(f"Device ID: {device.DeviceID}, Description: {device.Description}")

list_usb_ports()
