# KL Agent Backend

This project is a Flask-based backend API for managing computer data.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute:

```
python server.py
```

The API will be available at `http://localhost:5000`.

## Endpoints

- `GET /api/computers`: Returns a list of computers.
- `GET /api/computers/<pc>`: Returns data for a specific computer identified by `<pc>`.