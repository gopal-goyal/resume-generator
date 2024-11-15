import streamlit as st
import json
from datetime import datetime
from utils import append_to_json_file  # Assuming this function is in utils.py
from resume_creation import generate_resume
from pdf2image import convert_from_path
import os
from docx import Document
from fpdf import FPDF
from PIL import Image

# Function to generate PDF from docx
def docx_to_pdf(docx_file, pdf_file):
    doc = Document(docx_file)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Convert docx content to PDF (basic version)
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)
    
    pdf.output(pdf_file)

# Function to generate resume image from PDF
def generate_resume_image(file_name):
    pdf_path = f'data/{file_name}.pdf'
    image_path = f'data/{file_name}.png'
    
    # Convert PDF to image (you may need to install poppler-utils)
    images = convert_from_path(pdf_path)
    
    # Save the first page as an image
    images[0].save(image_path, 'PNG')
    return image_path

# Function to get user input
def main():
    # Set the page layout to wide
    st.set_page_config(layout="wide")
    # Title of the page
    st.title("Resume Generator")
    a1, a2 = st.columns([2,1])
    # Section 1: Personal Details
    with a1:
        st.header("Personal Details")
        name = st.text_input("Name")
        designation = st.text_input("Designation")
        department = st.text_input("Department")
        company = st.text_input("Company")   
    ## Section 1.1: Contact Details
    with a2:
        st.header("Contact Details")
        contact = {
            "phone": st.text_input("Phone Number"),
            "email": st.text_input("Email"),
            "github": st.text_input("GitHub URL"),
            "linkedin": st.text_input("LinkedIn URL")
        }
    st.divider()
    b1, b2 = st.columns([2,1])
    # Section 2: Professional Summary
    with b1:
        st.header("Professional Summary")
        summary = st.text_input("Enter your professional summary here")
    # Section 3: Skills
    with b2:
        st.header("Skills")
        skills_input = st.text_input("Enter your skills (comma-separated)")
        skills = [skill.strip() for skill in skills_input.split(',')] if skills_input else []
    c1, c2 = st.columns([2,1])
    with c1:
        # Section 4: Experience
        st.header("Experience")
        experience = st.text_input("Enter your work experience details")

        # Section 5: Projects
        st.header("Projects")
        projects_input = st.text_input("Enter your projects (comma-separated)")
        projects = [project.strip() for project in projects_input.split(',')] if projects_input else []
    with c2:
        # Section 6: Education
        st.header("Education")
        education = []
        degrees = st.number_input("How many degrees do you have?", min_value=1, max_value=5, value=1)
        
        for i in range(degrees):
            degree = st.text_input(f"Degree {i+1}")
            institute = st.text_input(f"Institution for Degree {i+1}")
            cgpa = st.text_input(f"CGPA/Percentage for Degree {i+1}")
            year = st.text_input(f"Year of Graduation for Degree {i+1}")
            education.append({
                "degree": degree,
                "institute": institute,
                "cgpa": cgpa,
                "year": year
            })
    # Collect all the details into a dictionary
    data = {
        "name": name,
        "designation": designation,
        "department": department,
        "company": company,
        "contact": contact,
        "summary": summary,
        "skills": skills,
        "experience": experience,
        "projects": projects,
        "education": education
    }
    # Display the collected data (for debugging purposes)
    st.subheader("Collected Data (For Review)")
    st.write(data)
    # Button to Generate the Resume
    if st.button("Generate Resume and Save Data"):
        if name and designation:
            # Save the data to JSON with a key as the file_name as username_resume with current time
            current_datetime = datetime.now().strftime("%y%m%dT%H%M%S")
            file_name = f'{data["name"]}_resume_{current_datetime}'
            
            # Save data to a JSON file
            append_to_json_file(data, file_name)
            
            # Use the saved data to generate the resume (in .docx format)
            generate_resume(file_name)
            
            # Provide feedback to the user
            st.success(f"Data successfully saved for {name} on {current_datetime}.")
            
            # Allow the user to download the resume
            with open(f'data/{file_name}.docx', "rb") as file:
                st.download_button(
                    label="Download Resume",
                    data=file,
                    file_name=f'{file_name}.docx',
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        else:
            st.warning("Please fill out the required fields (Name and Designation).")

if __name__ == "__main__":
    main()
