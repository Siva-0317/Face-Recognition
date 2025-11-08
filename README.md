# Face Recognition System

A simple Python project (suitable for a 12th‑grade project) that uses OpenCV and face-recognition to register faces via webcam and recognize them in real time. Face encodings are stored locally so data persists between runs.

## Features
- Register new faces using your webcam
- Real-time face detection and recognition
- Shows name + confidence/percentage on screen
- Persist face encodings to disk (no re-registration required)
- View registered users
- Delete all stored data

## Requirements
Install required packages with:
```bash
pip install -r requirements.txt
```

Example requirements.txt content:
```
numpy==1.26.4
opencv-python==4.5.5.64
opencv-contrib-python==4.5.5.64
face-recognition==1.3.0
cmake
dlib==19.24.0
```
If dlib fails to build on your machine, ask for a precompiled wheel for Windows.

## Quick Start
1. Open a terminal in the project folder (Windows):
   ```powershell
   cd "d:\Face Recognition"
   ```
2. Run:
   ```bash
   python face_recognition_system.py
   ```

## Menu Overview
When the program runs you will see:
1. Register New Face  
2. Start Recognition  
3. View Registered People  
4. Delete All Data  
5. Exit

### Registering a New Face
1. Choose option `1`.  
2. Position your face in front of the webcam.  
3. Press `SPACE` when your face is clear.  
4. Enter your name and confirm.  
5. Encoding saved to disk.

Tips: use good lighting, one face in frame, camera at face level.

### Starting Recognition
1. Choose option `2`.  
2. Webcam opens and detects faces in real time.  
3. Known faces: name displayed in green.  
   Unknown faces: label in red.  
4. Controls while recognition runs:
   - `q` — quit recognition
   - `r` — register another face

## Data Storage
Saved file:
- `face_encodings.pkl` — stores names and face encodings

To remove all data, use menu option `4` (Delete All Data) or delete `face_encodings.pkl`.

## Project Layout
Face Recognition/
├─ face_recognition_system.py  
├─ face_encodings.pkl   (auto-created after first registration)  
├─ requirements.txt  
├─ README.md

## Troubleshooting
- No webcam detected: ensure camera drivers are installed and not used by another app.  
- Poor recognition: improve lighting, ensure frontal face, collect several samples.  
- dlib install errors: request a prebuilt wheel for Windows.

## License
Use and modify for learning and non-commercial projects. Add a license file if you plan to publish.

If you want, I can also:
- generate an improved requirements.txt,
- add sample screenshots or usage GIFs,
- or produce unit tests for key modules.
```// filepath: d:\Face Recognition\README.md
# Face Recognition System

A simple Python project (suitable for a 12th‑grade project) that uses OpenCV and face-recognition to register faces via webcam and recognize them in real time. Face encodings are stored locally so data persists between runs.

## Features
- Register new faces using your webcam
- Real-time face detection and recognition
- Shows name + confidence/percentage on screen
- Persist face encodings to disk (no re-registration required)
- View registered users
- Delete all stored data

## Requirements
Install required packages with:
```bash
pip install -r requirements.txt
```

Example requirements.txt content:
```
numpy==1.26.4
opencv-python==4.5.5.64
opencv-contrib-python==4.5.5.64
face-recognition==1.3.0
cmake
dlib==19.24.0
```
If dlib fails to build on your machine, ask for a precompiled wheel for Windows.

## Quick Start
1. Open a terminal in the project folder (Windows):
   ```powershell
   cd "d:\Face Recognition"
   ```
2. Run:
   ```bash
   python face_recognition_system.py
   ```

## Menu Overview
When the program runs you will see:
1. Register New Face  
2. Start Recognition  
3. View Registered People  
4. Delete All Data  
5. Exit

### Registering a New Face
1. Choose option `1`.  
2. Position your face in front of the webcam.  
3. Press `SPACE` when your face is clear.  
4. Enter your name and confirm.  
5. Encoding saved to disk.

Tips: use good lighting, one face in frame, camera at face level.

### Starting Recognition
1. Choose option `2`.  
2. Webcam opens and detects faces in real time.  
3. Known faces: name displayed in green.  
   Unknown faces: label in red.  
4. Controls while recognition runs:
   - `q` — quit recognition
   - `r` — register another face

## Data Storage
Saved file:
- `face_encodings.pkl` — stores names and face encodings

To remove all data, use menu option `4` (Delete All Data) or delete `face_encodings.pkl`.

## Project Layout
Face Recognition/
├─ face_recognition_system.py  
├─ face_encodings.pkl   (auto-created after first registration)  
├─ requirements.txt  
├─ README.md

## Troubleshooting
- No webcam detected: ensure camera drivers are installed and not used by another app.  
- Poor recognition: improve lighting, ensure frontal face, collect several samples.  
- dlib install errors: request a prebuilt wheel for Windows.

## License
Use and modify for learning and non-commercial projects. Add a license file if you plan to publish.

If you want, I can also:
- generate an improved requirements.txt,
- add sample screenshots or usage GIFs,
- or produce unit tests for key modules.