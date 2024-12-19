import cv2
import pytesseract
from pytesseract import Output

# Load the image
image_path = 'image..jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply OCR to detect text
custom_config = r'--oem 3 --psm 6'  # Optimal for text block detection
detection_data = pytesseract.image_to_data(gray, output_type=Output.DICT, config=custom_config)

# Draw rectangles around all detected text
for i in range(len(detection_data['text'])):
    if detection_data['text'][i].strip() and int(detection_data['conf'][i]) > 0:  # Valid text with confidence
        x, y, w, h = (detection_data['left'][i], detection_data['top'][i], 
                      detection_data['width'][i], detection_data['height'][i])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle

# Display the image with highlighted text
cv2.imshow('Text Highlighted', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output image (optional)
output_path = 'highlighted_text_image.jpg'
cv2.imwrite(output_path, image)