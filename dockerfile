FROM amazonlinux:latest

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN amazon-linux-extras install -y python3.8 && \
    echo 'alias python=python3.8' >> ~/.bashrc && \
    source ~/.bashrc

RUN pip3.8 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

RUN pip3.8 install fastapi==0.92.0 uvicorn==0.20.0 transformers==4.26.1 fugashi==1.2.1 ipadic==1.0.0 pytest==7.2.1 httpx==0.23.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /usr/local/lib/python3.8/site-packages:$PYTHONPATH
ENV PYTHONPATH /usr/local/lib64/python3.8/site-packages:$PYTHONPATH
EXPOSE 8000
RUN mkdir -p /sentence-vector-generator
WORKDIR /
