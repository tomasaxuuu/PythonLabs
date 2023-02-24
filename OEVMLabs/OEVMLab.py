# системные библиотеки для получения полной информации, необходимой для решения задачи
import win32api
import win32file
import wmi

# константа с типами НМЖД
DRIVE_TYPES = """
0 	Unknown
1 	No Root Directory
2 	Removable Disk
3 	Local Disk
4 	Network Drive
5 	Compact Disc
6 	RAM Disk
"""
# инфорация лишь о типа НМЖД в системе
# с помощью словаря ищем названия НМЖД в системе и сравнием их с вариантами, заданными в нашей константе
# если совпадает, то выводим информацию на экран
drive_types = dict((int (i), j) for (i, j) in (l.split ("\t") for l in DRIVE_TYPES.splitlines () if l))

drives = (drive for drive in win32api.GetLogicalDriveStrings ().split ("\000") if drive)
for drive in drives:
  print (drive, "=>", drive_types[win32file.GetDriveType (drive)])

print('-' * 64)
# константа с типами НМЖД
DRIVE_TYPES = {
    0: "Unknown",
    1: "No Root Directory",
    2: "Removable Disk",
    3: "Local Disk",
    4: "Network Drive",
    5: "Compact Disc",
    6: "RAM Disk"
}

# вывод полной информации о каждом НМЖД
c = wmi.WMI()
for drive in c.Win32_LogicalDisk():
    # prints all the drives details including name, type and size
    print(drive)
    print(drive.Caption, drive.VolumeName, DRIVE_TYPES[drive.DriveType])
    
