# Description Guide — ロブロックス海外

## 目的
動画説明文のテンプレート化を防止し、YouTube「量産型コンテンツ」判定を回避する。

---

## 鉄則
1. **コピペ禁止** — 説明文は毎回ゼロから書く
2. **前回と90%以上一致はNO-GO** — validate_authenticity.pyが自動検出
3. **全て英語** — 日本語の混入はvalidate_metadata.pyが検出

---

## 必須要素（全動画共通）

### Element 1: Story Summary（必須・毎回ユニーク）
動画の内容を2-3文で説明。**毎回異なる文章にすること。**

```
❌ BAD (テンプレ):
"Watch what happens when our characters get into trouble!"

✅ GOOD (個別):
"TV-Head finds a mysterious chair in an empty room. What could go wrong? Everything."

✅ GOOD (個別):
"Cone-Head challenges CCTV-Head to a building contest. The results are... explosive."
```

### Element 2: AI Disclosure（必須・固定文OK）
```
🎬 Visuals created with AI tools (Google Veo 3), with manual editing and creative direction.
```

### Element 3: Human Credits（必須・名前は固定OK、フォーマットは毎回変える）
```
✅ Format A:
🔊 Sound Design & Foley: [Name]
🎭 Voice/Simlish: [Name]
📝 Story & Direction: [Name]

✅ Format B:
Credits: Sound by [Name] | Voice by [Name] | Directed by [Name]

✅ Format C:
Made with ❤️ by [Name] — Sound, Voice, Story & Direction
```

### Element 4: Character/Series Info（任意・あれば差別化になる）
```
🤖 Meet TV-Head — the glitchiest character in Roblox history.
🔶 Cone-Head is back, and this time luck is NOT on his side.
📹 CCTV-Head sees everything. Except what's behind him.
```

---

## 説明文テンプレート（フレームワーク）

以下はフレームワーク。**Story Summaryは毎回必ず書き直すこと。**

```
[2-3文のユニークなストーリーサマリー]

🎬 Visuals created with AI tools (Google Veo 3), with manual editing and creative direction.

🔊 Sound Design & Foley: [Name]
🎭 Voice/Simlish: [Name]
📝 Story & Direction: [Name]

[キャラクター/シリーズ情報（任意）]

#Roblox #Shorts #Animation
```

---

## NG例

```
❌ 毎回同じ説明文:
"Funny Roblox animation! Like and subscribe for more!
Sound Design: Toshi | Voice: Toshi
#Roblox #Shorts"

❌ 日本語混入:
"面白いロブロックスアニメ！ Subscribe!"

❌ AI開示なし:
"Original Roblox animation by our team."
（Veo 3を使用しているのに開示していない）
```

---

## バリデーション
```bash
python3 Universal_Tools/validate_authenticity.py --channel roblox --script <台本パス> --description "説明文テキスト"
python3 Universal_Tools/validate_metadata.py --channel roblox --title "タイトル" --description "説明文テキスト"
```

チェック項目:
- AI開示の有無
- 人間クレジットの有無
- テンプレート依存度（直近10本との類似度）
- 日本語混入
- 禁止ワード
