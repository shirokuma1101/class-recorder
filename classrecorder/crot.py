# standard
import datetime
import json
import os
import subprocess
import time

# obs
from obswebsocket import obsws, requests


# class recorder obs tools
class CROT:

    # public
    DATE_FORMAT = '%y%m%d'
    SAVE_DIR = os.popen('powershell -Command ([Environment])::GetFolderPath("""MyVideos""")').read().rstrip('\n')
    FILE_PATH = fr'{SAVE_DIR}\{datetime.date.today().strftime(DATE_FORMAT)}.mp4'

    def __init__(self, config_path: str):
        with open(config_path, encoding='utf-8') as f:
            self.config = json.load(f)
        if self.config is None:
            raise ValueError('config is None')

    def start(self, wait_sec: int = 5) -> None:
        cmd = f'start "obs" "{self.config["path"]}" --profile "{self.config["profile"]}" --minimize-to-tray'
        subprocess.Popen(cmd, shell=True)
        time.sleep(wait_sec)
        self.client = obsws(self.config['host'], self.config['port'], self.config['password'])
        self.client.connect()
        self.client.call(requests.OpenSourceProjector(sourceName=self.config['source_name']))

    def stop(self) -> None:
        self.client.disconnect()
        self.client = None
        subprocess.Popen('taskkill /im obs64.exe')
        subprocess.Popen('taskkill /im obs64.exe')

    def start_recording(self):
        self.client.call(requests.StartRecord())

    def stop_recording(self):
        self.client.call(requests.StopRecord())

