docker run --rm -v ~/sentence-vector-generator:/sentence-vector-generator -w /sentence-vector-generator -p 8000:8000 --name sentence-vector-generator -it sentence-vector-generator uvicorn main:app --reload --host 0.0.0.0 --port 8000
