# 🇰🇷 spaCy Korean Language Model Training

A comprehensive repository for training and experimenting with Korean language models using spaCy. This project explores multiple approaches to Korean NLP, including custom NER (Named Entity Recognition) training, tokenization strategies, and pre-trained model integration.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Training Iterations](#training-iterations)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Entity Types](#entity-types)
- [Contributing](#contributing)

## 🎯 Overview

This repository documents multiple experiments in training Korean language models with spaCy. The project focuses on:

- **Named Entity Recognition (NER)** for Korean business documents
- **Custom tokenization** using various Korean morphological analyzers
- **Pre-trained model integration** and fine-tuning
- **Automated labeling** and dataset preparation workflows

### Key Features

- Multiple training approaches documented across 4 iterations
- Integration with Korean tokenizers (KiwiPiePy, MeCab)
- Custom entity types for business/project domain
- Automated entity detection for stock tickers
- Dataset preparation scripts and utilities

## 📁 Project Structure

```
spacy-model-korean/
├── .devcontainer/          # Development container configuration
├── dlp/                    # Data loss prevention related files
├── kiwipiepy/             # KiwiPiePy tokenizer integration
│   ├── kiwi-spacy.ipynb
│   ├── regex-kiwispacy.ipynb
│   └── spacy.ipynb
├── pre-trained/           # Pre-trained model experiments
│   ├── dlpt.ipynb
│   └── spacy.ipynb
├── train-i/               # First training iteration
│   ├── base_config.cfg
│   ├── config.cfg
│   ├── sample.json
│   ├── spacy.ipynb
│   └── output/
├── train-ii/              # Second training iteration (automated labeling)
│   ├── auto_label.py
│   ├── build_docbin.py
│   ├── load_raw_data.py
│   ├── stock_dict.py
│   ├── base_config.cfg
│   ├── config.cfg
│   ├── spacy2.ipynb
│   ├── dataset/
│   └── output/
├── train-iii/             # Third training iteration (MeCab integration)
│   ├── base_config.cfg
│   ├── config.cfg
│   ├── dataset.ipynb
│   ├── mecab.ipynb
│   ├── mecab2.ipynb
│   ├── trainmecab.ipynb
│   └── data/
├── train-iv/              # Fourth training iteration (advanced NER)
│   ├── dlp_train_data.py
│   ├── ners.ipynb
│   └── ners.html
└── README.md
```

## 🔄 Training Iterations

### Train-I: Basic Training Setup
**Approach:** Initial spaCy model training with basic configuration
- Basic `config.cfg` setup for Korean language
- Sample JSON data format
- Simple training pipeline

**Files:**
- `base_config.cfg` / `config.cfg` - spaCy training configuration
- `sample.json` - Example training data
- `spacy.ipynb` - Training notebook

### Train-II: Automated Labeling
**Approach:** Automated entity detection with custom scripts
- Automated stock ticker detection using regex
- DocBin format for efficient training data storage
- Custom entity labeling pipeline

**Key Components:**
- `auto_label.py` - Automatic entity labeling for stock tickers
- `build_docbin.py` - Convert labeled data to spaCy DocBin format
- `stock_dict.py` - Stock ticker dictionary
- `load_raw_data.py` - Raw data loading utilities

**Usage:**
```python
from auto_label import find_entities

text = "삼성전자 주가가 상승했습니다."
entities = find_entities(text)
# Returns: [(0, 4, "TICKER")]
```

### Train-III: MeCab Integration
**Approach:** Korean morphological analysis with MeCab tokenizer
- MeCab-ko integration for improved Korean tokenization
- Custom dictionary building
- Morpheme-level analysis

**Files:**
- `mecab.ipynb` / `mecab2.ipynb` - MeCab setup and experiments
- `trainmecab.ipynb` - Training with MeCab tokenizer
- `dataset.ipynb` - Dataset preparation

### Train-IV: Advanced NER Training
**Approach:** Comprehensive NER training for business documents
- Rich entity types for project management domain
- DLP (Data Loss Prevention) focused training data
- Advanced entity recognition patterns

**Entity Examples:**
- `PROJECT_NAME`: 알파, 베타, 감마, 델타, etc.
- `PROJECT_MANAGER`: 김민수, 정하늘, 윤도현, etc.
- `PROJECT_DATE`: 2025년 3월 1일부터 2026년 12월 31일까지
- `PROJECT_BUDGET`: 15억 원, 22억 원, etc.
- `ORG_INTERNAL`: 마케팅팀, 재무팀, R&D혁신팀, etc.
- `PROJECT_TERM`: 코드명 레드존, 내부등급A, etc.

**Files:**
- `dlp_train_data.py` - Comprehensive training data with 66+ examples
- `ners.ipynb` - NER training notebook
- `ners.html` - Visualization of NER results

## 🔧 Prerequisites

- Python 3.8+
- spaCy 3.x
- Korean language processing libraries (depending on iteration):
  - `kiwipiepy` (for KiwiPiePy integration)
  - `mecab-python3` (for MeCab integration)

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/rusestudio/spacy-model-korean.git
cd spacy-model-korean
```

2. **Install spaCy:**
```bash
pip install spacy
```

3. **Install Korean tokenizers (choose based on your training iteration):**

For KiwiPiePy:
```bash
pip install kiwipiepy
```

For MeCab:
```bash
pip install mecab-python3
```

4. **Install additional dependencies:**
```bash
pip install jupyter pandas numpy
```

## 🚀 Usage

### Quick Start - Training a Model

#### Option 1: Using Pre-configured Training (Train-II)

```bash
cd train-ii

# 1. Prepare your raw data
python load_raw_data.py

# 2. Auto-label entities
python auto_label.py

# 3. Build DocBin format
python build_docbin.py

# 4. Train the model
python -m spacy train config.cfg --output ./output --paths.train ./dataset/train.spacy --paths.dev ./dataset/dev.spacy
```

#### Option 2: Using Jupyter Notebooks

Each training iteration includes Jupyter notebooks for interactive experimentation:

```bash
# Navigate to your chosen training iteration
cd train-i  # or train-ii, train-iii, train-iv

# Start Jupyter
jupyter notebook

# Open the respective .ipynb file
```

### Using the Trained Model

```python
import spacy

# Load your trained model
nlp = spacy.load("./train-ii/output/model-best")

# Process text
text = "프로젝트 알파는 총 예산 15억 원으로 김민수 PM이 담당한다."
doc = nlp(text)

# Extract entities
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")

# Output:
# 알파 - PROJECT_NAME
# 15억 원 - PROJECT_BUDGET
# 김민수 - PROJECT_MANAGER
```

### Generating Base Config

If you want to create a new configuration:

```bash
python -m spacy init config config.cfg --lang ko --pipeline ner
```

## 🏷️ Entity Types

The models support the following entity types (primarily in Train-IV):

| Entity Type | Description | Example |
|------------|-------------|---------|
| `PROJECT_NAME` | Project names and codenames | 알파, 베타, 클라우드 전환 |
| `PROJECT_MANAGER` | Project manager names | 김민수, 정하늘, 윤도현 |
| `PROJECT_DATE` | Project timeline dates | 2025년 3월 1일부터 2026년 12월 31일까지 |
| `PROJECT_BUDGET` | Project budget amounts | 15억 원, 22억 원 |
| `ORG_INTERNAL` | Internal organization names | 마케팅팀, 재무팀, R&D혁신팀 |
| `PROJECT_TERM` | Project-specific terminology | 코드명 레드존, 내부등급A |
| `TICKER` | Stock ticker symbols | 삼성전자, SK하이닉스 |

## 🛠️ Development

### Using DevContainer

This project includes a `.devcontainer` configuration for consistent development environment:

1. Open the project in VS Code
2. Install the "Remote - Containers" extension
3. Click "Reopen in Container" when prompted

### Training Data Format

Training data follows spaCy's JSON format:

```json
{
  "text": "프로젝트 알파는 총 예산 15억 원으로 김민수 PM이 담당한다.",
  "entities": [
    [5, 8, "PROJECT_NAME"],
    [17, 22, "PROJECT_BUDGET"],
    [25, 28, "PROJECT_MANAGER"]
  ]
}
```

## 📊 Model Performance

Each training iteration's output includes:
- Training/validation metrics
- Loss curves
- Best model checkpoint
- Evaluation reports

Check the `output/` directory in each training folder for detailed results.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional entity types for different domains
- More training data for improved accuracy
- Integration with other Korean tokenizers
- Performance optimization
- Documentation improvements

## 📝 Notes

- **Train-iii output** is excluded via `.gitignore` due to size
- Large dictionary files (`.dic`, `matrix.def`) are not tracked
- MeCab build files are ignored to reduce repository size
- Each training iteration is self-contained and can be used independently

## 📄 License

This project is open source. Please check individual dependencies for their licenses.

## 🔗 Useful Links

- [spaCy Documentation](https://spacy.io/)
- [KiwiPiePy GitHub](https://github.com/bab2min/kiwipiepy)
- [MeCab-ko](https://bitbucket.org/eunjeon/mecab-ko)
- [spaCy Korean Models](https://spacy.io/models/ko)

---

**Repository:** [https://github.com/rusestudio/spacy-model-korean](https://github.com/rusestudio/spacy-model-korean)
