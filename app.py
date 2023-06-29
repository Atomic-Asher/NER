import spacy
from annotated_text import annotated_text
import streamlit as st

def main():
    # Load the trained model
    trained_model = spacy.load("ner_pretrained_model")

    st.title("Named Entity Recognition")
    st.write("Enter your text below:")

    #User input
    if st.button("Analyze"):
        doc = trained_model(example_text)

        # Process the text and display the labeled entities
        labeled_text = process_entities(doc, example_text)

        # Display the modified text with labeled entities
        st.markdown("Labeled Text:")
        st.write(labeled_text)
def process_entities(doc, example_text):
    labeled_text = example_text

    for ent in doc.ents:
        labeled_entity = ent.text + " [" + ent.label_ + "]"
        labeled_text = labeled_text.replace(ent.text, labeled_entity)

    return labeled_text

if __name__ == "__main__":
    main()