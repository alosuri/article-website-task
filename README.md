# Recruitment task

![alt-text](https://github.com/alosuri/article-website-task/blob/main/screenshot.png)


## How to install and run

1. Clone repository:

```
git clone https://github.com/alosuri/article-website-task.git
```

2. (Optional) Create and activate virtual environment:

- On macOS/Linux:
```
cd article-website-task
pip install virtualenv
python -m venv venv
source venv/bin/activate
```

- On Windows:
```
cd article-website-task
pip install virtualenv
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Add your API key to main.py:

Open the main.py file and add your API key as shown below:

```
client = OpenAI(
    api_key="PUT_YOUR_API_KEY_HERE"
)
```

5. Run program:

```
python main.py
```
