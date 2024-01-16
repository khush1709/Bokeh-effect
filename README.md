# Bokeh Effect Web App

This repository contains a simple web application that applies a Bokeh effect to an uploaded image. The application is built using Flask, a Python web framework, and utilizes the Pillow library (PIL) for image processing.

## Files and Directory Structure

- **index.py**: The main Python script containing the Flask application. It handles the web routes, image processing, and file uploads.
  
- **templates/index.html**: HTML template for the web interface. It includes a form for uploading an image file.

- **upload**: Directory to store uploaded images. It contains both the input image (`input.jpg`) and the output image with the Bokeh effect applied (`output.jpg`).

## Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install the required dependencies. You can use the following command in the terminal:

    ```bash
    pip install Flask Pillow
    ```

## How to Run

1. Navigate to the project directory.

    ```bash
    cd <project-directory>
    ```

2. Run the Flask application.

    ```bash
    python index.py
    ```

3. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the Bokeh Effect Web App.

## Usage

1. The main page displays a form with a file input and a button.

2. Choose an image file using the file input.

3. Click the "Upload and Apply Bokeh Effect" button to process the image.

4. The processed image with the Bokeh effect applied will be available for download.

## Notes

- The uploaded images are temporarily stored in the `uploads` directory.

- The Bokeh effect is applied using the GaussianBlur filter from the Pillow library.

- The web interface is styled with simple CSS for a clean and responsive design.

Feel free to explore and modify the code to enhance or customize the Bokeh effect web application according to your preferences.