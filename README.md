# Driver Sleep Detection System

## Overview
This repository contains the design and implementation of a Driver Sleep Detection System, which utilizes image processing techniques to detect and calculate the closing time of the driver's eyes. The system's objective is to ensure driver safety by monitoring their alertness and preventing potential accidents caused by drowsiness.

## Components
- **Python OpenCV**: OpenCV is used for image processing and computer vision tasks. It plays a crucial role in analyzing the driver's facial features and detecting eye closure.
- **Raspberry Pi 3**: The Raspberry Pi 3 serves as the hardware platform for this system, providing the computational power required for real-time image processing.
- **8MP Camera**: An 8-megapixel camera is used to capture images of the driver's face for analysis. It provides high-quality images essential for accurate eye detection.

## How it Works
1. The system captures images of the driver's face using the 8MP camera at regular intervals.

2. Python OpenCV is employed to process these images and identify the driver's eyes.

3. The system calculates the closing time of the eyes by analyzing the duration between eye open and close events.

4. If the system detects prolonged eye closure, it triggers alerts to keep the driver awake or notifies them to take a break, thus enhancing road safety.

## Usage
To set up and use this Driver Sleep Detection System:

1. Assemble the hardware components, including the Raspberry Pi 3 and the 8MP camera.

2. Install Python and OpenCV on the Raspberry Pi 3. You can refer to the [OpenCV installation guide](https://docs.opencv.org/master/df/d65/tutorial_table_of_content_introduction.html) for details.

3. Upload the provided Python script ([driver_sleep_detection.py](driver_sleep_detection.py)) to your Raspberry Pi 3.

4. Connect the 8MP camera to the Raspberry Pi 3.

5. Power on the system and run the Python script to initiate the sleep detection process.

6. Monitor the system's output and take appropriate actions if drowsiness is detected.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
If you have any questions or need further information, feel free to contact me at [mrezamostafavi98@gmail.com](mailto:mrezamostafavi98@gmail.com).

Stay awake and drive safely!
