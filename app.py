import streamlit as st
import os
import zipfile

st.title("📂 Bulk Zip Extractor (Organized)")
st.write("Extract all ZIP files into separate folders automatically.")


# Folder input
folder_path = st.text_input("Enter Folder Path:")

if st.button("Extract ZIP Files"):
    if not os.path.isdir(folder_path):
        st.error("❌ Invalid folder path! Please enter a correct one.")
    else:
        # Get all ZIP files
        zip_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".zip")]

        if not zip_files:
            st.warning("⚠️ No ZIP files found in this folder.")
        else:
            progress_bar = st.progress(0)
            total_files = len(zip_files)

            for idx, file in enumerate(zip_files):
                zip_path = os.path.join(folder_path, file)
                # Create a folder with the name of the ZIP file (without .zip)
                folder_name = os.path.splitext(file)[0]
                extract_folder = os.path.join(folder_path, folder_name)
                os.makedirs(extract_folder, exist_ok=True)

                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_folder)
                    os.remove(zip_path)
                    st.success(f"✅ Extracted: {file} → {folder_name}")
                except zipfile.BadZipFile:
                    st.error(f"❌ Failed to extract: {file} (Bad ZIP file)")

                progress_bar.progress((idx + 1) / total_files)

            st.balloons()
            st.success("All ZIP files extracted into separate folders and original ZIPs removed!")

# Display creator name at the bottom
st.markdown("---")  # optional horizontal line
st.caption("Created by: Ayush Radharaman Pandey")

