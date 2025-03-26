# openai-agents-sdk-mcp

OpenAIのAgents SDKを使用して、MCPサーバーを利用したAIエージェントを作成します。

## 使用方法

1. このリポジトリをクローンします。
2. 必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

3. `.env`ファイルを作成します。

```bash
cp .env.example .env
```

4. .envファイルを編集します。

```bash
OPENAI_API_KEY=your_openai_api_key
BRAVE_API_KEY=your_brave_api_key
```

5. プログラムを実行します。

```bash
python main.py
```
