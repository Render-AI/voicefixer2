# VoiceFixer 2

Welcome to VoiceFixer 2, the next generation of VoiceFixer. VoiceFixer is a general speech restoration tool, using AI to remove background noise, fix degraded speech, enhance audio quality from old recordings, upscale low resolution, and more, all in one model!

VoiceFixer aims to restore human speech, regardless of how seriously degraded it is. It can handle noise, reverberation, low resolution, and clipping effect within one model!

## What’s different from the original VoiceFixer?

The [original version of VoiceFixer](https://github.com/haoheliu/voicefixer) continues to be updated with minor changes and bug fixes, however if one tries to install it and run it out of the box, one would encounter several errors that require modifying installed packages to fix.

**What’s the problem? How does this fix it?** VoiceFixer requires an old version of the `librosa` library, which is incompatible with new versions of the `numpy` library. We’ve fixed this issue by fixing the old version of `librosa` and `voicefixer`. We also added several new features.

### New features in VoiceFixer 2

We’ve added the following features in VoiceFixer 2:

* We’ve added MPS support, which means you can use GPU acceleration on M1 macs. You can enable this by setting the `cuda` parameter to `True`. It’s automatically enabled when using the command line interface (CLI).
* More features coming soon!
## To-Do
Here’s what we still need to do:
* Implement .mp3 support (currently only supports .wav)
## Demo

[Check out the demos to see what VoiceFixer can do!](https://haoheliu.github.io/demopage-voicefixer/)

## Installation

PyPi package coming soon!

```bash
pip install git+https://github.com/fakerybakery/voicefixer
```

## Usage

**Important:** VoiceFixer can only process files in the `wav` format. We recommend using `ffmpeg` library to convert `mp3`s to `wav`s. We’re working on supporting this.

### Command Line

Process a file:

```bash
voicefixer --infile test/utterance/original/original.wav
```

Process all files in a directory:

```bash
voicefixer --infolder /path/to/input --outfolder /path/to/output
```

Change modes (default 0):

```bash
voicefixer --infile /path/to/input.wav --outfile /path/to/output.wav --mode 1
```

Run all modes:

```bash
voicefixer --infile /path/to/input.wav --outfile /path/to/output.wav --mode all
```

For more information:

```bash
voicefixer -h
```

### Python API

```python
from voicefixer import VoiceFixer
voicefixer = VoiceFixer()
# Mode 0: Original Model (suggested by default)
# Mode 1: Add preprocessing module (remove higher frequency)
# Mode 2: Train mode (might work sometimes on seriously degraded real speech)
for mode in [0,1,2]:
    print("Testing mode",mode)
    voicefixer.restore(input=os.path.join(git_root,"test/utterance/original/original.flac"), # low quality .wav/.flac file
                       output=os.path.join(git_root,"test/utterance/output/output_mode_"+str(mode)+".flac"), # save file path
                       cuda=False, # GPU acceleration
                       mode=mode)
    if(mode != 2):
        check("output_mode_"+str(mode)+".flac")
    print("Pass")
```


## License

Both VoiceFixer and VoiceFixer 2 are licensed under the permissive MIT license, allowing for redistribution and commercial use!
