# AI目標提案機能のセットアップ

## 概要
このアプリケーションは、Google Gemini APIを使用してユーザーの情報を分析し、個別化された目標提案を生成します。

## セットアップ手順

### 1. Google Gemini API キーの取得

1. [Google AI Studio](https://aistudio.google.com/) にアクセス
2. Googleアカウントでログイン
3. 「Get API key」をクリック
4. 新しいAPIキーを作成
5. 生成されたAPIキーをコピー

### 2. 環境変数の設定

#### Windows (PowerShell)
```powershell
$env:GOOGLE_API_KEY="your_actual_api_key_here"
```

#### Windows (Command Prompt)
```cmd
set GOOGLE_API_KEY=your_actual_api_key_here
```

#### Linux/Mac (Bash)
```bash
export GOOGLE_API_KEY="your_actual_api_key_here"
```

### 3. アプリケーションの起動

環境変数を設定後、アプリケーションを起動してください：

```bash
python app.py
```

## 機能

- **動的目標生成**: ユーザーの基本情報、プロフィール、暮らしの詳細を分析
- **個別化された提案**: ユーザーの強み、興味、不安を考慮した目標
- **フォールバック機能**: AIが利用できない場合は従来の方法で目標生成
- **重複防止**: 同じ内容の目標が重複して保存されない

## トラブルシューティング

### APIキーエラー
- 環境変数 `GOOGLE_API_KEY` が正しく設定されているか確認
- APIキーが有効か確認

### ネットワークエラー
- インターネット接続を確認
- ファイアウォール設定を確認

### 目標生成エラー
- ユーザー情報が正しく入力されているか確認
- ログファイルでエラー詳細を確認

## 注意事項

- APIキーは機密情報です。他人と共有しないでください
- 本番環境では、環境変数ファイル（.env）の使用を推奨
- Google Gemini APIの利用制限にご注意ください
