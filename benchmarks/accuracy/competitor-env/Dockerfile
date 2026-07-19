FROM node:22.17.0-bookworm-slim@sha256:b04ce4ae4e95b522112c2e5c52f781471a5cbc3b594527bcddedee9bc48c03a0 AS node-runtime

WORKDIR /opt/opencc-js
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --ignore-scripts --no-audit --no-fund

FROM python:3.12.11-slim-bookworm@sha256:519591d6871b7bc437060736b9f7456b8731f1499a57e22e6c285135ae657bf7

ARG ENVIRONMENT_HASH
LABEL org.zhtw.benchmark.environment-sha256="${ENVIRONMENT_HASH}"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY python-artifacts.lock.json install-python-artifacts.py /opt/competitors/
RUN python /opt/competitors/install-python-artifacts.py

COPY --from=node-runtime /usr/local/bin/node /usr/local/bin/node
COPY --from=node-runtime /opt/opencc-js/node_modules /opt/opencc-js/node_modules
COPY adapter.py opencc-js-adapter.mjs /opt/competitors/

USER 65534:65534
ENTRYPOINT ["python", "/opt/competitors/adapter.py"]
