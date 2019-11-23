FROM python:3

ADD setup.py /
ADD index.py /

ENTRYPOINT [ "python", "./index.py" ]
