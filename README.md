# Class Recorder

## 設定

### 必須ファイル

* config.json
* secrets/credentials.json
* secrets/client_secret.json

#### config.jsonの構文

``` json
{
  "path": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OBS Studio\\OBS Studio (64bit).lnk",
  "profile": "Recording for class",
  "source_name": "zoom",
  "host": "localhost",
  "port": 4455,
  "password": "yourpassword",
  "subjects": {
    "sub1": "google drive folder id",
    "sub2": "google drive folder id"
  }
}
```

## 推奨設定

* OBSでprofileを用意しておくと`config.json`で指定することができます。
* sourceの名前を`config.json`で指定することでプロジェクター(ウィンドウ)を表示させることができます。

## 注意

* `config.json`の`path`にはOBSのショートカットのパスを指定してください。
