
# **NFT Viewer**

A sleek and interactive web application to explore and view metadata for NFTs on the Ethereum blockchain. Built with Python, Streamlit, and Web3.py, this app provides a seamless way to fetch and display NFT details directly from the blockchain using a smart contract's ABI.

---

## **Features**

- **NFT Metadata Viewer**: Fetches metadata for individual or multiple NFTs from a smart contract.
- **IPFS Integration**: Automatically converts IPFS links to public gateway URLs for seamless access.
- **Smart Contract Support**: Connects to any Ethereum-based NFT contract using its address and ABI.
- **User-Friendly Interface**: Intuitive and easy-to-use UI built with Streamlit.
- **Secure Environment Variables**: Leverages `.env` files to protect sensitive information like API keys.

---

## **Technologies Used**

- [Streamlit](https://streamlit.io) – For building the web application.
- [Web3.py](https://web3py.readthedocs.io/) – For interacting with the Ethereum blockchain.
- [Python-Dotenv](https://github.com/theskumar/python-dotenv) – For managing environment variables.
- [IPFS](https://ipfs.io/) – To fetch metadata hosted on decentralized storage.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/Cryptolyfe/Python-NFT-Viewer.git
cd Python-NFT-Viewer
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Create a `.env` File**
Create a `.env` file in the root of the project and add your **Infura Project ID**:
```plaintext
INFURA_PROJECT_ID=your-infura-project-id
```

---

## **Usage**

1. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
2. Open the app in your browser. By default, it will run at:
   ```
   http://localhost:8501
   ```

3. Use the interface to:
   - Enter a token ID to fetch metadata for a specific NFT.
   - Specify a range of token IDs to fetch metadata for multiple NFTs.

---

## **Deployment**

### Deploy on Streamlit Community Cloud

1. Push your project to a public or private GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Deploy the app:
   - Select your repository.
   - Specify the main file (`streamlit_app.py` or `nft_viewer.py`).
4. Add your **Infura Project ID** in the app's **Secrets** section.

---

## **Contributing**

We welcome contributions! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- [Ethereum](https://ethereum.org/) for enabling decentralized applications.
- [Bored Ape Yacht Club (BAYC)](https://boredapeyachtclub.com/) as the example NFT collection.
- [Infura](https://infura.io/) for blockchain connectivity.
- [Streamlit Community Cloud](https://share.streamlit.io/) for hosting the app.

---

Let me know if you'd like to customize this further!