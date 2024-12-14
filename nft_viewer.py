import streamlit as st
from web3 import Web3
import json
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Load the ABI from a local file
with open("abi.json", "r") as abi_file:
    contract_abi = json.load(abi_file)

# Get Infura Project ID from .env
infura_project_id = os.getenv("INFURA_PROJECT_ID")
if not infura_project_id:
    st.error("Infura Project ID is missing in the .env file")
    st.stop()

# Connect to Ethereum
infura_url = f"https://mainnet.infura.io/v3/{infura_project_id}"
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.isConnected():
    st.sidebar.success("Connected to Ethereum Mainnet")
else:
    st.sidebar.error("Failed to connect to Ethereum")

# Hardcoded BAYC contract address
contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Fetch metadata for an NFT
def fetch_metadata(token_id):
    try:
        token_uri = contract.functions.tokenURI(token_id).call()
        token_uri = token_uri.replace("ipfs://", "https://ipfs.io/ipfs/")
        response = requests.get(token_uri)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        st.error(f"Error fetching metadata: {e}")
        return None

# Streamlit UI
st.title("NFT Viewer")
token_id = st.number_input("Enter Token ID", min_value=1, step=1)

if st.button("Fetch NFT"):
    metadata = fetch_metadata(token_id)
    if metadata:
        st.json(metadata)
        image = metadata.get("image", "").replace("ipfs://", "https://ipfs.io/ipfs/")
        if image:
            st.image(image, caption=f"NFT #{token_id}")
