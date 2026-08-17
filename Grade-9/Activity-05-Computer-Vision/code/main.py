import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:

    # Capture a frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the colour frame to greyscale
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show the original colour camera
    cv2.imshow("Colour Camera", frame)

    # Show the greyscale camera
    cv2.imshow("Greyscale Camera", grey_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()