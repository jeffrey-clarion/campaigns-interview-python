# Campaigns Interview (Python)

This is a simple Python application that demonstrates asynchronous call handling with simulated success/failure outcomes.

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd campaigns-interview-node
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python src/main.py
```

This will execute three simulated calls with different job IDs. Each call:

- Takes 2-5 seconds to complete
- Has a 70% chance of success
- Logs the start and completion of each call with its metadata

## Project Structure

- `src/utils.py`: Contains the core `send_call` function that simulates async calls
- `src/main.py`: Main application entry point that demonstrates the usage
- `requirements.txt`: Project dependencies

## Function Documentation

### send_call(job_id: str, metadata: Any) -> CallOutcome

Simulates an asynchronous call with the following characteristics:

- Random duration between 2-5 seconds
- 70% success rate
- Logs the start and completion of each call
- Returns either 'success' or 'failure'

Parameters:

- `job_id`: String identifier for the job
- `metadata`: Any additional data to be included with the call

Returns:

- `CallOutcome`: Literal type of either 'success' or 'failure'
