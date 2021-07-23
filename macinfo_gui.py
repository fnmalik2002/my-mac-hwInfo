# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Feb 26 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx


###########################################################################
## Class MacInfo
###########################################################################

class MacInfo(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Mac Info", pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                          style=wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        # Create Menu Bar
        def mymenu(self):
            self.m_menubar = wx.MenuBar(wx.MB_DOCKABLE)

            # Create Menus
            self.m_menu_File = wx.Menu()
            self.m_menu_settings = wx.Menu()
            self.m_menu_help = wx.Menu()

            # Create menu items
            self.m_menuItem_file_start_scan = wx.MenuItem(self.m_menu_File, wx.ID_ANY, u"Start Scan", wx.EmptyString,
                                                          wx.ITEM_NORMAL)
            # self.m_menuItem_file_submit = wx.MenuItem(self.m_menu_File, wx.ID_ANY, u"Submit", wx.EmptyString,
            #                                           wx.ITEM_NORMAL)
            self.m_menuItem_file_close = wx.MenuItem(self.m_menu_File, wx.ID_ANY, u"Close", wx.EmptyString,
                                                     wx.ITEM_NORMAL)
            # self.m_menuItem_settings_ip_address = wx.MenuItem(self.m_menu_settings, wx.ID_ANY, u"Server IP Address",
            #                                                   wx.EmptyString, wx.ITEM_NORMAL)
            self.m_menuItem_help_About = wx.MenuItem(self.m_menu_help, wx.ID_ANY, u"About", wx.EmptyString,
                                                     wx.ITEM_NORMAL)

            # add menu items to menus
            self.m_menu_File.Append(self.m_menuItem_file_start_scan)
            # self.m_menu_File.Append(self.m_menuItem_file_submit)
            self.m_menu_File.Append(self.m_menuItem_file_close)
            # self.m_menu_settings.Append(self.m_menuItem_settings_ip_address)
            self.m_menu_help.Append(self.m_menuItem_help_About)

            # add menus to menu bar
            self.m_menubar.Append(self.m_menu_File, u"File")
            self.m_menubar.Append(self.m_menu_settings, u"Settings")
            self.m_menubar.Append(self.m_menu_help, u"Help")

            self.SetMenuBar(self.m_menubar)
        mymenu(self)

        # create status bar
        def mystatusbar(self):
            self.m_statusBar = self.CreateStatusBar(1, wx.STB_DEFAULT_STYLE, wx.ID_ANY)
        # mystatusbar(self)

        #create all layout sizers
        bSizer_mainSizer = wx.BoxSizer(wx.VERTICAL)
        bSizer_greenSizer = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_greenSizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_bookSizer = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_mainSizer.Add(bSizer_greenSizer, 1, wx.EXPAND, 5)
        bSizer_mainSizer.Add(bSizer_bookSizer, 4, wx.EXPAND, 5)
        bSizer_mainSizer.Add(bSizer_buttonSizer, 0, wx.ALIGN_RIGHT, 5)
        self.SetSizer(bSizer_mainSizer)



        # Create panels

        self.m_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.m_panel.SetFont(
            wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        self.m_panel.SetBackgroundColour(wx.Colour(147, 215, 157))



        # create gui labels and inputs
        self.m_staticText_name_of_module = wx.StaticText(self.m_panel, wx.ID_ANY, u"Mac Info", wx.DefaultPosition,
                                                         wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText_name_of_module.Wrap(-1)

        self.m_staticText_name_of_module.SetFont(
            wx.Font(36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        self.m_staticText_name_of_module.SetForegroundColour(wx.Colour(255, 255, 255))




        bSizer_greenSizer_1.Add(self.m_staticText_name_of_module, 1,
                                wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel.SetSizer(bSizer_greenSizer_1)
        self.m_panel.Layout()
        bSizer_greenSizer_1.Fit(self.m_panel)
        bSizer_greenSizer.Add(self.m_panel, 1, wx.EXPAND | wx.ALL, 5)




        # create notebook
        self.m_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # create notebook panel
        self.m_panel_basic_hardware = wx.Panel(self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.TAB_TRAVERSAL)
        bSizer_book_basic = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_book_basic_1 = wx.BoxSizer(wx.VERTICAL)


        bSizer_basic_1_0 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_d = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Date : ",
                                           wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText_d.Wrap(-1)

        bSizer_basic_1_0.Add(self.m_staticText_d, 0, wx.ALL, 2)

        self.m_textCtrl_date = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_0.Add(self.m_textCtrl_date, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_0, 0, wx.EXPAND, 5)


        bSizer_basic_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText9 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Serial Number : ",
                                           wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText9.Wrap(-1)

        bSizer_basic_1_1.Add(self.m_staticText9, 0, wx.ALL, 2)

        self.m_textCtrl_serial_number = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_1.Add(self.m_textCtrl_serial_number, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_1, 0, wx.EXPAND, 5)

        bSizer_basic_1_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Model Info : ", wx.DefaultPosition,
                                           wx.Size(150, -1), 0)
        self.m_staticText2.Wrap(-1)

        bSizer_basic_1_2.Add(self.m_staticText2, 0, wx.ALL, 2)

        self.m_textCtrl_model_info = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                 wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_2.Add(self.m_textCtrl_model_info, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_2, 0, wx.EXPAND, 5)

        bSizer_basic_1_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText4 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Processor : ", wx.DefaultPosition,
                                           wx.Size(150, -1), 0)
        self.m_staticText4.Wrap(-1)

        bSizer_basic_1_3.Add(self.m_staticText4, 0, wx.ALL, 2)

        self.m_textCtrl_procesor = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_3.Add(self.m_textCtrl_procesor, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_3, 0, wx.EXPAND, 5)

        bSizer_basic_1_4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"RAM Info : ", wx.DefaultPosition,
                                           wx.Size(150, -1), 0)
        self.m_staticText5.Wrap(-1)

        bSizer_basic_1_4.Add(self.m_staticText5, 0, wx.ALL, 2)

        self.m_textCtrl_ram_info = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_4.Add(self.m_textCtrl_ram_info, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_4, 0, wx.EXPAND, 5)

        bSizer_basic_1_5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Storage Media : ",
                                           wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText7.Wrap(-1)

        bSizer_basic_1_5.Add(self.m_staticText7, 0, wx.ALL, 2)

        self.m_textCtrl_storage_media = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_5.Add(self.m_textCtrl_storage_media, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_5, 0, wx.EXPAND, 5)

        bSizer_basic_1_6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Graphic Card : ",
                                           wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText8.Wrap(-1)

        bSizer_basic_1_6.Add(self.m_staticText8, 0, wx.ALL, 2)

        self.m_textCtrl_graphic_card = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                   wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_6.Add(self.m_textCtrl_graphic_card, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_6, 0, wx.EXPAND, 5)

        bSizer_basic_1_7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText18 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Optical Drive : ",
                                            wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText18.Wrap(-1)

        bSizer_basic_1_7.Add(self.m_staticText18, 0, wx.ALL, 2)

        self.m_textCtrl_optical_drive = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_7.Add(self.m_textCtrl_optical_drive, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_7, 0, wx.EXPAND, 5)

        bSizer_basic_1_8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText10 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Battery Status : ",
                                            wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText10.Wrap(-1)

        bSizer_basic_1_8.Add(self.m_staticText10, 0, wx.ALL, 2)

        self.m_textCtrl_battery_status = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                     wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_8.Add(self.m_textCtrl_battery_status, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_8, 0, wx.EXPAND, 5)

        bSizer_basic_1_9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_operating_system = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Wireless Card : ",
                                                           wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText_operating_system.Wrap(-1)

        bSizer_basic_1_9.Add(self.m_staticText_operating_system, 0, wx.ALL, 2)

        self.m_textCtrl_wireless_card = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_9.Add(self.m_textCtrl_wireless_card, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_9, 0, wx.EXPAND, 5)

        bSizer_basic_1_10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText21 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Bluetooth : ", wx.DefaultPosition,
                                            wx.Size(150, -1), 0)
        self.m_staticText21.Wrap(-1)

        bSizer_basic_1_10.Add(self.m_staticText21, 0, wx.ALL, 2)

        self.m_textCtrl_bluetooth = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_10.Add(self.m_textCtrl_bluetooth, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_10, 1, wx.EXPAND, 5)

        bSizer_basic_1_11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Ethernet : ", wx.DefaultPosition,
                                            wx.Size(150, -1), 0)
        self.m_staticText22.Wrap(-1)

        bSizer_basic_1_11.Add(self.m_staticText22, 0, wx.ALL, 2)

        self.m_textCtrl_ethernet = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_11.Add(self.m_textCtrl_ethernet, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_11, 1, wx.EXPAND, 5)

        bSizer_basic_1_12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText23 = wx.StaticText(self.m_panel_basic_hardware, wx.ID_ANY, u"Operating System : ",
                                            wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_staticText23.Wrap(-1)

        bSizer_basic_1_12.Add(self.m_staticText23, 0, wx.ALL, 2)

        self.m_textCtrl_operating_system = wx.TextCtrl(self.m_panel_basic_hardware, wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.Size(700, -1), 0)
        bSizer_basic_1_12.Add(self.m_textCtrl_operating_system, 0, wx.ALL, 2)

        bSizer_book_basic_1.Add(bSizer_basic_1_12, 1, wx.EXPAND, 5)

        bSizer_book_basic.Add(bSizer_book_basic_1, 0, wx.EXPAND, 5)

        self.m_panel_basic_hardware.SetSizer(bSizer_book_basic)
        self.m_panel_basic_hardware.Layout()
        bSizer_book_basic.Fit(self.m_panel_basic_hardware)
        self.m_notebook.AddPage(self.m_panel_basic_hardware, u"Basic Hardware", False)


        bSizer_bookSizer.Add(self.m_notebook, 1, wx.EXPAND | wx.ALL, 5)





        self.m_button_reset = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_buttonSizer.Add(self.m_button_reset, 0, wx.ALL | wx.SHAPED, 5)

        self.m_button_start_scan = wx.Button(self, wx.ID_ANY, u"Start Scan", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_buttonSizer.Add(self.m_button_start_scan, 0, wx.ALL | wx.SHAPED, 5)

        # self.m_button_submit = wx.Button(self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        # bSizer_buttonSizer.Add(self.m_button_submit, 0, wx.ALL | wx.SHAPED, 5)

        self.m_staticText_space_adjuster_after_submit_button = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                                                             wx.DefaultPosition, wx.Size(0, -1), 0)
        self.m_staticText_space_adjuster_after_submit_button.Wrap(-1)

        bSizer_buttonSizer.Add(self.m_staticText_space_adjuster_after_submit_button, 0, wx.ALL, 5)

        self.Layout()
        bSizer_mainSizer.Fit(self)
        self.Centre(wx.BOTH)


        # attach the key bind event to accelerator table (to use cmd+q keys to close app)
        randomId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onkeycombo, id=randomId)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('q'), randomId)])
        self.SetAcceleratorTable(accel_tbl)

        self.Show()

    def __del__(self):
        pass

    def onkeycombo(self, event):
        self.Destroy()
        # print "You pressed CTRL+Q!"


