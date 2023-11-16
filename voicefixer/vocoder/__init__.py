import os
from voicefixer.vocoder.config import Config
import urllib.request

if not os.path.exists(Config.ckpt):
    os.makedirs(os.path.dirname(Config.ckpt), exist_ok=True)
    print("Downloading the weight of neural vocoder: TFGAN")
    urllib.request.urlretrieve(
        "https://huggingface.co/voicefixer/voicefixer/resolve/main/vocoder/model.ckpt-1490000_trimed.pt?download=true",
        Config.ckpt,
    )
    print(
        "Weights downloaded in: {} Size: {}".format(
            Config.ckpt, os.path.getsize(Config.ckpt)
        )
    )
