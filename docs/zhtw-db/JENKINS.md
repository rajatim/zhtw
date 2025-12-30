# Jenkins CI/CD 需求規格

本文件提供給 Jenkins AI 或 DevOps 團隊建立 CI/CD Pipeline。

---

## Pipeline 概述

```yaml
pipeline_name: zhtw-db-ci
repository: github.com/rajatim/zhtw-db
```

---

## 觸發條件

```yaml
triggers:
  push:
    branches: ["*"]
  pull_request:
    branches: ["main"]
  tag:
    pattern: "v*"
```

---

## 環境變數

```yaml
environment:
  global:
    PYTHON_DEFAULT: "3.11"

  matrix:
    PYTHON_VERSION: ["3.9", "3.10", "3.11", "3.12"]
    POSTGRES_VERSION: ["12", "13", "14", "15", "16"]
    MYSQL_VERSION: ["5.7", "8.0"]
    MONGODB_VERSION: ["5.0", "6.0", "7.0"]
```

---

## 階段定義

### 階段 1: Lint（每次 push）

```yaml
- name: lint
  agent: any
  steps:
    - checkout: scm
    - sh: pip install ruff
    - sh: ruff check src/ tests/
    - sh: ruff format --check src/ tests/
```

### 階段 2: 單元測試（每次 push，多 Python 版本）

```yaml
- name: unit-tests
  parallel: true
  matrix:
    python: ${PYTHON_VERSION}
  agent:
    docker:
      image: python:${python}-slim
  steps:
    - checkout: scm
    - sh: pip install -e ".[dev]"
    - sh: pytest tests/unit/ -v --cov=zhtw_db --cov-report=xml
  artifacts:
    - coverage-${python}.xml
  post:
    always:
      - junit: test-results.xml
      - cobertura: coverage-${python}.xml
```

### 階段 3: 整合測試（PR 和 main）

```yaml
- name: integration-tests
  condition:
    anyOf:
      - branch: main
      - changeRequest: {}
  parallel: true
  matrix:
    include:
      # SQLite（不需容器）
      - name: sqlite
        python: "3.11"
        services: []

      # PostgreSQL（最新穩定版）
      - name: postgres-15
        python: "3.11"
        services:
          - postgres:15
        env:
          DATABASE_URL: postgres://test:test@localhost:5432/test

      # MySQL（最新穩定版）
      - name: mysql-8
        python: "3.11"
        services:
          - mysql:8.0
        env:
          DATABASE_URL: mysql://root:test@localhost:3306/test

      # MongoDB（最新穩定版）
      - name: mongodb-6
        python: "3.11"
        services:
          - mongo:6.0
        env:
          DATABASE_URL: mongodb://localhost:27017/test

  steps:
    - checkout: scm
    - sh: pip install -e ".[dev,${db_type}]"
    - sh: pytest tests/integration/test_${db_type}.py -v
```

### 階段 4: 相容性矩陣（只在 main 和 tag）

```yaml
- name: compatibility-matrix
  condition:
    anyOf:
      - branch: main
      - tag: "v*"
  parallel: true
  max_parallel: 4  # 限制並行數，避免資源耗盡
  matrix:
    postgres: ${POSTGRES_VERSION}
    python: ["3.9", "3.11"]  # 只測最舊和較新
  services:
    - postgres:${postgres}
  steps:
    - sh: pytest tests/integration/test_postgres.py -v
```

### 階段 5: 發布（只在 tag）

```yaml
- name: publish
  condition:
    tag: "v*"
  steps:
    - sh: pip install build twine
    - sh: python -m build
    - withCredentials:
        - usernamePassword:
            id: pypi-credentials
            usernameVariable: TWINE_USERNAME
            passwordVariable: TWINE_PASSWORD
    - sh: twine upload dist/*
```

---

## 服務定義（Docker 容器）

### PostgreSQL

```yaml
postgres:
  image: postgres:${version}
  environment:
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    POSTGRES_DB: test
  ports:
    - "5432:5432"
  healthcheck:
    command: pg_isready -U test
    interval: 5s
    timeout: 5s
    retries: 10
```

### MySQL

```yaml
mysql:
  image: mysql:${version}
  environment:
    MYSQL_ROOT_PASSWORD: test
    MYSQL_DATABASE: test
  ports:
    - "3306:3306"
  command: --default-authentication-plugin=mysql_native_password
  healthcheck:
    command: mysqladmin ping -h localhost
    interval: 5s
    timeout: 5s
    retries: 10
```

### MongoDB

