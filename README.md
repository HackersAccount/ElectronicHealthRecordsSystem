# ElectronicHealthRecordsSystem
A robust and secure electronic health records (EHR) management system designed to streamline the storage, retrieval, and management of patient data for healthcare providers. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- PostgreSQL (optional, if you're using a different database adjust accordingly)

### Installation

1. Clone the repository to your local machine: `git clone https://github.com/HackersAccount/ElectronicHealthRecordsSystem.git`

2. Navigate to the project directory: `cd ElectronicHealthRecordsSystem`

3. Install the required packages: `pip install -r requirements.txt`

4. Set up your database:
   - Update the `DATABASES` configuration in `settings.py` with your database name, user, password, and host.
   - Run the following command to create the necessary tables: `python manage.py migrate`

5. Run the server: `python manage.py runserver`

Now, you should be able to access the application at `localhost:8000` in your web browser.



