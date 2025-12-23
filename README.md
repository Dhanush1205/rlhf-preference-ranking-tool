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
