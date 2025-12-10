import streamlit as st
import pandas as pd
import utils

# --- Page Config ---
st.set_page_config(
    page_title="RLHF Preference Ranking",
    layout="wide",
    page_icon="⚖️"
)

# --- CSS for Minimalism ---
st.markdown("""
<style>
    .main {
        max-width: 1200px;
        margin: 0 auto;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em; 
    }
    .question-box {
        background-color: #f0f2f6; 
        padding: 20px; 
        border-radius: 10px; 
        margin-bottom: 20px;
        border-left: 5px solid #4CAF50;
    }
    .response-box {
        background-color: #ffffff;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        height: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if 'data' not in st.session_state:
    st.session_state.data = None
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# --- Callbacks ---
def submit_label(choice):
    row = st.session_state.data.iloc[st.session_state.current_index]
    utils.save_label(
        question=row['question'],
        response_a=row['response_a'],
        response_b=row['response_b'],
        preferred=choice
    )
    st.session_state.current_index += 1

def restart_labeling():
    st.session_state.current_index = 0

# --- Sidebar / Upload ---
with st.sidebar:
    st.title("Settings")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file:
        if st.session_state.data is None:
            df, error = utils.load_csv(uploaded_file)
            if error:
                st.error(error)
            else:
                st.session_state.data = df
                st.success(f"Loaded {len(df)} items.")
    
    st.markdown("---")
    st.info("**Instructions**:\n1. Upload a CSV.\n2. Read the Question.\n3. Compare Response A vs B.\n4. Choose the better response.")

# --- Main Interface ---
st.title("⚖️ RLHF Preference Ranking")

if st.session_state.data is None:
    st.info("👋 Welcome! Please upload a CSV file inside the sidebar to start labeling.")
    
    # Show sample format
    st.subheader("Expected CSV Format")
    st.dataframe(pd.DataFrame({
        "question": ["Example Question..."],
        "response_a": ["Response A text..."],
        "response_b": ["Response B text..."]
    }))
    
else:
    total_items = len(st.session_state.data)
    current_idx = st.session_state.current_index
    
    # Check if we are done
    if current_idx >= total_items:
        st.balloons()
        st.success("🎉 Labeling Complete!")
        
        # Show stats
        count, stats = utils.get_progress(total_items)
        st.subheader("Session Summary")
        col1, col2 = st.columns(2)
        with col1:
             st.metric("Total Labeled (All Time)", count)
        with col2:
             st.write("Preferences Distribution:")
             st.write(stats)

        if st.button("Restart Labeling"):
            restart_labeling()
            st.rerun()
            
    else:
        # Progress
        progress = (current_idx / total_items)
        st.progress(progress)
        st.caption(f"Item {current_idx + 1} of {total_items}")

        # Get current row
        row = st.session_state.data.iloc[current_idx]

        # Display Question
        st.markdown(f"""
        <div class="question-box">
            <h3>Question / Prompt</h3>
            <p style="font-size:1.1em;">{row['question']}</p>
        </div>
        """, unsafe_allow_html=True)

        # Display Responses
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("### 🅰️ Response A")
            st.markdown(f'<div class="response-box">{row["response_a"]}</div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Choose A", key="btn_a", type="primary"):
                submit_label("A")
                st.rerun()

        with col_b:
            st.markdown("### 🅱️ Response B")
            st.markdown(f'<div class="response-box">{row["response_b"]}</div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Choose B", key="btn_b", type="primary"):
                submit_label("B")
                st.rerun()
        
        # Tie / Skip buttons below
        st.markdown("<br>", unsafe_allow_html=True)
        col_tie, col_skip = st.columns([1, 1])
        with col_tie:
            if st.button("🤝 Tie", key="btn_tie"):
                submit_label("Tie")
                st.rerun()
        with col_skip:
            if st.button("⏩ Skip", key="btn_skip"):
                submit_label("Skip")
                st.rerun()

