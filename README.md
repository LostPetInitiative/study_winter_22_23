# study_winter_22_23
A repo for MDS student projects in winter 2022-2023

# Pets-Face-Recognition

## Create New Conda Env
```
conda create --name pet2023 python=3.8
conda activate pet2023
```
## Install requirements
```
pip3 install -r requirements.txt
```

## Download the datasets
List of the datasets:

All3img_ExtraIG_train: (https://zenodo.org/record/7606128#.Y97B4HZBxD8)<br>
All3img_ExtraIG_val: (https://zenodo.org/record/7606128#.Y97B4HZBxD8)<br>
Kashtanka_test_alignment: (https://zenodo.org/record/7606149#.Y960CXZBxPY)<br>
Pet_face_detection_dataset1: (https://zenodo.org/record/7604865#.Y96vv3ZBxPY)<br>
Pet_face_detection_dataset2: (https://zenodo.org/record/7606080#.Y98jXnZBxPY)<br>

After downloading `All3img_ExtraIG_train.zip` and `All3img_ExtraIG_val.zip`, unzip them into `datasets` folder. Those two dataset for training the pet face recognition model.<br>
`Pet_face_detection_dataset1` unzip it into `./yolov7_bbox_landmarks/`, for training the first yolov7 detector. <br>
`Pet_face_detection_dataset2` unzip it into `./yolov7_bbox/data/`, for training the second yolov7 detector.

## Download Pretrained model
First Yolov7 Model:<br>(https://drive.google.com/u/6/uc?id=1MLjkpruH_VhACIz4Ow3oav0gS50uBPRE&export=download)<br>
Second Yolov7 Model:<br>(https://drive.google.com/u/6/uc?id=1NrnR4w-4Q4Nlw2hN-Ty4ZhTkT7J3EPWv&export=download)<br>
ResNet100 Pretrained Model:<br>(https://drive.google.com/u/0/uc?id=1-ITaMieQqLFgtYAmyQ8pIzpwaNDhE1Dt&export=download)<br>
Pet2023_BestBackbone Model:<br>(https://drive.google.com/u/8/uc?id=17IxKOmBRiKjbzkMw5IX59DQcMVyxnBwl&export=download)<br>
Pet2023_BestHeader Model:<br>(https://drive.google.com/u/8/uc?id=1--YMiueKiduYO5Njp_sE3cHUTzqE2hrF&export=download)<br>

Put `ResNet100 Pretrained Model`, `Pet2023_BestBackbone Model`, `Pet2023_BestHeader Model` into `./source` folder,<br>
Put `First Yolov7 Model` into `./yolov7_bbox_landmarks/weights`,<br>
Put `Second Yolov7 Model` into `./yolov7_bbox/weights`,

## Model training
Here are two pretrained backbones are provided, put them into the "source" folder
- ms1mv3_arcface_r100_fp16_backbone.pth (https://drive.google.com/u/0/uc?id=1MHjiSy3Snvqptf0K71sr2IzXGjC4Lbcq&export=download providied by deepinsight)
- Pet2023_BestBackbone.pth (the best backbone in this study, download in the Download Pretrained model section)
- Pet2023_BestHeader.pth (the best header in this study, download in the Download Pretrained model section)

Train model from scratch, use ms1mv3_arcface_r100_fp16_backbone.pth as the initial weight --backbone ms1mv3_arcface_r100_fp16_backbone.pth
```
cd myrun  # the folder path
python train.py --exp_name exp1 --backbone ms1mv3_arcface_r100_fp16_backbone.pth
```

Continue the previous training, input --exp_name and --continue_train,<br>
the default backbone and header are last_backbone.pth and last_header.pth
## Continue train the previous experiment
```
cd myrun  # the folder path
python train.py --exp_name exp1 --continue_train
```

### Optional setting
- train_data_path: change train path, default=train
- val_data_path: change val path, default=val
- continue_train: default=False
- backbone: backbone name, default:None
- header: header name, default:None
- num_epoch: default:30



## Inference on the test set and submit to the Pet3Challenge

Download the kashtanka test set `Test.zip` dataset and unzip it to the path `datasets`, Test.zip includes two folders
```
Test/
├── found
├── lost
├── synthetic_found
├── synthetic_lost
...
...
cat_dog_class_csv/
├── ff2.csv
├── fsl2.csv
├── ll2.csv
├── lsf2.csv
...
Load the model and run the test.py, it will generate a submit.tsv file in eval
```
cd eval  # the folder path
python test.py --backbone Res_mag_del2img_ExtraIG_replaced_backbone.pth
```

## Yolov7 Pet face detectors
### Train the first Yolov7 pet face detector
The first yolov7 detects both 3 landmarks (two eyes and nose) and bboxes, for training the first yolov7 detector, download the pet_face_detection_dataset_1, and unzip in the path: `./yolov7_bbox_landmarks/`

Download the initial weights file: (https://drive.google.com/file/d/1oIaGXFd4goyBvB1mYDK24GLof53H9ZYo/view), and put it in the path `weights/yolov7-face.pt`.

 ```
cd yolov7_bbox_landmarks  # the folder path
pip3 install -r requirements.txt
python train.py --data data/pet_train.yaml --cfg cfg/yolov7-face_3pt.yaml --weights weights/yolov7-face.pt --batch-size 4 --epochs 300 --kpt-label 3 --img 640 --name pet_face_detector1 --hyp data/hyp.scratch.p6.yaml
```

After training, test the Yolov7 on test set:
```
python test.py --data data/pet_test.yaml --kpt-label 3 --img 640 --batch 4 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/pet_face_detector1/weights/best.pt --name test
```

In addition, I had also labeled 300 images from kashtanka dataset, test the Yolov7 on kashtanka test set:
```
python test.py --data data/pet_test_kashtanka.yaml --kpt-label 3 --img 640 --batch 4 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/pet_face_detector1/weights/best.pt --name test_kashtanka
```

### Train the second Yolov7 pet face detector
The second only detects the bboxes, for training the second yolov7 detector, download the pet_face_detection_dataset_2, and unzip in the path: `./yolov7_bbox/data`. And download the initial weights from (https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt), and put it into `./yolov7_bbox/weights/yolov7x.pt`


 ```
cd yolov7_bbox  # the folder path
pip3 install -r requirements.txt
python train.py --workers 1 --device 0 --batch-size 4 --epochs 30 --img 640 640 --data data/pet_face_train.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7x_custom.yaml --name pet_face_detector2 --weights yolov7x.pt
```

After training, test the Yolov7 on test set:
```
python test.py --data data/pet_face_test.yaml --img 640 --batch 4 --conf 0.05 --iou 0.5 --device 0 --weights runs/train/pet_face_detector2/weights/best.pt --name test
```

In addition, I had also labeled 300 images from kashtanka dataset, test the Yolov7 on kashtanka test set:
```
python test.py --data data/kashtanka_test.yaml --img 640 --batch 4 --conf 0.05 --iou 0.5 --device 0 --weights runs/train/pet_face_detector2/weights/best.pt --name kashtanka_test
```

<b>Result of the first Yolov7 detectors </b>
| Dataset | Precision | Recall | mAP@.5 | mAP@.5:.95 | 
| ------- | ---------- | ---------- | ---------- | ---------- |
| test set  | 0.925 | 0.95 | 0.926 | 0.724 |
| kashtanka test | 0.959 | 0.913 | 0.972 | 0.584 | 

<b>Result of the second Yolov7 detectors </b>
| Dataset | Precision | Recall | mAP@.5 | mAP@.5:.95 | 
| ------- | ---------- | ---------- | ---------- | ---------- |
| test set  | 0.901 | 0.902 | 0.833 | 0.629 |
| kashtanka test | 0.977 | 0.997 | 0.994 | 0.671 | 

### Pet face alignmnet
The figure shows our two yolo detecters workflow:

<b>Workflow</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/yolo_flow.jpg "Yolov7's workflow")

The --source directory can be folder of images:
```
example_images/
├── image1.jpg
├── image2.jpg
...
```

Or folder of folder of images:
```
example_images/
├── cat1
│   ├── cat1_1.jpg
│   ├── cat1_2.jpg
│   ├── ...
│   └── cat1_5.jpg
├── dog1
│   ├── dog1_1.jpg
│   ├── dog1_2.jpg
│   ├── ...
│   └── dog1_5.jpg
...
└── cat10
    ├── cat10_1.jpg
    ├── cat10_2.jpg
    ├── ...
    └── cat10_5.jpg
```

First run kpts_and_bboxes_inf.py, it will create a json file (exp_kpt.json), which stores the images path, the landmarks and the bboxes.
```
python kpts_and_bboxes_inf.py --source example_images --weights yolov7_bbox_landmarks/runs/train/pet_face_detector1/weights/best.pt --name exp
```

Similarly, run bboxes_inf.py, it will create an oter json file (exp_bbox.json), which stores the images path and the bboxes.
```
python bboxes_inf.py --source example_images --weights yolov7_bbox/runs/train/pet_face_detector2/weights/best.pt --name exp
```

Finally, pass those two json files to the face_alignment.py, it will process face alignment on images and save it in exp_face_alignment folder 
```
python face_alignment.py --kpt-json exp_kpt.json --bbox-json exp_bbox.json --name exp_face_alignment
```


## Pet2023_BestModel Train Log and Test Result
- Pet2023_BestModel Training Log
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/Res_mag_All_Data_del2img_Extra2_replaced_train_log.png "Training")

- Pet2023_BestModel result
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/res_mag_new_test.jpg "Pet2023_BestModel result")

## DataSets Description
<b>Description</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/DataSet.png "Description")

<b>Examples of DataSets</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/examples_of_extraig.png "Examples of DataSets")



