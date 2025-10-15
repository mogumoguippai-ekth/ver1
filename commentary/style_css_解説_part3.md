# style.css解説 - 第3部：プロフィール・IWLM・日記関連スタイル

## 概要
「私の望む暮らし」アプリケーションの統合CSSファイル（第3部）です。プロフィール、IWLM（I Want to Live My Life）、日記関連のスタイリングを担当します。

---

## 📋 目次

### 15. プロフィール関連スタイル
- [15.1 プロフィールページ](#151-プロフィールページ)
- [15.2 プロフィールコンテナ](#152-プロフィールコンテナ)
- [15.3 プロフィールカード](#153-プロフィールカード)
- [15.4 プロフィールヘッダー](#154-プロフィールヘッダー)
- [15.5 プロフィールアバター](#155-プロフィールアバター)
- [15.6 プロフィールタイトル](#156-プロフィールタイトル)
- [15.7 プロフィールサブタイトル](#157-プロフィールサブタイトル)
- [15.8 プロフィールボディ](#158-プロフィールボディ)
- [15.9 プロフィールセクション](#159-プロフィールセクション)
- [15.10 プロフィールセクションタイトル](#1510-プロフィールセクションタイトル)
- [15.11 プロフィール情報](#1511-プロフィール情報)
- [15.12 プロフィール情報アイテム](#1512-プロフィール情報アイテム)
- [15.13 プロフィール情報値](#1513-プロフィール情報値)
- [15.14 プロフィールアクション](#1514-プロフィールアクション)
- [15.15 プロフィール編集ボタン](#1515-プロフィール編集ボタン)
- [15.16 プロフィール印刷ボタン](#1516-プロフィール印刷ボタン)

### 16. IWLM関連スタイル
- [16.1 IWLMページ](#161-iwlmページ)

### 17. 日記関連スタイル
- [17.1 日記ページ](#171-日記ページ)

### 18. 日記モーダル関連スタイル
- [18.1 日記モーダル](#181-日記モーダル)

---

## 15. プロフィール関連スタイル <a id="15-プロフィール関連スタイル"></a>

### 15.1 プロフィールページ <a id="151-プロフィールページ"></a>
```css
.profile-page {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px 0;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールページの背景グラデーション

### 15.2 プロフィールコンテナ <a id="152-プロフィールコンテナ"></a>
```css
.profile-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 20px;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールの最大幅制限

### 15.3 プロフィールカード <a id="153-プロフィールカード"></a>
```css
.profile-card {
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    margin-bottom: 30px;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールカードの基本スタイル

### 15.4 プロフィールヘッダー <a id="154-プロフィールヘッダー"></a>
```css
.profile-header {
    background: linear-gradient(135deg, #FF5192 0%, #FF1493 100%);
    color: white;
    padding: 30px;
    text-align: center;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールヘッダーのグラデーション背景

### 15.5 プロフィールアバター <a id="155-プロフィールアバター"></a>
```css
.profile-avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 4px solid white;
    margin: 0 auto 20px;
    display: block;
    object-fit: cover;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールアバターの円形スタイル

### 15.6 プロフィールタイトル <a id="156-プロフィールタイトル"></a>
```css
.profile-title {
    font-size: 2rem;
    margin: 0 0 10px 0;
    font-weight: bold;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールタイトルのスタイル

### 15.7 プロフィールサブタイトル <a id="157-プロフィールサブタイトル"></a>
```css
.profile-subtitle {
    font-size: 1.1rem;
    margin: 0;
    opacity: 0.9;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールサブタイトルのスタイル

### 15.8 プロフィールボディ <a id="158-プロフィールボディ"></a>
```css
.profile-body {
    padding: 30px;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールボディのパディング

### 15.9 プロフィールセクション <a id="159-プロフィールセクション"></a>
```css
.profile-section {
    margin-bottom: 30px;
    padding-bottom: 20px;
    border-bottom: 1px solid #e9ecef;
}

.profile-section:last-child {
    border-bottom: none;
    margin-bottom: 0;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールセクションの区切り

### 15.10 プロフィールセクションタイトル <a id="1510-プロフィールセクションタイトル"></a>
```css
.profile-section-title {
    font-size: 1.3rem;
    color: #2c3e50;
    margin-bottom: 15px;
    font-weight: bold;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールセクションタイトルのスタイル

### 15.11 プロフィール情報 <a id="1511-プロフィール情報"></a>
```css
.profile-info {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィール情報のグリッドレイアウト

### 15.12 プロフィール情報アイテム <a id="1512-プロフィール情報アイテム"></a>
```css
.profile-info-item {
    display: flex;
    flex-direction: column;
}

.profile-info-label {
    font-weight: bold;
    color: #666;
    margin-bottom: 5px;
    font-size: 0.9rem;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィール情報アイテムのスタイル

### 15.13 プロフィール情報値 <a id="1513-プロフィール情報値"></a>
```css
.profile-info-value {
    color: #333;
    font-size: 1rem;
    line-height: 1.4;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィール情報値のスタイル

### 15.14 プロフィールアクション <a id="1514-プロフィールアクション"></a>
```css
.profile-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 30px;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィールアクションの配置

### 15.15 プロフィール編集ボタン <a id="1515-プロフィール編集ボタン"></a>
```css
.profile-edit-btn {
    background: linear-gradient(135deg, #FF5192 0%, #FF1493 100%);
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.profile-edit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 81, 146, 0.4);
    color: white;
    text-decoration: none;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィール編集ボタンのスタイル

### 15.16 プロフィール印刷ボタン <a id="1516-プロフィール印刷ボタン"></a>
```css
.profile-print-btn {
    background: #28a745;
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.profile-print-btn:hover {
    background: #218838;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(40, 167, 69, 0.4);
    color: white;
    text-decoration: none;
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィール印刷ボタンのスタイル

---

## 16. IWLM関連スタイル <a id="16-iwlm関連スタイル"></a>

### 16.1 IWLMページ <a id="161-iwlmページ"></a>
```css
.iwlm-page {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    min-height: 100vh;
    padding: 20px 0;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMページの背景グラデーション

### 16.2 IWLMコンテナ
```css
.iwlm-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 20px;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMの最大幅制限

### 16.3 IWLMカード
```css
.iwlm-card {
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    margin-bottom: 30px;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMカードの基本スタイル

### 16.4 IWLMヘッダー
```css
.iwlm-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 25px 30px;
    text-align: center;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMヘッダーのグラデーション背景

### 16.5 IWLMタイトル
```css
.iwlm-title {
    font-size: 1.8rem;
    margin: 0 0 10px 0;
    font-weight: bold;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMタイトルのスタイル

### 16.6 IWLMサブタイトル
```css
.iwlm-subtitle {
    font-size: 1rem;
    margin: 0;
    opacity: 0.9;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMサブタイトルのスタイル

### 16.7 IWLMボディ
```css
.iwlm-body {
    padding: 30px;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMボディのパディング

### 16.8 IWLMセクション
```css
.iwlm-section {
    margin-bottom: 25px;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 10px;
    border-left: 4px solid #667eea;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMセクションのスタイル、左境界線

### 16.9 IWLMセクションタイトル
```css
.iwlm-section-title {
    font-size: 1.2rem;
    color: #2c3e50;
    margin-bottom: 15px;
    font-weight: bold;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMセクションタイトルのスタイル

### 16.10 IWLM項目
```css
.iwlm-item {
    margin-bottom: 15px;
    padding: 15px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLM項目のスタイル

### 16.11 IWLM項目ラベル
```css
.iwlm-item-label {
    font-weight: bold;
    color: #667eea;
    margin-bottom: 8px;
    font-size: 0.9rem;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLM項目ラベルのスタイル

### 16.12 IWLM項目値
```css
.iwlm-item-value {
    color: #333;
    line-height: 1.5;
    font-size: 1rem;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLM項目値のスタイル

### 16.13 IWLMアクション
```css
.iwlm-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 30px;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLMアクションの配置

### 16.14 IWLM編集ボタン
```css
.iwlm-edit-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.iwlm-edit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    color: white;
    text-decoration: none;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLM編集ボタンのスタイル

### 16.15 IWLM印刷ボタン
```css
.iwlm-print-btn {
    background: #28a745;
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.iwlm-print-btn:hover {
    background: #218838;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(40, 167, 69, 0.4);
    color: white;
    text-decoration: none;
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLM印刷ボタンのスタイル

---

## 17. 日記関連スタイル <a id="17-日記関連スタイル"></a>

### 17.1 日記ページ <a id="171-日記ページ"></a>
```css
.diary-page {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    min-height: 100vh;
    padding: 20px 0;
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記ページの背景グラデーション

### 17.2 日記コンテナ
```css
.diary-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記の最大幅制限

### 17.3 日記ヘッダー
```css
.diary-header {
    background: white;
    border-radius: 15px;
    padding: 25px 30px;
    margin-bottom: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    text-align: center;
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記ヘッダーのスタイル

### 17.4 日記タイトル
```css
.diary-title {
    font-size: 2rem;
    color: #2c3e50;
    margin: 0 0 10px 0;
    font-weight: bold;
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記タイトルのスタイル

### 17.5 日記サブタイトル
```css
.diary-subtitle {
    font-size: 1.1rem;
    color: #7f8c8d;
    margin: 0;
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記サブタイトルのスタイル

### 17.6 日記アクション
```css
.diary-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 20px;
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記アクションの配置

### 17.7 日記追加ボタン
```css
.diary-add-btn {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    color: #2c3e50;
    padding: 12px 25px;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.diary-add-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(168, 237, 234, 0.4);
    color: #2c3e50;
    text-decoration: none;
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記追加ボタンのスタイル

### 17.8 日記リストボタン
```css
.diary-list-btn {
    background: #17a2b8;
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.diary-list-btn:hover {
    background: #138496;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(23, 162, 184, 0.4);
    color: white;
    text-decoration: none;
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記リストボタンのスタイル

### 17.9 日記カレンダー
```css
.diary-calendar {
    background: white;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    margin-bottom: 30px;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記カレンダーのスタイル

### 17.10 カレンダーヘッダー
```css
.calendar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid #e9ecef;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダーヘッダーの配置

### 17.11 カレンダータイトル
```css
.calendar-title {
    font-size: 1.5rem;
    color: #2c3e50;
    margin: 0;
    font-weight: bold;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダータイトルのスタイル

### 17.12 カレンダーナビゲーション
```css
.calendar-nav {
    display: flex;
    gap: 10px;
    align-items: center;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダーナビゲーションの配置

### 17.13 カレンダーナビゲーションボタン
```css
.calendar-nav-btn {
    background: #6c757d;
    color: white;
    border: none;
    border-radius: 50%;
    width: 35px;
    height: 35px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}

.calendar-nav-btn:hover {
    background: #5a6268;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダーナビゲーションボタンのスタイル

### 17.14 カレンダーグリッド
```css
.calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 1px;
    background: #e9ecef;
    border-radius: 8px;
    overflow: hidden;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダーグリッドのスタイル

### 17.15 カレンダーセル
```css
.calendar-cell {
    background: white;
    padding: 15px 10px;
    text-align: center;
    min-height: 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダーセルのスタイル

### 17.16 カレンダーセルのホバー効果
```css
.calendar-cell:hover {
    background: #f8f9fa;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダーセルのホバー効果

### 17.17 カレンダーセル（日記あり）
```css
.calendar-cell.has-diary {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    color: #2c3e50;
    font-weight: bold;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記がある日のセルのスタイル

### 17.18 カレンダーセル（今日）
```css
.calendar-cell.today {
    background: #FF5192;
    color: white;
    font-weight: bold;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 今日のセルのスタイル

### 17.19 カレンダーセル（他の月）
```css
.calendar-cell.other-month {
    background: #f8f9fa;
    color: #adb5bd;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 他の月のセルのスタイル

### 17.20 カレンダーセル（日曜日）
```css
.calendar-cell.sunday {
    color: #dc3545;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日曜日のセルのスタイル

### 17.21 カレンダーセル（土曜日）
```css
.calendar-cell.saturday {
    color: #007bff;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 土曜日のセルのスタイル

### 17.22 カレンダーセル番号
```css
.calendar-cell-number {
    font-size: 1rem;
    margin-bottom: 5px;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダーセル番号のスタイル

### 17.23 カレンダーセルアイコン
```css
.calendar-cell-icon {
    font-size: 0.8rem;
    opacity: 0.7;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** カレンダーセルアイコンのスタイル

### 17.24 日記リスト
```css
.diary-list {
    background: white;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    margin-bottom: 30px;
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リストのスタイル

### 17.25 日記リストアイテム
```css
.diary-list-item {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    border-left: 4px solid #a8edea;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.diary-list-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リストアイテムのスタイル

### 17.26 日記リストヘッダー
```css
.diary-list-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
    flex-wrap: wrap;
    gap: 10px;
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リストヘッダーの配置

### 17.27 日記リスト日付
```css
.diary-list-date {
    font-size: 1.1rem;
    color: #2c3e50;
    font-weight: bold;
    margin: 0;
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リスト日付のスタイル

### 17.28 日記リストアクション
```css
.diary-list-actions {
    display: flex;
    gap: 10px;
    align-items: center;
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リストアクションの配置

### 17.29 日記リスト編集ボタン
```css
.diary-list-edit-btn {
    background: #17a2b8;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 8px 12px;
    font-size: 0.9rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.diary-list-edit-btn:hover {
    background: #138496;
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リスト編集ボタンのスタイル

### 17.30 日記リスト削除ボタン
```css
.diary-list-delete-btn {
    background: #dc3545;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 8px 12px;
    font-size: 0.9rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.diary-list-delete-btn:hover {
    background: #c82333;
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リスト削除ボタンのスタイル

### 17.31 日記リストコンテンツ
```css
.diary-list-content {
    color: #333;
    line-height: 1.6;
    margin-bottom: 15px;
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リストコンテンツのスタイル

### 17.32 日記リスト画像
```css
.diary-list-image {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin-top: 15px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
```
**使用ページ:** `diary_list.html`  
**説明:** 日記リスト画像のスタイル

---

## 18. 日記モーダル関連スタイル <a id="18-日記モーダル関連スタイル"></a>

### 18.1 日記モーダル <a id="181-日記モーダル"></a>
```css
.diary-modal {
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: none;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルの基本スタイル

### 18.2 日記モーダルコンテンツ
```css
.diary-modal-content {
    background-color: white;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    width: 90%;
    max-width: 600px;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルコンテンツのスタイル

### 18.3 日記モーダルヘッダー
```css
.diary-modal-header {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    color: #2c3e50;
    padding: 20px 25px;
    border-radius: 15px 15px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルヘッダーのスタイル

### 18.4 日記モーダルタイトル
```css
.diary-modal-title {
    font-size: 1.3rem;
    margin: 0;
    font-weight: bold;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルタイトルのスタイル

### 18.5 日記モーダル閉じるボタン
```css
.diary-modal-close {
    color: #2c3e50;
    font-size: 24px;
    font-weight: bold;
    cursor: pointer;
    line-height: 1;
    transition: color 0.3s ease;
}

.diary-modal-close:hover {
    color: #FF5192;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダル閉じるボタンのスタイル

### 18.6 日記モーダルボディ
```css
.diary-modal-body {
    padding: 25px;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルボディのパディング

### 18.7 日記モーダルフォーム
```css
.diary-modal-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルフォームの配置

### 18.8 日記モーダルフォームグループ
```css
.diary-modal-form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルフォームグループの配置

### 18.9 日記モーダルラベル
```css
.diary-modal-label {
    font-weight: bold;
    color: #2c3e50;
    font-size: 0.9rem;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルラベルのスタイル

### 18.10 日記モーダル入力
```css
.diary-modal-input {
    padding: 12px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
}

.diary-modal-input:focus {
    outline: none;
    border-color: #a8edea;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダル入力のスタイル

### 18.11 日記モーダルテキストエリア
```css
.diary-modal-textarea {
    padding: 12px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    font-size: 1rem;
    resize: vertical;
    min-height: 120px;
    transition: border-color 0.3s ease;
}

.diary-modal-textarea:focus {
    outline: none;
    border-color: #a8edea;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルテキストエリアのスタイル

### 18.12 日記モーダルファイル入力
```css
.diary-modal-file-input {
    padding: 12px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    font-size: 1rem;
    background: white;
    cursor: pointer;
    transition: border-color 0.3s ease;
}

.diary-modal-file-input:focus {
    outline: none;
    border-color: #a8edea;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルファイル入力のスタイル

### 18.13 日記モーダルフッター
```css
.diary-modal-footer {
    display: flex;
    justify-content: flex-end;
    gap: 15px;
    padding: 20px 25px;
    border-top: 1px solid #e9ecef;
    background: #f8f9fa;
    border-radius: 0 0 15px 15px;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルフッターの配置

### 18.14 日記モーダルキャンセルボタン
```css
.diary-modal-cancel-btn {
    background: #6c757d;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 20px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.diary-modal-cancel-btn:hover {
    background: #5a6268;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダルキャンセルボタンのスタイル

### 18.15 日記モーダル保存ボタン
```css
.diary-modal-save-btn {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    color: #2c3e50;
    border: none;
    border-radius: 8px;
    padding: 12px 20px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
}

.diary-modal-save-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(168, 237, 234, 0.4);
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダル保存ボタンのスタイル

---

## まとめ

第3部では、プロフィール、IWLM、日記関連のスタイリングを解説しました。

### 主要機能
1. **プロフィール**: カードレイアウト、アバター、情報表示
2. **IWLM**: セクション別表示、項目管理、アクションボタン
3. **日記**: カレンダー表示、リスト表示、モーダル編集
4. **アニメーション**: ホバー効果、トランジション
5. **レスポンシブ**: モバイル対応、柔軟なレイアウト

### 技術的特徴
- **CSS Grid**: カレンダー、情報表示のレイアウト
- **Flexbox**: ボタン配置、ヘッダー配置
- **グラデーション**: 視覚的なアクセント
- **モーダル**: 日記編集のポップアップ
- **ホバー効果**: インタラクティブな要素

### デザインシステム
- **カラーパレット**: 各ページ固有のグラデーション
- **タイポグラフィ**: 階層的な文字サイズ
- **スペーシング**: 統一された余白とパディング
- **ボーダー**: 角丸、シャドウの統一
- **アニメーション**: 0.3s easeのトランジション

このファイルは、アプリケーションの主要機能であるプロフィール、IWLM、日記の美しいデザインと使いやすさを提供しています。
