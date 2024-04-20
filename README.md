# General Recommendation System

A versatile recommendation system project (using Python) suitable for a variety of contexts, from job placements to educational events and more, designed as part of a unstop's detailed solution presentation.

#### Scope of the System
This project is a Flask-based web application tailored for users and organizers across various platforms. It supports functionalities for both individual users, such as job seekers or event participants, and administrators, such as recruiters or event organizers. The system enables users to sign up, log in, and receive personalized recommendations based on their skills, experiences, and past interactions. Organizers can log in to view listings (jobs, hackathons, courses, etc.) and see lists of participants or candidates tailored to their needs. This application provides a user-friendly platform aimed at streamlining the process of connecting individuals with relevant opportunities.

#### Software Requirements
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python with Flask
- **Database:** PostgreSQL
- **Operating System:** Linux
- **Data Science:** Utilizes Python libraries such as Pandas, NumPy, and Scikit-learn for complex recommendation algorithms.

#### Hardware Requirements
- A standard personal computer or laptop capable of running Python and PostgreSQL.

#### Files Included
- `app.py`: The main Flask application code.
- `jobs1.py`, `hackathon1.py`: Python code containing the logic for job and event recommendations.
- `jobs_info.csv`, `hackathons_data.csv`: CSV files containing detailed data for jobs and various events.
- `companies_table.txt`: Includes SQL statements to create and populate the ‘companies’ table with sample data.
- `templates`: Directory containing HTML templates for the user interface.

### Operational Instructions

1. **Setting up the Environment:**
   - Ensure Python is installed on your system.
   - Install the required Python packages using the following pip command:
     ```bash
     pip install flask psycopg2-binary pandas scikit-learn numpy werkzeug
     ```

2. **Setting up the Database:**
   - Confirm PostgreSQL is installed and running on your system.
   - Create a new database named 'placement':
     ```bash
     CREATE DATABASE placement;
     ```
   - Set your PostgreSQL password to 'project'.
   - Execute the SQL statements from `companies_table.txt` to set up and populate the ‘companies’ table.

3. **Running the Application:**
   - Navigate to the directory containing the `app.py`, `jobs1.py`, `hackathon1.py`, and respective CSV files.
   - Start the Flask application by running:
     ```bash
     python3 app.py
     ```

4. **Using the Application:**
   - Access the application by visiting ‘http://localhost:5000’ in your web browser.
   - On the welcome page, choose your role to proceed (e.g., job seeker, recruiter, event participant, organizer).
   - For individual users, log in or sign up to receive personalized recommendations based on predefined criteria such as skills, experience, and past activities.
   - For organizers, log in to view listings and receive a curated list of participants or candidates.
   - To log out, click on the Log Out button, redirecting you back to the welcome page.

This general recommendation system is designed to be adaptable, allowing easy integration and customization according to specific needs for various recommendation scenarios.

## Recommendations Output
![Recommendations Output](https://github.com/Manoramsharma/General_recommendation_system/blob/main/recommendations.png?raw=true)

## Kudos <3
