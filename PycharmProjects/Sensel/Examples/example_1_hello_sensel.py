
from SenselUse import sensel

if __name__ == "__main__":

    handle = None
    (error, device_list) = sensel.getDeviceList()
    if device_list.num_devices != 0:
        (error, handle) = sensel.openDeviceByID(device_list.devices[0].idx)
    if handle != None:
        (error, info) = sensel.getSensorInfo(handle)

        print("\nSensel Device: "+str(bytearray(device_list.devices[0].serial_num)))
        print("Width: "+str(info.width)+"mm")
        print("Height: "+str(info.height)+"mm")
        print("Cols: "+str(info.num_cols))
        print("Rows: "+str(info.num_rows))
        error= sensel.close(handle)

