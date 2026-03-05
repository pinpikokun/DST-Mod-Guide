# CLAUDE.md — DST-Mod-Tools ドキュメント運用ルール

## 前提：このリポジトリの目的と意義

DST-Mod-Tools は、Don't Starve Together (DST) の MOD 開発に必要なツール群と、その使い方ガイドを提供するリポジトリである。

**最終目標**: プログラミング経験がなくても、PC 操作に不慣れでも、このリポジトリのガイドだけを読めば誰でもキャラクター MOD を完成させて Steam Workshop に公開できる状態を維持すること。

ガイドは「MOD 初心者」かつ「PC 初心者」の両方を想定読者としている。専門知識を前提とせず、すべての手順を省略なく記述する。

---

## 1. ドキュメント執筆ルール

### 1.1 読者レベルの想定

- **MOD 初心者**: DST の MOD を作ったことがない人。プレハブ・Bank・Build 等の用語を知らない。
- **PC 初心者**: コマンドプロンプトや Git Bash を使ったことがない人。「フォルダを右クリック」のレベルから説明する。
- 専門用語は初出時に必ず日本語で説明する（例: `prefab（プレハブ）とは？`）。
- 「なぜそうするのか」を `> **なぜ...？**:` ブロックで補足する。
- ファイルの作成方法（VSCode での新規ファイル作成手順など）も省略しない。
- 画像作成ソフトの案内（ペイント、GIMP 等）も記載する。

### 1.2 文体・トーン

- 日本語、です/ます調で統一する。
- 技術用語（ツール名、拡張子、コード識別子）は英語のまま残す。
- 初出の技術用語は英語＋括弧で日本語説明: `MOD（モッド）`。
- 励ましの表現を使う（`心配いりません`、`まずは仮画像で OK`）。
- 絵文字は使用しない。

### 1.3 用語の統一

以下の用語は全ガイドで表記を統一すること。

| 用語 | 正しい表記 | NG 例 |
|---|---|---|
| ポートレート画像 | ポートレート | 肖像画、portrait |
| MOD | MOD（半角大文字、前後にスペース） | mod、Mod |
| DST | DST（初出時に正式名称を併記） | dst |
| ktools | ktools（小文字） | keytool、Ktools |
| 各辺が 2 の累乗 | 各辺が 2 の累乗（例: 256 x 512 は OK） | 正方形でなければならない |
| キャラクター MOD のマップアイコン | `images/map_icons/` | `images/minimap/` |
| 建造物のマップアイコン | `images/minimap/` | `images/map_icons/` |
| スクリプトの場所 | `data\databundles\scripts.zip` を展開 | `data\scripts\prefabs\` に直接ある |

### 1.4 ポートレート画像サイズ（全ガイド共通の正値）

| 用途 | サイズ |
|---|---|
| saveslot_portraits | 128 x 128 |
| selectscreen_portraits | 256 x 512 |
| bigportraits | 512 x 512 以上 |
| avatar | 64 x 64 |
| map_icons | 64 x 64 |

---

## 2. Markdown 記法ルール

### 2.1 構成順序

すべてのガイドは以下の順序で構成する。

1. `#` タイトル（H1、1 ファイルに 1 つだけ）＋ 1〜2 文の概要
2. `---`
3. `## 目次`（目次またはガイド一覧）
4. `---`
5. 概念説明（「〜とは」「このガイドで学べること」）
6. インストール・セットアップ
7. ステップバイステップ手順（本体）
8. よくあるトラブル / エラーと対処法
9. Tips・参考情報
10. 参考リンク
11. `---`
12. `## ライセンス`
13. `---`
14. 作者フッター（`<sub>` タグ）

### 2.2 見出しレベル

- `#`: ドキュメントタイトル（1 つのみ）
- `##`: 大セクション
- `###`: サブセクション / `### Step N: タイトル`
- `####`: 個別手順 / エラーメッセージ見出し

### 2.3 コードブロック

