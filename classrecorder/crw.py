# standard
import os
import time

# wx
import wx

# crgd
from classrecorder.crgd import CRGD
# crot
from classrecorder.crot import CROT
# window
from classrecorder.window.window import Window


# class recorder window
class CRW(Window):

    # public

    def __init__(self, crgd: CRGD, crot: CROT, suffix_limit: int = 5):
        self.app = wx.App()
        super().__init__(None)

        self.crgd = crgd
        self.crot = crot
        self.subjects = self.crot.config['subjects']

        self.crot.start()
        self.choice_subject.SetItems(list(self.subjects.keys()))
        self.choice_suffix.SetItems([str(i) for i in range(1, suffix_limit + 1)])
        self.switch_button_record(False)

    def __del__(self):
        self.crot.stop()
        return super().__del__()

    def click_button_recordstart(self, event):
        self.switch_button_record(True)
        self.crot.start_recording()

    def click_button_recordstop(self, event):
        self.switch_button_record(False)
        self.crot.stop_recording()
        time.sleep(1)
        suffix_index = self.choice_suffix.GetSelection()
        subject_index = self.choice_subject.GetSelection()
        subject = [k for i, k in enumerate(self.subjects.keys()) if i == subject_index][0]
        file_path = f'{self.crot.SAVE_DIR}\{os.path.basename(self.crot.FILE_PATH)}_{suffix_index+1:02}_{subject}.mp4'
        os.rename(self.crot.FILE_PATH, file_path)
        self.crgd.upload(file_path, self.subjects[subject])
        os.remove(file_path)

    def run(self) -> None:
        self.Show()
        self.app.MainLoop()

    def switch_button_record(self, is_recording: bool) -> None:
        if is_recording:
            self.button_recordstart.Disable()
            self.button_recordstop.Enable()
        else:
            self.button_recordstart.Enable()
            self.button_recordstop.Disable()

