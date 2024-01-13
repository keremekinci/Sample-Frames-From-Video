import cv2
import os
from datetime import datetime
import sys
def create_directory(output_name):
    if not os.path.exists(output_name):
        print('==> Creating the {} directory...'.format(output_name))
        os.makedirs(output_name)
    else:
        print('==> Skipping create the {} directory...'.format(output_name))

def main(video_path):
    vidcap = cv2.VideoCapture(video_path)

    fps = vidcap.get(cv2.CAP_PROP_FPS)

    print(f"Video FPS: {fps}")

    desired_capture_interval = 6
    frame_interval = int(desired_capture_interval * fps)

    success = True
    count = 0
    minute = 1
    second = 0
    current_date = datetime.now().date()
    # ClassName= input("Sınıfın ismini giriniz")
    Input_dir = "Inputs_raw"
    create_directory(Input_dir);
    first_Min = Input_dir + "/Minute_1_raw"
    create_directory(first_Min)

    while success:
        success, image = vidcap.read()
        minuteString="Minute_"+str(minute)+"_raw"
        if count % frame_interval == 0:
            print(f'Read a new frame at time {count/fps} seconds.')
            cv2.imwrite(f"{Input_dir}/{minuteString}/second_{second}_raw.png",image)
            second+=6
        if(second==60):
            minute+=1
            minuteString="Minute_"+str(minute)+"_raw"
            create_directory(Input_dir+"/"+minuteString)
            second=0
        count += 1

    vidcap.release()

if __name__ == '__main__':
    video_path = 0
    main(video_path)