# QR Code Generator

## Description
A simple desktop application built using `Tkinter` for generating QR codes from user-provided links. The generated QR codes can be saved as `.png` files and displayed within the application.

## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/JordanVF/QRCodeGenerator.git
2. Navigate to the project directory: 
```bash
cd QRCodeGenerator
```
3. Install the required dependencies:
```bash
pip install pyqrcode pillow
```
 
## Usage
1. Run the application
2. Features:
   - Link Name: Provide a name for the file that will store the QR code (e.g., "MyQR").
   - Link: Enter the URL or text you want to convert into a QR code.
   - Generate QR Code: Click the button to generate and display the QR code.

## How it works
- Input Fields: The user provides a name and a link using Entry widgets in the Tkinter window.
- QR Code Generation: The application uses the pyqrcode library to generate the QR code for the provided link. The url.png() method saves the QR code as a .png file with the name provided by the user.
- Display: The generated QR code is displayed within the application using the PIL (Pillow) library to render the image.
- Canvas: A Tkinter Canvas widget is used to manage the layout and positioning of the application elements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