- Lua コード: ` ```lua `
- シェルコマンド: ` ```bash `
- ファイルパス・ディレクトリツリー: ` ``` `（言語指定なし）
- Windows パスはバックスラッシュ: `C:\Program Files (x86)\Steam\...`
- Git Bash パスはスラッシュ: `"/c/Users/<ユーザー名>/..."`
- ユーザー固有値は山括弧プレースホルダー: `<ユーザー名>`

### 2.4 Lua コード内のマーカー

- `-- ★書き換え:` ユーザーが必ず変更する行
- `-- ★変更任意:` カスタマイズ可能な行
- `-- そのまま` 変更不要の行
- `-- ========` セクション区切り

### 2.5 ブロック引用パターン

| ラベル | 用途 |
|---|---|
| `> **注意**:` | やると壊れる・失敗する警告 |
| `> **重要**:` | 絶対に見逃してはいけない情報 |
| `> **ポイント**:` | 重要な要点・コツ |
| `> **Tips**:` / `> **初心者向けTip:**` | 便利な豆知識 |
| `> **ヒント**:` | 文脈に応じた補助情報 |
| `> **補足**:` | 追加の説明 |
| `> **なぜ...？**:` | 初心者向けの「なぜそうするか」 |

### 2.6 テーブル

- セパレータは `|---|---|`（ハイフン 3 つ、アライメント指定なし）
- トラブルシューティング: `| 症状 | 原因 | 解決法 |` の 3 列

### 2.7 相互リンク

- 別ディレクトリへの参照: `[ガイド名](DST-TextureConverter/README.md)`
- 同一ディレクトリ内: `[ファイル名](README-character.md)`
- 親ディレクトリへの戻り: `[← README.md に戻る](../README.md)`
- 各ガイドは「このガイドで扱わないもの」セクションで関連ガイドへリンクする
- HTML 版リンク: すべての `.md` ファイルの冒頭（タイトル＋概要文の直後、最初の `---` の前）に対応する HTML 版へのリンクを配置する: `> **HTML 版**: [ファイル名.html](ファイル名.html)`

### 2.8 UI ナビゲーションパス（矢印手順）

UI 操作の手順（「Steam → 設定 → ストレージ」のような矢印で繋ぐナビゲーション）は、矢印テキストで横に並べず **縦タイムライン方式** で記述する。

**Markdown での記述:**

```markdown
以下の手順で mods フォルダを開きます。

1. Steam を開く
2. Don't Starve Together を右クリック
3. 「管理」を選択
4. 「ローカルファイルを閲覧」をクリック
5. `mods` フォルダを開く
```

**HTML での記述:**

```html
<ol class="nav-path">
  <li>Steam を開く</li>
  <li>Don't Starve Together を右クリック</li>
  <li><strong>管理</strong> を選択</li>
  <li><strong>ローカルファイルを閲覧</strong> をクリック</li>
  <li><code>mods</code> フォルダを開く</li>
</ol>
```

**CSS 仕様（`.nav-path`）:**

- 左側に縦線（`var(--border)`、2px）とドット（`var(--accent-warm)`、10px 円）を配置
- 各ステップは縦に並び、ドットが縦線上に表示される
- `position: absolute` で `::before`（縦線）と `::after`（ドット）を配置
- 先頭・末尾のアイテムで縦線の開始・終了位置を調整

**適用基準:**

- 3 ステップ以上の UI 操作手順に適用する
- 2 ステップ以下の短い手順や、文中に埋め込まれた簡潔な参照（例: 「右クリック → コピー」）はそのままでよい

### 2.9 フッター

ライセンスセクションの後、ファイル末尾に以下を配置する。

```markdown
---

