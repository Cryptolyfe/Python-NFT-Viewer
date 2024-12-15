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
   Installation:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Verify installation:

bash
Copy code
brew --version
xcode-select (macOS only)
Required for Watchdog, which improves Streamlit performance.
Installation:

bash
Copy code
xcode-select --install
Python 3.10 or later
Verify installation:

bash
Copy code
python3 --version
Installation:

macOS/Linux (via Homebrew):
bash
Copy code
brew install python@3.10
Windows:
Download the installer from python.org.
Git
Used to clone the repository.
Verify installation:

bash
Copy code
git --version
Installation:

macOS/Linux (via Homebrew):
bash
Copy code
brew install git
Windows:
Install Git for Windows.
A Code Editor (Recommended: VS Code)
Download and install from Visual Studio Code.
Optional: Install the Python extension in VS Code.

Infura API Key
Sign up at Infura and create a project to get your Infura Project ID.

Setup Instructions
Step 1: Clone the Repository
Open a terminal.
Navigate to the Documents folder (optional but recommended):
bash
Copy code
cd ~/Documents
Create a folder for your projects:
bash
Copy code
mkdir projects
cd projects
Clone the repository:
bash
Copy code
git clone https://github.com/Cryptolyfe/Python-NFT-Viewer.git
Navigate into the project folder:
bash
Copy code
cd Python-NFT-Viewer
Step 2: Set Up the Environment
Create a virtual environment:
bash
Copy code
python3 -m venv venv
Activate the virtual environment:
macOS/Linux:
bash
Copy code
source venv/bin/activate
Windows:
bash
Copy code
venv\Scripts\activate
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Step 3: Configure Environment Variables
Create a .env file in the project directory:
bash
Copy code
touch .env
Open the .env file in a text editor (e.g., VS Code).
Add your Infura Project ID to the .env file:
env
Copy code
INFURA_PROJECT_ID=your_infura_project_id
Step 4: Run the Application
Start the app:

bash
Copy code
streamlit run nft_viewer.py
Open the local URL displayed in your terminal (e.g., http://localhost:8501) in a web browser.

Enter a Token ID (e.g., 1) in the app and click "Fetch NFT" to display the metadata and image.

Stop the application:
Press Ctrl+C in the terminal.

Troubleshooting
Connection Issues:

Ensure your Infura Project ID is correct in the .env file.
Verify your internet connection.
Dependency Issues:

Ensure all dependencies are installed using pip install -r requirements.txt.
License
This project is licensed under the AGPL-3.0 License.
For details, see the LICENSE file.
