# Valorant_Computer_Vision_aim_bot

in this repo is an implementation of yolov5 algorithim for riot games Valorant to create an AI based aim_bot that can detect enemies, predict bounding boxes for enemeies heads
and sends a mouse click to shoot the enemey

<details>
<summary>Demo</summary>
  sdasd
</details>

<details>
<summary>Custom_data</summary>

- 3K data were gathered from valorant clips and gameplays, using scutti you can convert videos into frames or capture screen shots at intervals while playing  [SCUTTI](https://github.com/TrevorSatori/Scutti)

- images was then labeled using pyImgLabel which creates BB txt files and suitable for yolo format [LblIMG](https://github.com/luishengjie/pyImgLabel)

</details>

<details>
<summary>Transfer Learning</summary>
  - training was done on yolov5 using yolov5s.pt pretrained weights with custom the dataset created and custom yaml file 
  - training was done for 5 epochs on google collab and best weights are later used to detect enemeis in game
  - !python train.py --img 640 --batch 16 --epochs 5 --data valorant.yaml --weights yolov5s.pt
</details>

<details>
<summary>aim_bot.py</summary>
  - mss is used to grab a live feed of computer screen 
  - loading live capture frames into cv2 and modeling the frames to get predictions
  - if enemeies are detected in the frame calculate enemey head position
  - move curosor and perform mouse click to kill the enemey
  
</details>
