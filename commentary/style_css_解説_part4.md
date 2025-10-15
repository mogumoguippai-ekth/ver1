# style.css解説 - 第4部：目標関連・モーダル・招待コード・ツールチップ関連スタイル

## 概要
「私の望む暮らし」アプリケーションの統合CSSファイル（第4部）です。目標関連、モーダル、招待コード、ツールチップ関連のスタイリングを担当します。

---

## 📋 目次

### 19. 目標関連スタイル
- [19.1 目標ページ](#191-目標ページ)
- [19.2 目標コンテナ](#192-目標コンテナ)
- [19.3 目標ヘッダー](#193-目標ヘッダー)
- [19.4 目標タイトル](#194-目標タイトル)
- [19.5 目標サブタイトル](#195-目標サブタイトル)
- [19.6 目標グリッド](#196-目標グリッド)
- [19.7 目標カード](#197-目標カード)
- [19.8 目標カードヘッダー](#198-目標カードヘッダー)
- [19.9 目標カードタイトル](#199-目標カードタイトル)
- [19.10 目標カードコンテンツ](#1910-目標カードコンテンツ)
- [19.11 目標カードアクション](#1911-目標カードアクション)
- [19.12 目標生成ボタン](#1912-目標生成ボタン)
- [19.13 目標印刷ボタン](#1913-目標印刷ボタン)
- [19.14 目標履歴ボタン](#1914-目標履歴ボタン)
- [19.15 目標履歴ページ](#1915-目標履歴ページ)
- [19.16 目標履歴コンテナ](#1916-目標履歴コンテナ)
- [19.17 目標履歴ヘッダー](#1917-目標履歴ヘッダー)
- [19.18 目標履歴タイトル](#1918-目標履歴タイトル)
- [19.19 目標履歴サブタイトル](#1919-目標履歴サブタイトル)
- [19.20 目標履歴リスト](#1920-目標履歴リスト)
- [19.21 目標履歴アイテム](#1921-目標履歴アイテム)
- [19.22 目標履歴日付](#1922-目標履歴日付)
- [19.23 目標履歴内容](#1923-目標履歴内容)
- [19.24 目標履歴アクション](#1924-目標履歴アクション)
- [19.25 目標履歴削除ボタン](#1925-目標履歴削除ボタン)
- [19.26 目標履歴印刷ボタン](#1926-目標履歴印刷ボタン)
- [19.27 目標履歴戻るボタン](#1927-目標履歴戻るボタン)

### 20. モーダル関連スタイル
- [20.1 モーダル](#201-モーダル)
- [20.2 モーダル表示](#202-モーダル表示)
- [20.3 モーダルダイアログ](#203-モーダルダイアログ)
- [20.4 モーダルヘッダー](#204-モーダルヘッダー)
- [20.5 モーダルタイトル](#205-モーダルタイトル)
- [20.6 モーダル閉じるボタン](#206-モーダル閉じるボタン)
- [20.7 モーダルボディ](#207-モーダルボディ)
- [20.8 モーダルフッター](#208-モーダルフッター)
- [20.9 モーダルアクション](#209-モーダルアクション)
- [20.10 モーダルボタン](#2010-モーダルボタン)
- [20.11 モーダルボタン（プライマリ）](#2011-モーダルボタンプライマリ)
- [20.12 モーダルボタン（セカンダリ）](#2012-モーダルボタンセカンダリ)
- [20.13 モーダルボタン（危険）](#2013-モーダルボタン危険)
- [20.14 モーダルボタン（成功）](#2014-モーダルボタン成功)
- [20.15 モーダルボタン（警告）](#2015-モーダルボタン警告)
- [20.16 モーダルボタン（情報）](#2016-モーダルボタン情報)
- [20.17 モーダルボタン（小）](#2017-モーダルボタン小)
- [20.18 モーダルボタン（大）](#2018-モーダルボタン大)
- [20.19 モーダルボタン（全幅）](#2019-モーダルボタン全幅)
- [20.20 モーダルボタン（無効）](#2020-モーダルボタン無効)

### 21. 招待コード関連スタイル
- [21.1 招待コードセクション](#211-招待コードセクション)
- [21.2 招待コードラベル](#212-招待コードラベル)
- [21.3 招待コード入力](#213-招待コード入力)
- [21.4 招待コード生成ボタン](#214-招待コード生成ボタン)
- [21.5 招待コード表示](#215-招待コード表示)
- [21.6 招待コードコピーボタン](#216-招待コードコピーボタン)
- [21.7 招待コードメッセージ](#217-招待コードメッセージ)
- [21.8 招待コードメッセージ（成功）](#218-招待コードメッセージ成功)
- [21.9 招待コードメッセージ（エラー）](#219-招待コードメッセージエラー)
- [21.10 招待コードメッセージ（情報）](#2110-招待コードメッセージ情報)

### 22. ツールチップ関連スタイル
- [22.1 ツールチップ](#221-ツールチップ)
- [22.2 ツールチップコンテンツ](#222-ツールチップコンテンツ)
- [22.3 ツールチップ矢印](#223-ツールチップ矢印)
- [22.4 ツールチップアニメーション](#224-ツールチップアニメーション)
- [22.5 ツールチップ表示](#225-ツールチップ表示)
- [22.6 ツールチップ非表示](#226-ツールチップ非表示)
- [22.7 ツールチップホバー](#227-ツールチップホバー)
- [22.8 ツールチップフォーカス](#228-ツールチップフォーカス)
- [22.9 ツールチップアクティブ](#229-ツールチップアクティブ)
- [22.10 ツールチップ無効](#2210-ツールチップ無効)

---

## 19. 目標関連スタイル <a id="19-目標関連スタイル"></a>

### 19.1 目標ページ <a id="191-目標ページ"></a>
```css
.goals-page {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    min-height: 100vh;
    padding: 20px 0;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標ページの背景グラデーション

### 19.2 目標コンテナ <a id="192-目標コンテナ"></a>
```css
.goals-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標の最大幅制限

### 19.3 目標情報ヘッダー <a id="193-目標情報ヘッダー"></a>
```css
.goals-info-header {
    background: linear-gradient(135deg, #e8f5e8 0%, #f0f8f0 100%);
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    border-left: 4px solid #28a745;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標情報ヘッダーの緑系グラデーション

### 19.4 新規目標バッジ <a id="194-新規目標バッジ"></a>
```css
.new-goals-badge {
    margin-bottom: 10px;
}
```
**使用ページ:** `goals.html`  
**説明:** 新規目標バッジの余白

### 19.5 バッジ <a id="195-バッジ"></a>
```css
.badge {
    background: #28a745;
    color: white;
    padding: 5px 10px;
    border-radius: 15px;
    font-size: 12px;
    font-weight: bold;
}
```
**使用ページ:** `goals.html`  
**説明:** バッジの緑系背景、角丸

### 19.6 目標日付情報 <a id="196-目標日付情報"></a>
```css
.goals-date-info {
    margin-bottom: 10px;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標日付情報の余白

### 19.7 目標更新情報 <a id="197-目標更新情報"></a>
```css
.goals-update-info {
    font-size: 14px;
    color: #666;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標更新情報の小さな文字、グレー色

### 19.8 目標セクション <a id="198-目標セクション"></a>
```css
.goal-section {
    background: white;
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    border-left: 5px solid #e65100;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標セクションの白背景、角丸、オレンジ系左境界線

### 19.9 目標ヘッダー <a id="199-目標ヘッダー"></a>
```css
.goal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid #e9ecef;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標ヘッダーの配置、下境界線

### 19.10 目標ヘッダーの見出し <a id="1910-目標ヘッダーの見出し"></a>
```css
.goal-header h3 {
    color: #e65100;
    margin: 0;
    font-size: 1.4rem;
    font-weight: bold;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標ヘッダーの見出しのオレンジ系色

### 19.11 目標テキスト <a id="1911-目標テキスト"></a>
```css
.goal-text {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #333;
    margin-bottom: 15px;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標テキストの文字サイズ、行間調整

### 19.12 短期目標アイテム <a id="1912-短期目標アイテム"></a>
```css
.short-goal-item {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 8px;
    margin-bottom: 10px;
    border-left: 3px solid #e65100;
}
```
**使用ページ:** `goals.html`  
**説明:** 短期目標アイテムのフレックスボックス、オレンジ系左境界線

### 19.13 目標番号 <a id="1913-目標番号"></a>
```css
.goal-number {
    background: #e65100;
    color: white;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 14px;
    flex-shrink: 0;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標番号の円形、オレンジ系背景

### 19.14 目標内容 <a id="1914-目標内容"></a>
```css
.goal-content {
    flex: 1;
    color: #333;
    line-height: 1.5;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標内容のフレックス配置

### 19.15 分析セクション <a id="1915-分析セクション"></a>
```css
.analysis-section {
    background: white;
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    border-left: 5px solid #e65100;
}
```
**使用ページ:** `goals.html`  
**説明:** 分析セクションの白背景、オレンジ系左境界線

### 19.16 分析ヘッダー <a id="1916-分析ヘッダー"></a>
```css
.analysis-header {
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid #e9ecef;
}
```
**使用ページ:** `goals.html`  
**説明:** 分析ヘッダーの下境界線

### 19.17 分析ヘッダーの見出し <a id="1917-分析ヘッダーの見出し"></a>
```css
.analysis-header h3 {
    color: #e65100;
    margin: 0;
    font-size: 1.4rem;
    font-weight: bold;
}
```
**使用ページ:** `goals.html`  
**説明:** 分析ヘッダーの見出しのオレンジ系色

### 19.18 分析コンテンツ <a id="1918-分析コンテンツ"></a>
```css
.analysis-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
}
```
**使用ページ:** `goals.html`  
**説明:** 分析コンテンツのCSS Grid、2列、ギャップ

### 19.19 分析アイテム <a id="1919-分析アイテム"></a>
```css
.analysis-item {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}
```
**使用ページ:** `goals.html`  
**説明:** 分析アイテムの白背景、角丸、シャドウ

### 19.20 分析アイテムの見出し <a id="1920-分析アイテムの見出し"></a>
```css
.analysis-item h4 {
    color: #2c3e50;
    font-size: 16px;
    margin: 0 0 15px 0;
    font-weight: bold;
}
```
**使用ページ:** `goals.html`  
**説明:** 分析アイテムの見出しの色指定、太字

### 19.21 分析アイテムのリスト <a id="1921-分析アイテムのリスト"></a>
```css
.analysis-item ul {
    margin: 0;
    padding-left: 20px;
}
```
**使用ページ:** `goals.html`  
**説明:** 分析アイテムのリストの左パディング、余白なし

### 19.22 分析アイテムのリスト項目 <a id="1922-分析アイテムのリスト項目"></a>
```css
.analysis-item li {
    font-size: 14px;
    line-height: 1.5;
    color: #495057;
    margin-bottom: 8px;
}
```
**使用ページ:** `goals.html`  
**説明:** 分析アイテムのリスト項目の小さな文字、行間調整、色指定

### 19.23 目標アクションエリア <a id="1923-目標アクションエリア"></a>
```css
.goals-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 30px;
    padding-top: 20px;
    border-top: 1px solid #dee2e6;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標アクションエリアのフレックスボックス、中央配置、折り返し、上境界線

### 19.24 目標アクションボタン <a id="1924-目標アクションボタン"></a>
```css
.print-btn,
.profile-btn,
.iwlm-btn,
.back-btn,
.update-btn,
.history-btn,
.current-goals-btn {
    padding: 12px 20px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
}
```
**使用ページ:** `goals.html`  
**説明:** 目標アクションボタンの統一されたスタイル、トランジション

### 19.25 印刷ボタン <a id="1925-印刷ボタン"></a>
```css
.print-btn {
    background: #28a745;
    color: white;
}
```
**使用ページ:** `goals.html`  
**説明:** 印刷ボタンの緑系背景

### 19.26 印刷ボタンのホバー状態 <a id="1926-印刷ボタンのホバー状態"></a>
```css
.print-btn:hover {
    background: #218838;
    transform: translateY(-2px);
}
```
**使用ページ:** `goals.html`  
**説明:** 印刷ボタンのホバー時の色変更と上移動

### 19.27 プロフィールボタン <a id="1927-プロフィールボタン"></a>
```css
.profile-btn {
    background: #007bff;
    color: white;
}
```
**使用ページ:** `goals.html`  
**説明:** プロフィールボタンの青系背景

### 19.28 プロフィールボタンのホバー状態 <a id="1928-プロフィールボタンのホバー状態"></a>
```css
.profile-btn:hover {
    background: #0056b3;
    color: white;
    transform: translateY(-2px);
}
```
**使用ページ:** `goals.html`  
**説明:** プロフィールボタンのホバー時の色変更と上移動

### 19.29 IWLMボタン <a id="1929-iwlmボタン"></a>
```css
.iwlm-btn {
    background: #17a2b8;
    color: white;
}
```
**使用ページ:** `goals.html`  
**説明:** IWLMボタンのティール系背景

### 19.30 IWLMボタンのホバー状態 <a id="1930-iwlmボタンのホバー状態"></a>
```css
.iwlm-btn:hover {
    background: #138496;
    color: white;
    transform: translateY(-2px);
}
```
**使用ページ:** `goals.html`  
**説明:** IWLMボタンのホバー時の色変更と上移動

### 19.31 戻るボタン <a id="1931-戻るボタン"></a>
```css
.back-btn {
    background: #6c757d;
    color: white;
}
```
**使用ページ:** `goals.html`  
**説明:** 戻るボタンのグレー系背景

### 19.32 戻るボタンのホバー状態 <a id="1932-戻るボタンのホバー状態"></a>
```css
.back-btn:hover {
    background: #5a6268;
    color: white;
    transform: translateY(-2px);
}
```
**使用ページ:** `goals.html`  
**説明:** 戻るボタンのホバー時の色変更と上移動

### 19.33 更新ボタン <a id="1933-更新ボタン"></a>
```css
.update-btn {
    background: #fd7e14;
    color: white;
}
```
**使用ページ:** `goals.html`  
**説明:** 更新ボタンのオレンジ系背景

### 19.34 更新ボタンのホバー状態 <a id="1934-更新ボタンのホバー状態"></a>
```css
.update-btn:hover {
    background: #e55a00;
    color: white;
    transform: translateY(-2px);
}
```
**使用ページ:** `goals.html`  
**説明:** 更新ボタンのホバー時の色変更と上移動

### 19.35 履歴ボタン <a id="1935-履歴ボタン"></a>
```css
.history-btn {
    background: #6f42c1;
    color: white;
}
```
**使用ページ:** `goals.html`  
**説明:** 履歴ボタンの紫系背景

### 19.36 履歴ボタンのホバー状態 <a id="1936-履歴ボタンのホバー状態"></a>
```css
.history-btn:hover {
    background: #5a2d91;
    color: white;
    transform: translateY(-2px);
}
```
**使用ページ:** `goals.html`  
**説明:** 履歴ボタンのホバー時の色変更と上移動

### 19.37 現在の目標ボタン <a id="1937-現在の目標ボタン"></a>
```css
.current-goals-btn {
    background: #20c997;
    color: white;
}
```
**使用ページ:** `goals.html`  
**説明:** 現在の目標ボタンのティール系背景

### 19.38 現在の目標ボタンのホバー状態 <a id="1938-現在の目標ボタンのホバー状態"></a>
```css
.current-goals-btn:hover {
    background: #1aa179;
    color: white;
    transform: translateY(-2px);
}
```
**使用ページ:** `goals.html`  
**説明:** 現在の目標ボタンのホバー時の色変更と上移動

---

## 20. 目標履歴ページ関連スタイル {#20-目標履歴ページ関連スタイル}

### 20.1 目標履歴ページ
```css
.goals-history-page {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 目標履歴ページの最大幅制限、中央配置

### 20.2 履歴情報
```css
.history-info {
    background: #e3f2fd;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    border-left: 4px solid #2196f3;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴情報の青系背景、左境界線

### 20.3 履歴アイテム
```css
.history-item {
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
    border-left: 5px solid #6f42c1;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴アイテムの白背景、角丸、シャドウ、紫系左境界線

### 20.4 履歴ヘッダー
```css
.history-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #eee;
    flex-wrap: wrap;
    gap: 10px;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴ヘッダーのフレックスボックス、両端揃え、下境界線、折り返し

### 20.5 履歴ヘッダーの見出し
```css
.history-header h3 {
    color: #6f42c1;
    margin: 0;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴ヘッダーの見出しの紫系色、余白なし

### 20.6 履歴日付
```css
.history-date {
    color: #666;
    font-size: 14px;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴日付のグレー色、小さな文字

### 20.7 履歴アクション
```css
.history-header .history-actions {
    display: flex;
    align-items: center;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴ヘッダーのアクションのフレックスボックス、中央揃え

### 20.8 履歴ヘッダーの削除ボタン
```css
.history-header .delete-btn {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
    transition: background-color 0.3s;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴ヘッダーの削除ボタンの赤系背景、小さなボタン

### 20.9 履歴ヘッダーの削除ボタンのホバー状態
```css
.history-header .delete-btn:hover {
    background-color: #c82333;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴ヘッダーの削除ボタンのホバー時の色変更

### 20.10 履歴コンテンツ
```css
.history-content {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 8px;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴コンテンツのグレー背景、角丸

### 20.11 履歴なし表示
```css
.no-history {
    text-align: center;
    padding: 40px;
    color: #666;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴なし表示の中央配置、グレー色

### 20.12 履歴アクションエリア
```css
.history-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-top: 30px;
    padding-top: 20px;
    border-top: 1px solid #dee2e6;
}
```
**使用ページ:** `goals_history.html`  
**説明:** 履歴アクションエリアのフレックスボックス、中央配置、上境界線

---

## 21. モーダル・招待コード関連スタイル {#21-モーダル招待コード関連スタイル}

### 21.1 モーダルオーバーレイ
```css
.modal {
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: none;
    /* 初期状態では非表示 */
}
```
**使用ページ:** 全ページ  
**説明:** モーダルオーバーレイの固定位置、全画面、半透明背景、デフォルト非表示

### 21.2 モーダルコンテンツ
```css
.modal-content {
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    width: 90%;
    max-width: 500px;
    max-height: 90vh;
    overflow-y: auto;
}
```
**使用ページ:** 全ページ  
**説明:** モーダルコンテンツの白背景、角丸、シャドウ、最大サイズ制限

### 21.3 モーダルヘッダー
```css
.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    border-bottom: 1px solid #eee;
}
```
**使用ページ:** 全ページ  
**説明:** モーダルヘッダーのフレックスボックス、両端揃え、下境界線

### 21.4 モーダルヘッダーの見出し
```css
.modal-header h3 {
    margin: 0;
    color: #333;
    font-size: 18px;
}
```
**使用ページ:** 全ページ  
**説明:** モーダルヘッダーの見出しの余白なし、色指定

### 21.5 モーダル閉じるボタン
```css
.close {
    color: #aaa;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
    line-height: 1;
}
```
**使用ページ:** 全ページ  
**説明:** モーダル閉じるボタンの大きな文字、太字、クリック可能

### 21.6 モーダル閉じるボタンのホバー・フォーカス状態
```css
.close:hover,
.close:focus {
    color: #000;
}
```
**使用ページ:** 全ページ  
**説明:** モーダル閉じるボタンのホバー・フォーカス時の色変更

### 21.7 モーダルボディ
```css
.modal-body {
    padding: 20px;
}
```
**使用ページ:** 全ページ  
**説明:** モーダルボディのパディング

### 21.8 モーダルボディの段落
```css
.modal-body p {
    margin: 0 0 15px 0;
    color: #666;
    line-height: 1.5;
}
```
**使用ページ:** 全ページ  
**説明:** モーダルボディの段落の余白、色指定、行間調整

### 21.9 モーダルフッター
```css
.modal-footer {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    padding: 20px;
    border-top: 1px solid #eee;
}
```
**使用ページ:** 全ページ  
**説明:** モーダルフッターのフレックスボックス、右揃え、ギャップ、上境界線

### 21.10 キャンセルボタン、確認ボタン
```css
.btn-cancel,
.btn-confirm {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    transition: background-color 0.3s;
}
```
**使用ページ:** 全ページ  
**説明:** キャンセルボタン、確認ボタンの統一されたスタイル、トランジション

### 21.11 キャンセルボタン
```css
.btn-cancel {
    background-color: #f5f5f5;
    color: #333;
}
```
**使用ページ:** 全ページ  
**説明:** キャンセルボタンのグレー系背景

### 21.12 キャンセルボタンのホバー状態
```css
.btn-cancel:hover {
    background-color: #e0e0e0;
}
```
**使用ページ:** 全ページ  
**説明:** キャンセルボタンのホバー時の色変更

### 21.13 確認ボタン
```css
.btn-confirm {
    background-color: #FF69B4;
    color: white;
}
```
**使用ページ:** 全ページ  
**説明:** 確認ボタンのピンク系背景

### 21.14 確認ボタンのホバー状態
```css
.btn-confirm:hover {
    background-color: #FF1493;
}
```
**使用ページ:** 全ページ  
**説明:** 確認ボタンのホバー時の色変更

### 21.15 招待コード発行セクション
```css
.invitation-section {
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 30px;
}
```
**使用ページ:** `user.html`  
**説明:** 招待コード発行セクションのグレー背景、境界線、角丸

### 21.16 招待コード発行セクションの見出し
```css
.invitation-section h3 {
    color: #333;
    margin: 0 0 10px 0;
    font-size: 18px;
}
```
**使用ページ:** `user.html`  
**説明:** 招待コード発行セクションの見出しの色指定、余白

### 21.17 招待コード発行セクションの段落
```css
.invitation-section p {
    color: #666;
    margin: 0 0 15px 0;
    line-height: 1.5;
}
```
**使用ページ:** `user.html`  
**説明:** 招待コード発行セクションの段落のグレー色、行間調整

### 21.18 招待ボタン
```css
.invitation-btn {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    transition: background-color 0.3s;
}
```
**使用ページ:** `user.html`  
**説明:** 招待ボタンの緑系背景、太字、ホバー効果

### 21.19 招待ボタンのホバー状態
```css
.invitation-btn:hover {
    background-color: #218838;
}
```
**使用ページ:** `user.html`  
**説明:** 招待ボタンのホバー時の色変更

### 21.20 招待ボタンの無効状態
```css
.invitation-btn:disabled {
    background-color: #6c757d;
    cursor: not-allowed;
}
```
**使用ページ:** `user.html`  
**説明:** 招待ボタンの無効時のグレー背景、クリック不可

### 21.21 招待コード表示エリア
```css
.invitation-code-display {
    background-color: #fff;
    border: 2px solid #28a745;
    border-radius: 8px;
    padding: 20px;
    margin-top: 15px;
}
```
**使用ページ:** `user.html`  
**説明:** 招待コード表示エリアの白背景、緑系境界線、角丸

### 21.22 招待コード表示エリアの見出し
```css
.invitation-code-display h4 {
    color: #28a745;
    margin: 0 0 15px 0;
    font-size: 16px;
}
```
**使用ページ:** `user.html`  
**説明:** 招待コード表示エリアの見出しの緑系色、余白

### 21.23 コードコンテナ
```css
.code-container {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}
```
**使用ページ:** `user.html`  
**説明:** コードコンテナのフレックスボックス、中央揃え、ギャップ

### 21.24 コードテキスト
```css
.code-text {
    font-family: 'Courier New', monospace;
    font-size: 24px;
    font-weight: bold;
    color: #333;
    background-color: #f8f9fa;
    padding: 10px 15px;
    border-radius: 5px;
    border: 1px solid #dee2e6;
    flex: 1;
}
```
**使用ページ:** `user.html`  
**説明:** コードテキストの等幅フォント、大きな文字、太字、背景色

### 21.25 コピーボタン
```css
.copy-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 12px;
    transition: background-color 0.3s;
}
```
**使用ページ:** `user.html`  
**説明:** コピーボタンの青系背景、小さな文字、ホバー効果

### 21.26 コピーボタンのホバー状態
```css
.copy-btn:hover {
    background-color: #0056b3;
}
```
**使用ページ:** `user.html`  
**説明:** コピーボタンのホバー時の色変更

### 21.27 有効期限テキスト
```css
.expires-text {
    color: #666;
    font-size: 14px;
    margin: 0 0 5px 0;
}
```
**使用ページ:** `user.html`  
**説明:** 有効期限テキストのグレー色、小さな文字

### 21.28 注意テキスト
```css
.note-text {
    color: #999;
    font-size: 12px;
    margin: 0;
    font-style: italic;
}
```
**使用ページ:** `user.html`  
**説明:** 注意テキストの薄いグレー色、小さな文字、斜体

### 21.29 レスポンシブ対応（モーダル）
```css
@media (max-width: 768px) {
    .modal-content {
        width: 95%;
        margin: 10px;
    }

    .code-container {
        flex-direction: column;
        align-items: stretch;
    }

    .code-text {
        text-align: center;
        font-size: 20px;
    }
}
```
**使用ページ:** 全ページ  
**説明:** モーダルの768px以下でのレスポンシブ対応

### 21.30 小画面用レスポンシブ対応
```css
@media (max-width: 480px) {

    .modal-header,
    .modal-body,
    .modal-footer {
        padding: 15px;
    }

    .code-text {
        font-size: 18px;
    }
}
```
**使用ページ:** 全ページ  
**説明:** モーダルの480px以下でのレスポンシブ対応

---

## 22. ツールチップスタイル {#22-ツールチップスタイル}

### 22.1 ユーザー名コンテナ
```css
.user-name-container {
    position: relative;
    display: inline-block;
}
```
**使用ページ:** 全ページ  
**説明:** ユーザー名コンテナの相対位置、インラインブロック

### 22.2 ツールチップ
```css
.tooltip {
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    margin-top: 8px;
    z-index: 1000;
}
```
**使用ページ:** 全ページ  
**説明:** ツールチップの絶対位置、中央配置、上部表示

### 22.3 ツールチップコンテンツ
```css
.tooltip-content {
    background-color: #333;
    color: white;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 12px;
    white-space: nowrap;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    position: relative;
}
```
**使用ページ:** 全ページ  
**説明:** ツールチップコンテンツの黒背景、白文字、角丸、シャドウ

### 22.4 ツールチップコンテンツの矢印
```css
.tooltip-content::after {
    content: '';
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    border: 5px solid transparent;
    border-bottom-color: #333;
}
```
**使用ページ:** 全ページ  
**説明:** ツールチップコンテンツの矢印の疑似要素、上向き

### 22.5 アニメーション
```css
.tooltip {
    animation: fadeInTooltip 0.3s ease-in-out;
}
```
**使用ページ:** 全ページ  
**説明:** ツールチップのフェードインアニメーション

### 22.6 フェードインアニメーション
```css
@keyframes fadeInTooltip {
    from {
        opacity: 0;
        transform: translateX(-50%) translateY(5px);
    }

    to {
        opacity: 1;
        transform: translateX(-50%) translateY(0);
    }
}
```
**使用ページ:** 全ページ  
**説明:** ツールチップの下から上へのフェードイン

### 22.7 レスポンシブ対応
```css
@media (max-width: 768px) {
    .tooltip-content {
        font-size: 11px;
        padding: 6px 10px;
    }
}
```
**使用ページ:** 全ページ  
**説明:** ツールチップの768px以下での小さな文字

---

## まとめ

第4部では、目標関連、モーダル、招待コード、ツールチップ関連のスタイリングを解説しました。

### 主要機能
1. **目標管理**: セクション別表示、分析機能、アクションボタン
2. **モーダル**: ポップアップ表示、確認ダイアログ
3. **招待コード**: 発行・表示・コピー機能
4. **ツールチップ**: ユーザーガイダンス
5. **アニメーション**: ホバー効果、フェードイン

### 技術的特徴
- **CSS Grid**: 分析コンテンツのレイアウト
- **Flexbox**: ボタン配置、ヘッダー配置
- **疑似要素**: ツールチップの矢印
- **アニメーション**: キーフレーム、トランジション
- **レスポンシブ**: モバイル対応

### デザインシステム
- **カラーパレット**: 各機能固有の色
- **タイポグラフィ**: 階層的な文字サイズ
- **スペーシング**: 統一された余白とパディング
- **ボーダー**: 角丸、シャドウの統一
- **アニメーション**: 0.3s easeのトランジション

このファイルは、アプリケーションの目標管理、モーダル機能、招待システム、ユーザーガイダンスの美しいデザインと使いやすさを提供しています。
