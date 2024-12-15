# Python NFT Viewer

This project provides a Python-based interface to interact with the Ethereum blockchain and view metadata for NFTs in the **Bored Ape Yacht Club (BAYC)** collection. Built with Streamlit and powered by Infura, it offers a beginner-friendly way to work with blockchain data using Python.

---

## Features
- Fetch and display NFT metadata using the **Token ID**.
- Retrieve NFT images stored on IPFS and display them in the app.
- Built with Python and Streamlit for simplicity and interactivity.
- Ethereum mainnet connection via Infura.

---

## Prerequisites

### Required Tools

1. **Homebrew (macOS/Linux)**  
   Homebrew is a package manager that simplifies the installation of dependencies.  

   **Installation**:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```  

   **Verify installation**:  
   ```bash
   brew --version
   ```

2. **xcode-select (macOS only)**  
   Required for `Watchdog`, which improves Streamlit performance.  

   **Installation**:  
   ```bash
   xcode-select --install
   ```

3. **Python 3.10 or later**  

   **Verify installation**:  
   ```bash
   python3 --version
   ```  

   **Installation**:  
   - macOS/Linux (via Homebrew):  
     ```bash
     brew install python@3.10
     ```  
   - Windows:  
     Download the installer from [python.org](https://www.python.org/).

4. **Git**  
   Used to clone the repository.  

   **Verify installation**:  
   ```bash
   git --version
   ```  

   **Installation**:  
   - macOS/Linux (via Homebrew):  
     ```bash
     brew install git
     ```  
   - Windows:  
     Install [Git for Windows](https://gitforwindows.org/).

5. **A Code Editor (Recommended: VS Code)**  
   Download and install from [Visual Studio Code](https://code.visualstudio.com/).  

   **Optional**: Install the Python extension in VS Code:
   1. Open VS Code and navigate to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`).
   2. Search for "Python" and click **Install**.

6. **Infura API Key**  
   Sign up at [Infura](https://infura.io/) and create a project to get your **Infura Project ID**.

---

## Setup Instructions

### Step 1: Clone the Repository

1. Open a terminal.
2. Navigate to the **Documents** folder (optional but recommended):  
   ```bash
   cd ~/Documents
   ```
3. Create a folder for your projects:  
   ```bash
   mkdir projects
   cd projects
   ```
4. Clone the repository:  
   ```bash
   git clone https://github.com/Cryptolyfe/Python-NFT-Viewer.git
   ```
5. Navigate into the project folder:  
   ```bash
   cd Python-NFT-Viewer
   ```

---

### Step 2: Set Up the Environment

1. Create a virtual environment:  
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:  
   - macOS/Linux:  
     ```bash
     source venv/bin/activate
     ```
   - Windows:  
     ```bash
     venv\Scripts\activate
     ```
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

### Step 3: Configure Environment Variables

1. Create a `.env` file in the project directory:  
   ```bash
   touch .env
   ```
2. Open the `.env` file in a text editor (e.g., VS Code).
3. Add your **Infura Project ID** to the `.env` file:  
   ```env
   INFURA_PROJECT_ID=your_infura_project_id
   ```

---

### Step 4: Run the Application

1. Start the app:  
   ```bash
   venv/bin/python -m streamlit run nft_viewer.py
   ```
2. Open the local URL displayed in your terminal (e.g., `http://localhost:8501`) in a web browser.
3. Enter a **Token ID** (e.g., `1`) in the app and click "Fetch NFT" to display the metadata and image.

4. Stop the application:  
   Press `Ctrl+C` in the terminal.

---

## Troubleshooting

1. **Connection Issues**:  
   - Ensure your **Infura Project ID** is correct in the `.env` file.
   - Verify your internet connection.

2. **Dependency Issues**:  
   - Ensure all dependencies are installed using `pip install -r requirements.txt`.

---

## License

This project is licensed under the **AGPL-3.0 License**.  
For details, see the [LICENSE](./LICENSE) file.
``` 

This Markdown version ensures proper rendering and clarity on GitHub. Let me know if further adjustments are needed!
