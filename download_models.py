import os
import shutil
from torchvision.datasets.utils import download_and_extract_archive, download_url

if __name__ == "__main__":
    # download models:
    if not os.path.exists("./source/Res_mag_del2img_ExtraIG_replaced_backbone.pth"):
        print("Download Res_mag_del2img_ExtraIG_replaced_backbone.pth to ./source")
        url = 'https://zenodo.org/record/7606128/files/Res_mag_del2img_ExtraIG_replaced_backbone.pth?download=1'
        download_url(url, "./source", 'Res_mag_del2img_ExtraIG_replaced_backbone.pth')
    else:
        print("Res_mag_del2img_ExtraIG_replaced_backbone.pth already exists ./source")

    if not os.path.exists("./source/Res_mag_del2img_ExtraIG_replaced_header.pth"):
        print("Download Res_mag_del2img_ExtraIG_replaced_header.pth to ./source")
        url = 'https://zenodo.org/record/7606128/files/Res_mag_del2img_ExtraIG_replaced_header.pth?download=1'
        download_url(url, "./source", 'Res_mag_del2img_ExtraIG_replaced_header.pth')
    else:
        print("Res_mag_del2img_ExtraIG_replaced_header.pth already exists ./source")

    if not os.path.exists("./source/ms1mv3_arcface_r100_fp16_backbone.pth"):
        print("Download ms1mv3_arcface_r100_fp16_backbone.pth to ./source")
        url = 'https://zenodo.org/record/7606233/files/ms1mv3_arcface_r100_fp16_backbone.pth?download=1'
        download_url(url, "./source", 'ms1mv3_arcface_r100_fp16_backbone.pth')
    else:
        print("ms1mv3_arcface_r100_fp16_backbone.pth already exists ./source")

    if not os.path.exists("./yolov7_bbox_landmarks/weights/yolov7-pet-face.pt"):
        print("Download yolov7-pet-face.pt to ./yolov7_bbox_landmarks/weights")
        url = 'https://zenodo.org/record/7607110/files/yolov7-pet-face.pt?download=1'
        download_url(url, "./yolov7_bbox_landmarks/weights", 'yolov7-pet-face.pt')
    else:
        print("yolov7-pet-face.pt already exists ./yolov7_bbox_landmarks/weights")
    
    if not os.path.exists("./yolov7_bbox/weights/yolov7x-pet-face.pt"):
        print("Download yolov7x-pet-face.pt to ./yolov7_bbox/weights")
        url = 'https://zenodo.org/record/7607110/files/yolov7x-pet-face.pt?download=1'
        download_url(url, "./yolov7_bbox/weights", 'yolov7x-pet-face.pt')
    else:
        print("yolov7x-pet-face.pt already exists ./yolov7_bbox/weights")

    if not os.path.exists("./yolov7_bbox_landmarks/weights/yolov7-face.pt"):
        print("Download yolov7-face.pt to ./yolov7_bbox_landmarks/weights")
        url = "https://zenodo.org/record/7607110/files/yolov7-face.pt?download=1"
        download_url(url, "./yolov7_bbox_landmarks/weights", 'yolov7-face.pt')
    else:
        print("yolov7-face.pt already exists ./yolov7_bbox_landmarks/weights")

    if not os.path.exists("./yolov7_bbox/weights/yolov7x.pt"):
        print("Download yolov7x.pt to ./yolov7_bbox/weights")
        url = "https://zenodo.org/record/7607110/files/yolov7x.pt?download=1"
        download_url(url, "./yolov7_bbox/weights", 'yolov7x.pt')
    else:
        print("yolov7x.pt already exists ./yolov7_bbox/weights")
