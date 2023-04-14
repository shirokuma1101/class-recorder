# standard
import json

# crgd
from classrecorder.crgd import CRGD
# crot
from classrecorder.crot import CROT
# crw
from classrecorder.crw import CRW


def main():

    with open('config.json', encoding='utf-8') as f:
        config = json.load(f)

    crgd = CRGD()
    crot = CROT(config)
    crw = CRW(crgd, crot)
    crw.run()


if __name__ == '__main__':
    main()

