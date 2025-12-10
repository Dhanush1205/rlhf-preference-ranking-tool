# RLHF Preference Ranking App

A fast, minimalistic, and effective tool for comparison-based labeling of model responses. Built with Python and Streamlit.

## 🚀 Features
- **Simple Interface**: Clean side-by-side comparison of two responses.
- **Efficient Labeling**: Quickly choose A, B, Tie, or Skip.
- **Auto-Saving**: Results are immediately saved to `labels.csv`.
- **Progress Tracking**: See how many items you've labeled.
- **Session Management**: Restart labeling easily without losing data.

## 🛠️ How to Run
1. **Install Requirements**:
   ```bash
   pip install streamlit pandas
   ```
2. **Run the App**:
   ```bash
   streamlit run app.py
   ```
3. **Open in Browser**: The app will open automatically at (usually) `http://localhost:8501`.

## 📖 How to Use
1. **Upload Data**: On the sidebar, upload a CSV file.
   - Required columns: `question`, `response_a`, `response_b`.
   - A sample file is provided in `sample_data/data.csv`.
2. **Label**: Read the prompt and both responses. Click the button corresponding to the better response.
3. **Finish**: When done, you'll see a summary page. You can close the tab or restart.
4. **Export**: Your labels are saved in `labels.csv` in the project directory.

## 🎓 Why this project is useful for RLHF internships

Reinforcement Learning from Human Feedback (RLHF) is the engine behind modern LLMs like ChatGPT and Gemini. This project demonstrates core competencies for working in AI alignment:

1.  **Human Preference Annotation**: You are building the exact tool interfaces that human labelers use to teach models what is "helpful and harmless".
2.  **Response Ranking**: It models the "Reward Modeling" phase of RLHF, where a model learns to predict human preferences between two outputs.
3.  **Understanding Alignment Workflows**: It shows you understand how raw model outputs are converted into a training signal (the preference dataset).
4.  **Dataset Creation**: By running this tool, you are actively creating a dataset (`labels.csv`) that could be used to train a Reward Model.
5.  **Evaluation UX Design**: It highlights the importance of clean UI/UX in reducing cognitive load for annotators, ensuring higher quality data.
