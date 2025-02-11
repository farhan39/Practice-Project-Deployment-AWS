FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN practice_project_deployment_aws create-db
RUN practice_project_deployment_aws populate-db
RUN practice_project_deployment_aws add-user -u admin -p admin
EXPOSE 5000
CMD ["practice_project_deployment_aws", "run"]
