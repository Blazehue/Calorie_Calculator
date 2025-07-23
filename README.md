# Calorie Calculator

This project provides a simple web-based calorie calculator based on the Basal Metabolic Rate (BMR) formula. It allows users to input their height, weight, age, and gender to estimate their daily caloric needs.

## Features and Functionality

*   **BMR Calculation:** Calculates BMR based on user-provided height, weight, age, and gender using standard formulas.
*   **User-Friendly Interface:** Provides an HTML form for users to input their data.
*   **Clear Output:** Displays the calculated daily caloric needs to the user.
*   **Error Handling:** Handles invalid gender inputs and other potential errors gracefully.

## Technology Stack

*   **Python:**  Backend logic and API development.
*   **Flask:**  Web framework for creating the API.
*   **HTML:** Structure and content of the web pages.
*   **CSS:** Styling and visual presentation of the web pages (defined in `api/static/style.css` - not provided but referenced).

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.6+:** Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   **pip:** Python package installer (usually included with Python installations).
*   **Flask:** Install using `pip install Flask`

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Blazehue/Calorie_Calculator.git
    cd Calorie_Calculator
    ```

2.  **Navigate to the `api` directory:**

    ```bash
    cd api
    ```

3.  **Install Flask:**

    ```bash
    pip install Flask
    ```

## Usage Guide

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    This will start the development server.  The default address is usually `http://127.0.0.1:5000/`

2.  **Access the application in your web browser:**

    Open your web browser and go to `http://127.0.0.1:5000/`.

3.  **Enter your details:**

    Fill in the height, weight, age, and gender fields in the form.

4.  **Click "Calculate":**

    The calculated daily caloric needs will be displayed on the page.

## API Documentation

The application provides a simple API with the following routes:

*   **`/` (GET):**  Renders the `index.html` template, displaying the home page with the input form.

*   **`/calculate` (POST):**  Receives user input from the form (height, weight, age, gender), calculates the BMR, and returns the result as an HTML heading.

    **Request Body (form data):**

    *   `height`: Height in centimeters (float).
    *   `weight`: Weight in kilograms (float).
    *   `age`: Age in years (integer).
    *   `gender`: Gender ('male' or 'female').

    **Response:**

    Returns an HTML string containing the calculated daily caloric needs (e.g., `<h1>Your daily caloric needs are approximately 1500.00 kcal</h1>`) or an error message if there are any issues.

## Contributing Guidelines

Contributions are welcome!  To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request to the main repository.

Please ensure your code follows the existing style and includes appropriate comments and tests (if applicable).

## License Information

This project is licensed under the MIT License. See the `LICENSE` file (not present in the file list, but implied) for details.

## Contact/Support Information

For questions or support, please contact [Provide contact information or a link to discussions/issues].