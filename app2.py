import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_openai
from urllib.parse import urlparse

st.set_page_config(page_title="SHL Assessment Recommender")

st.title("🧠 SHL Assessment Recommender ")

# Input Mode Selection
input_mode = st.radio("How would you like to provide the job description?", ["🔗 Full SHL Job URL", "🧾 SHL Job Slug"])

# Get URL or Slug
if input_mode == "🔗 Full SHL Job URL":
    user_input = st.text_input("Enter SHL Job URL", placeholder="https://www.shl.com/solutions/products/product-catalog/view/account-manager-solution/")
else:
    user_input = st.text_input("Enter SHL Job Slug", placeholder="e.g., account-manager-solution")

if st.button("🔍 Extract & Recommend"):
    if not user_input.strip():
        st.warning("Please enter a valid SHL Job URL or Slug")
        st.stop()

    # Construct URL
    if input_mode == "🧾 SHL Job Slug":
        slug = user_input.strip().strip("/")
        url = f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/"
    else:
        url = user_input.strip()
        parsed_url = urlparse(url)
        slug = parsed_url.path.strip("/").split("/")[-1]

    st.markdown(f"📄 Parsing: [{url}]({url})")

    # Step 1: Scrape & Clean
    try:
        dom = scrape_website(url)
        body = extract_body_content(dom)
        cleaned = clean_body_content(body)
        with st.expander("🧼 Cleaned Job Description Text"):
            st.text_area("Cleaned HTML Body Text", cleaned, height=300)
    except Exception as e:
        st.error(f"❌ Error while scraping the job page: {e}")
        st.stop()

    # Step 2: LLM Prompt
    instruction = f"""
You are helping HR professionals identify relevant SHL Assessments.

From the SHL job description text below, do the following:

1. Suggest the **most likely job title** if it's not obvious from the slug: `{slug}`.
2. Recommend up to 10 individual SHL Assessments for this role.
3. Output only a **markdown table** with the following columns:

- Assessment Name (as markdown link to SHL catalog)
- Remote Testing Support (Yes/No)
- Adaptive/IRT Support (Yes/No)
- Duration (e.g., 20 mins)
- Test Type (e.g., Cognitive, Personality, etc.)
"""

    # Step 3: Call OpenAI via parse_with_openai
    with st.spinner("🔍 Generating assessment recommendations using AI..."):
        chunks = split_dom_content(cleaned)
        llm_output = parse_with_openai(chunks, instruction)

    # Step 4: Display Output
    st.subheader("🧪 Recommended SHL Assessments")
    st.markdown(llm_output)
