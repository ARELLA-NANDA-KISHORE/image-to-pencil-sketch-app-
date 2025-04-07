import cv2
import numpy as np

def convert_to_sketch(image_path, output_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_image = cv2.bitwise_not(gray_image)
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    # Show the sketch
    cv2.imshow("Pencil Sketch", pencil_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result
    cv2.imwrite(output_path, pencil_sketch)
    print(f"Sketch saved to {output_path}")

# Example usage
convert_to_sketch("DSC_0204.jpg", "sketch_output.jpg")