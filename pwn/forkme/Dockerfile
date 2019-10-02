FROM ubuntu:18.04

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN	apt-get install socat -y

RUN useradd -m vuln
COPY vuln flag.txt /home/vuln/
RUN chown -R root:vuln /home/vuln/
RUN chmod -R 750 /home/vuln/
EXPOSE 4444
USER vuln
CMD /home/vuln/vuln