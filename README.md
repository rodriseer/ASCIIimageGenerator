# Image to ASCII Art Converter

This project converts images into ASCII art using the Python Imaging Library (PIL). The script reads an image, processes it to grayscale, and then maps the pixel intensity to a set of ASCII characters. 
As a final output, it generates the ASCII art as a text file and also generates an image file with the colored ASCII representation.

# Features
- Converts images into a text-based ASCII representation.
- Produces an image where each pixel is replaced with a corresponding ASCII character.
- Supports customization of ASCII characters for different visual styles.
- 
# Usage
Install dependencies: Ensure you have the Python Imaging Library (PIL) installed. You can install it using the following command:
pip install pillow

# Adjust settings
- Modify the chars variable to change the characters used for mapping pixel intensity.
- Tweak the scaleFactor to control the level of detail. A higher value adds more ASCII characters to the image, while a lower value makes it simpler.
- Set the correct path to the image you want to convert and the font file location in the script.
 
# Run the script
After configuring the paths, run the Python script to generate the ASCII art text file (Output.txt) and the image file.

# Key Concepts
- ASCII Mapping: The chars list contains characters ordered by their visual density, allowing darker pixels to be mapped to denser characters (e.g., '@'), and lighter pixels to less dense ones (e.g., '.').
- Grayscale Conversion: The script averages the RGB values to create a grayscale image before converting it to ASCII.
- Output: Two outputs are generated—a text file containing the raw ASCII art and an image where the ASCII characters are rendered using colored fonts.
  
# Customization:
- Characters: Feel free to adjust the chars variable to include or exclude different characters, based on the look you want.
- Font: You can change the font used in the final image by modifying the path to your preferred .ttf font file.
- Scale Factor: The scaleFactor controls the level of detail in the ASCII conversion. Lower values create a simpler image, while higher values increase the complexity.

