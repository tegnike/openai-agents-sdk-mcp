<div align="center">

![](assets/header.png)

# 🤖 openai-agents-sdk-mcp minimal

  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/OpenAI-Agents-green.svg" alt="OpenAI Agents">
  <img src="https://img.shields.io/badge/Brave-Search-orange.svg" alt="Brave Search">

</div>

<p align="center">
🌟 OpenAIのAgents SDKを使用して、MCPサーバーを利用したAIエージェントを作成します。 🌟
</p>

## 📚 目次

- [🚀 環境のセットアップ](#環境のセットアップ)
- [⚙️ 環境に応じた設定](#環境に応じた設定)
- [▶️ 実行方法](#実行方法)
- [🔑 環境変数](#環境変数)
- [💫 互換モード](#互換モード)

## 🚀 環境のセットアップ

1. 📥 このリポジトリをクローンします。

2. 🐍 Python仮想環境を作成してアクティベートします。

```bash
# uvをインストール（初回のみ）
sudo snap install astral-uv --classic

# 仮想環境の作成
uv venv

# 仮想環境のアクティベート
source .venv/bin/activate
```

3. 📦 必要なパッケージをインストールします。

```bash
uv pip install -r requirements.txt
```

4. 📄 `.env`ファイルを作成します。

```bash
cp .env.example .env
```

## 🔑 環境変数

以下の環境変数を`.env`ファイルに設定する必要があります：

| 環境変数 | 説明 | 取得方法 |
|----------|------|----------|
| `OPENAI_API_KEY` 🔒 | OpenAI APIのキー | [OpenAIのダッシュボード](https://platform.openai.com/api-keys)から取得 |
| `OPENAI_COMPATIBLE_API_KEY` 🔄 | 互換APIのキー | 互換サービスから取得 |
| `OPENAI_COMPATIBLE_BASE_URL` 🌐 | 互換APIのベースURL | 互換サービスの提供URL |
| `OPENAI_COMPATIBLE_MODEL` 🤖 | 使用する互換モデル名 | 互換サービスの提供モデル |
| `BRAVE_API_KEY` 🔍 | Brave Search APIのキー | [Brave Search API](https://brave.com/search/api/)から取得 |

```bash
# OpenAI API設定
OPENAI_API_KEY=your_openai_api_key
OPENAI_COMPATIBLE_API_KEY=your_compatible_api_key
OPENAI_COMPATIBLE_BASE_URL=https://api.x.ai/v1
OPENAI_COMPATIBLE_MODEL=grok-2-1212

# Brave Search API設定
BRAVE_API_KEY=your_brave_api_key
```

## ⚙️ 環境に応じた設定

`main.py`のnpxコマンドのパスは、使用する環境に応じて変更してください：

```python
"command": "npx"
```

## ▶️ 実行方法

✨ 標準モードでプログラムを実行：

```bash
python main.py
```

✨ 互換モードでプログラムを実行：

```bash
python main_compatible.py
```

## 💫 互換モード

main_compatible.pyでは、OpenAI API互換のサービスを使用してエージェントを実行できます。実行時には以下のデバッグ情報が表示されます：

```
🔧 デバッグ情報 🔧
----------------------------------------
📍 BASE URL: [設定されたベースURL]
🤖 使用モデル: [設定されたモデル名]
🔑 API KEY設定: ✅ or ❌
----------------------------------------
```

## 🛠️ プロジェクト構造

```
.
├── main.py           # 🎯 メインのアプリケーションファイル
├── main_compatible.py # 🔄 互換モード用アプリケーション
├── README.md         # 📝 プロジェクトのドキュメント
├── requirements.txt  # 📦 Pythonの依存関係
├── .env.example     # 🔒 環境変数のテンプレート
└── .gitignore       # 🚫 Gitの除外設定
```
