import streamlit as st
from web3 import Web3
import json
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Load the ABI from the abi.json file
with open("abi.json", "r") as abi_file:
    contract_abi = json.load(abi_file)

# Get the Infura project ID from the .env file
infura_project_id = os.getenv("INFURA_PROJECT_ID")
if not infura_project_id:
    st.error("Infura Project ID is not set. Please add it to the .env file.")
    st.stop()

# Construct the Infura URL
infura_url = f"https://mainnet.infura.io/v3/{infura_project_id}"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Verify connection
if web3.provider is not None:
    st.sidebar.success("Connected to Ethereum Mainnet")
else:
    st.sidebar.error("Failed to connect to Ethereum")

# Set the NFT contract address
contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"

# Initialize the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Validate ABI by listing available functions
try:
    st.sidebar.write("Contract Functions:", [func.fn_name for func in contract.functions])
except Exception as e:
    st.sidebar.error(f"Error validating ABI: {e}")

# Function to fetch metadata for an NFT
def fetch_metadata(token_id):
    try:
        # Get the token URI from the contract
        token_uri = contract.functions.tokenURI(token_id).call()

        # Replace 'ipfs://' with a public IPFS gateway URL
        if token_uri.startswith("ipfs://"):
            token_uri = token_uri.replace("ipfs://", "https://ipfs.io/ipfs/")

        # Fetch the metadata JSON from the token URI
        response = requests.get(token_uri)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch metadata for token {token_id}")
            return None
    except Exception as e:
        st.error(f"Error fetching metadata: {e}")
        return None

# Streamlit UI
st.title("NFT Viewer")
st.subheader("View NFTs from a Smart Contract")

# Input for single token ID
token_id = st.number_input("Enter Token ID", min_value=1, step=1)

if st.button("Fetch NFT"):
    metadata = fetch_metadata(token_id)
    if metadata:
        st.subheader(f"NFT #{token_id}")
        st.write("Metadata:", metadata)  # Display the full metadata for debugging
        image = metadata.get("image", None)
        name = metadata.get("name", "Unknown NFT")
        
        # Convert IPFS image URL to HTTP URL
        if image and image.startswith("ipfs://"):
            image = image.replace("ipfs://", "https://ipfs.io/ipfs/")
        
        if image:
            st.image(image, caption=name)
        else:
            st.error("No valid image URL found in the metadata.")

# Input for range of token IDs
st.subheader("Fetch Multiple NFTs")
start_id = st.number_input("Start Token ID", min_value=1, step=1, key="start")
end_id = st.number_input("End Token ID", min_value=start_id, step=1, key="end")

if st.button("Fetch Collection"):
    for token_id in range(start_id, end_id + 1):
        metadata = fetch_metadata(token_id)
        if metadata:
            st.subheader(f"NFT #{token_id}: {metadata.get('name', 'Unknown NFT')}")
            image = metadata.get("image", None)
            
            # Convert IPFS image URL to HTTP URL
            if image and image.startswith("ipfs://"):
                image = image.replace("ipfs://", "https://ipfs.io/ipfs/")
            
            if image:
                st.image(image, caption=f"Token {token_id}")
            for attribute in metadata.get("attributes", []):
                st.write(f"- {attribute['trait_type']}: {attribute['value']}")
        else:
            st.error(f"Failed to fetch metadata for token {token_id}")
