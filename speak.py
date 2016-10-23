#!/usr/bin/python3
#-*- coding:utf-8 -*-


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import subprocess
import os

class EntryWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_size_request(300, 250)
        self.set_title("PySpeak")
        self.set_border_width(5)
        icon = os.getcwd() + "/blur-48.png"
        self.set_default_icon_from_file(icon)
        self.timeout_id = None

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)
        
        self.ahbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox.pack_start(self.ahbox,True, True, 0)
        
        self.label = Gtk.Label()
        self.label.set_text("Locale:")
        self.ahbox.pack_start(self.label, True, True, 0)
        
        self.accent_store = Gtk.ListStore(str, str)
        accents = [("Default", "en"), 
                  ("English", "en-gb"), 
                  ("English-Scottish", "en-sc"), 
                  ("English-Northern", "en-uk-north"),
                  ("English-West Midlands", "en-wi"),
                  ("English-RP", "en-uk-rp"),
                  ("English-American", "en-us"),
                  ("English-West Indies", "en-wi"),
                  ("Afrikaans", "af"),
                  ("Albanian", "sq"),
                  ("Aragonese", "an"),
                  ("Armenian", "hy"),
                  ("Armenian-west", "hy-west"),
                  ("Brazil", "pt-br"),
                  ("Bulgarian", "bg"),
                  ("Bosnian", "ca"),
                  ("Cantonese", "zh-yue"),
                  ("Croatian", "hr"),
                  ("Czech", "cs"),
                  ("Danish", "da"),
                  ("Esperanto", "eo"),
                  ("Estonian", "et"),
                  ("Farsi", "fa"),
                  ("Farsi-Pinglish", "fa-pin"),
                  ("Finnish", "fi"),
                  ("French-Belgium ", "fr-be"),
                  ("French", "fr-fr"),
                  ("Georgian", "ka"),
                  ("German", "de"),
                  ("Greek", "el"),
                  ("Greek-Ancient", "grc"),
                  ("Hindi", "hi"),
                  ("Hungarian", "hu"),
                  ("Icelandic", "is"),
                  ("Indonesian", "id"),
                  ("Irish-Gaeilge", "ga"),
                  ("Italian", "it"),
                  ("Lojban", "jbp"),
                  ("Kannada", "kn"),
                  ("Kurdish", "ku"),
                  ("Latin", "la"),
                  ("Lithuanian", "lt"),
                  ("Latvian", "lv"),
                  ("Macedonian", "mk"),
                  ("Malayalam", "ml"),
                  ("Malay", "ms"),
                  ("Mandarin", "zh"),
                  ("Nepali", "ne"),
                  ("Dutch", "nl"),
                  ("Norwegian", "no"),
                  ("Punjabi", "pa"),
                  ("Polish", "pl"),
                  ("Portugal", "pt-pt"),
                  ("Romanian", "ro"),
                  ("Russian", "ru"),
                  ("Slovak", "sk"),
                  ("Serbian", "sr"),
                  ("Spanish", "es"),
                  ("Spanish-Latin-AM", "es-la"),
                  ("Swedish", "sv"),
                  ("Swahili-unstable", "sw"),
                  ("Tamil", "ta"),
                  ("Turkish", "tr"),
                  ("Vietnam", "vi"),
                  ("Vietnam-HUE", "vi-hue"),
                  ("vietnam-SGN", "vi-sgn"),
                  ("Welsh", "cy")
                  
                  
                  ]
        for self.accent in accents:
            self.accent_store.append([self.accent][0])

        self.accent_combo = Gtk.ComboBox.new_with_model(self.accent_store)
        self.accent_combo.connect("changed", self.on_accent_combo_changed)
        self.accent_combo.set_vexpand(False)
        self.text_renderer = Gtk.CellRendererText()
        self.accent_combo.pack_start(self.text_renderer, True)
        self.accent_combo.add_attribute(self.text_renderer, "text", 0)
        self.ahbox.pack_start(self.accent_combo, False, False, True)
        
        self.speed_label = Gtk.Label()
        self.speed_label.set_text("Speed:")
        self.ahbox.pack_start(self.speed_label, True, True, 0)
         
        self.speed_store = Gtk.ListStore(str, str)
        speeds = [
                 ("Slow Motion", "70"),
                 ("Slowest", "100"),
                 ("Slower", "110"),
                 ("Slow", "120"),
                 ("Normal", "130"),
                 ("Fast", "140"),
                 ("Faster", "150"),
                 ("Fastest", "160"),
                 ("Rocket Speed", "180"),           
                 ]
        for self.speed in speeds:
            self.speed_store.append([self.speed][0])

        self.speed_combo = Gtk.ComboBox.new_with_model(self.speed_store)
        self.speed_combo.connect("changed", self.on_speed_combo_changed)
        #self.set_active_accent = self.accent_combo.set_active()
        #self.set_active_accent([accents]([0]))
        self.spext_renderer = Gtk.CellRendererText()
        self.speed_combo.pack_start(self.spext_renderer, True)
        self.speed_combo.add_attribute(self.spext_renderer, "text", 0)
        self.ahbox.pack_start(self.speed_combo, False, False, True)
        
        self.label = Gtk.Label()
        self.label.set_text("Male/Female:")
        self.ahbox.pack_start(self.label, True, True, 0)
         
        self.sex_store = Gtk.ListStore(str, str)
        sexes = [
                ("Female 1", "f1"),
                ("Female 2", "f2"),
                ("Female 3", "f3"),
                ("Female 4", "f4"),
                ("Female 5", "f5"),
                ("Female Whisper", "whisperf"),
                ("Male 1", "m1"),
                ("Male 2", "m2"),
                ("Male 3", "m3"),
                ("Male 4", "m4"),
                ("Male 5", "m5"),
                ("Male 6", "m6"),
                ("Male 7", "m7"),
                ("Male Whisper", "whisper"),
                ("Male Croak", "croak"),
                
                  ]
        for self.sex in sexes:
            self.sex_store.append([self.sex][0])

        self.sex_combo = Gtk.ComboBox.new_with_model(self.sex_store)
        self.sex_combo.connect("changed", self.on_sex_combo_changed)
        #self.set_active_accent = self.accent_combo.set_active()
        #self.set_active_accent([accents]([0]))
        self.sext_renderer = Gtk.CellRendererText()
        self.sex_combo.pack_start(self.sext_renderer, True)
        self.sex_combo.add_attribute(self.sext_renderer, "text", 0)
        self.ahbox.pack_start(self.sex_combo, False, False, True)
        
        self.vhbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox.pack_start(self.vhbox,True, True, 0)
                
        self.label = Gtk.Label()
        self.label.set_text("Volume:")
        self.vhbox.pack_start(self.label, True, True, 0)

        spin_adjustment = Gtk.Adjustment(0, 0, 200, 1, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(spin_adjustment)
        self.spinbutton.set_numeric(True)
        self.spinbutton.set_value(100)
        self.vhbox.pack_start(self.spinbutton, False, False, 0)
        
        self.save_label = Gtk.Label()
        self.save_label.set_text("Save to File:")
        self.vhbox.pack_start(self.save_label, True, True, 0)
        
        self.save_switch = Gtk.Switch()
        self.save_switch.connect("notify::active", self.on_go_clicked)
        self.save_switch.connect("notify::active", self.on_save_switch_changed)
        self.save_switch.set_active(False)
        self.save_switch.set_tooltip_text("Switch on to save output to audio file")
        self.vhbox.pack_start(self.save_switch, True, True, 0)
               
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("What do you want to say?")
        self.vbox.pack_start(self.entry, True, True, 0)

        self.lhbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.vbox.pack_start(self.lhbox, True, True, 0)

        self.st_label = Gtk.Label()
        self.st_label.set_text("Waiting...")
        self.lhbox.pack_start(self.st_label, True, True, 0)
        
        self.spinner = Gtk.Spinner()
        self.lhbox.pack_start(self.spinner, True, True, 0)
        
        self.bhbox = Gtk.Box(spacing=6)
        self.vbox.pack_start(self.bhbox, True, True, 0)

        self.quit = Gtk.Button("Quit")
        self.quit.connect("clicked", self.on_quit_clicked)
        self.quit.set_hexpand(False)
        self.bhbox.pack_end(self.quit, True, True, 0)

        self.go = Gtk.Button("Go")
        self.go.connect("clicked", self.on_go_clicked)
        self.go.set_hexpand(False)
        self.bhbox.pack_start(self.go, True, True, 0)

    def on_save_switch_changed(self, switch, gparam):
        dialog = Gtk.FileChooserDialog("Please name and save the file", self,
            Gtk.FileChooserAction.SAVE,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, Gtk.ResponseType.OK))


        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def on_accent_combo_changed(self, combo):
        active_accent = self.accent_combo.get_active_iter()
        if active_accent != None:
            accent_model = self.accent_combo.get_model()
            self.accent = accent_model[active_accent][0]
            self.accent_code = accent_model[active_accent][1]
            print("Selected Accent: {0}".format(self.accent))
            self.st_label.set_text("Selected: {0}/{1}/{2}".format(self.accent, self.speed, self.sex))

    def on_sex_combo_changed(self, combo):
        active_sex = self.sex_combo.get_active_iter()
        if active_sex != None:
            sex_model = self.sex_combo.get_model()
            self.sex = sex_model[active_sex][0]
            self.sex_code = sex_model[active_sex][1]
            print("Selected Accent: {0}".format(self.sex))
            self.st_label.set_text("Selected: {0}/{1}/{2}".format(self.accent, self.speed, self.sex))

    def on_speed_combo_changed(self, combo):
        active_speed = self.speed_combo.get_active_iter()
        if active_speed != None:
            speed_model = self.speed_combo.get_model()
            self.speed = speed_model[active_speed][0]
            self.speed_code = speed_model[active_speed][1]
            print("Selected Speed: {0}".format(self.speed))
            self.st_label.set_text("Selected: {0}/{1}/{2}".format(self.accent, self.speed, self.sex))
            
            
    def on_go_clicked(self, button):
        if len(self.entry.get_text()) == 0:
            self.st_label.set_text("You did not enter any text to speak!")
        else:
            if self.save_switch.get_active() == True:
                self.save_file = " -w 'speak.wav'"
            elif self.save_switch.get_active() == False:
                self.save_file = ""
            print("Selected sex:", self.sex)
            print("Selected accent:", self.accent)
            print("Selected speed:", self.speed)
            self.volume = int(self.spinbutton.get_value())
            self.st_label.set_text("Speaking...")
            self.spinner.start()
            msg = self.entry.get_text()
            data_path = os.getcwd() + "/lib"
            bin = os.getcwd() + "/lib/speak"
            cmd = [bin, "--path=" + data_path, "-m", "-g2", "-a" + str(self.volume), "-s" + self.speed_code, "-v" + self.accent_code + "+" + self.sex_code, msg, self.save_file]
            print("Using command: ", cmd)
            subprocess.check_call(cmd)
            self.spinner.stop()
            self.st_label.set_text("Waiting...")
            
    def on_quit_clicked(self, button):
        print("[+] Quitting application")
        msg = "Goodbye"
        cmd = ["espeak", "-s150", "-ven+m3", msg]
        subprocess.check_call(cmd)
        Gtk.main_quit()
        
win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
