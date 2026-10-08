# Tech Stack Recommender

A simple content-based recommendation system that suggests career paths from a user's technical skills. It uses TF-IDF vectorization and cosine similarity, then ranks and displays the top matching roles.

## Features

- Select technical skills or enter additional skills.
- Convert role skill descriptions into TF-IDF vectors.
- Compare the user profile with roles using cosine similarity.
- Rank career paths and show the top-N recommendations.
- Display similarity scores and each role's typical skills.
- Includes a small editable sample dataset.

## Tech stack

- Python
- Streamlit
- pandas
- scikit-learn

## Run locally

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Create and activate a virtual environment (recommended).

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, you can run the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The app should open in your browser at the local address shown in the terminal.

## Dataset

`data/raw_skills.csv` contains three fields:

- `role`: the career path name
- `skills`: comma-separated skills associated with that role
- `description`: a short role summary

You can add rows or edit the skills to customize the recommender.

## How it works

1. **Input:** collect at least three skills from the user.
2. **Vectorization:** transform role skill text into TF-IDF feature vectors.
3. **Similarity:** calculate cosine similarity between the user's profile and each role.
4. **Ranking:** sort the roles by similarity score.
5. **Filtering:** return the top-N roles.

Cosine similarity measures text-vector alignment. The displayed percentage is a similarity score, not a job acceptance probability or a guarantee of career suitability.

## Limitations and possible improvements

- The included dataset is small and intended for demonstration.
- Skills are matched as text, so synonyms such as `ML` and `Machine Learning` may not be treated as identical.
- A larger, validated dataset and skill normalization would improve results.
- Future improvements could include skill-gap suggestions, unit tests, a larger dataset, and deployment.

## Project objective

This project demonstrates a basic AI recommendation pipeline using user input, feature extraction, similarity scoring, ranking, and top-N output.
