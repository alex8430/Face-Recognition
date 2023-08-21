# Face-Recognition

## Face Recognition model With OpenCV Python

A Face Recognition model built using OpenCV and Python. This project allows you to train the machine to recognize your face by providing it with multiple images of yourself.

### Getting Started

Follow these steps to get started with the Face Recognition model:

1. Gather your photographs: Collect at least 5-6 photographs of yourself. The more photographs you provide, the higher the accuracy of the model.

2. Organize your photographs: Place your photographs in the `Test_Image` folder. Create a subfolder with your name and put your images there.

3. Train the model: Run the `face_train.py` file. This will create a `trainer.yml` file that holds the training data.

4. Recognize yourself: Run the `face_recognition.py` file. This will open a camera window and attempt to recognize your face in real-time.

## Note

- Download Required Libraries: Ensure you have the required libraries downloaded before running the scripts.

- Image Format: If your images are not in the JPG format, you need to modify the `face_train.py` script. Open the script and locate line 22. Change the line to match your image format:
  ```python
  if file.endswith('your_img_format'):

## Prerequisites
1. Python 
2. OpenCV library 
3. Additional libraries or packages specific to your project

## Installation 
1. Clone this repository: git clone https://github.com/alex8430/face-recognition.git
2. Navigate to the project directory: cd face-recognition
3. Install required packages: pip install -r requirements.txt

## Usage
1. Prepare your photographs as described above.
2. Train the model using face_train.py.
3. Run the model with real-time face recognition using face_recognition.py.


## Contact

For questions or suggestions, feel free to reach out to me at pankajvermacr7@gmail.com or through [LinkedIn](https://www.linkedin.com/in/pankajvermacr7/).

