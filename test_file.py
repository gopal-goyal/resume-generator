'''
This test file will test various parts of the project, such as the resume generation functionality, file name sanitization, and JSON handling.
'''
import unittest
import os
import json
from datetime import datetime
from resume_creation import append_to_json_file, generate_resume


class TestResumeGenerator(unittest.TestCase):

    def setUp(self):
        # Setup a test directory to save generated files
        self.test_dir = 'test_data'
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_json = os.path.join(self.test_dir, 'data.json')
        self.test_file_name = "TestUser_resume_23_11_15-16:30:00"

        # Test data to be used in generating the resume
        self.test_data = {
            "name": "Test User",
            "designation": "Software Engineer",
            "department": "Development",
            "company": "Test Company",
            "contact": {
                "phone": "9876543210",
                "email": "testuser@example.com",
                "github": "https://github.com/testuser",
                "linkedin": "https://linkedin.com/in/testuser"
            },
            "summary": "Experienced in Python, AI, and software development.",
            "skills": ["Python", "Machine Learning", "AI", "JavaScript"],
            "experience": "Worked on several AI projects.",
            "projects": ["AI-based chatbot", "Data visualization tool"],
            "education": [{"degree": "B.Tech", "institute": "XYZ University", "cgpa": "8.7", "year": "2022"}]
        }

    def test_append_to_json_file(self):
        # Test appending data to JSON file
        append_to_json_file(self.test_data, self.test_file_name)
        
        # Check if file exists and data is added
        self.assertTrue(os.path.exists(self.test_json))
        with open(self.test_json, 'r') as f:
            data = json.load(f)
            self.assertIn(self.test_file_name, data)
            self.assertEqual(data[self.test_file_name]['name'], "Test User")

    def test_generate_resume(self):
        # Test if resume file is generated
        append_to_json_file(self.test_data, self.test_file_name)
        resume_file = generate_resume(self.test_file_name)

        # Check if the resume file is created with a valid name
        self.assertTrue(os.path.exists(resume_file))
        self.assertTrue(resume_file.endswith('.docx'))

    def test_sanitize_file_name(self):
        # Test sanitizing file name
        invalid_file_name = 'TestUser_resume_23_11_15-16:30:00'
        sanitized_name = generate_resume(invalid_file_name)

        # Check if the file name is sanitized (no colons in the name)
        self.assertNotIn(":", sanitized_name)
        self.assertTrue(sanitized_name.endswith('.docx'))

    def tearDown(self):
        # Cleanup test files after tests are done
        if os.path.exists(self.test_json):
            os.remove(self.test_json)
        
        # Remove any generated resume file
        if os.path.exists(resume_file):
            os.remove(resume_file)

        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)


if __name__ == '__main__':
    unittest.main()
