import cv2
import numpy as np

cap = cv2.VideoCapture("test2.mp4")

def image_to_canny(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    canny_img = cv2.Canny(blur_img, 50, 150)
    return canny_img

def region_of_interest(image):
    height = image.shape[0]
    triangle = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, triangle, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 50, 0), 10)
    return line_image

def fill_lane(image, lines):
    if lines is None or len(lines) != 2:
        return image
    
    left_line, right_line = lines
    poly_points = np.array([
        [left_line[0], left_line[1]],
        [left_line[2], left_line[3]],
        [right_line[2], right_line[3]],
        [right_line[0], right_line[1]]
    ])
    
    cv2.fillPoly(image, [poly_points], color=(0, 120, 0))
    return image

def make_coordinates(image, line_parameters):
    if line_parameters is None:
        return None
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1 * (3 / 5))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    
    left_fit_average = np.average(left_fit, axis=0) if left_fit else None
    right_fit_average = np.average(right_fit, axis=0) if right_fit else None
    
    left_line = make_coordinates(image, left_fit_average) if left_fit_average is not None else None
    right_line = make_coordinates(image, right_fit_average) if right_fit_average is not None else None
    
    return np.array([line for line in [left_line, right_line] if line is not None])

while (cap.isOpened()):

    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    _, frame = cap.read()

    if frame is None:
        break

    canny = image_to_canny(frame)
    cropped_img = region_of_interest(canny)
    lines = cv2.HoughLinesP(cropped_img, 2, np.pi / 180, threshold=100, lines=np.array([]), minLineLength=40, maxLineGap=5)
    averaged_lines = average_slope_intercept(cropped_img, lines)
    line_image = display_lines(frame, averaged_lines)
    filled_image = fill_lane(line_image, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, filled_image, 1, 1)

    frame=cv2.resize(frame,(640,360))
    combo_image=cv2.resize(combo_image,(640,360))
    cv2.imshow("Original Video", frame)
    cv2.imshow("Lane detection", combo_image)

    if cv2.waitKey(1) & 0xFF == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
