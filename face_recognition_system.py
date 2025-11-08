
import face_recognition
import cv2
import numpy as np
import pickle
import os
from datetime import datetime

class FaceRecognitionSystem:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.encodings_file = 'face_encodings.pkl'
        self.load_encodings()

    def load_encodings(self):
        '''Load previously saved face encodings'''
        if os.path.exists(self.encodings_file):
            try:
                with open(self.encodings_file, 'rb') as f:
                    data = pickle.load(f)
                    self.known_face_encodings = data['encodings']
                    self.known_face_names = data['names']
                print(f"Loaded {len(self.known_face_names)} known faces")
            except:
                print("No previous encodings found. Starting fresh!")
        else:
            print("No previous encodings found. Starting fresh!")

    def save_encodings(self):
        '''Save face encodings to file'''
        with open(self.encodings_file, 'wb') as f:
            pickle.dump({
                'encodings': self.known_face_encodings,
                'names': self.known_face_names
            }, f)
        print(f"Saved encodings for {len(self.known_face_names)} people")

    def register_new_face(self):
        '''Capture a selfie and register a new face'''
        print("\n=== REGISTRATION MODE ===")
        print("Position your face in the frame and press SPACE to capture")
        print("Press ESC to cancel\n")

        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            print("Error: Could not open camera")
            return

        captured = False
        face_encoding = None

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # Detect faces in real-time
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)

            # Draw rectangles around detected faces
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, "Press SPACE to capture", (left, top - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Display instructions
            cv2.putText(frame, "REGISTRATION MODE", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.putText(frame, f"Faces detected: {len(face_locations)}", (10, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            cv2.imshow('Register New Face', frame)

            key = cv2.waitKey(1) & 0xFF

            # Press SPACE to capture
            if key == ord(' '):
                if len(face_locations) == 1:
                    # Encode the face
                    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                    if face_encodings:
                        face_encoding = face_encodings[0]
                        captured = True
                        print("Face captured successfully!")
                        break
                elif len(face_locations) == 0:
                    print("No face detected! Please try again.")
                else:
                    print("Multiple faces detected! Please ensure only one face is visible.")

            # Press ESC to cancel
            elif key == 27:
                print("Registration cancelled")
                break

        video_capture.release()
        cv2.destroyAllWindows()

        if captured and face_encoding is not None:
            # Get person's name
            name = input("\nEnter your name: ").strip()
            if name:
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(name)
                self.save_encodings()
                print(f"\n✓ Successfully registered {name}!")
            else:
                print("Name cannot be empty. Registration cancelled.")

    def recognize_faces(self):
        '''Real-time face recognition from camera'''
        print("\n=== RECOGNITION MODE ===")
        print("Press 'q' to quit")
        print("Press 'r' to register a new face\n")

        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            print("Error: Could not open camera")
            return

        process_this_frame = True

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # Process every other frame for speed
            if process_this_frame:
                # Resize frame for faster processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                # Find faces
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    name = "Unknown Person"
                    confidence = 0

                    if len(self.known_face_encodings) > 0:
                        # Compare with known faces
                        matches = face_recognition.compare_faces(
                            self.known_face_encodings, face_encoding, tolerance=0.6)
                        face_distances = face_recognition.face_distance(
                            self.known_face_encodings, face_encoding)

                        if len(face_distances) > 0:
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index]:
                                name = self.known_face_names[best_match_index]
                                confidence = (1 - face_distances[best_match_index]) * 100

                    face_names.append((name, confidence))

            process_this_frame = not process_this_frame

            # Display results
            for (top, right, bottom, left), (name, confidence) in zip(face_locations, face_names):
                # Scale back up
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Choose color based on recognition
                if name == "Unknown Person":
                    color = (0, 0, 255)  # Red for unknown
                    label = name
                else:
                    color = (0, 255, 0)  # Green for known
                    label = f"{name} ({confidence:.1f}%)"

                # Draw rectangle
                cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

                # Draw label background
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)

                # Draw label text
                cv2.putText(frame, label, (left + 6, bottom - 6),
                           cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

            # Display mode and instructions
            cv2.putText(frame, "RECOGNITION MODE", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.putText(frame, f"Known faces: {len(self.known_face_names)}", (10, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, "Press 'r' to register | 'q' to quit", (10, frame.shape[0] - 20),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            cv2.imshow('Face Recognition System', frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break
            elif key == ord('r'):
                video_capture.release()
                cv2.destroyAllWindows()
                self.register_new_face()
                video_capture = cv2.VideoCapture(0)

        video_capture.release()
        cv2.destroyAllWindows()

    def run(self):
        '''Main menu to run the system'''
        while True:
            print("\n" + "="*50)
            print("FACE RECOGNITION SYSTEM")
            print("="*50)
            print(f"Currently registered: {len(self.known_face_names)} people")
            if self.known_face_names:
                print(f"Names: {', '.join(set(self.known_face_names))}")
            print("\nOptions:")
            print("1. Register New Face")
            print("2. Start Recognition")
            print("3. View Registered People")
            print("4. Delete All Data")
            print("5. Exit")
            print("="*50)

            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == '1':
                self.register_new_face()
            elif choice == '2':
                self.recognize_faces()
            elif choice == '3':
                print("\n=== REGISTERED PEOPLE ===")
                if self.known_face_names:
                    unique_names = set(self.known_face_names)
                    for i, name in enumerate(unique_names, 1):
                        count = self.known_face_names.count(name)
                        print(f"{i}. {name} ({count} encoding(s))")
                else:
                    print("No registered people yet!")
            elif choice == '4':
                confirm = input("\nAre you sure you want to delete all data? (yes/no): ")
                if confirm.lower() == 'yes':
                    self.known_face_encodings = []
                    self.known_face_names = []
                    if os.path.exists(self.encodings_file):
                        os.remove(self.encodings_file)
                    print("All data deleted!")
                else:
                    print("Deletion cancelled")
            elif choice == '5':
                print("\nThank you for using Face Recognition System!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("WELCOME TO FACE RECOGNITION SYSTEM")
    print("12th Standard Project")
    print("="*50)

    system = FaceRecognitionSystem()
    system.run()
