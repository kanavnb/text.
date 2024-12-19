import cv2


def highlight_handwriting(image_path, output_path, color=(0, 255, 0), thickness=2):
    """
    Highlights handwritten text in an image.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the highlighted image.
        color (tuple): Color of the highlight box in BGR format. Default is green.
        thickness (int): Thickness of the rectangle lines. Default is 2.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw rectangles around contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 10 and h > 10:  # Filter out small noise
            cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)
    
    # Save the result
    cv2.imwrite(output_path, image)
    print(f"Highlighted image saved to {output_path}")


highlight_handwriting("image.jpg", "highlighted_output.jpg")