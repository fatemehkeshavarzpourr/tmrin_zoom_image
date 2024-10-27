import cv2

def zoom_image(image, zoom_factor):
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Calculate the new dimensions
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

    # Resize the image
    zoomed_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Crop the center of the zoomed image to get back to original size
    start_x = (new_width - width) // 2
    start_y = (new_height - height) // 2

    cropped_image = zoomed_image[start_y:start_y + height, start_x:start_x + width]

    return cropped_image

def main():
    # Input image path and zoom factor
    image_path = input("Enter the path to the image: ")
    zoom_factor = float(input("Enter the zoom factor (e.g., 1.5 for 50% zoom): "))

    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not read the image.")
        return

    # Zoom the image
    zoomed_image = zoom_image(image, zoom_factor)

    # Display the original and zoomed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Zoomed Image", zoomed_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if name == "__main__":
    main()