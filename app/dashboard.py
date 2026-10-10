import streamlit as st, time, pandas as pd, json
from monitor import get_stats
from pathlib import Path
st.set_page_config(page_title="Self-Healing System Monitor", layout="wide")

config_file = Path(Path(__file__).parent).parent / "config" / "config.json"

with open(config_file, 'r') as f:
    config = json.load(f)

st.title("🛡️ Self-Healing System Monitor Dashboard")

# Real-time metrics section
st.header("Real-Time System Health")

placeholder = st.empty()

while True:
    # 1. Get stats as a Python dictionary
    stats = get_stats()
    
    # 2. Convert dictionary to a single-row DataFrame
    df = pd.DataFrame([stats])
    
    # 3. Update the UI inside the placeholder
    with placeholder.container():
        st.write("Current System Metrics:")
        
        # Optional: display individual metrics clearly
        col1, col2, col3, col4 = st.columns(4, border=True)
        col1.metric("CPU Usage", f"{stats['cpu']}%")
        col2.metric("Memory Usage", f"{stats['memory']}%")
        col3.metric("Disk Usage", f"{stats['disk']}%")
        col4.metric("Active Tasks", stats['tasks'])

        # Warning Message
        if(stats['cpu'] > config['cpu_warning']):
            st.warning("CPU Overloading")


    # Wait for 4 seconds before the next iteration
    time.sleep(4)
    
    # Rerun the script to refresh the loop in Streamlit
    st.rerun()


