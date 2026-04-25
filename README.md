# Software Testing Project

## Run the app
pip install -r requirements.txt
python app.py

## Run Tests
python -m pytest

## Performance Test
python -m locust -f performance/locustfile.py
## E2E Test
cd playwright
npm install
npx playwright test
