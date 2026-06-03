# CI/CD 整合指南

將 zhtw 整合到你的 CI/CD 流程，確保每次提交都符合台灣繁體中文用語規範。

## GitHub Actions

### 基本設定

建立 `.github/workflows/chinese-check.yml`：

```yaml
name: Chinese Check

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  zhtw-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Install zhtw
        run: pip install zhtw

      - name: Check Traditional Chinese
        run: zhtw check . --json
```

### 進階設定：只檢查變更的檔案

```yaml
name: Chinese Check (Changed Files Only)

on:
  pull_request:
    branches: [main]

jobs:
  zhtw-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # 需要完整歷史來比較

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install zhtw
        run: pip install zhtw

      - name: Get changed files
        id: changed
        run: |
          FILES=$(git diff --name-only origin/${{ github.base_ref }}...HEAD | grep -E '\.(py|md|txt|yaml|yml|json)$' || true)
          echo "files=$FILES" >> $GITHUB_OUTPUT

      - name: Check changed files
        if: steps.changed.outputs.files != ''
        run: |
          echo "${{ steps.changed.outputs.files }}" | xargs zhtw check
```

### 進階設定：PR 評論

```yaml
- name: Check and Comment
  run: |
    OUTPUT=$(zhtw check . --json 2>&1) || true
    if echo "$OUTPUT" | grep -q '"total_issues":'; then
      ISSUES=$(echo "$OUTPUT" | jq -r '.total_issues')
      if [ "$ISSUES" -gt 0 ]; then
        echo "::warning::發現 $ISSUES 處需要修正的中文用語"
      fi
    fi
```

---

## GitLab CI

### 基本設定

在 `.gitlab-ci.yml` 加入：

```yaml
stages:
  - lint

chinese-check:
  stage: lint
  image: python:3.12-slim
  before_script:
    - pip install zhtw
  script:
    - zhtw check . --json
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == "main"
```

### 快取加速

```yaml
chinese-check:
  stage: lint
  image: python:3.12-slim
  cache:
    key: zhtw-pip
    paths:
      - .cache/pip
  variables:
    PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  before_script:
    - pip install zhtw
  script:
    - zhtw check . --json
```

---

## Jenkins

### Pipeline 設定

```groovy
pipeline {
    agent any
    stages {
        stage('Chinese Check') {
            steps {
                sh '''
                    python3 -m pip install zhtw
                    zhtw check . --json
                '''
            }
        }
    }
}
```

### 搭配 Docker

```groovy
pipeline {
    agent {
        docker { image 'python:3.12-slim' }
    }
    stages {
        stage('Chinese Check') {
            steps {
                sh 'pip install zhtw && zhtw check . --json'
            }
        }
    }
}
```

---

## Azure DevOps

```yaml
# azure-pipelines.yml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.12'

  - script: |
      pip install zhtw
      zhtw check . --json
    displayName: 'Check Traditional Chinese'
```

---

## CircleCI

```yaml
# .circleci/config.yml
version: 2.1

jobs:
  chinese-check:
    docker:
      - image: cimg/python:3.12
    steps:
      - checkout
      - run:
          name: Install zhtw
          command: pip install zhtw
      - run:
          name: Check Traditional Chinese
          command: zhtw check . --json

workflows:
  version: 2
  check:
    jobs:
      - chinese-check
```

---

## 排除特定檔案

### 方法 1：使用 .zhtwignore

在專案根目錄建立 `.zhtwignore`：

```gitignore
# 測試資料
tests/fixtures/
tests/data/

# 第三方程式碼
vendor/
node_modules/

# 產生的檔案
dist/
build/
*.min.js
```

### 方法 2：命令列排除

```bash
zhtw check . --exclude node_modules,dist,vendor
```

### 方法 3：CI 設定檔中排除

```yaml
- name: Check Traditional Chinese
  run: zhtw check . --exclude tests/fixtures,docs/examples
```

---

## 常見問題

### Q: CI 執行太慢？

A: zhtw 使用 Aho-Corasick 演算法，10 萬行程式碼 < 1 秒。如果覺得慢，可能是：
- 掃描了 node_modules 等大型目錄 → 使用 .zhtwignore 排除
- 網路延遲下載套件 → 使用 pip cache

### Q: 如何只在特定分支執行？

```yaml
on:
  push:
    branches: [main, release/*]
```

### Q: 如何讓檢查失敗但不阻擋合併？

```yaml
- name: Check Traditional Chinese
  run: zhtw check . --json || true
  continue-on-error: true
```

### Q: 如何在 monorepo 只檢查特定套件？

```yaml
- name: Check Package A
  run: zhtw check ./packages/package-a
```

---

## 最佳實踐

1. **先跑 check，再考慮 fix** - 避免自動修改產生非預期結果
2. **搭配 pre-commit** - 在本機就擋住問題，減少 CI 失敗
3. **使用 .zhtwignore** - 排除測試資料和第三方程式碼
4. **加入 cache** - 加速 CI 執行時間
5. **只檢查有中文的檔案類型** - 避免掃描二進位檔案

---

更多資訊請參考 [README](../README.md) 或 [開 Issue](https://github.com/rajatim/zhtw/issues)。
