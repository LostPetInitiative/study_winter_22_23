import os
import shutil
from torchvision.datasets.utils import download_and_extract_archive, download_url

if __name__ == "__main__":
    # download dataset:
    if not os.path.exists("./datasets/All3img_ExtraIG_train"):
        url = "https://zenodo.org/record/7606233/files/All3img_ExtraIG_train.zip?download=1"
        download_and_extract_archive(url, download_root=str("./datasets"), filename=f'train_set.zip')
    else:
        print("All3img_ExtraIG_train already exists in ./datasets/All3img_ExtraIG_train")

    if not os.path.exists("./datasets/All3img_ExtraIG_val"):
        url = 'https://zenodo.org/record/7606233/files/All3img_ExtraIG_val.zip?download=1'
        download_and_extract_archive(url, download_root=str("./datasets"), filename=f'val_set.zip')
    else:
        print("All3img_ExtraIG_val already exists in ./datasets/All3img_ExtraIG_val")

    if not os.path.exists("./datasets/Test"):
        url = 'https://zenodo.org/record/7606233/files/test_alignment.zip?download=1'
        download_and_extract_archive(url, download_root=str("./datasets"),filename=f'test.zip')
    else:
        print("Test already exists in ./datasets/Test")

    if not os.path.exists("./yolov7_bbox_landmarks/pet_face_detection_dataset_1"):
        url = 'https://zenodo.org/record/7604865/files/pet_face_detection_dataset_1.zip?download=1'
        download_and_extract_archive(url, download_root=str("./yolov7_bbox_landmarks/"), filename=f'pet_face_detection_dataset_1.zip')
    else:
        print("pet_face_detection_dataset_1 already exists in ./yolov7_bbox_landmarks/pet_face_detection_dataset_1")

    if not os.path.exists("./yolov7_bbox/data/pet_face_detection_dataset_2.zip"):
        url = 'https://zenodo.org/record/7606080/files/pet_face_detection_dataset_2.zip'
        download_and_extract_archive(url, download_root=str("./yolov7_bbox/data/"), filename=f'pet_face_detection_dataset_2.zip')
    else:
        print("pet_face_detection_dataset_2.zip already exists in ./yolov7_bbox/data/")
