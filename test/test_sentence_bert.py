from sentence_vector_generator.sentence_bert import SentenceBertJapanese as SentenceBertJapanese
import pytest
import torch

@pytest.fixture
def model():
  model = SentenceBertJapanese("sonoisa/sentence-bert-base-ja-mean-tokens")
  return model

def test_encode_vector_response_length(model):
  response = model.encode(sentences = ['感動してみんなで泣ける映画'])
  assert response.shape == torch.Size([1, 768])

def test_encode_vector_response_type(model):
  response = model.encode(sentences = ['感動してみんなで泣ける映画'])
  assert type(response) == torch.Tensor

def test_encode_vector_response_error(model):
  with pytest.raises(ValueError) as e:
    response = model.encode(sentences = [1])
  assert str(e.value) == "Input is not valid. Should be a string, a list/tuple of strings or a list/tuple of integers."
