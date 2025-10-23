# Calorie Calculator 🥗

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A modern, web-based calorie calculator that accurately estimates your daily caloric needs using scientifically-backed Basal Metabolic Rate (BMR) formulas. Perfect for fitness enthusiasts, health professionals, and anyone looking to maintain a healthy lifestyle.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [BMR Formula](#-bmr-formula)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

## 🎯 Overview

This project provides a simple yet effective web-based calorie calculator that helps users understand their daily caloric requirements. By inputting basic personal metrics (height, weight, age, and gender), users receive an accurate estimation of their Basal Metabolic Rate (BMR) - the number of calories their body burns at rest.

### Why Use This Calculator?

- **Evidence-Based**: Uses the widely-accepted Mifflin-St Jeor equation for accurate BMR calculations
- **Easy to Use**: Simple, intuitive interface requiring just 4 basic inputs
- **Fast & Lightweight**: No database required, instant calculations
- **Privacy-Focused**: All calculations done locally, no data stored or tracked
- **Open Source**: Free to use, modify, and contribute to

## ✨ Features

- ✅ **Accurate BMR Calculation**: Uses gender-specific formulas for precise results
- ✅ **User-Friendly Interface**: Clean, intuitive HTML form with proper validation
- ✅ **Instant Results**: Real-time calculation without page refresh
- ✅ **Error Handling**: Graceful handling of invalid inputs with helpful error messages
- ✅ **Responsive Design**: Fully responsive layout that works on desktop, tablet, and mobile devices
- ✅ **Cross-Browser Compatible**: Works on all modern browsers (Chrome, Firefox, Safari, Edge)
- ✅ **Lightweight**: Minimal dependencies for fast loading and performance
- ✅ **RESTful API**: Clean API endpoints for potential integration with other applications

## 🎬 Demo

![Calorie Calculator Demo](demo.gif)

> **Note**: Replace `demo.gif` with an actual screenshot or GIF of your application

**Live Demo**: [Coming Soon](#) <!-- Add your deployed app link here -->

## 🛠️ Technology Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Backend logic and calculations | 3.6+ |
| **Flask** | Web framework and API | 2.0+ |
| **HTML5** | Structure and semantic markup | - |
| **CSS3** | Styling and responsive design | - |
| **JavaScript** | Form validation and interactivity (optional) | ES6+ |

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.6 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (included with Python 3.4+)
- **Git**: For cloning the repository ([Download Git](https://git-scm.com/downloads))

### Verify Installation

```bash
# Check Python version
python --version  # or python3 --version

# Check pip version
pip --version  # or pip3 --version

# Check Git version
git --version
```

## 🚀 Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Blazehue/Calorie_Calculator.git
cd Calorie_Calculator
```

### 2. Create a Virtual Environment (Recommended)

Using a virtual environment keeps your project dependencies isolated:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
cd api
pip install -r requirements.txt
```

**Note**: If `requirements.txt` doesn't exist, create it with:
```
Flask==2.3.0
Werkzeug==2.3.0
```

### 4. Verify Installation

```bash
flask --version
```

## 📖 Usage

### Running the Application

1. **Start the Flask server**:

   ```bash
   cd api
   python app.py
   ```

   You should see output similar to:
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on
   ```

2. **Access the application**:
   
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Calculate your daily caloric needs**:
   
   - Enter your **height** (in centimeters)
   - Enter your **weight** (in kilograms)
   - Enter your **age** (in years)
   - Select your **gender** (male or female)
   - Click the **"Calculate"** button

4. **View your results**:
   
   Your estimated daily caloric needs will be displayed on the page.

### Example Calculation

**Input:**
- Height: 175 cm
- Weight: 70 kg
- Age: 30 years
- Gender: Male

**Output:**
```
Your daily caloric needs are approximately 1680.50 kcal
```

## 📡 API Documentation

The application provides a RESTful API with the following endpoints:

### Endpoints

#### `GET /`

Renders the home page with the calorie calculator form.

**Response:**
- **Status Code**: `200 OK`
- **Content-Type**: `text/html`
- **Body**: HTML page with input form

---

#### `POST /calculate`

Calculates BMR based on provided user data.

**Request:**

- **Content-Type**: `application/x-www-form-urlencoded`
- **Body Parameters**:
  
  | Parameter | Type | Required | Description |
  |-----------|------|----------|-------------|
  | `height` | float | Yes | Height in centimeters (e.g., 175.5) |
  | `weight` | float | Yes | Weight in kilograms (e.g., 70.2) |
  | `age` | integer | Yes | Age in years (e.g., 30) |
  | `gender` | string | Yes | Gender: 'male' or 'female' |

**Example Request (cURL):**

```bash
curl -X POST http://127.0.0.1:5000/calculate \
  -d "height=175" \
  -d "weight=70" \
  -d "age=30" \
  -d "gender=male"
```

**Response:**

- **Success (200 OK)**:
  ```html
  <h1>Your daily caloric needs are approximately 1680.50 kcal</h1>
  ```

- **Error (400 Bad Request)**:
  ```html
  <h1>Error: Invalid gender. Please specify 'male' or 'female'.</h1>
  ```

## 🧮 BMR Formula

This calculator uses the **Mifflin-St Jeor Equation**, which is considered one of the most accurate BMR formulas:

### For Men:
```
BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) + 5
```

### For Women:
```
BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) - 161
```

### About BMR

**Basal Metabolic Rate (BMR)** is the number of calories your body needs to perform basic life-sustaining functions while at rest, including:
- Breathing
- Blood circulation
- Nutrient processing
- Cell production

### Activity Multipliers

To calculate total daily calorie needs, multiply your BMR by an activity factor:

| Activity Level | Multiplier | Description |
|---------------|------------|-------------|
| Sedentary | 1.2 | Little to no exercise |
| Lightly Active | 1.375 | Light exercise 1-3 days/week |
| Moderately Active | 1.55 | Moderate exercise 3-5 days/week |
| Very Active | 1.725 | Hard exercise 6-7 days/week |
| Extremely Active | 1.9 | Very hard exercise, physical job |

## 📁 Project Structure

```
Calorie_Calculator/
│
├── api/
│   ├── app.py                 # Flask application and routes
│   ├── requirements.txt       # Python dependencies
│   └── templates/
│       └── index.html         # Main HTML page
│
├── static/                    # (Optional) Static assets
│   ├── css/
│   │   └── styles.css        # Custom stylesheets
│   ├── js/
│   │   └── script.js         # JavaScript files
│   └── images/
│       └── logo.png          # Images and icons
│
├── tests/                     # (Optional) Unit tests
│   └── test_app.py           # Test cases
│
├── .gitignore                # Git ignore file
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## 🗺️ Roadmap

Future enhancements planned for this project:

- [ ] **Activity Level Integration**: Add activity multipliers for total daily energy expenditure (TDEE)
- [ ] **Multiple BMR Formulas**: Include Harris-Benedict and Katch-McArdle formulas
- [ ] **Unit Conversion**: Support imperial units (lbs, inches)
- [ ] **Macronutrient Calculator**: Add protein, carbs, and fat recommendations
- [ ] **Goal Setting**: Add weight loss/gain calculators
- [ ] **History Tracking**: Store and visualize calculation history
- [ ] **Export Functionality**: Download results as PDF or CSV
- [ ] **Multi-language Support**: Internationalization (i18n)
- [ ] **Dark Mode**: Add theme toggle
- [ ] **REST API Expansion**: JSON response format option
- [ ] **Database Integration**: Optional data persistence
- [ ] **User Authentication**: Optional user accounts and profiles

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

### How to Contribute

1. **Fork the Project**
   
   Click the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**
   
   ```bash
   git clone https://github.com/YOUR_USERNAME/Calorie_Calculator.git
   cd Calorie_Calculator
   ```

3. **Create a Feature Branch**
   
   ```bash
   git checkout -b feature/AmazingFeature
   ```

4. **Make Your Changes**
   
   - Write clean, readable code
   - Follow existing code style and conventions
   - Add comments where necessary
   - Test your changes thoroughly

5. **Commit Your Changes**
   
   ```bash
   git add .
   git commit -m "Add some AmazingFeature"
   ```

6. **Push to Your Fork**
   
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open a Pull Request**
   
   Go to the original repository and click "New Pull Request"

### Contribution Guidelines

- Write clear, descriptive commit messages
- Update documentation for any changed functionality
- Add tests for new features (if applicable)
- Ensure your code passes all existing tests
- Follow PEP 8 style guide for Python code
- Be respectful and constructive in discussions

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

### What does this mean?

You are free to:
- ✅ Use this project commercially
- ✅ Modify the code
- ✅ Distribute the code
- ✅ Use it privately

Under the condition that:
- ℹ️ You include the original license and copyright notice

## 📧 Contact

**Rajat Pandey (Blazehue)**

- 📧 Email: [pandrajat123@gmail.com](mailto:pandrajat123@gmail.com)
- 🐙 GitHub: [@Blazehue](https://github.com/Blazehue)
- 💼 LinkedIn: [Add your LinkedIn profile](#)
- 🌐 Portfolio: [Add your portfolio site](#)

### Support

If you encounter any issues or have questions:

1. **Check existing issues**: [GitHub Issues](https://github.com/Blazehue/Calorie_Calculator/issues)
2. **Create a new issue**: [New Issue](https://github.com/Blazehue/Calorie_Calculator/issues/new)
3. **Email me directly**: pandrajat123@gmail.com

## 🙏 Acknowledgments

- **Mifflin-St Jeor Equation**: For the accurate BMR calculation formula
- **Flask Community**: For the excellent web framework and documentation
- **Contributors**: Thanks to all who have contributed to this project
- **Open Source Community**: For inspiration and support

## ⭐ Show Your Support

If you find this project helpful, please consider:

- ⭐ Starring the repository
- 🍴 Forking it for your own use
- 🐛 Reporting bugs or issues
- 💡 Suggesting new features
- 🤝 Contributing code improvements

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/Blazehue/Calorie_Calculator?style=social)
![GitHub forks](https://img.shields.io/github/forks/Blazehue/Calorie_Calculator?style=social)
![GitHub issues](https://img.shields.io/github/issues/Blazehue/Calorie_Calculator)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Blazehue/Calorie_Calculator)

---

<p align="center">
  Made with ❤️ and ☕ by <a href="https://github.com/Blazehue">Blazehue</a>
</p>

<p align="center">
  <i>If this project helped you, consider buying me a coffee!</i><br>
  <a href="https://www.buymeacoffee.com/blazehue">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee">
  </a>
</p>
