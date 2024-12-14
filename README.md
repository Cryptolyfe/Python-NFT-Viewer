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




---

