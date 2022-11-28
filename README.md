# The-Anatomy-of-Video-Editing
This is the official repository for our ECCV 2022 paper titled, "[The Anatomy of Video Editing: A Dataset and Benchmark Suite for AI-Assisted Video Editing](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136680195.pdf)".

![image info](./overview.PNG)

### To-Do List
- [x] Dataset and Annotations
- [ ] Shot embeddings from SOTA audio and video models
- [ ] Downstream tasks

## Getting Started
You can download all the labels in AVE using the following [link](https://drive.google.com/file/d/1b_4yO94UbkkUAiRo4TB6QLfNef4WQ3t-/view). The annotation file is organized as follows,

```json
{
  "scene id (ex. xBr1UV3kWqA)":
  {
    "shot id (ex. 02a91bd7-feda-4844-8a85-b01d43437140)":
    {
      "clip-type": ["shot"],
      "start-time": [51.05],
      "end-time": [62.15],
      "shot-size": ["medium"],
      "shot-angle": ["low-angle"],
      "shot-type": ["two-shot"],
      "shot-motion": ["handheld"],
      "shot-subject": ["human"],
      "shot-location": ["int"],
      "num-people": [2],
      "sound-source": ["on-screen"]
    },
  },
}
```

#### Preparing AVE Dataset
We do not own the movie clips used in this work. However, they are publicly available on the [MovieClips YouTube channel](https://www.youtube.com/@MOVIECLIPS). Please follow the following steps to obtain the AVE dataset,
1. You can download all the movie scene clips using the [yt-dlp](https://github.com/yt-dlp/yt-dlp) package and the scenes url file in the dataset folder

```
python3 -m pip install -U yt-dlp
source download.sh
```
Note that geographic restriction might be an issue when downloading some of the videos depending on where you are located. We recommend you to use a [VPN](https://nordvpn.com/) if such case happens. It is also possible that some of the videos may no longer be available in the future. If such incidents happen, feel free to send me an email (<dawitmureja@kaist.ac.kr>) and I will gladly help.

2. After downloading the movie scenes, the shot clips of each scene can be obtained using the [FFmpeg](http://ffmpeg.org/download.html) module and the "start-time" and "end-time" labels of the shots in the [annotation file](https://drive.google.com/file/d/1b_4yO94UbkkUAiRo4TB6QLfNef4WQ3t-/view). 
```
sudo apt install ffmpeg
python scenes_to_shots.py
```

### Citation
If you find our work to be useful, please don't forget to cite us.
```bibtex
@inproceedings{argaw2022anatomy,
  Author    = {Argaw, Dawit Mureja and Heilbron, Fabian Caba and Lee, Joon-Young and Woodson, Markus and Kweon, In So},
  Title     = {The Anatomy of Video Editing: A Dataset and Benchmark Suite for AI-Assisted Video Editing},
  Booktitle = {ECCV},
  Year      = {2022}}
```
