import cv2

video_path = "videos/Join Global March Now.mp4"
frame_number_to_load = 300  # specify your frame here

cap = cv2.VideoCapture(video_path)
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number_to_load)
ret, frame = cap.read()
cap.release()

if not ret:
    raise Exception(f"Could not read frame number {frame_number_to_load}")

# For drawing rectangle
drawing = False
ix, iy = -1, -1
ex, ey = -1, -1

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, ex, ey, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            ex, ey = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ex, ey = x, y
        x_final = min(ix, ex)
        y_final = min(iy, ey)
        w_final = abs(ex - ix)
        h_final = abs(ey - iy)
        print(f"\n=== SELECTED AREA ===")
        print(f"x, y, w, h = {x_final}, {y_final}, {w_final}, {h_final}")
        print(f"=====================\n")
        with open("selected_area.txt", "w") as f:
            f.write(f"{x_final},{y_final},{w_final},{h_final}")

# Show frame and allow selection
cv2.namedWindow('Select Watermark Area')
cv2.setMouseCallback('Select Watermark Area', draw_rectangle)

while True:
    display_frame = frame.copy()
    if ix >= 0 and iy >= 0 and ex >= 0 and ey >= 0:
        cv2.rectangle(display_frame, (ix, iy), (ex, ey), (0, 255, 0), 2)

    cv2.imshow('Select Watermark Area', display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
