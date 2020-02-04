#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Sun Feb  2 04:02:06 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Preferences(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Preferences.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((395, 424))
        self.combobox_board = wx.ComboBox(self, wx.ID_ANY, choices=["M2", "B2", "M", "M1", "A", "B", "B1"], style=wx.CB_DROPDOWN)
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, "Flip X")
        self.checkbox_3 = wx.CheckBox(self, wx.ID_ANY, "Home Right")
        self.checkbox_2 = wx.CheckBox(self, wx.ID_ANY, "Flip Y")
        self.checkbox_4 = wx.CheckBox(self, wx.ID_ANY, "Home Bottom")
        self.checkbox_mock_usb = wx.CheckBox(self, wx.ID_ANY, "Mock USB Connection Mode")
        self.spin_device_index = wx.SpinCtrl(self, wx.ID_ANY, "-1", min=-1, max=5)
        self.spin_device_address = wx.SpinCtrl(self, wx.ID_ANY, "-1", min=-1, max=5)
        self.spin_device_bus = wx.SpinCtrl(self, wx.ID_ANY, "-1", min=-1, max=5)
        self.spin_device_bus_copy = wx.SpinCtrl(self, wx.ID_ANY, "-1", min=-1, max=255)
        self.spin_home_x = wx.SpinCtrlDouble(self, wx.ID_ANY, "0.0", min=-50000.0, max=50000.0)
        self.spin_home_y = wx.SpinCtrlDouble(self, wx.ID_ANY, "0.0", min=-50000.0, max=50000.0)
        self.button_home_by_current = wx.Button(self, wx.ID_ANY, "Set Current")
        self.spin_bedwidth = wx.SpinCtrlDouble(self, wx.ID_ANY, "330.0", min=1.0, max=1000.0)
        self.spin_bedheight = wx.SpinCtrlDouble(self, wx.ID_ANY, "230.0", min=1.0, max=1000.0)
        self.checkbox_autolock = wx.CheckBox(self, wx.ID_ANY, "Automatically lock rail")
        self.checkbox_autohome = wx.CheckBox(self, wx.ID_ANY, "Home after job complete")
        self.checkbox_autobeep = wx.CheckBox(self, wx.ID_ANY, "Beep after job complete")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_combobox_boardtype, self.combobox_board)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_flip_x, self.checkbox_1)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_home_right, self.checkbox_3)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_flip_y, self.checkbox_2)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_home_bottom, self.checkbox_4)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_mock_usb, self.checkbox_mock_usb)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_device_index, self.spin_device_index)
        self.Bind(wx.EVT_TEXT, self.spin_on_device_index, self.spin_device_index)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_device_index, self.spin_device_index)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_device_address, self.spin_device_address)
        self.Bind(wx.EVT_TEXT, self.spin_on_device_address, self.spin_device_address)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_device_address, self.spin_device_address)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_device_bus, self.spin_device_bus)
        self.Bind(wx.EVT_TEXT, self.spin_on_device_bus, self.spin_device_bus)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_device_bus, self.spin_device_bus)
        self.Bind(wx.EVT_SPINCTRL, self.spin_on_device_version, self.spin_device_bus_copy)
        self.Bind(wx.EVT_TEXT, self.spin_on_device_version, self.spin_device_bus_copy)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_device_version, self.spin_device_bus_copy)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_home_x, self.spin_home_x)
        self.Bind(wx.EVT_TEXT, self.spin_on_home_x, self.spin_home_x)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_home_x, self.spin_home_x)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_home_y, self.spin_home_y)
        self.Bind(wx.EVT_TEXT, self.spin_on_home_y, self.spin_home_y)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_home_y, self.spin_home_y)
        self.Bind(wx.EVT_BUTTON, self.on_button_set_home_current, self.button_home_by_current)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_bedwidth, self.spin_bedwidth)
        self.Bind(wx.EVT_TEXT, self.spin_on_bedwidth, self.spin_bedwidth)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_bedwidth, self.spin_bedwidth)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_bedheight, self.spin_bedheight)
        self.Bind(wx.EVT_TEXT, self.spin_on_bedheight, self.spin_bedheight)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_bedheight, self.spin_bedheight)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autolock, self.checkbox_autolock)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autohome, self.checkbox_autohome)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autobeep, self.checkbox_autobeep)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Preferences.__set_properties
        self.SetTitle("Preferences")
        self.combobox_board.SetToolTip("Select the board to use. This has an effects the speedcodes used.")
        self.combobox_board.SetSelection(0)
        self.checkbox_1.SetToolTip("Flip the Right and Left commands sent to the controller")
        self.checkbox_1.Enable(False)
        self.checkbox_3.SetToolTip("Indicates the device Home is on the right")
        self.checkbox_3.Enable(False)
        self.checkbox_2.SetToolTip("Flip the Top and Bottom commands sent to the controller")
        self.checkbox_2.Enable(False)
        self.checkbox_4.SetToolTip("Indicates the device Home is on the bottom")
        self.checkbox_4.Enable(False)
        self.checkbox_mock_usb.SetToolTip("DEBUG. Without a K40 connected continue to process things as if there was one.")
        self.spin_device_index.SetToolTip("-1 match anything. 0-5 match exactly that value.")
        self.spin_device_index.Enable(False)
        self.spin_device_address.SetToolTip("-1 match anything. 0-5 match exactly that value.")
        self.spin_device_address.Enable(False)
        self.spin_device_bus.SetToolTip("-1 match anything. 0-5 match exactly that value.")
        self.spin_device_bus.Enable(False)
        self.spin_device_bus_copy.SetToolTip("-1 match anything. 0-255 match exactly that value.")
        self.spin_device_bus_copy.Enable(False)
        self.spin_home_x.SetMinSize((80, 23))
        self.spin_home_x.SetToolTip("Translate Home X")
        self.spin_home_x.Enable(False)
        self.spin_home_y.SetMinSize((80, 23))
        self.spin_home_y.SetToolTip("Translate Home Y")
        self.spin_home_y.Enable(False)
        self.button_home_by_current.SetToolTip("Set Home Position based on the current position")
        self.button_home_by_current.Enable(False)
        self.spin_bedwidth.SetMinSize((80, 23))
        self.spin_bedwidth.SetToolTip("Width of the laser bed.")
        self.spin_bedheight.SetMinSize((80, 23))
        self.spin_bedheight.SetToolTip("Height of the laser bed.")
        self.checkbox_autolock.SetToolTip("Lock rail after operations are finished.")
        self.checkbox_autolock.SetValue(1)
        self.checkbox_autohome.SetToolTip("Home the machine after job is finished")
        self.checkbox_autobeep.SetToolTip("Beep after the job is finished.")
        self.checkbox_autobeep.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Preferences.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_general = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "General Options"), wx.VERTICAL)
        sizer_bed = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Bed Dimensions"), wx.HORIZONTAL)
        sizer_home = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Shift Home Position"), wx.HORIZONTAL)
        sizer_usb = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "USB Settings"), wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_board = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Board Setup"), wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_board.Add(self.combobox_board, 0, 0, 0)
        sizer_board.Add((20, 20), 0, 0, 0)
        sizer_17.Add(self.checkbox_1, 0, 0, 0)
        sizer_17.Add(self.checkbox_3, 0, 0, 0)
        sizer_board.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_16.Add(self.checkbox_2, 0, 0, 0)
        sizer_16.Add(self.checkbox_4, 0, 0, 0)
        sizer_board.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_board, 1, wx.EXPAND, 0)
        sizer_usb.Add(self.checkbox_mock_usb, 0, 0, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Device Index:")
        sizer_3.Add(label_6, 1, 0, 0)
        sizer_3.Add(self.spin_device_index, 1, 0, 0)
        sizer_usb.Add(sizer_3, 1, wx.EXPAND, 0)
        label_7 = wx.StaticText(self, wx.ID_ANY, "Device Address:")
        sizer_10.Add(label_7, 1, 0, 0)
        sizer_10.Add(self.spin_device_address, 1, 0, 0)
        sizer_usb.Add(sizer_10, 1, wx.EXPAND, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, "Device Bus:")
        sizer_11.Add(label_8, 1, 0, 0)
        sizer_11.Add(self.spin_device_bus, 1, 0, 0)
        sizer_usb.Add(sizer_11, 1, wx.EXPAND, 0)
        label_13 = wx.StaticText(self, wx.ID_ANY, "Chip Version:")
        sizer_12.Add(label_13, 1, 0, 0)
        sizer_12.Add(self.spin_device_bus_copy, 1, 0, 0)
        sizer_usb.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_usb, 1, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, "X")
        sizer_home.Add(label_9, 0, 0, 0)
        sizer_home.Add(self.spin_home_x, 0, 0, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, "mil")
        sizer_home.Add(label_12, 0, 0, 0)
        sizer_home.Add((20, 20), 0, 0, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, "Y")
        sizer_home.Add(label_10, 0, 0, 0)
        sizer_home.Add(self.spin_home_y, 0, 0, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, "mil")
        sizer_home.Add(label_11, 0, 0, 0)
        sizer_home.Add((20, 20), 0, 0, 0)
        sizer_home.Add(self.button_home_by_current, 0, 0, 0)
        sizer_1.Add(sizer_home, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Width")
        sizer_bed.Add(label_2, 0, 0, 0)
        sizer_bed.Add(self.spin_bedwidth, 0, 0, 0)
        label_17 = wx.StaticText(self, wx.ID_ANY, "mm")
        sizer_bed.Add(label_17, 0, 0, 0)
        sizer_bed.Add((20, 20), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Height")
        sizer_bed.Add(label_3, 0, 0, 0)
        sizer_bed.Add(self.spin_bedheight, 0, 0, 0)
        label_18 = wx.StaticText(self, wx.ID_ANY, "mm")
        sizer_bed.Add(label_18, 0, 0, 0)
        sizer_1.Add(sizer_bed, 1, wx.EXPAND, 0)
        sizer_general.Add(self.checkbox_autolock, 0, 0, 0)
        sizer_general.Add(self.checkbox_autohome, 0, 0, 0)
        sizer_general.Add(self.checkbox_autobeep, 0, 0, 0)
        sizer_1.Add(sizer_general, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_combobox_boardtype(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_combobox_boardtype' not implemented!")
        event.Skip()

    def on_check_flip_x(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_flip_x' not implemented!")
        event.Skip()

    def on_check_home_right(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_home_right' not implemented!")
        event.Skip()

    def on_check_flip_y(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_flip_y' not implemented!")
        event.Skip()

    def on_check_home_bottom(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_home_bottom' not implemented!")
        event.Skip()

    def on_checkbox_mock_usb(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_checkbox_mock_usb' not implemented!")
        event.Skip()

    def spin_on_device_index(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_device_index' not implemented!")
        event.Skip()

    def spin_on_device_address(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_device_address' not implemented!")
        event.Skip()

    def spin_on_device_bus(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_device_bus' not implemented!")
        event.Skip()

    def spin_on_device_version(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_device_version' not implemented!")
        event.Skip()

    def spin_on_home_x(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_home_x' not implemented!")
        event.Skip()

    def spin_on_home_y(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_home_y' not implemented!")
        event.Skip()

    def on_button_set_home_current(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_button_set_home_current' not implemented!")
        event.Skip()

    def spin_on_bedwidth(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_bedwidth' not implemented!")
        event.Skip()

    def spin_on_bedheight(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_bedheight' not implemented!")
        event.Skip()

    def on_check_autolock(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_autolock' not implemented!")
        event.Skip()

    def on_check_autohome(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_autohome' not implemented!")
        event.Skip()

    def on_check_autobeep(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_autobeep' not implemented!")
        event.Skip()

# end of class Preferences

class MyApp(wx.App):
    def OnInit(self):
        self.Preferences = Preferences(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Preferences)
        self.Preferences.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
