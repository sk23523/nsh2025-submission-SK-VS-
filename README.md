# nsh2025-submission-SK-VS-

# Space Cargo Management System

This folder contains the backend implementation of our Space Cargo Management System. Built with Flask, the application provides APIs for managing storage containers, items, and their placement in a space station environment. It supports features like item search, waste management, time simulation, and logging.

The backend communicates with a frontend (if implemented) or directly via API calls to fetch, create, and manipulate container and item data, ensuring efficient space utilization and placement optimization for space missions.

## Project Overview

The backend is designed to address key functionalities:
- **Container Management**: Add and list storage containers with their dimensions and zones.
- **Item Placement**: Simulate and execute item placement within containers, prioritizing space efficiency and mission-critical requirements.
- **Real-Time Data Handling**: Process API requests for placement recommendations, item search, waste management, and time simulation.
- **Logging**: Track all actions performed by astronauts for future reference.

This codebase is modular and extensible, allowing seamless addition of new endpoints and services as the project evolves.

## Directory Structure
├── codeportion.py                  # Main Flask application file with API routes
├── Dockerfile              # Dockerfile for containerization
├── README.md               # This file
└── requirements.txt        # Python dependencies


### Key Components and Flow

1. **`codeportion.py`**
   - Acts as the entry point for the Flask application.
   - Defines API endpoints for adding containers, adding items, searching items, simulating time, and logging.
   - Uses in-memory data structures (`containers`, `items`) to store application state.

2. **API Endpoints**
   - `/api/add/container`: Add a new storage container.
   - `/api/add/item`: Add a new item to the system.
   - `/api/search`: Search for an item by its ID.
   - `/api/simulate/day`: Simulate time passing and update item statuses.
   - `/api/waste/identify`: Identify expired or depleted items as waste.
   - `/api/logs`: Retrieve logs of all actions performed.

3. **Dockerfile**
   - Contains instructions for building and running the application inside a Docker container.
   - Ensures compatibility across environments by using the `ubuntu:22.04` base image.

4. **`requirements.txt`**
   - Lists Python dependencies (e.g., Flask).

## Getting Started

Follow these steps to set up and run the Space Cargo Management System locally.

### Prerequisites

- **Python**: Version 3.x installed on your system.
- **pip**: Python package manager.
- **Git**: For cloning the repository.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>

