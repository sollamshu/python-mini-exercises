## 1.Set Up Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies. Open your terminal in the project's root directory and run:


mkdir mi-proyecto-python
cd mi-proyecto-python

# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

## 2. Install Dependencies
Install the necessary Python packages (like pytest) using pip:


pip install -r requirements.txt



If you haven't created requirements.txt yet, you can install pytest first and then generate the file:

pip install pytest
pip freeze > requirements.txt


Running Tests
pytest

pytest will automatically discover and run all files named test_*.py or *_test.py in the tests/ directory and its subdirectories. You'll see a clear report of which tests passed and which, if any, failed.