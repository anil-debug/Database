import cv2
import numpy as np

def upscale_video(input_video_path, output_video_path):
    # Open the video file
    video_capture = cv2.VideoCapture(input_video_path)

    # Get video properties
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Upscale to 4K resolution
    target_width = 3840
    target_height = 2160

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (target_width, target_height))

    # Process each frame
    while True:
        ret, frame = video_capture.read()

        if not ret:
            break  # Break the loop when no more frames are available

        # Upscale the frame to 4K resolution
        upscaled_frame = cv2.resize(frame, (target_width, target_height))

        # Apply sharpening to the frame
        sharpened_frame = cv2.filter2D(upscaled_frame, -1, sharpening_kernel)

        # Increase brightness
        brightened_frame = increase_brightness(sharpened_frame)

        # Write the processed frame to the output video
        video_writer.write(brightened_frame)

        # Display progress
        current_frame = int(video_capture.get(cv2.CAP_PROP_POS_FRAMES))
        print(f"Processing frame {current_frame}/{total_frames}")

    # Release the VideoCapture and VideoWriter objects
    video_capture.release()
    video_writer.release()

    print("Video enhancement complete.")

# Define the sharpening kernel
sharpening_kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])

def increase_brightness(image, value=30):
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Split the image into hue, saturation, and value channels
    h, s, v = cv2.split(hsv_image)

    # Increase the brightness by adding a constant value
    v = cv2.add(v, value)

    # Merge the channels back together
    enhanced_hsv_image = cv2.merge([h, s, v])

    # Convert the image back to BGR color space
    enhanced_image = cv2.cvtColor(enhanced_hsv_image, cv2.COLOR_HSV2BGR)

    return enhanced_image

# Example usage
input_video_path = "original_video.mp4"
output_video_path = "enhanced_video_4k.mp4"
upscale_video(input_video_path, output_video_path)
