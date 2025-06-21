# RestoreFileClassifier

2025/06/21 初版
Created by Studio Mitsu

## 【背景 / Background】

データ復元ソフトやバイナリスキャンなどを使用して復元されたファイルは、もはや元の名前や抽出ロジックが失われていることが多く、別のディレクトリに同じような抽出物が並ぶ、カオスな状態になりがちです。

そのようなカオスな中から、有効な動画や画像だけをスパッと挙げ、簡単な設定で自動分類されたディレクトリ構造を作りたい。そのような必要性から、RestoreFileClassifierは誕生しました。

## 【目的 / Purpose】

復元されたファイル群を:
- 正常な動画 (映像ストリームを含む)
- 正常な画像 (抽出エラーのないファイル)
- それ以外の不明ファイル (壊れている、または非対応)

に自動分類し、保存しながらログを取得することにより、

- 大量ファイルの中から有効なデータのみを残す
- 相対的に危険なファイル操作を防ぐ
- 他システムへの転送を簡略化

を目指しています。

## 【環境 / Environment】

- Windows 10 / 11 上の Python 3.10 - 3.12
- VSCode (Visual Studio Code)
- ffmpeg/ffprobe が PATH に通っていること
- pip が利用可能

## 【セットアップ / Setup】

1. このリポジトリをクローン
1. VSCodeでプロジェクトルルートとして開く
1. .venv を作成 (任意)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

4. ffmpeg を利用可能にする（Windowsの環境変数PATHにffmpegの/binパスを追加）

## 【使い方 / Usage】

1. input/ フォルダに復元ファイルを入れる
1. classify.py を実行
```bash
python classify.py
```
3. Windowsなら run.bat をダブルクリック

## 【出力結果 / Output】

|フォルダ|内容|
| ---- | ---- |
|output/videos/|有効な動画ファイル|
|output/images/|有効な画像ファイル (拡張子判定 + 読込確認)|
|output/others/|無効、非対応、または壊れたファイル|
|log/result_xxxx.csv|処理結果ログ (CSV形式)|

## 【ディレクトリ構成 / Directory Structure】

```bash
RestoreFileClassifier/
├── classify.py              # メインスクリプト
├── requirements.txt         # 依存ライブラリ
├── run.bat                  # Windows用ワンクリック実行ファイル
├── README.md                # 本ファイル
├── LICENSE                  # ライセンス
├── .gitignore               # Git無視設定
├── .vscode/
│   └── extensions.json      # 推奨拡張機能
├── input/                   # 処理対象の復元ファイルを格納
├── output/
│   ├── videos/              # 判定された動画ファイルの保存先
│   ├── images/              # 判定された画像ファイルの保存先
│   └── others/              # 不明・破損ファイルの保存先
└── log/                     # 処理ログ保存ディレクトリ
```

## 【ライセンス / License】

MIT License │ 自由に使用・改変・再配布可能

## 【著作権 / Copyright】

(c) 2026 Studio Mitsu

本ツールは教育・復旧支援目的で開発されており、不正アクセスやファイル改竄を目的とした使用は禁止されています。

💡 このツールが役立ったと感じたら、  
[Buy Me a Coffee ☕](https://www.buymeacoffee.com/mitsuarchive) で応援していただけると嬉しいです！
