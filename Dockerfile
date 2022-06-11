FROM python 

WORKDIR /Desktop/projects

COPY banana.py .

CMD ['monke', 'banana.py']