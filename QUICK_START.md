# 🚀 Quick Start Guide - Run in VS Code

## Step 1: Open Project in VS Code

1. Open **VS Code**
2. Click **File** → **Open Folder...**
3. Navigate to: `AI Powered E-Waste` folder
4. Click **Open**

---

## Step 2: Open Terminal in VS Code

Press **`` Ctrl+` ``** (backtick key) or go to **Terminal** → **New Terminal**

You should see a terminal at the bottom of VS Code.

---

## Step 3: Set Up Python Environment (First Time Only)

Copy and paste these commands one by one into the terminal:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# OR if on Windows, use:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

You should see `(venv)` in your terminal prompt when activated.

---

## Step 4: Check if Model Exists

The model should already exist, but if you get an error, run:

```bash
# Generate data (if needed)
python src/gen_data.py

# Train model (if needed)
python src/train.py
```

---

## Step 5: Run the Application

### **Easiest Method - Press F5:**

1. Press **F5** key (or click the ▶️ play button in the left sidebar)
2. Select **"Python: FastAPI App"** from the dropdown
3. Press **F5** again or click the green play button
4. Wait for: `Uvicorn running on http://0.0.0.0:8000`
5. Open browser: **http://localhost:8000**

### **Alternative Method - Terminal:**

In the VS Code terminal, run:

```bash
cd src
python app.py
```

Then open: **http://localhost:8000**

---

## ✅ You're Done!

The web interface should open. Try entering:
- Device Model: `iPhone 12`
- Fill in other fields
- Click **"Predict Recovery"**

---

## 🐛 Troubleshooting

**"Module not found" error?**
- Make sure `(venv)` is shown in terminal
- Run: `pip install -r requirements.txt`

**"Model file not found" error?**
- Run: `python src/train.py`

**Port 8000 already in use?**
- Stop previous server: Press `Ctrl+C` in terminal
- Or change port in `src/app.py` line 118: `port=8001`

**Python not found?**
- Install Python 3.8+ from python.org
- Restart VS Code

---

## 💡 Pro Tips

- **Auto-reload**: Use `uvicorn src.app:app --reload` for automatic restarts
- **Debug**: Press F5 → Select configuration → Set breakpoints
- **Terminal**: Press `` Ctrl+` `` to toggle terminal
- **Multiple terminals**: Click `+` button in terminal panel

---

**That's it! Your project is running! 🎉**

