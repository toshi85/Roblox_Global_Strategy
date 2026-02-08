# Production Evidence Guide — ロブロックス海外

## 目的
YouTubeの収益化停止・チャンネル削除に対する異議申し立ての証拠を確保する。
2026年1月のAIチャンネル大量削除（16チャンネル、3500万登録者）を受けた防衛策。

---

## フォルダ構造

```
ロブロックス海外/Production_Evidence/
├── 2026-02-15_physics-fail-chair/
│   ├── foley_raw/
│   │   ├── chair_break.wav
│   │   ├── vine_boom.wav
│   │   └── character_grunt_raw.wav
│   ├── veo3_prompts.md
│   ├── storyboard.md
│   ├── edit_notes.md
│   └── timeline_screenshot.png
├── 2026-02-17_justice-noob-vs-rich/
│   └── ...
└── ...
```

---

## 各ファイルの記録ルール

### 1. foley_raw/ — 生音声データ
- フォリー収録の**加工前**の音声ファイルを保存
- ファイル命名: `<効果音の説明>.wav` (例: `door_slam.wav`, `grunt_pitch_raw.wav`)
- Simlish音声は**ピッチシフト前**のオリジナルを保存
- 最低解像度: 44.1kHz / 16bit

### 2. veo3_prompts.md — AI生成プロンプトログ
```markdown
# Veo 3 Generation Log

## Shot 1: Opening - Chair Walk
- **Prompt**: "Roblox-style TV-Head character in business suit walking confidently toward a wooden chair, cinematic lighting, toy texture, subsurface scattering, 15fps"
- **Settings**: Resolution 1080x1920, Duration 3s
- **Generations**: 3 attempts, selected #2
- **Manual edits**: Color grading adjusted (warmer), cropped 5% top

## Shot 2: Chair Explosion
- **Prompt**: ...
```

### 3. storyboard.md — ストーリーボード
```markdown
# Storyboard: The Physics Fail

## Shot List
| # | Time | Action | Camera | Audio |
|---|---|---|---|---|
| 1 | 0-3s | TV-Head walks to chair | Wide, static | Footstep foley |
| 2 | 3-5s | Sits down, chair explodes | Medium → Zoom | CRASH + block scatter |
| 3 | 5-8s | Blocks flying everywhere | Slow-mo tracking | Whoosh foley |
| 4 | 8-12s | TV-Head looks at camera | Close-up, push in | Vine boom |
| 5 | 12-15s | Static screen, end card | Static | - |
```

### 4. edit_notes.md — 手動編集記録
```markdown
# Edit Notes: The Physics Fail

## AI Output → Final Video の変更点
1. Shot 1: Veo3出力のライティングが暗すぎた → DaVinciで明るさ+15%
2. Shot 2: 爆発エフェクトが不自然 → 手動でブロック散乱をタイミング調整
3. Shot 3: AIが生成した余計なキャラを削除（マスク処理）
4. 全体: カラーグレーディングを統一（LUT: Warm Toy Look）
5. 音声: 全フォリーを手動同期（フレーム単位で調整）

## 使用ソフトウェア
- 映像編集: DaVinci Resolve 19
- 音声編集: Audacity
- 画像加工: Photoshop（サムネイル）
```

### 5. timeline_screenshot.png — タイムラインスクリーンショット
- 編集ソフトのタイムライン全体が映るスクリーンショット
- 複数トラック（映像+音声）が確認できること
- 日付・プロジェクト名が画面内に表示されていること（可能なら）

---

## 保存ルール

| 項目 | ルール |
|---|---|
| 保存期間 | 最低12ヶ月（収益化停止の異議申し立て期間をカバー） |
| 保存場所 | ローカル + Google Driveバックアップ推奨 |
| Git管理 | foley_raw/は.gitignoreに追加（大容量）。MD/PNGはGit管理対象 |
| 命名規則 | `YYYY-MM-DD_<英語タイトルスラッグ>/` |

---

## 異議申し立て時の使い方

YouTubeから収益化停止・チャンネル削除の通知を受けた場合:

1. **該当動画のProduction_Evidenceフォルダを開く**
2. **以下を異議申し立て文に添付/記載**:
   - 「各動画は手動でストーリーボードを作成し、音声は人間が録音・編集しています」
   - フォリー収録の生データ（foley_raw/）の存在を提示
   - Veo 3の出力に対して手動編集を加えた記録（edit_notes.md）を提示
   - 編集タイムライン（timeline_screenshot.png）で複数トラック編集の証拠を提示
3. **キーメッセージ**: 「AIツールは映像生成の補助として使用していますが、ストーリー構成・音声制作・映像編集は全て人間が行っています」
