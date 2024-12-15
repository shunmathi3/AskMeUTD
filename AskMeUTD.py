from transformers import pipeline

# Loading pre-trained Q&A model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Implements function to ask questions to chatbot
def ask_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# UTD data
context = """
The University of Texas at Dallas (UTD) was founded in 1969. 
Its main campus is located in Richardson, Texas. 
UTD is known for its programs in STEM, business, and arts and technology. 
The official mascot is Temoc. 
The university colors are flame orange, eco green, and white. 
The Eugene McDermott Library is a major resource for students and researchers. 
UTD's Naveen Jindal School of Management is highly ranked for its MBA programs. 
The campus features the Margaret McDermott Trellis Plaza and the Love Jack sculpture. 
The university has a chess team that is internationally recognized.
UTD offers over 140 academic programs across its eight schools.
The Green Center houses the physics department and cutting-edge research facilities.
The UTDallas esports team competes at a national level.
"""


print("Ask questions about UTD! Enter 'exit' if your done with questions.")
while True:
    question = input("You: ")
    if question.lower() == "exit":
        print("Goodbye!")
        break
    answer = ask_question(question, context)
    print(f"AskMeBot: {answer}")
