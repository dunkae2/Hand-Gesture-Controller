# Gesture Controller

This project uses hand gestures to control system brightness and volume. It is built on top of the [hand-gesture-recognition-using-mediapipe](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe) repository, with modifications to enable gesture-based system control.

## Features

- **Thumbs Up**: Increases brightness.
- **Thumbs Down**: Decreases brightness.
- **Horns Up (Index and Pinky Finger Up)**: Increases volume.
- **Horns Down (Index and Pinky Finger Down)**: Decreases volume.

## How to Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd GestureController
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Perform the gestures in front of your webcam to control brightness and volume.

## Requirements

- **mediapipe** 0.8.1
- **OpenCV** 3.4.2 or Later
- **TensorFlow** 2.3.0 or Later  
  (tf-nightly 2.5.0.dev or later is required only when creating a TFLite for an LSTM model)
- **scikit-learn** 0.23.2 or Later  
  (Only if you want to display the confusion matrix)
- **matplotlib** 3.3.2 or Later  
  (Only if you want to display the confusion matrix)

## Credits

This project is based on the original repository by [Kazuhito Takahashi](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe). The original implementation was translated and improved by [Nikita Kiselov](https://github.com/kinivi). This version customizes the functionality to control system brightness and volume using gestures.

## License

This project is under the [Apache v2 license](LICENSE).
