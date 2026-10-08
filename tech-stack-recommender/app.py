
import streamlit as st
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="TechMatch | Career AI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_PATH = Path(__file__).parent / "data" / "raw_skills.csv"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: #0b1020;
    color: #eef2ff;
}
header[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
[data-testid="stSidebar"] {
    background: #11182b;
    border-right: 1px solid #26314b;
}
.hero {
    padding: 34px;
    border-radius: 24px;
    background: linear-gradient(125deg, #172554 0%, #312e81 55%, #4c1d95 100%);
    border: 1px solid #45458a;
    margin-bottom: 28px;
}
.eyebrow {
    color: #a5b4fc;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.hero h1 {
    color: white;
    font-size: clamp(32px, 4vw, 48px);
    line-height: 1.15;
    margin: 12px 0;
    font-weight: 800;
}
.hero p {
    color: #dbe4ff;
    font-size: 16px;
    max-width: 650px;
}
.section-label {
    color: #a5b4fc;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.panel {
    background: #11182b;
    border: 1px solid #293550;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 16px;
}
.role-card {
    background: linear-gradient(145deg, #151e33, #11182b);
    border: 1px solid #293550;
    border-radius: 18px;
    padding: 23px;
    margin: 12px 0;
}
.role-title {
    color: #f8fafc;
    font-size: 22px;
    font-weight: 700;
}
.role-description {
    color: #aebbd2;
    font-size: 14px;
    line-height: 1.7;
}
.score {
    color: #a5b4fc;
    font-size: 30px;
    font-weight: 800;
    text-align: right;
}
.score-label {
    color: #94a3b8;
    font-size: 11px;
    text-align: right;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.skill-tag {
    display: inline-block;
    color: #c7d2fe;
    background: #202b49;
    border: 1px solid #35446b;
    border-radius: 20px;
    padding: 6px 10px;
    margin: 4px 4px 0 0;
    font-size: 12px;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    border: none;
    color: white;
    border-radius: 12px;
    font-weight: 700;
    min-height: 48px;
}
div.stButton > button[kind="primary"]:hover {
    border: 1px solid #c4b5fd;
    color: white;
}
div[data-baseweb="select"] > div {
    background: #151e33;
    border-color: #35446b;
    border-radius: 10px;
}
div[data-testid="stMetric"] {
    background: #11182b;
    border: 1px solid #293550;
    padding: 16px;
    border-radius: 14px;
}
hr {
    border-color: #293550;
}
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_roles():
    data = pd.read_csv(DATA_PATH)
    required = {"role", "skills", "description"}
    if not required.issubset(data.columns):
        raise ValueError(f"Dataset must contain: {sorted(required)}")
    data["skills"] = data["skills"].fillna("")
    data["description"] = data["description"].fillna("")
    return data


try:
    roles = load_roles()
except Exception as exc:
    st.error(f"Could not load the career dataset: {exc}")
    st.stop()


st.sidebar.markdown("## 🧭 TechMatch")
st.sidebar.caption("AI-powered career discovery")
st.sidebar.divider()
st.sidebar.markdown("### How it works")
st.sidebar.write("01 · Select your technical skills")
st.sidebar.write("02 · Compare your profile with career paths")
st.sidebar.write("03 · Explore your strongest matches")
st.sidebar.divider()
st.sidebar.caption("Powered by TF-IDF + cosine similarity")
st.sidebar.caption("Portfolio project · Python & Streamlit")

st.markdown("""
<div class="hero">
    <div class="eyebrow">Your skills. Your next move.</div>
    <h1>Find your place<br>in tech.</h1>
    <p>Discover career paths that align with your technical skills
    using an intelligent content-based recommendation engine.</p>
</div>
""", unsafe_allow_html=True)

all_skills = sorted({
    skill.strip()
    for cell in roles["skills"]
    for skill in cell.split(",")
    if skill.strip()
})

col1, col2 = st.columns([1.25, 0.75], gap="large")

with col1:
    st.markdown('<div class="section-label">01 / Your profile</div>',
                unsafe_allow_html=True)
    st.subheader("What do you work with?")
    selected_skills = st.multiselect(
        "Choose your technical skills",
        options=all_skills,
        default=[
            skill for skill in ["Python", "SQL", "Machine Learning"]
            if skill in all_skills
        ],
        placeholder="Search and select skills...",
    )
    extra_skills = st.text_input(
        "Additional skills",
        placeholder="e.g. Git, Linux, REST APIs",
    )

with col2:
    st.markdown('<div class="section-label">02 / Preferences</div>',
                unsafe_allow_html=True)
    st.subheader("Your recommendations")
    top_n = st.slider(
        "Number of career matches",
        min_value=1,
        max_value=min(5, len(roles)),
        value=min(3, len(roles)),
    )
    st.markdown("""
    <div class="panel">
        <b>✨ Personalised matching</b>
        <p style="color:#aebbd2;font-size:14px;line-height:1.7">
        Your skills are compared with the skill profiles of each career.
        The strongest matches appear first.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")
run = st.button("✦  Discover my career matches", type="primary",
                use_container_width=True)

if run:
    chosen = list(selected_skills)
    chosen.extend(
        item.strip()
        for item in extra_skills.split(",")
        if item.strip()
    )
    chosen = list(dict.fromkeys(chosen))

    if len(chosen) < 3:
        st.warning("Choose or enter at least three skills to continue.")
    else:
        vectorizer = TfidfVectorizer(
            lowercase=True,
            token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z+#.]*\b",
            ngram_range=(1, 2),
        )
        role_matrix = vectorizer.fit_transform(roles["skills"])
        user_vector = vectorizer.transform([" ".join(chosen)])
        scores = cosine_similarity(user_vector, role_matrix).flatten()

        results = roles.copy()
        results["match_score"] = scores
        results = results.sort_values(
            "match_score", ascending=False
        ).head(top_n)

        st.divider()
        st.markdown(
            '<div class="section-label">03 / Your results</div>',
            unsafe_allow_html=True,
        )
        st.subheader("Career paths worth exploring")
        st.caption(
            "Ranked by similarity between your skills and each career profile."
        )

        best = float(results["match_score"].max())
        m1, m2, m3 = st.columns(3)
        m1.metric("Skills in your profile", len(chosen))
        m2.metric("Careers compared", len(roles))
        m3.metric("Top similarity", f"{best * 100:.1f}%")

        if best == 0:
            st.info(
                "No vocabulary overlap was found. Try skills such as Python, "
                "SQL, Cloud, Docker, Java, or Machine Learning."
            )

        for rank, (_, row) in enumerate(results.iterrows(), start=1):
            score = float(row["match_score"])
            role_skills = [
                item.strip()
                for item in row["skills"].split(",")
                if item.strip()
            ]
            chosen_lower = {item.lower() for item in chosen}
            matched = [
                skill for skill in role_skills
                if skill.lower() in chosen_lower
            ]

            st.markdown(
                f"""
                <div class="role-card">
                    <div style="display:flex;justify-content:space-between;
                                align-items:center;gap:20px;flex-wrap:wrap">
                        <div>
                            <div class="section-label">MATCH #{rank}</div>
                            <div class="role-title">{row['role']}</div>
                        </div>
                        <div>
                            <div class="score">{score * 100:.1f}%</div>
                            <div class="score-label">Similarity</div>
                        </div>
                    </div>
                    <p class="role-description">{row['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.progress(score)
            if matched:
                st.markdown("**Skills you already have**")
                st.markdown(
                    " ".join(
                        f'<span class="skill-tag">{skill}</span>'
                        for skill in matched
                    ),
                    unsafe_allow_html=True,
                )
            with st.expander(f"Explore skills for {row['role']}"):
                st.write("**Typical skill profile**")
                st.write(", ".join(role_skills))
                missing = [
                    skill for skill in role_skills
                    if skill.lower() not in chosen_lower
                ]
                if missing:
                    st.write("**Skills to explore next**")
                    st.write(", ".join(missing))

        st.caption(
            "Similarity scores measure text alignment, not hiring probability "
            "or a guarantee of career suitability."
        )
        
        export_data = results[["role", "skills", "description", "match_score"]].copy()
        export_data["match_score"] = (
            export_data["match_score"] * 100
        ).round(1)
        export_data = export_data.rename(
            columns={"match_score": "similarity_percent"}
        )

        st.download_button(
            label="⬇️ Download career matches (CSV)",
            data=export_data.to_csv(index=False).encode("utf-8"),
            file_name="my_career_matches.csv",
            mime="text/csv",
            use_container_width=True,
        )


with st.expander("🧠 Understand the recommendation engine"):
    st.markdown("""
    1. **Input:** collect the user's technical skills.
    2. **TF-IDF:** represent each career's skills as weighted text features.
    3. **Cosine similarity:** compare the user profile with career vectors.
    4. **Ranking:** sort career paths from highest to lowest similarity.
    5. **Top-N filtering:** display the requested number of matches.

    This is content-based filtering and does not require historical ratings
    from other users.
    """)

st.divider()
st.markdown(
    "<p style='text-align:center;color:#7786a5;font-size:12px'>"
    "TECHMATCH · Built with Python, Streamlit & scikit-learn</p>",
    unsafe_allow_html=True,
)
