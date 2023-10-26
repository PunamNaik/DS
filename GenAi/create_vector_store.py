import os
import sys
sys.path.append("C:/Users/punam.anil.naik/PycharmProjects/ice_breaker")
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
import config
import pandas as pd
import templates

llm = AzureChatOpenAI(deployment_name=config.deployment_name,
                      model_name=config.model_name,
                      openai_api_base=config.openai_api_base,
                      openai_api_version=config.openai_api_version,
                      openai_api_key=config.openai_api_key)
                        # temperature=0.5)

#process_map = "process_map.csv"
upstream = "EBPM_A_23_Upstream_PH_KIPs_Aug.csv"
#ticket_dump = pd.read_csv("ticket_dump.csv")

#sentence-transformers/multi-qa-mpnet-base-dot-v1
#sentence-transformers/all-MiniLM-l6-v2
#sentence-transformers/all-MiniLM-l6-v1
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': False})


loader = CSVLoader(file_path=upstream, encoding="utf-8", csv_args={'delimiter': ','})
data = loader.load()

print(type(data))
print(len(data))
print(data)

'''
# This block is 1 time run to create vector store
doc_list = data
embed_fn=embeddings
faiss_db = FAISS.from_documents(doc_list,embed_fn)

index_store = 'faiss_index'
first_run = True
if first_run:
    faiss_db.save_local(folder_path=index_store)
    print('Run 1')
    print("New store created...")
else:
    if os.path.exists(index_store):
        local_db = FAISS.load_local(index_store, embed_fn)
        # merging the new embedding with the existing index store
        local_db.merge_from(faiss_db)
        print("Merge completed")
        local_db.save_local(index_store)
        print("Updated index saved")
    else:
        faiss_db.save_local(folder_path=index_store)
        print("New store created...")


text = "This is a test document."
query_result = embeddings.embed_query(text)
print(query_result)
'''


vectorStore = FAISS.load_local('faiss_index',embeddings)
print("Vector Model Loaded")

question = templates.query2
searchDocs = vectorStore.similarity_search(question)
print(searchDocs[0].page_content)

retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
docs = retriever.get_relevant_documents(templates.query2)
print(docs[0].page_content)

