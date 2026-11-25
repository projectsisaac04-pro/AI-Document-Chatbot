import streamlit as st
from pypdf import PdfReader
from io import BytesIO
from langchain_text_splitters import CharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
llm = ChatAnthropic(
    model="claude-sonnet-4-5",
    temperature=0
)
db=Chroma("collection1",model,".")

def create_chunks(extracted_text,chunk_size,overlap):
    content=[]
    
    starting_position=0
    ending_position=starting_position+chunk_size

    char_split = CharacterTextSplitter( separator="",chunk_size=chunk_size)
    # while starting_position<len(extracted_text):
    portion = char_split.split_text(extracted_text)
    # gen_val=generate_embedding(portion)
    db.add_texts(portion)
    # documents = [Document(page_content=chunk) for chunk in portion]
    # db.add_documents(documents)
def generate_answer(query, context):
    # prompt = f"""
    # Answer the question using only the provided context.

    # Context:
    # {context}

    # Question:
    # {query}
    # """

    prompt = f"""
    You are a document question-answering assistant.

    RULES:
    1. Answer only using the supplied document context.
    2. Never use outside knowledge.
    3. Do not invent facts.
    4. Every factual claim must have a citation.
    5. Use citations in this format: [Page X].
    6. If the answer is unavailable in the context,
       say: "The answer is not available in the document."

    DOCUMENT CONTEXT:
    {context}

    QUESTION:
    {query}

    Provide a clear answer with citations.
    """

    response = llm.invoke(prompt)
    return response.content





def get_results(query):
    results = db.similarity_search(query, k=3)

    context = "\n\n".join(
        result.page_content for result in results
    )

    answer = generate_answer(query, context)

    st.subheader("AI Generated Answer")
    st.write(answer)

    
st.title("AI DOCUMENT ASSISTANT")
pdf_data=""
st.write("Ask questions about your PDF documents!")

query=st.chat_input("Ask your Queries")
file=st.file_uploader("File Attach",type=["pdf"])

if file is None:
    st.warning("No File Found")

else:
    st.success("File Uploaded Successfully!")

    st.write("Filename:", file.name)
    st.write("File Size:", file.size)
    st.write("File Type:", file.type)



    pdf_data=BytesIO(file.getvalue())
    reader=PdfReader(pdf_data)
    total_pages=len(reader.pages)
    st.write("Total Pages : ",total_pages)
    extracted_text=""
    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            extracted_text += page_text + "\n"

    st.text_area("Extracted PDF Text", extracted_text, height=300)

    create_chunks(extracted_text,500,50)

    if query:
        get_results(query)