# 📝 Code-Commentor

**Code-Commentor** is an AI-powered Python code comment generator built using a fine-tuned [Hugging Face](https://huggingface.co/) model ([CodeLlama](https://huggingface.co/models?search=codellama)). It provides instant, high-quality docstrings and inline comments for your Python functions, classes, and scripts.

## 🚀 Features

- **Automatic Python Code Commenting:** Paste raw Python code and receive commented code with clear explanations.
- **State-of-the-Art Model:** Uses your custom fine-tuned model hosted on Hugging Face (`Hemz1416/ai-code-commentor-v1`).
- **Modern Web UI:** Beautiful, responsive HTML interface for easy copy/paste and viewing results.
- **Fast & Local:** Runs entirely on your machine via Flask, no third-party API calls (except Hugging Face model download on first run).
- **Simple Backend:** Flask server handles inference and serves the frontend.
- **Easy to Extend:** Clean codebase for easy modification or retraining with new datasets.

## 🏝️ Demo

![Code-Commentor Screenshot](screenshot.png) <!-- Add a screenshot named screenshot.png in repo for best effect -->

## 📦 Installation

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [Flask](https://flask.palletsprojects.com/)
- [transformers](https://huggingface.co/docs/transformers/)
- Your fine-tuned model on Hugging Face Hub

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hemz1416/Code-Commentor.git
   cd Code-Commentor
   ```

2. **Install dependencies:**
   ```bash
   pip install flask transformers
   ```

3. **Download your fine-tuned model:**  
   The model will automatically be downloaded on first run based on `MODEL_NAME` in `ai_commentor.py`.  
   Make sure the model name is set to your Hugging Face repo (default: `Hemz1416/ai-code-commentor-v1`).

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Open in browser:**  
   Go to [http://localhost:5000](http://localhost:5000)

## 💡 Usage

1. Paste your Python code in the **Add Your Python Code Here** box.
2. Click **Go**.
3. View the commented code output on the right.
4. Copy the result and use it in your project!

## 🛠️ Project Structure

```
.
├── app.py              # Flask web server
├── ai_commentor.py     # Model loading and comment generation logic
├── dataset.json        # Sample dataset (for training/fine-tuning)
├── index2.html         # Frontend HTML (served via Flask)
├── README.md           # You're reading it!
└── ...
```

## 🤖 Model Info

- **Base Model:** CodeLlama (or similar code model from Hugging Face)
- **Fine-Tuned By:** [Hemz1416](https://huggingface.co/Hemz1416)
- **Model Repo:** [`Hemz1416/ai-code-commentor-v1`](https://huggingface.co/Hemz1416/ai-code-commentor-v1)

## 📚 Training Dataset

See `dataset.json` for sample pairs. You can extend this with your own code-commented pairs for further fine-tuning.

## ⚡ API Endpoint

- `POST /comment`  
  **Input:**  
  ```json
  { "code": "your python code here" }
  ```
  **Output:**  
  ```json
  { "commented_code": "code with generated comments" }
  ```

## 🖼️ Customization

- **Change Model:** Edit `MODEL_NAME` in `ai_commentor.py` to use a different Hugging Face model.
- **UI Improvements:** Modify `index2.html` for frontend tweaks.
- **Train Your Own Model:** Use `dataset.json` as a template for training examples.

## 💬 Feedback & Contributions

Pull requests, issues, and stars are welcome!  
If you use, extend, or retrain this project, let me know!

---

**Made with ❤️ by [Hemz1416](https://github.com/Hemz1416)**  
