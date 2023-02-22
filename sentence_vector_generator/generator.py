from sentence_vector_generator.sentence_bert import SentenceBertJapanese
import json

def generate_vector(text):
    model = SentenceBertJapanese("sonoisa/sentence-bert-base-ja-mean-tokens")
    encoded_text = model.encode([text])
    vector_json = json.dumps(encoded_text[0].tolist())
    return vector_json
