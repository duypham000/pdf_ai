import streamlit as st

def main():
    st.set_page_config(page_title="Chat width multiple PDFs", page_icon=":books:")

    st.header("Chat width multiple PDFs :books:")
    st.text_input("Ask a question about pdfs:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your pdf here and click on 'Process'")
        st.button("Process")


if __name__ == "__main__":
    main()

