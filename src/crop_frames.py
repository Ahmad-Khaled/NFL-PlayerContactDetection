import cv2

def crop_video_frames(video_path, roi):
    # Open the video file using cv2.VideoCapture
    video_capture = cv2.VideoCapture(video_path)
    
    # Check if the video was opened successfully
    if not video_capture.isOpened():
        print(f'Error opening video file: {video_path}')
        return None
    
    # Extract the frames from the video
    frames = []
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        x1, y1, x2, y2 = roi
        cropped_frame = frame[y1:y2, x1:x2]
        frames.append(cropped_frame)
    
    # Release the VideoCapture object
    video_capture.release()
    
    return frames
