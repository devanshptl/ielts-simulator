# IELTS Speaking Simulator

A web application that simulates the IELTS Speaking test with a Django backend and Flask frontend.

## Features

- Three-part IELTS Speaking test simulation
- Part 1: Introduction & Interview questions
- Part 2: Cue Card with 1-minute preparation and 2-minute speaking time
- Part 3: Follow-up questions
- Modern, responsive UI
- Timer functionality for Part 2

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ielts-simulator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the Django database:
```bash
cd ielts-simulator
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser to manage questions:
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the Django backend (in one terminal):
```bash
cd ielts-simulator
python manage.py runserver
```

2. Start the Flask frontend (in another terminal):
```bash
cd frontend
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Admin Interface

To add or manage questions, visit:
```
http://localhost:8000/admin
```

## Project Structure

```
ielts-simulator/
├── ielts_backend/     # Django project settings
├── questions/         # Django app for question management
├── frontend/         # Flask frontend application
│   ├── templates/    # HTML templates
│   └── app.py       # Flask application
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 