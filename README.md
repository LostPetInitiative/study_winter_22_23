# study_winter_22_23
A repo for MDS student projects in winter 2022-2023

# Pets-Face-Recognition

## Create New Conda Env and install requirements
```
conda create --name pet2023 python=3.8
conda activate pet2023
```
## Install requirements
```
cd pet2023  # the folder path
pip3 install -r requirements.txt
```
## Train the new model
```
cd pet2023/myrun  # the folder path
python train.py --exp_name testing --train_data_path ../datasets/train --val_data_path ../datasets/val --continue_train --backbone last_backbone.pth --header last_header.pth --batch_size 16 --num_epoch 30
```
### Optional Setting
- train_data_path: change train path, default=train
- val_data_path: change val path, default=val
- continue_train: default=False
- backbone: backbone name, default:None
- header: header name, default:None
- num_epoch: default:30

## Download the datasets
List of the datasets:

All3img_ExtraIG_train.zip (https://somelink)<br>
All3img_ExtraIG_val.zip (https://somelink)<br>
Kashtanka_Dev_alignment.zip (https://somelink)<br>
Kashtanka_Test_alignment.zip (https://somelink)<br>

- cd Pet2023
After downloading these zip file, unzip them into "datasets" folder

## Download Pretrained model
Yolo Model: (https://somelink)<br>
ResNet100 Pretrained Model: (https://somelink)<br>
Pet2023_BestBackbone Model:  (https://somelink)<br>
Pet2023_BestHeader Model:  (https://somelink)<br>

After downloading these pretrained model, put them into "source" folder

## Our Yolov7 Checkpoints and configs
<b>Not finished</b>
- yolo result

<b>Yolov7's workflow</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/yolo_workflow.jpg "Yolov7's workflow")


## Our Pet2023_BestModel Checkpoints and configs
<b>Not finished</b>
- Pet2023_BestModel Training Log
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/Res_mag_All_Data_del2img_Extra2_replaced_train_log.png "Training")

- Pet2023_BestModel result
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/res_mag_new_test.jpg "Pet2023_BestModel result")

## DataSets Description
<b>Description</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/DataSet.png "Description")

<b>Examples of DataSets</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/examples_of_extraig.png "Examples of DataSets")



