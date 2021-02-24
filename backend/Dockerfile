FROM continuumio/miniconda3

ADD environment.yaml /tmp/environment.yaml
RUN conda env create -f /tmp/environment.yaml

RUN echo "source activate ERProject" > ~/.bashrc
ENV PATH /opt/conda/envs/ERProject/bin:$PATH
#RUN conda activate ERProject

RUN mkdir /app
COPY ./ /app
WORKDIR /app

ENTRYPOINT ["./boot.sh"]
