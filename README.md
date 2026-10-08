# 🧭 TechMatch | AI-Powered Career Recommender

**Find your place in tech.**

TechMatch is an interactive career recommendation application that helps users discover technical career paths based on their existing skills. It uses **TF-IDF vectorization** and **cosine similarity** to compare a user's skill profile with career requirements and recommend the closest matches.

🌐 **[Try TechMatch Live](https://techmatch-v3qovhntm76xtaymjkvimm.streamlit.app/)**

## ✨ Features

- 🎯 **Personalized recommendations:** Match your technical skills with relevant career paths.
- 🧠 **Content-based recommendation engine:** Uses TF-IDF and cosine similarity to rank career matches.
- 🛠️ **Skill exploration:** Select existing skills and enter additional skills.
- 📊 **Similarity scores:** Compare how closely your profile matches each career.
- 📚 **Skill gap exploration:** Explore the skills associated with recommended careers.
- 📥 **CSV export:** Download your career recommendations.
- 🎨 **Modern interface:** Dark-themed UI with a purple gradient hero section.

## 🖥️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Data handling |
| Scikit-learn | TF-IDF vectorization and cosine similarity |
| CSV | Career and skill dataset storage |

## ⚙️ How It Works

1. **Select your skills:** Choose the technical skills you already know.
2. **Build your profile:** Add any additional skills.
3. **Compare career paths:** TechMatch represents skill profiles using TF-IDF.
4. **Calculate similarity:** Cosine similarity measures the alignment between your profile and career profiles.
5. **Explore your matches:** Review recommended careers, similarity scores, and associated skills.

> Similarity scores measure text alignment. They do not represent hiring probability or guarantee career suitability.

## 🚀 Run Locally

### Prerequisites

- Python 3.10 or newer
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/singharindam20077/TechMatch.git
   ```

2. Navigate to the project directory:

   ```bash
   cd TechMatch/tech-stack-recommender
   ```

3. Create and activate a virtual environment:

   **Windows PowerShell**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS / Linux**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 📁 Project Structure

```text
TechMatch/
└── tech-stack-recommender/
    ├── app.py
    ├── requirements.txt
    ├── README.md
    └── data/
        └── raw_skills.csv
```

## 🎯 Project Goals

TechMatch demonstrates how content-based recommendation techniques can be applied to career discovery through an interactive Python application.

## 👨‍💻 Author

**Arindam Singh**

- GitHub: [@singharindam20077](https://github.com/singharindam20077)

---

⭐ If you find this project interesting, consider giving the repository a star!
