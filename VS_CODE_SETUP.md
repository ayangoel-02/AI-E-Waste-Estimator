# 🚀 Running the Project in VS Code

## ✅ Important: Your Code Won't Change!

**Opening files in VS Code will NOT change your code.** VS Code is just a text editor/IDE - it only reads and displays your files. Your code only changes when you:
- Save edits you make
- Run scripts that modify files
- Use Git to commit changes

You can safely open any file in VS Code to view or edit it.

---

## 📋 Step-by-Step Setup in VS Code

### 1. **Open the Project in VS Code**

1. Open VS Code
2. Go to `File` → `Open Folder...`
3. Navigate to and select: `AI Powered E-Waste` folder
4. Click "Open"

### 2. **Set Up Python Environment**

#### Option A: Using Terminal in VS Code (Recommended)

1. Open the integrated terminal in VS Code:
   - Press `` Ctrl+` `` (or `Cmd+` on Mac)
   - Or go to `Terminal` → `New Terminal`

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # On Mac/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Option B: Let VS Code Auto-Detect

- VS Code will prompt you to select a Python interpreter
- Choose the one in `venv/bin/python` (or `venv\Scripts\python.exe` on Windows)

### 3. **Prepare Data and Model** (First Time Only)

In the VS Code terminal, run:

```bash
# Generate training data (if not already generated)
python src/gen_data.py

# Train the model (if not already trained)
python src/train.py
```

### 4. **Run the Application**

#### Method 1: Using VS Code Debugger (Easiest)

1. Go to the **Run and Debug** panel:
   - Click the play icon in the sidebar, OR
   - Press `F5`, OR
   - Go to `Run` → `Start Debugging`

2. Select **"Python: FastAPI App"** from the dropdown

3. Click the green play button (or press `F5`)

4. The server will start and you'll see output in the Debug Console

5. Open your browser to: `http://localhost:8000`

#### Method 2: Using Terminal

1. Open the integrated terminal (`Ctrl+` ` or `Cmd+` `)

2. Make sure virtual environment is activated (you should see `(venv)` in the prompt)

3. Run:
   ```bash
   cd src
   python app.py
   ```

4. Open your browser to: `http://localhost:8000`

#### Method 3: Using uvicorn directly

```bash
uvicorn src.app:app --reload
```

The `--reload` flag automatically restarts the server when you make code changes!

---

## 🎯 Quick Start Checklist

- [ ] Open project folder in VS Code
- [ ] Create virtual environment: `python3 -m venv venv`
- [ ] Activate venv: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Generate data: `python src/gen_data.py` (if needed)
- [ ] Train model: `python src/train.py` (if needed)
- [ ] Run app: Press `F5` and select "Python: FastAPI App"
- [ ] Open browser: `http://localhost:8000`

---

## 🔧 VS Code Features You Can Use

### 1. **Integrated Terminal**
- Press `` Ctrl+` `` to open/close terminal
- Multiple terminals: Click the `+` button
- Split terminal: Click the split icon

### 2. **Python Debugger**
- Set breakpoints by clicking left of line numbers
- Use `F5` to start debugging
- Use `F10` to step over, `F11` to step into
- View variables in the Debug panel

### 3. **IntelliSense & Auto-completion**
- VS Code will suggest code completions as you type
- Hover over functions to see documentation
- Press `Ctrl+Space` to trigger suggestions

### 4. **Git Integration**
- View changes in the Source Control panel
- Commit and push directly from VS Code

### 5. **Extensions (Optional but Recommended)**
Install these from the Extensions marketplace (`Ctrl+Shift+X`):
- **Python** (by Microsoft) - Essential for Python development
- **Pylance** - Advanced Python language support
- **Python Docstring Generator** - Auto-generate docstrings

---

## 🐛 Troubleshooting

### "Module not found" errors
- Make sure virtual environment is activated
- Check that you installed requirements: `pip install -r requirements.txt`
- Verify Python interpreter is set to venv: `Ctrl+Shift+P` → "Python: Select Interpreter"

### Port 8000 already in use
- Stop the previous server (press `Ctrl+C` in terminal)
- Or change port in `app.py`: `uvicorn.run(app, host="0.0.0.0", port=8001)`

### Model file not found
- Run `python src/train.py` to generate the model
- Make sure you're in the project root directory

### Import errors
- The `.vscode/settings.json` file sets up the Python path correctly
- If issues persist, restart VS Code

---

## 📝 Running Other Scripts

### Generate New Data
- Press `F5` → Select "Python: Generate Data"
- Or in terminal: `python src/gen_data.py`

### Retrain Model
- Press `F5` → Select "Python: Train Model"
- Or in terminal: `python src/train.py`

---

## 💡 Pro Tips

1. **Use the integrated terminal** - It's already in the project directory
2. **Enable auto-reload** - Use `uvicorn src.app:app --reload` for automatic restarts
3. **Use breakpoints** - Click left of line numbers to pause execution
4. **Split view** - Open multiple files side-by-side (`Ctrl+\`)
5. **Command Palette** - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) for quick commands

---

## 🎉 You're All Set!

Your project is ready to run in VS Code. The code is safe - VS Code won't modify anything unless you explicitly save changes.

Happy coding! 🚀

