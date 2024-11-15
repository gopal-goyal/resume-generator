# Resume Generator with Python

## Create Professional Resumes Effortlessly

### Overview

Looking for an easy way to generate professional resumes? Our Python-based Resume Generator simplifies the process, offering users an intuitive interface to input their details, save them, and download polished resumes in `.docx` format. Whether you're an aspiring professional or just looking to update your resume, this tool is here to help!

### Getting Started

Follow these steps to get started with the Resume Generator:

#### Step 1: Clone the Repository

Clone the project to your local machine:
git clone https://github.com/yourusername/resume_with_python.git

#### Step 2: Navigate to Project Directory

Navigate into the project folder:
cd resume_with_python

#### Step 3: Set Up Virtual Environment

We recommend using a virtual environment to manage dependencies. Create and activate the environment with the following commands:

**Windows**
python -m venv env
.\env\Scripts\activate

**macOS/Linux**
python3 -m venv env
source env/bin/activate

#### Step 4: Install Dependencies

Install the required dependencies:
pip install -r requirements.txt

#### Step 5: Run the Application

Start the application with Streamlit:
streamlit run app.py
This will start the application and open it in your default browser. You can then start filling in your details to generate a custom resume.

### Key Features

- **User-Friendly Interface**: Easy-to-use form to input your details.
- **Dynamic Resume Generation**: Automatically generates a resume in `.docx` format based on user inputs.
- **Save Data**: Store your resume data in a structured JSON format for future edits.
- **Customizable Templates**: Tailor the sections like Skills, Experience, Education, and more.
- **Instant Download**: Download your generated resume instantly with a click of a button.

### Project Documentation

- **app.py - Main Application Logic**  
  This file is where the core functionality lives. It hosts the user interface (UI) created with Streamlit and collects inputs for the resume. It also handles saving the data and calling the resume creation logic.

- **resume_creation.py - Resume Generation Logic**  
  This file is responsible for taking the collected data and turning it into a professional resume using the `python-docx` library. It formats the content into sections such as contact information, skills, experience, and education.

- **data.json - User Data Storage**  
  Stores the user's resume data in JSON format. Each resume submission appends new data to this file, allowing users to track their inputs or make changes later.

### Testing and Quality Assurance

We’ve written comprehensive tests to ensure that the resume generation process is smooth and reliable. The project includes several tests for different types of data inputs and edge cases.
