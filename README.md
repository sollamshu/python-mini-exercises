# My Python Practice Project

Welcome to my Python practice project! This repository is designed to help me learn and master Python through a series of mini-exercises and challenges.

## Getting Started

To get this project up and running on your local machine, follow these steps:

### 1. Clone the Repository (Optional)

If you haven't already, clone this repository to your local machine:

```bash
git clone https://github.com/sollamshu/python-mini-exercises.git
cd python-mini-exercises
```

### 2. Create the virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment (macOS)

```bash
source .venv/bin/activate
```

### 4. Install Dependencies
Install the necessary Python packages (like pytest) using pip:

```bash
pip3 install -r requirements.txt
```

## Running Exercises
```bash
pytest
```

The pytest command will automatically discover and run all files named test_*.py or *_test.py in the tests/ directory and its subdirectories. You'll see a clear report of which tests passed and which, if any, failed.