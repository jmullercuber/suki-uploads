import datetime
import os
import time

import cv2
import boto3


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
CAMERA_PORT = 0
CAMERA_LOAD_TIME_SECS = 3.0
LOCAL_STORAGE_DIR = "data"
BUCKET_NAME = os.environ['BUCKET_NAME']

def get_image():
    camera = cv2.VideoCapture(CAMERA_PORT)
    time.sleep(CAMERA_LOAD_TIME_SECS)
    ret, img = camera.read()
    del(camera)  # free camera ASAP
    
    # no errors
    if ret:
        return img

def generate_file_name():
    iso_now = datetime.datetime.now().isoformat()
    file_name = f"{LOCAL_STORAGE_DIR}/{iso_now}.jpg"

    file_abs = f"{PROJECT_ROOT}/{file_name}"
    return file_name, file_abs

def save_image_locally(img, file_name):
    cv2.imwrite(file_name, img)
    return file_name

def upload(local_file_name, s3_key=None):
    # key default value
    if not s3_key:
        s3_key = local_file_name

    s3 = boto3.resource("s3")
    bucket = s3.Bucket(BUCKET_NAME)
    print(bucket.name)

    bucket.upload_file(local_file_name, s3_key)

def main():
    img = get_image()
    if img is not None:
        print("Captured image")
    else:
        print("Failed to get image T_T")
        return

    local_file_name, local_file_abs = generate_file_name()
    print(f"Generated File Name: {local_file_name}, {local_file_abs}")

    save_image_locally(img, local_file_abs)
    print("Successfully saved image locally")

    upload(local_file_abs, local_file_name)
    print(f"Upload of {local_file_name} done")

if __name__ == "__main__":
    main()