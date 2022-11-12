FROM public.ecr.aws/lambda/python:3.9.2022.11.11.19-x86_64
RUN pip install poetry
COPY pyproject.toml poetry.lock ./

ARG DEV=""
RUN poetry export --without-hashes ${DEV} --output requirements.txt
RUN pip install -r requirements.txt
COPY . ./

