from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch


## Example usage

if __name__ == "__main__":
    # docs = load_all_documents("data")
    store = FaissVectorStore()
    # store.build_from_documents(docs)
    store.load()
    # print(store.query("what is attention in machine learning?", top_k=5))

    rag_search = RAGSearch()
    while True:
        print("\nType 'exit', 'quit' or 'q' to stop.")
        query = input("Enter your question here: ")
        if query.lower() in ["exit", "quit", "q"]:
            break
        summary = rag_search.search_and_summarize(query=query, top_k=3)
        print("Summary: ", summary)
