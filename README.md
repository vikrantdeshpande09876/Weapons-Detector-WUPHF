# Weapons-Detector: WUPHF!

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

<ol>
<li>Ensure you're in the <code>main</code> branch of <code>Weapons-Detector-WUPHF</code>:</li>
<code>> git checkout main</code>


<li>Configure your environment parameters in the current directory as a <code>.env</code> file:</li>

<code>DEBUG=False</code>
<code>SECRET_KEY='vikrantsecretkey'</code>
<code>FLASK_HOST='0.0.0.0'</code>
<code>FLASK_PORT='5009'</code>
<code>KAFKA_SERVER='kafka:9093'</code>
<code>RESPONSE_TOPIC='REPORT_WEAPONS'</code>
<code>GROUP_ID='test-consumer-group'</code>
<li>Start the <code>weapons-detector</code> Dockerized application.</li>
<code>> start-app.sh</code>
<br>
<br>
<li>Switch into the Git branch called <code>wuphf-notification-sender</code>:</li>
<code>> git checkout wuphf-notification-sender</code>

<li>Follow the <b>EXECUTION</b> instructions in the <code>README.md</code> for that branch:</li>
<ul>
<li>Start the <code>kafka</code> Docker container (it already contains <code>zookeeper</code> as a dependency so should run fine):</li>
<code>> /kafka-dockerized/start-kafka.sh</code>

<li>Configure your environment parameters in the current directory as a <code>.env</code> file:</li>

<code>KAFKA_SERVER='kafka:9093'</code>
<code>REQUEST_TOPIC='REPORT_WEAPONS'</code>
<code>GROUP_ID='test-consumer-group'</code>
<code>SENDER_EMAIL='***your_outlook_email_address***'</code>
<code>SENDER_PASSWORD='***your_outlook_email_password***'</code>
<code>RECEIVER_EMAIL='vikdeshp@iu.edu'</code>

<li>Start the <code>wuphf-notification-sender</code> Docker container:</li>
<code>> start-app.sh</code>
</ul>

<li>Navigate to <code>localhost:5009</code> and start experimenting!</li>
</ol>