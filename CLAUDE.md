# CLAUDE.md — Claude Code 固有設定

共通ルール（用語統一・画像サイズ・リポジトリ構成）は AGENTS.md を参照すること。

@AGENTS.md

---

## スキル一覧

用途別の詳細ルールは `.claude/skills/` のスキルに分割されている。

| スキル | 用途 |
|---|---|
| **create-mod** | AI エージェントでキャラクター MOD を新規作成するワークフロー |
| **write-guide** | ガイド MD の執筆・編集ルールと Markdown 記法規約 |

## コマンド一覧

明示的に `/コマンド名` で呼び出すルールは `.claude/commands/` に配置されている。

| コマンド | 用途 |
|---|---|
| **/convert-html** | MD ファイルを HTML に変換・同期するルール |
| **/quality-check** | ガイドの品質チェック（レビュー）手順 |
