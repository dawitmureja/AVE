import os
import json
from tqdm import tqdm

annotation = json.load(open('/path/to/annotations.json', 'r'))
path = './dataset/scenes'
scenes = sorted([os.path.join(path, scene) for scene in os.listdir(path)])

save_path = './dataset/AVE'
if not os.path.exists(save_path):
    os.makedirs(save_path)

def convert_format(secs):
    hr = secs // 3600
    mi = (secs - (hr * 3600)) // 60
    sec = (secs - hr * 3600 - mi * 60) // 1
    msec = secs - hr * 3600 - mi * 60 - sec
    return '%02d:%02d:%02d'%(hr,mi,sec) + ('%f' % msec)[1:]

for scene in tqdm(scenes):
    scene_id = scene.split('/')[-1].split('.')[0]
    for shot_id in annotation[scene_id]:
        shot_st = annotation[scene_id][shot_id]['start-time'][0]
        shot_et = annotation[scene_id][shot_id]['end-time'][0]
        save_folder = os.path.join(save_path, scene_id)
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        os.system('ffmpeg -i {} -ss {} -t {} -async 1 {}'.format(scene, convert_format(shot_st), convert_format(shot_et-shot_st), os.path.join(save_folder, shot_id+'.mp4')))