```yaml
mongo:
  image: mongo:${version}
  ports:
    - "27017:27017"
  healthcheck:
    command: mongosh --eval "db.adminCommand('ping')"
    interval: 5s
    timeout: 5s
    retries: 10
```

---

## 通知設定

```yaml
notifications:
  failure:
    email:
      recipients: ["team@example.com"]
    slack:
      channel: "#zhtw-alerts"

  success:
    slack:
      channel: "#zhtw-releases"
      condition:
        tag: "v*"
```

---

## 超時設定

```yaml
timeout:
  global: 30  # 分鐘
  stages:
    lint: 5
    unit-tests: 10
    integration-tests: 15
    compatibility-matrix: 45
    publish: 10
```

---

## 工作區清理

```yaml
cleanup:
  always: true
```

---

## Jenkinsfile 範例

```groovy
pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
    }

    stages {
        stage('Lint') {
            steps {
                sh 'pip install ruff'
                sh 'ruff check src/ tests/'
            }
        }

        stage('Unit Tests') {
            matrix {
                axes {
                    axis {
                        name 'PYTHON'
                        values '3.9', '3.10', '3.11', '3.12'
                    }
                }
                stages {
                    stage('Test') {
                        agent {
                            docker {
                                image "python:${PYTHON}-slim"
                            }
                        }
                        steps {
                            sh 'pip install -e ".[dev]"'
                            sh 'pytest tests/unit/ -v --cov=zhtw_db'
                        }
                    }
                }
            }
        }

        stage('Integration Tests') {
            when {
                anyOf {
                    branch 'main'
                    changeRequest()
                }
            }
            parallel {
                stage('SQLite') {
                    steps {
                        sh 'pytest tests/integration/test_sqlite.py -v'
                    }
                }
                stage('PostgreSQL') {
                    agent {
                        docker {
                            image 'python:3.11-slim'
                        }
                    }
                    services {
                        postgres {
                            image 'postgres:15'
                            env {
                                POSTGRES_PASSWORD = 'test'
                            }
                        }
                    }
                    steps {
                        sh 'pip install -e ".[dev,postgres]"'
                        sh 'DATABASE_URL=postgres://test:test@postgres:5432/test pytest tests/integration/test_postgres.py -v'
                    }
                }
                stage('MySQL') {
                    agent {
                        docker {
                            image 'python:3.11-slim'
                        }
                    }
                    services {
                        mysql {
                            image 'mysql:8.0'
                            env {
                                MYSQL_ROOT_PASSWORD = 'test'
                            }
                        }
                    }
                    steps {
                        sh 'pip install -e ".[dev,mysql]"'
                        sh 'DATABASE_URL=mysql://root:test@mysql:3306/test pytest tests/integration/test_mysql.py -v'
                    }
                }
            }
        }

        stage('Publish') {
            when {
                tag pattern: "v*", comparator: "GLOB"
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'pypi', usernameVariable: 'TWINE_USERNAME', passwordVariable: 'TWINE_PASSWORD')]) {
                    sh 'pip install build twine'
                    sh 'python -m build'
                    sh 'twine upload dist/*'
                }
            }
        }
    }

    post {
        failure {
            slackSend channel: '#zhtw-alerts', message: "Build failed: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
        }
    }
}
```

---

## docker-compose.test.yml（本地測試）

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: test
      POSTGRES_PASSWORD: test
      POSTGRES_DB: test
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U test"]
      interval: 5s
      timeout: 5s
      retries: 5
    volumes:
      - postgres_data:/var/lib/postgresql/data

  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: test
      MYSQL_DATABASE: test
    ports:
      - "3306:3306"
    command: --default-authentication-plugin=mysql_native_password
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 5s
      timeout: 5s
      retries: 5
    volumes:
      - mysql_data:/var/lib/mysql

  mongodb:
    image: mongo:6.0
    ports:
      - "27017:27017"
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 5s
      timeout: 5s
      retries: 5
    volumes:
      - mongo_data:/data/db

volumes:
  postgres_data:
  mysql_data:
  mongo_data:
```

### 本地測試流程

```bash
# 啟動所有資料庫
docker-compose -f docker-compose.test.yml up -d

# 等待就緒
docker-compose -f docker-compose.test.yml ps

# 執行整合測試
pytest tests/integration/ -v

# 執行特定資料庫測試
DATABASE_URL=postgres://test:test@localhost:5432/test \
  pytest tests/integration/test_postgres.py -v

# 清理
docker-compose -f docker-compose.test.yml down -v
```

---

*Jenkins 需求規格 v1.0 - 2025-12-31*
