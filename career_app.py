import streamlit as st

st.title("🎯 Career Discovery System")
st.write("Answer these 5 questions to discover your ideal career path based on your interests and personality!")

score = {
    "govt": 0,
    "tech": 0,
    "creative": 0,
    "business": 0,
    "management": 0
}

# Questions List
questions = [
    {
        "q": "1. What excites you the most?",
        "options": {
            "Solving public issues": "govt",
            "Building apps or websites": "tech",
            "Designing, art, or content": "creative",
            "Leading and organizing teams": "management",
            "Running your own business": "business"
        }
    },
    {
        "q": "2. Your dream workplace?",
        "options": {
            "Government office": "govt",
            "MNC or remote tech job": "tech",
            "Studio or creative setup": "creative",
            "Corporate with leadership": "management",
            "Own startup or freelancing": "business"
        }
    },
    {
        "q": "3. What do you enjoy most?",
        "options": {
            "Helping society and being disciplined": "govt",
            "Solving problems or coding": "tech",
            "Creating content or art": "creative",
            "Handling people and teams": "management",
            "Making money independently": "business"
        }
    },
    {
        "q": "4. What are you naturally good at?",
        "options": {
            "Following rules and systems": "govt",
            "Fixing gadgets or tech": "tech",
            "Drawing, acting, writing": "creative",
            "Organizing or leading": "management",
            "Finding new ideas to earn": "business"
        }
    },
    {
        "q": "5. Your long-term goal?",
        "options": {
            "Secure job with social impact": "govt",
            "Stable tech career with growth": "tech",
            "Be known for your passion": "creative",
            "Become a manager/leader": "management",
            "Own a business or startup": "business"
        }
    }
]

# Ask questions
for q in questions:
    user_answer = st.radio(q["q"], list(q["options"].keys()))
    category = q["options"][user_answer]
    score[category] += 1

# Submit Button
if st.button("Discover My Career Path"):
    top_field = max(score, key=score.get)
    st.subheader("✨ Recommended Career Path:")

    if top_field == "govt":
        st.success("→ Civil Services, Government Jobs, Public Sector Officer")
    elif top_field == "tech":
        st.success("→ Software Engineer, Data Analyst, QA Tester")
    elif top_field == "creative":
        st.success("→ Designer, Content Creator, Filmmaker, Writer")
    elif top_field == "management":
        st.success("→ HR, Project Manager, Operations Manager")
    elif top_field == "business":
        st.success("→ Entrepreneur, Digital Marketer, Freelancer")

    st.info("📘 Tip: Start learning skills in this domain. Look for internships, mentors, or certifications.")

