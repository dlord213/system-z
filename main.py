import cpuinfo
import psutil
import datetime
import wmi
import platform
import sys
import math
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_design_ui import Ui_infoMainWindow

class mainApp(QMainWindow, Ui_infoMainWindow):

    currentDateTime = datetime.datetime.now().strftime(
        "%m/%d/%Y - %H:%M"
    )
    os_info = wmi.WMI().Win32_OperatingSystem()[0]
    sys_info = wmi.WMI().Win32_ComputerSystem()[0]
    gpu_info = wmi.WMI().Win32_VideoController()[0]
    mem_info = wmi.WMI().Win32_PhysicalMemory()
    memory_range = len(mem_info)

    bios_info = wmi.WMI().Win32_BIOS()[0]
    cpu_info = cpuinfo.get_cpu_info()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkSys()
        self.checkCPU()
        self.checkCPUFlags()
        self.checkGPU()
        self.checkMemory()
        self.infoWidget.setCurrentIndex(0)

        self.initializeBtns()

    def convert(self, bytes, to, bsize=1024):

        a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
        r = float(bytes)
        return bytes / (bsize ** a[to])

    def initializeBtns(self):
        self.homeBtn.clicked.connect(lambda: self.infoWidget.setCurrentIndex(0))
        self.cpuBtn.clicked.connect(lambda: self.infoWidget.setCurrentIndex(1))
        self.gpuBtn.clicked.connect(lambda: self.infoWidget.setCurrentIndex(2))
        self.memBtn.clicked.connect(lambda: self.infoWidget.setCurrentIndex(3))

    def checkSys(self):
        self.computerNameLbl.setText(str(platform.node()))
        self.dateTimeLbl.setText(f"Current Date/Time: {self.currentDateTime}")
        self.osLbl.setText(f"Operating System: {self.os_info.Caption}")
        self.langLbl.setText(f"Languages: {self.os_info.MUILanguages}")
        self.sysModelLbl.setText(f"System Model: {self.sys_info.Model} ({self.sys_info.Manufacturer})")
        self.biosLbl.setText(f"BIOS: {self.bios_info.Caption} ({self.bios_info.Manufacturer})")

    def checkCPU(self):
        self.cpuInfoHeadingLbl.setText(self.cpu_info['brand_raw'])
        self.cpuNumsLbl.setText(f"Number of cores & threads: {psutil.cpu_count(logical=False)} cores ({psutil.cpu_count(logical=True)} Threads)")
        self.cpuManufacturerLbl.setText(f"Manufacturer: {self.cpu_info['vendor_id_raw']}")
        self.cpuArchLbl.setText(f"Architecture: {self.cpu_info['arch']}")
        self.cpuMinHzLbl.setText(f"Minimum Clock Speed: {psutil.cpu_freq().min} GHz")
        self.cpuMaxHzLbl.setText(f"Maximum Clock Sped: {psutil.cpu_freq().max} GHz")

    def checkCPUFlags(self):
        flagList = self.cpu_info['flags']

        # COMMON INTEL-DEFINED FLAGS
        if 'lm' in flagList:
            self.lmCheck.setChecked(True)
            self.amdLMCheck.setChecked(True)
        if 'vmx' in flagList:
            self.vmxCheck.setChecked(True)
        if 'smx' in flagList:
            self.smxCheck.setChecked(True)
        if 'hypervisor' in flagList:
            self.hypervisorCheck.setChecked(True)
        if 'pae' in flagList:
            self.paeCheck.setChecked(True)
        if 'pn' in flagList:
            self.pnCheck.setChecked(True)
        if 'acpi' in flagList:
            self.acpiCheck.setChecked(True)
        if 'sse' in flagList:
            self.sseCheck.setChecked(True)
        if 'sse2' in flagList:
            self.sse2Check.setChecked(True)
        if 'ssse3' in flagList:
            self.sse3Check.setChecked(True)
        if 'sse4_1' in flagList:
            self.sse4_1Check.setChecked(True)
        if 'sse4_2' in flagList:
            self.sse4_2Check.setChecked(True)
        if 'ht' in flagList:
            self.htCheck.setChecked(True)
        if 'tm' in flagList:
            self.tmCheck.setChecked(True)
        if 'pdcm' in flagList:
            self.pdcmCheck.setChecked(True)

        # COMMON AMD-DEFINED FLAGS
        if 'mp' in flagList:
            self.mpCheck.setChecked(True)
        if 'svm' in flagList:
            self.svmCheck.setChecked(True)
        if 'abm' in flagList:
            self.abmCheck.setChecked(True)
        if 'sse4a' in flagList:
            self.sse4aCheck.setChecked(True)
        
        # COMMON ARM-DEFINED FLAGS
        if '26bit' in flagList:
            self.twoSixBitCheck.setChecked(True)
        if 'java' in flagList:
            self.javaCheck.setChecked(True)
        if 'neon' in flagList:
            self.neonCheck.setChecked(True)
        if 'lpae' in flagList:
            self.lpaeCheck.setChecked(True)
        if 'thumb' in flagList:
            self.thumbCheck.setChecked(True)

    def checkGPU(self):
        self.gpuInfoHeadingLbl.setText(f"{self.gpu_info.CurrentHorizontalResolution} x {self.gpu_info.CurrentVerticalResolution} ({self.gpu_info.CurrentBitsPerPixel}-bit depth)")
        self.gpuNameLbl.setText(f"Name: {self.gpu_info.Name}")
        self.gpuDriverVerLbl.setText(f"Driver Version: {self.gpu_info.DriverVersion}")
        self.gpuProcessorLbl.setText(f"Video Processor: {self.gpu_info.VideoProcessor}")
        self.gpuDACLbl.setText(f"Adapter DAC Type: {self.gpu_info.AdapterDACType}")
        self.gpuCompatLbl.setText(f"Adapter Compatibility: {self.gpu_info.AdapterCompatibility}")
        self.gpuMinHzLbl.setText(f"Minimum Refresh Rate: {self.gpu_info.MinRefreshRate}hz")
        self.gpuMaxHzLbl.setText(f"Maximum Refresh Rate: {self.gpu_info.MaxRefreshRate}hz")

    def checkMemory(self):
        totalMemorySize = 0

        count = 1

        activeMemStyle = "QFrame { background-color: #9a8c98; color: white;}"

        for memory_num in range(0, self.memory_range):
            totalMemorySize += self.convert(int(self.mem_info[memory_num].Capacity), 'm')
        self.memHeadingInfoLbl.setText(f"{self.memory_range} Physical Memory ({str(totalMemorySize).replace('.0', '').strip()} MB)")

        for memory_num in range(0, self.memory_range):
            if memory_num == 0:
                self.memNameLbl_0.setText(self.mem_info[memory_num].PartNumber)
                self.memClockSpeedLbl_0.setText(f"Clock Speed: {self.mem_info[memory_num].Speed}")
                self.memVoltageLbl_0.setText(f"Voltage: {self.mem_info[memory_num].MaxVoltage} V")
                self.memDataWidthLbl_0.setText(f"Data Width: {self.mem_info[memory_num].DataWidth}")
                self.memSerialNoLbl_0.setText(f"Serial Number: {self.mem_info[memory_num].SerialNumber}")
                self.memCapacityLbl_0.setText(f"Capacity: {str(self.convert(int(self.mem_info[memory_num].Capacity), 'm')).replace('.0', '')} MB")
            elif memory_num == 1:
                self.memNameLbl_1.setText(self.mem_info[memory_num].PartNumber)
                self.memClockSpeedLbl_1.setText(f"Clock Speed: {self.mem_info[memory_num].Speed}")
                self.memVoltageLbl_1.setText(f"Voltage: {self.mem_info[memory_num].MaxVoltage} V")
                self.memDataWidthLbl_1.setText(f"Data Width: {self.mem_info[memory_num].DataWidth}")
                self.memSerialNoLbl_1.setText(f"Serial Number: {self.mem_info[memory_num].SerialNumber}")
                self.memCapacityLbl_1.setText(f"Capacity: {str(self.convert(int(self.mem_info[memory_num].Capacity), 'm')).replace('.0', '')} MB")
                count = 2
            elif memory_num == 2:
                self.memNameLbl_2.setText(self.mem_info[memory_num].PartNumber)
                self.memClockSpeedLbl_2.setText(f"Clock Speed: {self.mem_info[memory_num].Speed}")
                self.memVoltageLbl_2.setText(f"Voltage: {self.mem_info[memory_num].MaxVoltage} V")
                self.memDataWidthLbl_2.setText(f"Data Width: {self.mem_info[memory_num].DataWidth}")
                self.memSerialNoLbl_2.setText(f"Serial Number: {self.mem_info[memory_num].SerialNumber}")
                self.memCapacityLbl_2.setText(f"Capacity: {str(self.convert(int(self.mem_info[memory_num].Capacity), 'm')).replace('.0', '')} MB")
                count = 3
            elif memory_num == 3:
                self.memNameLbl_3.setText(self.mem_info[memory_num].PartNumber)
                self.memClockSpeedLbl_3.setText(f"Clock Speed: {self.mem_info[memory_num].Speed}")
                self.memVoltageLbl_3.setText(f"Voltage: {self.mem_info[memory_num].MaxVoltage} V")
                self.memDataWidthLbl_3.setText(f"Data Width: {self.mem_info[memory_num].DataWidth}")
                self.memSerialNoLbl_3.setText(f"Serial Number: {self.mem_info[memory_num].SerialNumber}")
                self.memCapacityLbl_3.setText(f"Capacity: {str(self.convert(int(self.mem_info[memory_num].Capacity), 'm')).replace('.0', '')} MB")
                count = 4

        if count == 1:
            self.mem2Frame.hide()
            self.mem3Frame.hide()
            self.mem4Frame.hide()
        elif count == 2:
            self.mem2Frame.setStyleSheet(activeMemStyle)
            self.mem3Frame.hide()
            self.mem4Frame.hide()
        elif count == 3:
            self.mem2Frame.setStyleSheet(activeMemStyle)
            self.mem3Frame.setStyleSheet(activeMemStyle)
            self.mem4Frame.hide()
        elif count == 4:
            self.mem2Frame.setStyleSheet(activeMemStyle)
            self.mem3Frame.setStyleSheet(activeMemStyle)
            self.mem4Frame.setStyleSheet(activeMemStyle)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainApp()
    win.show()
    app.exec()