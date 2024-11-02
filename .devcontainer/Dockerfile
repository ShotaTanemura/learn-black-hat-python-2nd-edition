FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
        apt-get list --upgradable && \
        apt-get upgrade -y && \
        apt-get dist-upgrade -y && \
        apt-get autoremove -y && \
        apt-get autoclean -y && \
        apt-get install -y \
            python3 \
            python3-pip \
            python3-venv \
            git


