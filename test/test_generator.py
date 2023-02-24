from sentence_vector_generator import generator as generator
import json
import pytest

def test_generate_vector_response_status():
  response = generator.generate_vector("感動してみんなで泣ける映画")
  assert len(json.loads(response)) == 768

def test_generate_vector_response_type():
  response = generator.generate_vector("感動してみんなで泣ける映画")
  assert type(json.loads(response)[0]) == float

def test_generate_vector_response_error():
  with pytest.raises(ValueError) as e:
    response = generator.generate_vector(1)
  assert str(e.value) == "Input is not valid. Should be a string, a list/tuple of strings or a list/tuple of integers."
