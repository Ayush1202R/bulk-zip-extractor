import streamlit as st
import zipfile
import os
import shutil
import uuid

st.title("📂 Bulk ZIP Extractor (Online Version)")
st.write("Upload multiple ZIP files and extract them automatically.")

uploaded_files = st.file_uploader("Upload ZIP files", type="zip", accept_multiple_files=True)

if st.button("Extract ZIP Files"):
    if not uploaded_files:
        st.error("❌ Please upload at least one ZIP file.")
    else:
        # Create temp extraction folder
        session_id = str(uuid.uuid4())
        extract_folder = f"extracted_{session_id}"
        os.makedirs(extract_folder, exist_ok=True)

        progress_bar = st.progress(0)
        total_files = len(uploaded_files)

        for idx, uploaded_file in enumerate(uploaded_files):
            file_name = uploaded_file.name
            zip_path = os.path.join(extract_folder, file_name)

            # Save ZIP file temporarily
            with open(zip_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Extract
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    target_folder = os.path.join(extract_folder, file_name.replace(".zip", ""))
                    os.makedirs(target_folder, exist_ok=True)
                    zip_ref.extractall(target_folder)
                os.remove(zip_path)
            except:
                st.error(f"❌ Failed to extract: {file_name}")

            progress_bar.progress((idx + 1) / total_files)

        # Create ZIP of extracted folder for download
        download_zip = f"extracted_result_{session_id}.zip"
        shutil.make_archive(download_zip.replace(".zip", ""), 'zip', extract_folder)

        with open(download_zip, "rb") as f:
            st.download_button(
                label="📥 Download Extracted Files",
                data=f,
                file_name=download_zip,
                mime="application/zip"
            )

        # Cleanup local folders (optional)
        shutil.rmtree(extract_folder)

        st.success("✅ Extraction complete!")
        st.balloons()

st.markdown("---")
st.caption("Created by: Ayush Radharaman Pandey")
