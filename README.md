```markdown
# DriveSorter

DriveSorter is a full-stack application that includes a backend built with Django and a frontend built with React. This README file provides step-by-step instructions to set up and run the project.

## Prerequisites

Make sure you have the following installed on your machine:

- Docker
- Docker Compose

## Getting Started

### Clone the Repository

Clone the repository to your local machine using the following command:

```sh
git clone https://github.com/amir0135/DriveSorter1.git
cd DriveSorter1
```

### Running the Project with Docker Compose

The project is configured to use Docker Compose to manage both the frontend and backend services.

1. Ensure you are in the root directory of the project where the `docker-compose.yml` file is located.
2. Run the following command to build and start the services:

    ```sh
    docker-compose up --build
    ```

This command will build the Docker images for both the frontend and backend and start the containers.

### Accessing the Application

- **Frontend**: Open your browser and navigate to [http://localhost:3000](http://localhost:3000) to access the React frontend.
- **Backend**: The Django backend API will be running at [http://localhost:8000](http://localhost:8000).

## Project Structure

### Backend

The backend is a Django application located in the `backend` directory. It includes the following key files:

- `backend/Dockerfile`: Dockerfile for building the backend Docker image.
- `backend/manage.py`: Django's command-line utility for administrative tasks.
- `backend/requirements.txt`: List of Python dependencies (currently empty).

### Frontend

The frontend is a React application located in the `frontend` directory. It includes the following key files:

- `frontend/Dockerfile`: Dockerfile for building the frontend Docker image.
- `frontend/README.md`: Documentation for the frontend setup and scripts.
- `frontend/package.json`: Lists the dependencies and scripts for the React application.

## Available Scripts for Frontend

In the `frontend` directory, you can run the following scripts:

- `npm start`: Runs the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.
- `npm test`: Launches the test runner in the interactive watch mode.
- `npm run build`: Builds the app for production to the `build` folder.
- `npm run eject`: Ejects the configuration files and dependencies for customization.

For more details, refer to the `frontend/README.md` file in the `frontend` directory.

## Notes

- The backend currently has an empty `requirements.txt` file. You need to add the required Python packages for your Django application.
- Ensure that Docker and Docker Compose are properly installed and running on your machine before attempting to start the project.
```