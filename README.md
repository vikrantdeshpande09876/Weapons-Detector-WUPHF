# Weapons-Detector-WUPHF

An AI product package to detect harmful objects and immediately send notifications to authorities.

![Product phase-1](https://github.com/vikrantdeshpande09876/Weapons-Detector-WUPHF/blob/main/Documentation/Logo-creation.png)

* Current architecture includes uploading an image; if `knife` or `pistol` detected in the image, a Kafka-message is published.

* I've also enabled a feature to detect weapons in webcam footage.

* The overall goal is to have a real-time streaming application for `CCTV` footage in closed spaces (schools or offices) which detects weapons, and sends an SMS/Email/Push alert to relevant authorities.

* The product will be hosted on the cloud so having a Kafka cluster coupled with single-shot object detection will support a high throughput of messages.

* The custom dataset used to train the YOLOv5 model is open-sourced: [here](https://github.com/ari-dasci/OD-WeaponDetection/tree/master/Weapons%20and%20similar%20handled%20objects).

* The dataset has `['pistol', 'smartphone', 'knife', 'monedero', 'billete', 'tarjeta']` classes which I've used for training. To ensure better training MAP I intend to filter only the `knife` and `pistol` images to avoid overcomplicated scenarios.

* I've used Google Colab to train my model for `300` iterations, by freezing the backbone `CSPDarknet-53` neural-network, and [my model](https://github.com/vikrantdeshpande09876/Weapons-Detector-WUPHF/tree/main/weapons-detector-yolo/utils/yolov5s.pt) seems to be performing relatively well with an MAP of ~80%. More training is certainly encouraged.

* I'm also compiling [notes](https://github.com/vikrantdeshpande09876/Weapons-Detector-WUPHF/blob/main/Documentation/Yolo-v4-Notes.docx) from the `YOLOv4` architecture implementation, and how it inspired the creation of `YOLOv5`.

* The name <b>Weapons-Detector: WUPHF!</b> is inspired from <b>The Office</b>: Ryan's brainchild [WUPHF](https://www.youtube.com/watch?v=OrVskziCc4w)



# EXECUTION:

1. Start the `kafka` Docker container:
> `./kafka-dockerized/start-kafka.bat`

2. Start the `weapons-detector` Docker container:
> `./start-app.bat`