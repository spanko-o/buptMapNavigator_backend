FROM python:3.11
ENV PYTHONUNBUFFERED 1

# Setup MySQL client
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources

# 清理apt缓存以减小镜像大小
RUN rm -rf /var/lib/apt/lists/*


# Deploy application
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /app/
