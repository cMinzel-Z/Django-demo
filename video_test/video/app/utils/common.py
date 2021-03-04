import os
import time
import shutil
from django.conf import settings


def check_and_get_video_type(type_obj, type_value, message):
    try:
        type_obj(type_value)
    except:
        return {'code': -1, 'msg': message}

    return {'code': 0, 'msg': 'success'}


def handle_video(video_file, video_id, number):
    in_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp_input')
    out_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp_out')
    name = '{}_{}'.format(int(time.time()), video_file.name)
    path_name = '/'.join([in_path, name])

    temp_path = video_file.temporary_file_path()
    shutil.copyfile(temp_path, path_name)

    out_path = '/'.join([out_path, video_file.name.split('.')[0]])
    command = 'D:/FFMPEG/ffmpeg-4.3.2-2021-02-27-full_build/bin/ffmpeg -i {} -c copy {}.mp4'.format(path_name, out_path)

    os.system(command)
    return out_path
