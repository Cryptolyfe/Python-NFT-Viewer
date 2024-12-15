### Updated **README** for Current Code:

```markdown
# NFT Viewer App

This is a simple Streamlit-based app for viewing NFTs on the Ethereum blockchain. The app connects to the Ethereum mainnet using Infura and fetches metadata for NFTs in a specified collection.

## Features
- Fetch metadata for a single NFT by token ID.
- Fetch metadata for a range of NFTs by specifying start and end token IDs.
- Display NFT images and associated metadata in a simple, user-friendly web interface.

## Prerequisites
1. Python 3.10 or higher.
2. An Infura Project ID.
3. ABI file (`abi.json`) for the NFT smart contract.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a Virtual Environment**:
   ```bash
   /opt/homebrew/bin/python3.10 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

4. **Set Up Your Environment**:
   - Create a `.env` file in the project root and add your Infura Project ID:
     ```env
     INFURA_PROJECT_ID=your_infura_project_id
     ```

5. **Ensure the ABI File is Present**:
   - Place the ABI file for the desired NFT smart contract in the project root as `abi.json`.

6. **Run the App**:
   ```bash
   venv/bin/python -m streamlit run nft_viewer.py
   ```

7. **Access the App**:
   - Open the local URL provided in the terminal, typically `http://localhost:8501`.

## Usage

### **Fetching Metadata for a Single Token**
1. Enter a token ID (e.g., `1`) in the "Enter Token ID" field.
2. Click **Fetch NFT** to view the metadata and associated image for the token.

### **Fetching Metadata for a Range of Tokens**
1. Enter a starting token ID (e.g., `1`) and an ending token ID (e.g., `10`) in the respective fields.
2. Click **Fetch Range** to view metadata and images for all tokens in the range.

## Limitations and Future Improvements
This app is a simplified implementation designed for local use. Future enhancements could include:
1. Allowing dynamic input of contract addresses for multiple NFT collections.
2. Implementing advanced search features with trait and value filters.
3. Optimizing performance with caching or database support.
4. Improving error handling for invalid token IDs or unavailable metadata.

## License
This project is licensed under the AGPL-3.0 License. See the `LICENSE` file for details.

<br>

--------------------------------------------------------------------------------------------------------------------------------------------

Additional Tools for the Development Environment:


### 1. Homebrew (macOS/Linux)
- **Why**: A package manager for macOS/Linux that simplifies the installation of Python, Git, and other dependencies.
- **Installation**:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
- **Verify installation**:
  ```bash
  brew --version
  ```

---

### 2. Git (Version Control)
- **Why**: Used for cloning repositories and managing code changes.
- **Installation**:
  - **macOS (via Homebrew)**:
    ```bash
    brew install git
    ```
  - **Linux**:
    ```bash
    sudo apt install git
    ```
  - **Windows**:
    Download and install [Git for Windows](https://git-scm.com/).
- **Verify installation**:
  ```bash
  git --version
  ```

---

### 3. Python 3.10+
- **Why**: The app requires Python version 3.10 or newer.
- **Installation**:
  - **macOS (via Homebrew)**:
    ```bash
    brew install python@3.10
    ```
  - **Linux**:
    ```bash
    sudo apt install python3.10
    ```
  - **Windows**:
    Download the latest Python 3.10 installer from [python.org](https://www.python.org/downloads/).
- **Verify installation**:
  ```bash
  python3 --version
  ```

---

### 4. Code Editor (VS Code Recommended)
- **Why**: A powerful code editor for writing, debugging, and running your code.
- **Installation**:
  - Download and install from [code.visualstudio.com](https://code.visualstudio.com/).
- **Optional**: Install the Python extension in VS Code:
  1. Open VS Code and navigate to `Extensions` (`Ctrl+Shift+X` or `Cmd+Shift+X`).
  2. Search for `Python` and click `Install`.

---

### 5. IPFS (InterPlanetary File System) Gateway (Optional)
- **Why**: The app uses the `ipfs.io` gateway to fetch NFT metadata. For advanced users, running a local IPFS node can improve performance.
- **Installation**:
  - **macOS/Linux**:
    ```bash
    brew install ipfs
    ```
  - **Windows**:
    Download and install from [ipfs.tech](https://ipfs.tech/).
- **Start your local IPFS daemon**:
  ```bash
  ipfs daemon
  ```

---

### 6. xcode-select (macOS only) (For Watchdog Support in Streamlit)
- **Why**: Streamlit performs better with the Watchdog module for file watching. On macOS, this requires `xcode-select`.
- **Installation**:
  ```bash
  xcode-select --install
  ```

---
```





---

