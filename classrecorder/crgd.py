# standard
import os

# pydrive
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


# class recorder google drive
class CRGD:

    # public

    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload(self, file_path: str, folder_id: str):
        file = self.drive.CreateFile(
            {
                'title': os.path.basename(file_path),
                'mimeType': 'video/mp4',
                'parents': [{'id': folder_id}]
            })
        file.SetContentFile(file_path)
        file.Upload()

