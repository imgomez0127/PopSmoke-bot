    FROM archlinux:latest
    MAINTAINER Ian Gomez <ianm0127@gmail.com>

    #Sets working directory for docker image
    WORKDIR /src

    COPY requirements.txt .

    RUN pacman -Syu --noconfirm ffmpeg python-pip

    RUN pip install -r requirements.txt

    COPY . .

    CMD ["python", "pop_smoke.py"]
