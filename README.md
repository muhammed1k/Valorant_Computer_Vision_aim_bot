# Valorant_Computer_Vision_aim_bot

in this repo is an implementation of yolov5 algorithim for riot games Valorant to create an AI based aim_bot that can detect enemies, predict bounding boxes for enemeies heads
and sends a mouse click to shoot the enemey

<details>
<summary>Demo</summary>
  sdasd
</details>

<details>
<summary>Custom Data</summary>
3K data were gathered from valorant clips and gameplays, using scutti you can convert videos into frames or capture screen shots at intervals while playing 
[scutti](https://github.com/heartexlabs/labelImg)
</details>

<details>
<summary>Transfer Learning</summary>
  
</details>

<details>
<summary>aim_bot.py</summary>
  
</details>
<details>
<summary>Training</summary>

The commands below reproduce YOLOv5 [COCO](https://github.com/ultralytics/yolov5/blob/master/data/scripts/get_coco.sh)
results. [Models](https://github.com/ultralytics/yolov5/tree/master/models)
and [datasets](https://github.com/ultralytics/yolov5/tree/master/data) download automatically from the latest
YOLOv5 [release](https://github.com/ultralytics/yolov5/releases). Training times for YOLOv5n/s/m/l/x are
1/2/4/6/8 days on a V100 GPU ([Multi-GPU](https://github.com/ultralytics/yolov5/issues/475) times faster). Use the
largest `--batch-size` possible, or pass `--batch-size -1` for
YOLOv5 [AutoBatch](https://github.com/ultralytics/yolov5/pull/5092). Batch sizes shown for V100-16GB.

```bash
python train.py --data coco.yaml --cfg yolov5n.yaml --weights '' --batch-size 128
                                       yolov5s                                64
                                       yolov5m                                40
                                       yolov5l                                24
                                       yolov5x                                16
```

<img width="800" src="https://user-images.githubusercontent.com/26833433/90222759-949d8800-ddc1-11ea-9fa1-1c97eed2b963.png">

</details>
