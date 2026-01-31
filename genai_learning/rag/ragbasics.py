from langchain_community.document_loaders import PyPDFLoader

path = "budget_speech.pdf"

loader = PyPDFLoader(path)


doc = loader.load()


print(doc)