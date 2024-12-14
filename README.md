Your README is almost perfect! Here’s an **adjusted and polished version** with formatting fixes and consistent Markdown syntax. The main adjustments include:

1. **Code Block Fixes**:
   - Ensured proper syntax for all `bash`, `makefile`, and other code blocks.
   - Removed `Copy code` placeholders.
2. **Consistent Headings and Lists**:
   - Ensured consistent Markdown structure for sections, lists, and subheadings.

---

### **Polished README**

```markdown
# NFT Viewer App

This is a simple Streamlit-based app for viewing NFTs on the Ethereum blockchain. The app connects to the Ethereum mainnet using Infura and fetches metadata for NFTs in the **Bored Ape Yacht Club (BAYC)** collection.

## Features
- Fetch metadata for a single NFT by token ID.
- Fetch metadata for a range of NFTs by specifying start and end token IDs.
- Display NFT images and associated metadata in an easy-to-use web interface.

## Prerequisites
1. Python 3.8 or higher.
2. An Infura Project ID.
3. ABI file (`abi.json`) for the BAYC contract.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your Environment**:
   - Create a `.env` file in the project root and add your Infura Project ID:
     ```makefile
     INFURA_PROJECT_ID=your_infura_project_id
     ```

4. **Ensure the ABI File is Present**:
   - Place the ABI file for the BAYC contract in the project root as `abi.json`.

5. **Run the App**:
   ```bash
   streamlit run app.py
   ```

## Usage

### **Fetching Metadata for a Single Token**
1. Open the app in your browser.
2. Input a token ID (e.g., `1`) in the "Enter Token ID" field and click "Fetch NFT."
3. View the metadata and associated image for the token.

### **Fetching Metadata for a Range of Tokens**
1. Input a starting token ID (e.g., `1`) and an ending token ID (e.g., `10`) in the range fields.
2. Click "Fetch Range" to view metadata and images for all tokens in the range.

## Limitations and Future Improvements
This app is a simplified implementation for educational purposes. Future enhancements could include:
1. Allowing users to input any contract address to interact with different NFT collections.
2. Adding dynamic ABI fetching using the Etherscan API.
3. Improving search functionality with filters for traits and values.
4. Enhancing performance with caching and better error handling.

## License
This project is licensed under the AGPL-3.0 License.

As per the AGPL-3.0 License:
- You are free to use, modify, and distribute this software, provided that any modified or derivative works are also licensed under AGPL-3.0.
- Users interacting with this software over a network have the right to access the source code.

See the [LICENSE](./LICENSE) file for details.
```