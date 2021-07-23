import macinfo_gui
import mac_models as mm
import wx
import datetime
import subprocess


class MacInfo(wx.Frame):
    def __init__(self):
        super(MacInfo, self).__init__()
        self.initialize_variables()
        global gui
        gui = macinfo_gui.MacInfo(None)
        gui.m_button_start_scan.Bind(wx.EVT_BUTTON, self.start_scan)
        gui.m_button_reset.Bind(wx.EVT_BUTTON, self.reset_form)
        gui.m_button_reset.Disable()

    # initialize variables
    def initialize_variables(self):
        date_today = ''
        basic_serial_number = ''
        basic_model_info = 'Mac'
        basic_processor = ''
        basic_ram_info = ''
        basic_storage_media = ''
        basic_graphic_card = ''
        basic_optical_drive = ''
        basic_battery_status = ''
        basic_wireless_card = ''
        basic_bluetooth = ''
        basic_ethernet = ''
        basic_eth_status = ''
        basic_eth_ip = ''
        basic_wifi_status = ''
        basic_operating_system = ''
        basic_note = ''
        basic_model_identifier = ''
        basic_trackpad = basic_speakers = basic_webcam = \
            basic_headphone_jack = basic_battery_led = basic_webcam_led = \
            basic_keyboard_backlight = basic_caps_lock_led = True

    def start_scan(self, event):
        print("Scan Started")
        self.get_date()
        self.get_sn_and_model()
        self.get_processor()
        self.get_ram_info()
        self.get_storage()
        self.get_graphics()
        self.get_optical()
        self.get_battery()
        self.get_wireless()
        self.get_bluetooth()
        self.get_ethernet()
        self.get_os()
        gui.m_button_reset.Enable()
        gui.m_button_start_scan.Disable()


    def reset_form(self, event):
        # reset the gui elements
        gui.m_textCtrl_date.SetLabel("")
        gui.m_textCtrl_serial_number.SetLabel("")
        gui.m_textCtrl_model_info.SetLabel("")
        gui.m_textCtrl_procesor.SetLabel("")
        gui.m_textCtrl_ram_info.SetLabel("")
        gui.m_textCtrl_storage_media.SetLabel("")
        gui.m_textCtrl_graphic_card.SetLabel("")
        gui.m_textCtrl_optical_drive.SetLabel("")
        gui.m_textCtrl_battery_status.SetLabel("")
        gui.m_textCtrl_wireless_card.SetLabel("")
        gui.m_textCtrl_bluetooth.SetLabel("")
        gui.m_textCtrl_ethernet.SetLabel("")
        gui.m_textCtrl_operating_system.SetLabel("")

        # reset the variables
        self.initialize_variables()
        gui.m_button_start_scan.Enable()
        gui.m_button_reset.Disable()

    def run_cmd(self, cmd):
        # this function runs terminal commands in the background, which are given to it as input when it is called
        getcore = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = getcore.communicate()  # type: (str, str)
        result = str(out, "utf-8").lstrip().rstrip()
        # print("out = ",type(out), out)
        print("result = ", type(result), result)
        wx.Yield()
        return result

    def get_date(self):
        self.date_today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Date", type("self.date_today"), self.date_today)
        gui.m_textCtrl_date.SetLabel(self.date_today)

    def get_sn_and_model(self):
        sn = self.run_cmd("system_profiler SPHardwareDataType | awk '/Model Identifier/ {print $3} /Serial/ {print $4}'").split()
        self.basic_serial_number = sn[1]
        self.basic_model_identifier = sn[0]
        print(sn)
        # Use last 4 of sn to look up mac model from mac_models.py file
        last4 = self.basic_serial_number[-4::]
        print(last4)
        try:
            self.basic_model_info = mm.models[last4]
        except Exception as e:
            self.basic_model_info = "Not in the model list"
            print(e)

        print(self.basic_model_info, self.basic_model_identifier)
        model = self.basic_model_info + "      |      Model Identifier : " + self.basic_model_identifier
        gui.m_textCtrl_serial_number.SetLabel(self.basic_serial_number)
        gui.m_textCtrl_model_info.SetLabel(model)

    def get_processor(self):
        pr_cores = self.run_cmd("hostinfo | grep physically | awk ' {print $1}'")
        pr_model = self.run_cmd("sysctl machdep.cpu.brand_string | awk '{print $2, $3, $4, $5, $6, $7, $8, $9}'")
        print(pr_model, pr_cores)

        self.basic_processor = pr_model + "      |      Physical Cores : " + pr_cores
        print(self.basic_processor)
        gui.m_textCtrl_procesor.SetLabel(self.basic_processor)

    def get_ram_info(self):
        ram_total = self.run_cmd("system_profiler SPHardwareDataType | awk '/Memory/ {print $2 $3}'")
        # ram_speed = ''
        ram_speed_list = self.run_cmd("system_profiler SPMemoryDataType | awk '/Speed/ {print $2}'").split()
        print(ram_speed_list)
        i = 0
        while i < len(ram_speed_list):
            if ram_speed_list[i] != 'Empty':
                self.ram_speed = ram_speed_list[i] + ' MHz'
                print(ram_speed_list[i])
                print(self.ram_speed)
                i = len(ram_speed_list) + 1

            i = i + 1
        # RAM Slot info
        slots = self.run_cmd("system_profiler SPMemoryDataType | awk '/Size/ {print $2, $3}'").split('\n')
        print(slots)
        ram_slots = '  '.join([line.strip() for line in slots])
        self.basic_ram_info = ram_total + "      |      " + ram_slots + "      |      " + self.ram_speed
        print(self.basic_ram_info)
        gui.m_textCtrl_ram_info.SetLabel(self.basic_ram_info)

    def get_storage(self):
        hdd = ''
        print(hdd)
        hdd_sn = self.run_cmd("system_profiler SPSerialATADataType | awk '/Serial Number/{print $3}'")
        hdd_type = self.run_cmd("system_profiler SPSerialATADataType | awk '/Medium Type/{print $3,$4,$5}'")
        if hdd_type != "Solid State":
            hdd_speed = self.run_cmd("system_profiler SPSerialATADataType | awk '/Rotational Rate/ {print $3, $4}'")
        else:
            hdd_speed = "0"
        hdd_size = self.run_cmd("diskutil list | awk '/0:/ {print $3 $4}'| head -1")[1:]
        print(hdd_size, hdd_type, hdd_speed, hdd_sn)
        self.basic_storage_media = hdd_size + "      |      Type : " + hdd_type + "      |      Speed : " + hdd_speed + " rpm"
        gui.m_textCtrl_storage_media.SetLabel(self.basic_storage_media)

    def get_graphics(self):
        self.basic_graphic_card = self.run_cmd(
            "system_profiler SPDisplaysDataType | awk '/Model/ {print $3, $4, $5, $6, $7, $8}'")
        gui.m_textCtrl_graphic_card.SetLabel(self.basic_graphic_card)

    def get_optical(self):
        optical = self.run_cmd("drutil list | awk '/1/{print $2, $3}'")
        print(optical)
        if optical == '' or optical == []:
            self.basic_optical_drive = "None"
        else:
            opt = optical.split()
            self.basic_optical_drive = opt[1] + "      |      Manufacturer : " + opt[0]
        gui.m_textCtrl_optical_drive.SetLabel(self.basic_optical_drive)

    def get_battery(self):
        bat = self.run_cmd(
            "system_profiler SPPowerDataType | awk '/Condition/ {print $2, $3} /Cycle Count/ {print $3}'"
        ).split()
        print(bat)
        # if bat != []:
        if bat:
            bat_cycles = bat[0]
            bat_condition = bat[1]
            self.basic_battery_status = "Condition : " + bat_condition + "      |      Cycle Count : " + bat_cycles
            gui.m_textCtrl_battery_status.SetLabel(self.basic_battery_status)
            gui.m_textCtrl_physical_condition.AppendText(self.basic_battery_status + "\n")
        else:
            self.basic_battery_status = "No Battery"
            gui.m_textCtrl_battery_status.SetLabel(self.basic_battery_status)

    def get_wireless(self):
        wireless_type = self.run_cmd(
            "system_profiler SPAirPortDataType | awk '/Supported PHY Modes/{print }'"
        ).split(":")[1]
        self.basic_wifi_status = self.run_cmd("ifconfig en1 | awk '/status/ {print $2}'")
        print(self.basic_wifi_status)


        if self.basic_wifi_status == 'active':
            try:
                wireless_ip = self.run_cmd("ifconfig en1 | awk '/broad/ {print $2}'")
            except Exception as e:
                print(e)
            self.basic_wireless_card = "Card Type : " + wireless_type + "      |      IP Address : " + wireless_ip
        else:
            wireless_ip = ''
            self.basic_wireless_card = "Card Type : " + wireless_type + "      |      Status : " + self.basic_wifi_status
        print(wireless_type, wireless_ip)
        gui.m_textCtrl_wireless_card.SetLabel(self.basic_wireless_card)

    def get_bluetooth(self):
        bt_man = self.run_cmd("system_profiler SPBluetoothDataType | awk '/Manufacturer/{print }'")
        print("bluetooth manufacturer = ", type(bt_man), bt_man)
        bt_pwr = self.run_cmd("system_profiler SPBluetoothDataType | awk '/Bluetooth Power:/{print }'")
        print("Bluetooth Power = ", bt_pwr)
        if bt_man != "":
            self.basic_bluetooth = "Manufacturer : " + bt_man.split(":")[1] + "      |      " + bt_pwr
        else:
            self.basic_bluetooth = "No Bluetooth"
        gui.m_textCtrl_bluetooth.SetLabel(self.basic_bluetooth)

    def get_ethernet(self):
        try:
            self.basic_eth_ip = self.run_cmd("ifconfig en0 | awk '/broad/ {print $2}'")
        except Exception as e:
            print(e)
            pass
        eth_mac = self.run_cmd("ifconfig en0 | awk '/ether/ {print $2}' | head -1")
        self.basic_eth_status = self.run_cmd("ifconfig en0 | awk '/status/ {print $2}'")
        print("Ethernet mac = ", eth_mac)
        print("Ethernet ip = ", self.basic_eth_ip)
        print("Ethernet status = ", self.basic_eth_status)
        if self.basic_eth_status != "inactive":
            self.basic_ethernet = "Mac Address :  " + eth_mac.upper() + "      |      IP Address : " + self.basic_eth_ip
        else:
            self.basic_ethernet = "Mac Address :  " + eth_mac.upper() + "      |      Status : " + self.basic_eth_status
        gui.m_textCtrl_ethernet.SetLabel(self.basic_ethernet)

    def get_os(self):
        os = self.run_cmd("system_profiler SPSoftwareDataType | awk '/System Version/ {print $4}'")
        print("os = ", os)
        if os == "X" or os == "x":
            os = self.run_cmd("system_profiler SPSoftwareDataType | awk '/System Version/ {print $5}'")

        self.basic_operating_system = os
        print("Operating System = ", self.basic_operating_system)
        gui.m_textCtrl_operating_system.SetLabel(self.basic_operating_system)

if __name__ == '__main__':
    app = wx.App()
    frame = MacInfo()
    app.MainLoop()