<sub>Author: [pinpikokun](https://steamcommunity.com/profiles/76561198076111536/)</sub><br>
<sub>[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/pinpikokun/DST-teemo) [![Steam Workshop](https://img.shields.io/badge/Steam%20Workshop-Subscribe-blue?logo=steam)](https://steamcommunity.com/sharedfiles/filedetails/?id=390684095)</sub>
```

---

## 3. HTML 版の運用ルール

### 3.1 MD と HTML の 1:1 対応

- すべての `.md` ファイルに対応する `.html` ファイルを同じディレクトリに配置する。
- MD を修正したら、**必ず対応する HTML にも同じ内容を反映する**。
- HTML の新規作成時は、既存の HTML（例: DST-TextureConverter/README.html）のスタイルを参照して同じデザインシステムで作成する。

### 3.2 HTML 共通仕様

- `<!DOCTYPE html>`, `<html lang="ja">`, UTF-8
- Google Fonts: `Noto Serif JP`（400, 700）, `Noto Sans JP`（300, 400, 500, 600）
- CSS カスタムプロパティによるウォームカラーパレット（`--bg-primary: #faf9f7` 等）
- フッター形式（全ファイル統一）:
  ```
  ガイド名 &#8212; このドキュメントは自由に利用・改変・再配布できます。DST MOD 制作にお役立てください。
  Author: pinpikokun ｜ GitHub ｜ Steam Workshop（shields.io バッジ画像）
  ```

---

## 4. 品質チェック体制

### 4.1 複数エージェントによるレビュー

README の新規作成・大幅修正時は、以下の観点で複数エージェントによる並列レビューを実施する。

| 観点 | チェック内容 |
|---|---|
| **リンク検証** | 全ての内部リンク（MD 間・アンカー）が正しいパスを指しているか |
| **初心者視点** | PC 初心者が読んで迷わないか、用語は説明されているか、手順に飛躍がないか |
| **技術的正確性** | コマンド、パス、サイズ、オプションが実際のツールと一致しているか |
| **MOD 作成再現性** | ガイドに従って実際に MOD を作成できるか（手順の抜け漏れがないか） |

### 4.2 クロスチェック

- 各エージェントのレビュー結果を突き合わせ、矛盾や見落としがないか検証する。
- 複数のガイド間で用語・サイズ・パスなどの整合性を確認する（1 箇所の修正が他ガイドに波及する場合がある）。

### 4.3 実践テスト

人間の手が必要な部分（実際にアプリを操作する、画像を描く等）を除き、以下を可能な範囲で実際に実行して検証する。

- コマンドの実行（`ktech --help`、`krane --help` 等）
- パスの存在確認
- ファイル構成の正しさ
- Lua コードの文法チェック

---

## 5. 変更時のワークフロー

1. **MD を修正する**
2. **対応する HTML に同じ修正を反映する**
3. **他のガイドへの波及がないか確認する**（用語・サイズ・パスの整合性）
4. **大きな変更の場合は複数エージェントレビュー + クロスチェックを実施する**
5. **コミット＆プッシュ**

---

## 6. リポジトリ構成

```
DST-Mod-Tools/
├── README.md / .html              ← メインガイド（はじめてのキャラクター MOD）
├── CLAUDE.md                      ← 本ファイル（運用ルール）
├── DST-Spriter/
│   ├── README.md / .html          ← アニメーション総合ガイド
│   ├── README-character.md / .html ← キャラクターアニメーション編
│   ├── README-item-equipment.md / .html ← アイテム・武器防具編
│   ├── README-effect.md / .html   ← エフェクト編
│   └── sample/                    ← サンプルプロジェクト
├── DST-TextureConverter/
│   └── README.md / .html          ← PNG → TEX 変換ガイド
├── DST-ktools/
│   └── README.md / .html          ← krane/ktech デコンパイルガイド
├── DST-Lua-Scripting/
│   ├── README.md / .html          ← Lua スクリプティング総合ガイド
│   ├── README-DST-teemo.md / .html ← Captain Teemo MOD 実践解説
│   ├── README-speech.md / .html   ← キャラクターセリフ（Speech）作成ガイド
│   └── README-modinfo-config.md / .html ← modinfo コンフィグオプション詳細ガイド
├── DST-AI-Agent/
│   └── README.md / .html          ← AI エージェント活用ガイド
├── DST-Workshop-Upload/
│   └── README.md / .html          ← Steam ワークショップ公開ガイド
├── DST-FMOD-Designer/
│   └── README.md / .html          ← キャラクターボイス作成ガイド
└── DST-Chatterbox/
    └── README.md / .html          ← AI 音声合成ガイド
```

---

## 7. AI エージェントによる MOD 新規作成ワークフロー

AI エージェント経由でキャラクター MOD の新規作成を依頼された場合は、**必ずこのセクションの手順に従って進めること**。また、[DST-AI-Agent/README.md](DST-AI-Agent/README.md) も合わせて参照すること。

### 7.1 基本方針

- AI がすべてのファイルを作成・配置し、**人間の介入なしで「ゲーム内で動作する MOD」を完成させる**。
- 画像は**仮画像（単色 PNG）を AI が自動生成**する。まず動く MOD を作ることを最優先する。
- 画像の差し替え（オリジナルの顔・ポートレート等）は **MOD 完成後のオプションステップ** として案内する。
- `work/` フォルダを作業領域として使用し、中間ファイル（仮画像 PNG、sample_build コピー等）をそこに配置する。
- **外部ライブラリを追加インストールしない。** 仮画像生成を含むすべての処理は、DST Mod Tools 同梱のツール（TextureConverter、scml.exe、buildanimation.py、同梱の Python 2.7）または Windows 標準機能（PowerShell の `System.Drawing`）のみで行う。`pip install` 等で外部パッケージを追加してはならない。

### 7.2 work フォルダ

- 場所: リポジトリ直下の `work/<キャラクター名>/`
- `work/` は `.gitignore` に登録済みのため、Git にコミットされない。
- 用途: sample_build のコピー、仮画像 PNG の生成、TEX 変換の中間ファイル。
- フォルダ構成:

```
work/<キャラクター名>/
├── portraits/                    ← 仮画像 PNG（TEX 変換元）
│   ├── modicon.png
│   ├── <キャラクター名>_selectscreen.png
│   ├── <キャラクター名>_saveslot.png
│   ├── <キャラクター名>_bigportrait.png
│   ├── <キャラクター名>_avatar.png
│   ├── <キャラクター名>_avatar_ghost.png
│   └── <キャラクター名>_map_icon.png
├── build.scml                    ← Spriter プロジェクト（sample_build からコピー）
├── face/                         ← 顔パーツ（sample_build からコピー）
├── hair/                         ← 髪パーツ
├── torso/                        ← 胴体パーツ
└── ...（その他の sample_build パーツフォルダ）
```

### 7.3 Phase 1: スクリプトとフォルダ構成の作成

1. **MOD フォルダを作成する**
   - 場所: `C:\Program Files (x86)\Steam\steamapps\common\Don't Starve Together\mods\<キャラクター名>\`
   - サブフォルダ: `anim/`, `bigportraits/`, `images/avatars/`, `images/map_icons/`, `images/saveslot_portraits/`, `images/selectscreen_portraits/`, `scripts/prefabs/`, `sound/`

2. **Lua スクリプトを作成する**
   - `modinfo.lua` — MOD 基本情報（メインガイド README.md の Step 2 テンプレートに準拠）
   - `modmain.lua` — メインスクリプト（メインガイド README.md の Step 3 テンプレートに準拠）。**必ず `PrefabFiles` テーブルにキャラクター名を宣言すること**（宣言しないと prefab が読み込まれずゲームがフリーズする）
   - `scripts/prefabs/<キャラクター名>.lua` — キャラクター定義（メインガイド README.md の Step 4 テンプレートに準拠）
   - `scripts/speech_<キャラクター名>.lua` — セリフファイル（メインガイド README.md の Step 5 テンプレートに準拠）

3. **XML アトラスファイルを作成する**（7 個）
   - `modicon.xml`（MOD 直下）
   - `<キャラクター名>.xml`（`bigportraits/`）
   - `avatar_<キャラクター名>.xml`（`images/avatars/`）
   - `avatar_ghost_<キャラクター名>.xml`（`images/avatars/`）
   - `<キャラクター名>.xml`（`images/map_icons/`）
   - `<キャラクター名>.xml`（`images/saveslot_portraits/`）
   - `<キャラクター名>.xml`（`images/selectscreen_portraits/`）

### 7.4 Phase 2: 仮画像の生成と TEX 変換

1. **`work/<キャラクター名>/portraits/` フォルダを作成する**

2. **ダミーポートレート画像を `work/<キャラクター名>/portraits/` に配置する**
   - `DST-AI-Agent/dummy_portraits/` にダミーのポートレート画像が用意されている。これは人間が作成したテンプレートで、ユーザーが後から自分で描く際の参考になる。
   - 以下のファイルをコピーし、キャラクター名にリネームして配置する。**AI が独自に仮画像を生成してはならない。**

   | コピー元（dummy_portraits/） | コピー先（portraits/） | サイズ | 用途 |
   |---|---|---|---|
   | `modicon.png` | `modicon.png` | 128 x 128 | MOD アイコン |
   | `selectscreen.png` | `<キャラクター名>_selectscreen.png` | 256 x 512 | キャラクター選択画面 |
   | `saveslot.png` | `<キャラクター名>_saveslot.png` | 128 x 128 | セーブスロット |
   | `bigportrait.png` | `<キャラクター名>_bigportrait.png` | 512 x 512 | 大ポートレート |
   | `avatar.png` | `<キャラクター名>_avatar.png` | 64 x 64 | アバター |
   | `avatar_ghost.png` | `<キャラクター名>_avatar_ghost.png` | 64 x 64 | ゴーストアバター |
   | `map_icon.png` | `<キャラクター名>_map_icon.png` | 64 x 64 | マップアイコン |

3. **アニメーションのキャラクター固有パーツをダミー画像に差し替える**
   - sample_build をコピーした時点では Wilson の画像が入っている。このまま使うとゲーム内・キャラクター選択画面ともに Wilson の外見が表示されてしまう。
   - `DST-AI-Agent/dummy_parts/` に以下のダミー画像フォルダが用意されている。これらは輪郭と表情の参考になるよう人間が作成したもので、ユーザーが後から自分で描く際のテンプレートになる。
     - `face/` — 顔パーツ（face-0.png 〜 face-13.png）
     - `hair/` — 髪パーツ
     - `hair_hat/` — 帽子着用時の髪パーツ
     - `headbase/` — 頭の輪郭（素頭）
     - `headbase_hat/` — 頭の輪郭（帽子着用時）
   - `DST-AI-Agent/dummy_parts/` 内の各フォルダの全 PNG を `work/<キャラクター名>/` の対応するフォルダに上書きコピーする。**AI が独自に仮画像を生成してはならない。**

4. **TextureConverter で全ポートレート PNG を TEX に変換する**
   - TextureConverter のパス: `C:\Program Files (x86)\Steam\steamapps\common\Don't Starve Mod Tools\mod_tools\tools\bin\TextureConverter.exe`
   - コマンド形式:
     ```bash
     TextureConverter.exe -i <入力>.png -o <出力>.tex -f bc3 -p opengl --mipmap --premultiply
     ```

5. **変換した TEX ファイルを MOD フォルダの正しい場所に配置する**
   - `modicon.tex` → MOD 直下
   - `selectscreen` → `images/selectscreen_portraits/<キャラクター名>.tex`
   - `saveslot` → `images/saveslot_portraits/<キャラクター名>.tex`
   - `bigportrait` → `bigportraits/<キャラクター名>.tex`
   - `avatar` → `images/avatars/avatar_<キャラクター名>.tex`
   - `avatar_ghost` → `images/avatars/avatar_ghost_<キャラクター名>.tex`
   - `map_icon` → `images/map_icons/<キャラクター名>.tex`

### 7.5 Phase 3: アニメーション ZIP の作成

1. **work/<キャラクター名>/ に sample_build の中身をコピーする**
   - コピー元: `C:\Program Files (x86)\Steam\steamapps\common\Don't Starve Mod Tools\mod_tools\sample_build\`
   - コピー先: `work/<キャラクター名>/`（`build.scml` + 全パーツフォルダ）

2. **work の中身を `exported/<キャラクター名>/` にコピーし、scml ファイルをリネームする**
   - コピー先: `mod_tools\exported\<キャラクター名>\`
   - **重要: `build.scml` を `<キャラクター名>.scml` にリネームすること。** scml ファイル名がそのまま ZIP 内部の「ビルド名」になる。`MakePlayerCharacter("<キャラクター名>", ...)` はビルド名がキャラクター名と一致することを前提にしているため、ファイル名が異なるとキャラクターが透明になる。
   - work フォルダが画像編集の起点（ユーザーが見る場所）であり、exported はビルド用の一時コピーである。**画像の生成・編集は必ず work フォルダで行い、ビルド時に work → exported にコピーする**こと。exported に直接ファイルを生成・編集してはならない。

3. **scml.exe + buildanimation.py でアニメーション ZIP をビルドする**
   - autocompiler.exe は GUI ツールのため AI エージェントからは安定して動作しない場合がある。代わりに手動ビルドコマンドを使用する。
   ```bash
   MOD_TOOLS="C:/Program Files (x86)/Steam/steamapps/common/Don't Starve Mod Tools/mod_tools"
   cd "$MOD_TOOLS"
   # Step 1: scml.exe で中間 ZIP を生成
   ./scml.exe "exported/<キャラクター名>/<キャラクター名>.scml" "exported/<キャラクター名>"
   # Step 2: buildanimation.py で最終 ZIP を生成
   ./buildtools/windows/Python27/python.exe tools/scripts/buildanimation.py \
     "exported/<キャラクター名>/<キャラクター名>.zip" \
     --outputdir="exported/<キャラクター名>" --force --ignoreexceptions
   ```
   - 生成された `mod_tools\exported\<キャラクター名>\anim\<キャラクター名>.zip` を MOD の `anim/<キャラクター名>.zip` にコピーする。

4. **ゴーストアニメーション ZIP を配置する**
   - コピー元: `C:\Program Files (x86)\Steam\steamapps\common\Don't Starve Together\data\anim\ghost_wilson_build.zip`
   - コピー先: MOD の `anim/ghost_<キャラクター名>_build.zip`

### 7.6 Phase 4: 最終確認

1. MOD フォルダ内の全ファイルの存在を確認する。
2. `modmain.lua` の `Assets` テーブルに記載された全ファイルが実在するか検証する。
3. ファイル名の大文字・小文字の一致を確認する。
4. 完成したフォルダ構成を人間に報告する。

### 7.7 Phase 5: 画像の差し替え（オプション・MOD 完成後）

MOD が動作する状態になった後、人間がオリジナルの画像に差し替えたい場合は以下の流れで進める。

#### ポートレート等の画像差し替え

1. AI が `work/<キャラクター名>/portraits/` 内のファイルのフルパスとサイズ一覧を人間に提示し、「このファイルを画像編集ソフトで編集してください」と促す。
2. 人間が画像編集ソフト（ペイント、GIMP 等）でファイルを修正する。
3. 人間が AI に「画像を差し替えたから圧縮してファイルを差し替えて」と指示する。
4. AI が TextureConverter で TEX に再変換し、MOD フォルダの正しい場所に上書き配置する。

#### アニメーション画像の差し替え

1. AI が `work/<キャラクター名>/` 内の sample_build ファイル（特に `face/` フォルダ）のフルパスを人間に提示し、「このファイルを画像編集ソフトで編集してください」と促す。
2. 人間が画像編集ソフトでファイルを修正する。
3. 人間が AI に「画像を差し替えたから圧縮してファイルを差し替えて」と指示する。
4. AI が autocompiler で ZIP を再ビルドし、MOD の `anim/<キャラクター名>.zip` を上書きする。
