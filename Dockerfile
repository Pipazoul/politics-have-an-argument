FROM ubuntu

ENV LANG en_US.UTF-8
CMD ["/bin/bash"]


RUN apt update 
RUN apt upgrade -y
RUN apt install -y git 
RUN apt install -y python
RUN apt install -y ezstream
RUN apt install -y wget
RUN apt install -y zip
RUN apt install -y nano
RUN apt install -y iputils-ping
RUN apt install -y net-tools
RUN apt install -y curl
RUN apt install -y espeak
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN pip install python-twitter
RUN pip install gtts
RUN pip install pathlib

RUN git clone https://github.com/Pipazoul/politics-have-an-argument.git
WORKDIR /politics-have-an-argument
RUN ls
RUN git checkout ezstream
ADD . /politics-have-an-argument
RUN echo "export PYTHONIOENCODING=utf-8" >> /root/.bashrc
EXPOSE 8050