FROM python:3.8-alpine
ARG VERSION=1
WORKDIR /app
ADD . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt \
  && echo ${VERSION} > templates/version.html
CMD ["python", "app.py"]
EXPOSE 5000
