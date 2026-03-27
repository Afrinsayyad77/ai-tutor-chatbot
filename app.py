from utils.loader import load_pdf
from utils.splitter import split_docs
from utils.vectorstore import create_vectorstore
from utils.llm import load_llm
from utils.prompt import get_prompt

print("📚 Loading document...")

docs = load_pdf("data/Machine learning.pdf")

chunks = split_docs(docs)
db = create_vectorstore(chunks)

llm = load_llm()
prompt_template = get_prompt()

print("\n🤖 AI Tutor Chatbot Ready! (type 'exit' to quit)\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    results = db.similarity_search(query, k=3)
    context = " ".join([doc.page_content for doc in results])

    if len(context.strip()) < 100:
        print("Bot: This question is outside the provided material.\n")
        continue

    prompt = prompt_template.format(context=context, question=query)
    response = llm.invoke(prompt)

    print(f"Bot: {response}\n")