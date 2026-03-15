import streamlit as st
import PyPDF2
import io
import plotly.graph_objects as go
from langdetect import detect
from deep_translator import GoogleTranslator
from skill_extractor import extract_skills
from career_matcher import match_careers
from roadmap_generator import generate_roadmap

st.set_page_config(
    page_title="Career DNA Analyzer",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 AI Career DNA Analyzer")
st.subheader("Upload your resume in ANY language — get your personalized career roadmap")

st.markdown("---")

input_method = st.radio("Choose input method:", ["📝 Type your skills", "📄 Upload PDF resume"])

resume_text = ""

if input_method == "📝 Type your skills":
    resume_text = st.text_area(
        "Type your skills and experience here (any language!)",
        height=200,
        placeholder="Example: I know Python, Machine Learning, SQL... or type in your own language!"
    )
else:
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
        for page in pdf_reader.pages:
            resume_text += page.extract_text()
        st.success("✅ PDF uploaded successfully!")
        st.text_area("Extracted text:", resume_text, height=150)

if st.button("🔍 Analyze My Career DNA", type="primary"):
    if not resume_text.strip():
        st.warning("Please enter some text or upload a PDF first!")
    else:
        # Detect and translate language
        try:
            detected_lang = detect(resume_text)
            if detected_lang != "en":
                st.info(f"🌍 Detected language: **{detected_lang.upper()}** — Translating to English...")
                resume_text = GoogleTranslator(source="auto", target="en").translate(resume_text)
                st.success("✅ Translation complete!")
            else:
                st.info("🌍 Detected language: **English**")
        except:
            st.warning("Could not detect language, proceeding in English...")

        with st.spinner("Extracting your skills..."):
            skills_found = extract_skills(resume_text)

        if not skills_found:
            st.error("No skills found. Try mentioning Python, SQL, Machine Learning etc.")
        else:
            st.success(f"✅ Found {len(skills_found)} skills: {', '.join(skills_found)}")

            with st.spinner("Matching you to careers..."):
                career_results = match_careers(skills_found)

            st.markdown("---")
            st.header("🎯 Your Career Matches")

            # Bar chart
            careers = [r["career"] for r in career_results]
            scores = [r["match"] for r in career_results]
            colors = ["#00FFB2", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]

            fig = go.Figure(go.Bar(
                x=scores,
                y=careers,
                orientation="h",
                marker_color=colors[:len(careers)],
                text=[f"{s}%" for s in scores],
                textposition="outside"
            ))
            fig.update_layout(
                title="Career Match Scores",
                xaxis_title="Match %",
                yaxis_title="Career",
                height=350,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white")
            )
            st.plotly_chart(fig, use_container_width=True)

            # Top 3 metric cards
            cols = st.columns(3)
            for i, result in enumerate(career_results[:3]):
                with cols[i]:
                    st.metric(
                        label=result["career"],
                        value=f"{result['match']}%"
                    )
                    st.caption(result["description"])

            # Roadmap
            top_career = career_results[0]
            roadmap_data = generate_roadmap(skills_found, top_career["required_skills"])

            st.markdown("---")
            st.header(f"🗺️ Your Roadmap → {top_career['career']}")

            if roadmap_data["already_have"]:
                st.success(f"✅ You already have: {', '.join(roadmap_data['already_have'])}")

            if roadmap_data["roadmap"]:
                st.info(f"📅 Estimated time: {roadmap_data['total_weeks']} weeks")
                for item in roadmap_data["roadmap"]:
                    with st.expander(f"Week {item['week']} — Learn {item['skill']}"):
                        for step in item["steps"]:
                            st.markdown(f"- {step}")
            else:
                st.balloons()
                st.success("🎉 You already have all required skills for this career!")