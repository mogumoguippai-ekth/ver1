# style.css解説 - 第1部：基本スタイル・レイアウト・ナビゲーション・フォーム関連

## 概要
「私の望む暮らし」アプリケーションの統合CSSファイル（第1部）です。基本スタイル、レイアウト、ナビゲーション、フォーム関連のスタイリングを担当します。

---

## 📋 目次

### 1. 基本スタイル・リセット
- [1.1 全体リセット](#11-全体リセット)
- [1.2 ボディスタイル](#12-ボディスタイル)
- [1.3 リンクスタイル](#13-リンクスタイル)
- [1.4 見出しスタイル](#14-見出しスタイル)
- [1.5 段落スタイル](#15-段落スタイル)
- [1.6 リストスタイル](#16-リストスタイル)

### 2. レイアウト・コンテナ
- [2.1 メインコンテナ](#21-メインコンテナ)
- [2.2 フルワイドコンテナ](#22-フルワイドコンテナ)
- [2.3 セクション](#23-セクション)
- [2.4 セクション（小）](#24-セクション小)
- [2.5 セクション（大）](#25-セクション大)
- [2.6 フレックスボックス](#26-フレックスボックス)
- [2.7 グリッド](#27-グリッド)

### 3. ヘッダー・ナビゲーション
- [3.1 ヘッダー](#31-ヘッダー)
- [3.2 ヘッダーコンテナ](#32-ヘッダーコンテナ)
- [3.3 ロゴ](#33-ロゴ)
- [3.4 ナビゲーション](#34-ナビゲーション)
- [3.5 ナビゲーションアイテム](#35-ナビゲーションアイテム)
- [3.6 ナビゲーションリンク](#36-ナビゲーションリンク)
- [3.7 ユーザーメニュー](#37-ユーザーメニュー)
- [3.8 ユーザーメニューボタン](#38-ユーザーメニューボタン)
- [3.9 ドロップダウンメニュー](#39-ドロップダウンメニュー)
- [3.10 ドロップダウンメニューの表示](#310-ドロップダウンメニューの表示)
- [3.11 ドロップダウンアイテム](#311-ドロップダウンアイテム)
- [3.12 ドロップダウンセパレータ](#312-ドロップダウンセパレータ)

### 4. フッター
- [4.1 フッター](#41-フッター)
- [4.2 フッターコンテナ](#42-フッターコンテナ)
- [4.3 フッターリンク](#43-フッターリンク)

### 5. ボタン・フォーム要素
- [5.1 ボタン（基本）](#51-ボタン基本)
- [5.2 ボタン（セカンダリ）](#52-ボタンセカンダリ)
- [5.3 ボタン（成功）](#53-ボタン成功)
- [5.4 ボタン（警告）](#54-ボタン警告)
- [5.5 ボタン（危険）](#55-ボタン危険)
- [5.6 ボタン（小）](#56-ボタン小)
- [5.7 ボタン（大）](#57-ボタン大)
- [5.8 ボタン（全幅）](#58-ボタン全幅)
- [5.9 ボタン（無効）](#59-ボタン無効)

### 6. フォーム要素
- [6.1 フォームグループ](#61-フォームグループ)
- [6.2 フォームラベル](#62-フォームラベル)
- [6.3 フォーム入力](#63-フォーム入力)
- [6.4 フォーム入力（エラー）](#64-フォーム入力エラー)
- [6.5 フォーム入力（有効）](#65-フォーム入力有効)
- [6.6 フォームテキスト](#66-フォームテキスト)
- [6.7 フォームテキスト（エラー）](#67-フォームテキストエラー)
- [6.8 フォームテキスト（成功）](#68-フォームテキスト成功)
- [6.9 チェックボックス・ラジオボタン](#69-チェックボックスラジオボタン)
- [6.10 セレクトボックス](#610-セレクトボックス)
- [6.11 テキストエリア](#611-テキストエリア)

### 7. カード・パネル
- [7.1 カード](#71-カード)
- [7.2 カードヘッダー](#72-カードヘッダー)
- [7.3 カードボディ](#73-カードボディ)
- [7.4 カードフッター](#74-カードフッター)
- [7.5 パネル](#75-パネル)
- [7.6 パネルヘッダー](#76-パネルヘッダー)
- [7.7 パネルボディ](#77-パネルボディ)

### 8. アラート・メッセージ
- [8.1 アラート](#81-アラート)
- [8.2 アラート（成功）](#82-アラート成功)
- [8.3 アラート（情報）](#83-アラート情報)
- [8.4 アラート（警告）](#84-アラート警告)
- [8.5 アラート（危険）](#85-アラート危険)
- [8.6 アラート閉じるボタン](#86-アラート閉じるボタン)

### 9. ユーティリティクラス
- [9.1 テキスト関連](#91-テキスト関連)
- [9.2 背景色関連](#92-背景色関連)
- [9.3 余白関連](#93-余白関連)
- [9.4 表示関連](#94-表示関連)
- [9.5 位置関連](#95-位置関連)

---

## 1. 基本スタイル・リセット

### 1.1 全体リセット <a id="11-全体リセット"></a>
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```
**使用ページ:** 全ページ  
**説明:** 全要素のマージン・パディングをリセット、ボックスサイズをborder-boxに統一

### 1.2 ボディスタイル <a id="12-ボディスタイル"></a>
```css
body {
    font-family: 'Arial', 'ヒラギノ角ゴ ProN', 'Hiragino Kaku Gothic ProN', 'メイリオ', 'Meiryo', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f9fa;
}
```
**使用ページ:** 全ページ  
**説明:** フォント指定、行間調整、文字色、背景色

### 1.3 リンクスタイル <a id="13-リンクスタイル"></a>
```css
a {
    color: #FF5192;
    text-decoration: none;
    transition: color 0.3s ease;
}

a:hover {
    color: #FF1493;
}
```
**使用ページ:** 全ページ  
**説明:** ピンク系色、ホバー効果

### 1.4 見出しスタイル <a id="14-見出しスタイル"></a>
```css
h1, h2, h3, h4, h5, h6 {
    margin-bottom: 1rem;
    font-weight: bold;
}
```
**使用ページ:** 全ページ  
**説明:** 見出しの統一スタイル

### 1.5 段落スタイル <a id="15-段落スタイル"></a>
```css
p {
    margin-bottom: 1rem;
}
```
**使用ページ:** 全ページ  
**説明:** 段落の余白

### 1.6 リストスタイル <a id="16-リストスタイル"></a>
```css
ul, ol {
    margin-bottom: 1rem;
    padding-left: 2rem;
}
```
**使用ページ:** 全ページ  
**説明:** リストの余白とインデント

---

## 2. レイアウト・コンテナ <a id="2-レイアウトコンテナ"></a>

### 2.1 メインコンテナ <a id="21-メインコンテナ"></a>
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```
**使用ページ:** 全ページ  
**説明:** 最大幅制限、中央配置、左右パディング

### 2.2 フルワイドコンテナ <a id="22-フルワイドコンテナ"></a>
```css
.container-full {
    width: 100%;
    padding: 0 20px;
}
```
**使用ページ:** 全ページ  
**説明:** 全幅、左右パディング

### 2.3 セクション <a id="23-セクション"></a>
```css
.section {
    padding: 60px 0;
}
```
**使用ページ:** 全ページ  
**説明:** セクションの上下パディング

### 2.4 セクション（小） <a id="24-セクション小"></a>
```css
.section-sm {
    padding: 40px 0;
}
```
**使用ページ:** 全ページ  
**説明:** 小さいセクションのパディング

### 2.5 セクション（大） <a id="25-セクション大"></a>
```css
.section-lg {
    padding: 80px 0;
}
```
**使用ページ:** 全ページ  
**説明:** 大きいセクションのパディング

### 2.6 フレックスボックス <a id="26-フレックスボックス"></a>
```css
.flex {
    display: flex;
}

.flex-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

.flex-between {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.flex-column {
    display: flex;
    flex-direction: column;
}
```
**使用ページ:** 全ページ  
**説明:** フレックスボックスのユーティリティクラス

### 2.7 グリッド <a id="27-グリッド"></a>
```css
.grid {
    display: grid;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```
**使用ページ:** 全ページ  
**説明:** CSS Gridのユーティリティクラス

---

## 3. ヘッダー・ナビゲーション <a id="3-ヘッダーナビゲーション"></a>

### 3.1 ヘッダー <a id="31-ヘッダー"></a>
```css
.header {
    background: linear-gradient(135deg, #FF5192 0%, #FF1493 100%);
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}
```
**使用ページ:** 全ページ  
**説明:** ピンク系グラデーション、固定位置、シャドウ

### 3.2 ヘッダーコンテナ <a id="32-ヘッダーコンテナ"></a>
```css
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```
**使用ページ:** 全ページ  
**説明:** ヘッダー内のフレックスボックス

### 3.3 ロゴ <a id="33-ロゴ"></a>
```css
.logo {
    font-size: 1.8rem;
    font-weight: bold;
    color: white;
    text-decoration: none;
}
```
**使用ページ:** 全ページ  
**説明:** ロゴのスタイル

### 3.4 ナビゲーション <a id="34-ナビゲーション"></a>
```css
.nav {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
}
```
**使用ページ:** 全ページ  
**説明:** ナビゲーションリスト

### 3.5 ナビゲーションアイテム <a id="35-ナビゲーションアイテム"></a>
```css
.nav-item {
    margin-left: 2rem;
}
```
**使用ページ:** 全ページ  
**説明:** ナビゲーションアイテムの間隔

### 3.6 ナビゲーションリンク <a id="36-ナビゲーションリンク"></a>
```css
.nav-link {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
    padding: 0.5rem 1rem;
    border-radius: 5px;
}

.nav-link:hover {
    color: #FFB6C1;
    background-color: rgba(255, 255, 255, 0.1);
}
```
**使用ページ:** 全ページ  
**説明:** ナビゲーションリンクのスタイルとホバー効果

### 3.7 ユーザーメニュー <a id="37-ユーザーメニュー"></a>
```css
.user-menu {
    position: relative;
    display: inline-block;
}
```
**使用ページ:** 全ページ  
**説明:** ユーザーメニューの相対位置

### 3.8 ユーザーメニューボタン <a id="38-ユーザーメニューボタン"></a>
```css
.user-menu-btn {
    background: none;
    border: none;
    color: white;
    font-size: 1rem;
    cursor: pointer;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.user-menu-btn:hover {
    background-color: rgba(255, 255, 255, 0.1);
}
```
**使用ページ:** 全ページ  
**説明:** ユーザーメニューボタンのスタイル

### 3.9 ドロップダウンメニュー <a id="39-ドロップダウンメニュー"></a>
```css
.dropdown-menu {
    position: absolute;
    top: 100%;
    right: 0;
    background: white;
    min-width: 200px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    border-radius: 8px;
    padding: 0.5rem 0;
    display: none;
    z-index: 1001;
}
```
**使用ページ:** 全ページ  
**説明:** ドロップダウンメニューの絶対位置、シャドウ

### 3.10 ドロップダウンメニューの表示 <a id="310-ドロップダウンメニューの表示"></a>
```css
.dropdown-menu.show {
    display: block;
}
```
**使用ページ:** 全ページ  
**説明:** ドロップダウンメニューの表示制御

### 3.11 ドロップダウンアイテム <a id="311-ドロップダウンアイテム"></a>
```css
.dropdown-item {
    display: block;
    padding: 0.75rem 1rem;
    color: #333;
    text-decoration: none;
    transition: background-color 0.3s ease;
}

.dropdown-item:hover {
    background-color: #f8f9fa;
}
```
**使用ページ:** 全ページ  
**説明:** ドロップダウンアイテムのスタイルとホバー効果

### 3.12 ドロップダウンセパレータ <a id="312-ドロップダウンセパレータ"></a>
```css
.dropdown-divider {
    height: 1px;
    background-color: #e9ecef;
    margin: 0.5rem 0;
}
```
**使用ページ:** 全ページ  
**説明:** ドロップダウンの区切り線

---

## 4. フッター <a id="4-フッター"></a>

### 4.1 フッター <a id="41-フッター"></a>
```css
.footer {
    background-color: #343a40;
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: auto;
}
```
**使用ページ:** 全ページ  
**説明:** フッターの背景色、中央配置、上部マージン

### 4.2 フッターコンテナ <a id="42-フッターコンテナ"></a>
```css
.footer-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```
**使用ページ:** 全ページ  
**説明:** フッターコンテナの最大幅制限

### 4.3 フッターリンク <a id="43-フッターリンク"></a>
```css
.footer-link {
    color: #adb5bd;
    text-decoration: none;
    margin: 0 1rem;
    transition: color 0.3s ease;
}

.footer-link:hover {
    color: white;
}
```
**使用ページ:** 全ページ  
**説明:** フッターリンクのスタイルとホバー効果

---

## 5. ボタン・フォーム要素 <a id="5-ボタンフォーム要素"></a>

### 5.1 ボタン（基本） <a id="51-ボタン基本"></a>
```css
.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background-color: #FF5192;
    color: white;
    text-decoration: none;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 500;
    text-align: center;
    transition: all 0.3s ease;
}

.btn:hover {
    background-color: #FF1493;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(255, 81, 146, 0.3);
}
```
**使用ページ:** 全ページ  
**説明:** 基本ボタンのスタイル、ホバー効果、アニメーション

### 5.2 ボタン（セカンダリ） <a id="52-ボタンセカンダリ"></a>
```css
.btn-secondary {
    background-color: #6c757d;
    color: white;
}

.btn-secondary:hover {
    background-color: #5a6268;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(108, 117, 125, 0.3);
}
```
**使用ページ:** 全ページ  
**説明:** セカンダリボタンのスタイル

### 5.3 ボタン（成功） <a id="53-ボタン成功"></a>
```css
.btn-success {
    background-color: #28a745;
    color: white;
}

.btn-success:hover {
    background-color: #218838;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
}
```
**使用ページ:** 全ページ  
**説明:** 成功ボタンのスタイル

### 5.4 ボタン（警告） <a id="54-ボタン警告"></a>
```css
.btn-warning {
    background-color: #ffc107;
    color: #212529;
}

.btn-warning:hover {
    background-color: #e0a800;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(255, 193, 7, 0.3);
}
```
**使用ページ:** 全ページ  
**説明:** 警告ボタンのスタイル

### 5.5 ボタン（危険） <a id="55-ボタン危険"></a>
```css
.btn-danger {
    background-color: #dc3545;
    color: white;
}

.btn-danger:hover {
    background-color: #c82333;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(220, 53, 69, 0.3);
}
```
**使用ページ:** 全ページ  
**説明:** 危険ボタンのスタイル

### 5.6 ボタン（小） <a id="56-ボタン小"></a>
```css
.btn-sm {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
}
```
**使用ページ:** 全ページ  
**説明:** 小さいボタンのスタイル

### 5.7 ボタン（大） <a id="57-ボタン大"></a>
```css
.btn-lg {
    padding: 1rem 2rem;
    font-size: 1.125rem;
}
```
**使用ページ:** 全ページ  
**説明:** 大きいボタンのスタイル

### 5.8 ボタン（全幅） <a id="58-ボタン全幅"></a>
```css
.btn-block {
    width: 100%;
    display: block;
}
```
**使用ページ:** 全ページ  
**説明:** 全幅ボタンのスタイル

### 5.9 ボタン（無効） <a id="59-ボタン無効"></a>
```css
.btn:disabled {
    background-color: #6c757d;
    cursor: not-allowed;
    opacity: 0.6;
}

.btn:disabled:hover {
    transform: none;
    box-shadow: none;
}
```
**使用ページ:** 全ページ  
**説明:** 無効ボタンのスタイル

---

## 6. フォーム要素 <a id="6-フォーム要素"></a>

### 6.1 フォームグループ <a id="61-フォームグループ"></a>
```css
.form-group {
    margin-bottom: 1.5rem;
}
```
**使用ページ:** 全ページ  
**説明:** フォームグループの余白

### 6.2 フォームラベル <a id="62-フォームラベル"></a>
```css
.form-label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #333;
}
```
**使用ページ:** 全ページ  
**説明:** フォームラベルのスタイル

### 6.3 フォーム入力 <a id="63-フォーム入力"></a>
```css
.form-control {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ced4da;
    border-radius: 5px;
    font-size: 1rem;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-control:focus {
    outline: none;
    border-color: #FF5192;
    box-shadow: 0 0 0 3px rgba(255, 81, 146, 0.1);
}
```
**使用ページ:** 全ページ  
**説明:** フォーム入力のスタイル、フォーカス効果

### 6.4 フォーム入力（エラー） <a id="64-フォーム入力エラー"></a>
```css
.form-control.is-invalid {
    border-color: #dc3545;
}

.form-control.is-invalid:focus {
    border-color: #dc3545;
    box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.1);
}
```
**使用ページ:** 全ページ  
**説明:** エラー状態のフォーム入力

### 6.5 フォーム入力（有効） <a id="65-フォーム入力有効"></a>
```css
.form-control.is-valid {
    border-color: #28a745;
}

.form-control.is-valid:focus {
    border-color: #28a745;
    box-shadow: 0 0 0 3px rgba(40, 167, 69, 0.1);
}
```
**使用ページ:** 全ページ  
**説明:** 有効状態のフォーム入力

### 6.6 フォームテキスト <a id="66-フォームテキスト"></a>
```css
.form-text {
    font-size: 0.875rem;
    color: #6c757d;
    margin-top: 0.25rem;
}
```
**使用ページ:** 全ページ  
**説明:** フォームの説明テキスト

### 6.7 フォームテキスト（エラー） <a id="67-フォームテキストエラー"></a>
```css
.form-text.text-danger {
    color: #dc3545;
}
```
**使用ページ:** 全ページ  
**説明:** エラーメッセージのスタイル

### 6.8 フォームテキスト（成功） <a id="68-フォームテキスト成功"></a>
```css
.form-text.text-success {
    color: #28a745;
}
```
**使用ページ:** 全ページ  
**説明:** 成功メッセージのスタイル

### 6.9 チェックボックス・ラジオボタン <a id="69-チェックボックスラジオボタン"></a>
```css
.form-check {
    display: flex;
    align-items: center;
    margin-bottom: 0.5rem;
}

.form-check-input {
    margin-right: 0.5rem;
}

.form-check-label {
    margin-bottom: 0;
    cursor: pointer;
}
```
**使用ページ:** 全ページ  
**説明:** チェックボックス・ラジオボタンのスタイル

### 6.10 セレクトボックス <a id="610-セレクトボックス"></a>
```css
.form-select {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ced4da;
    border-radius: 5px;
    font-size: 1rem;
    background-color: white;
    cursor: pointer;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-select:focus {
    outline: none;
    border-color: #FF5192;
    box-shadow: 0 0 0 3px rgba(255, 81, 146, 0.1);
}
```
**使用ページ:** 全ページ  
**説明:** セレクトボックスのスタイル

### 6.11 テキストエリア <a id="611-テキストエリア"></a>
```css
.form-textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ced4da;
    border-radius: 5px;
    font-size: 1rem;
    resize: vertical;
    min-height: 100px;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-textarea:focus {
    outline: none;
    border-color: #FF5192;
    box-shadow: 0 0 0 3px rgba(255, 81, 146, 0.1);
}
```
**使用ページ:** 全ページ  
**説明:** テキストエリアのスタイル

---

## 7. カード・パネル <a id="7-カードパネル"></a>

### 7.1 カード <a id="71-カード"></a>
```css
.card {
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}
```
**使用ページ:** 全ページ  
**説明:** カードの基本スタイル、ホバー効果

### 7.2 カードヘッダー <a id="72-カードヘッダー"></a>
```css
.card-header {
    background: linear-gradient(135deg, #FF5192 0%, #FF1493 100%);
    color: white;
    padding: 1rem 1.5rem;
    font-weight: bold;
}
```
**使用ページ:** 全ページ  
**説明:** カードヘッダーのグラデーション背景

### 7.3 カードボディ <a id="73-カードボディ"></a>
```css
.card-body {
    padding: 1.5rem;
}
```
**使用ページ:** 全ページ  
**説明:** カードボディのパディング

### 7.4 カードフッター <a id="74-カードフッター"></a>
```css
.card-footer {
    background-color: #f8f9fa;
    padding: 1rem 1.5rem;
    border-top: 1px solid #e9ecef;
}
```
**使用ページ:** 全ページ  
**説明:** カードフッターの背景色と境界線

### 7.5 パネル <a id="75-パネル"></a>
```css
.panel {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 1.5rem;
}
```
**使用ページ:** 全ページ  
**説明:** パネルの基本スタイル

### 7.6 パネルヘッダー <a id="76-パネルヘッダー"></a>
```css
.panel-header {
    background-color: #f8f9fa;
    padding: 1rem 1.5rem;
    border-bottom: 1px solid #e9ecef;
    font-weight: bold;
    color: #333;
}
```
**使用ページ:** 全ページ  
**説明:** パネルヘッダーの背景色と境界線

### 7.7 パネルボディ <a id="77-パネルボディ"></a>
```css
.panel-body {
    padding: 1.5rem;
}
```
**使用ページ:** 全ページ  
**説明:** パネルボディのパディング

---

## 8. アラート・メッセージ <a id="8-アラートメッセージ"></a>

### 8.1 アラート <a id="81-アラート"></a>
```css
.alert {
    padding: 1rem 1.5rem;
    border-radius: 5px;
    margin-bottom: 1rem;
    border: 1px solid transparent;
}
```
**使用ページ:** 全ページ  
**説明:** アラートの基本スタイル

### 8.2 アラート（成功） <a id="82-アラート成功"></a>
```css
.alert-success {
    background-color: #d4edda;
    border-color: #c3e6cb;
    color: #155724;
}
```
**使用ページ:** 全ページ  
**説明:** 成功アラートのスタイル

### 8.3 アラート（情報） <a id="83-アラート情報"></a>
```css
.alert-info {
    background-color: #d1ecf1;
    border-color: #bee5eb;
    color: #0c5460;
}
```
**使用ページ:** 全ページ  
**説明:** 情報アラートのスタイル

### 8.4 アラート（警告） <a id="84-アラート警告"></a>
```css
.alert-warning {
    background-color: #fff3cd;
    border-color: #ffeaa7;
    color: #856404;
}
```
**使用ページ:** 全ページ  
**説明:** 警告アラートのスタイル

### 8.5 アラート（危険） <a id="85-アラート危険"></a>
```css
.alert-danger {
    background-color: #f8d7da;
    border-color: #f5c6cb;
    color: #721c24;
}
```
**使用ページ:** 全ページ  
**説明:** 危険アラートのスタイル

### 8.6 アラート閉じるボタン <a id="86-アラート閉じるボタン"></a>
```css
.alert-close {
    float: right;
    font-size: 1.5rem;
    font-weight: bold;
    line-height: 1;
    color: inherit;
    background: none;
    border: none;
    cursor: pointer;
    opacity: 0.5;
    transition: opacity 0.3s ease;
}

.alert-close:hover {
    opacity: 1;
}
```
**使用ページ:** 全ページ  
**説明:** アラート閉じるボタンのスタイル

---

## 9. ユーティリティクラス <a id="9-ユーティリティクラス"></a>

### 9.1 テキスト関連 <a id="91-テキスト関連"></a>
```css
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }
.text-justify { text-align: justify; }

.text-muted { color: #6c757d; }
.text-primary { color: #FF5192; }
.text-success { color: #28a745; }
.text-info { color: #17a2b8; }
.text-warning { color: #ffc107; }
.text-danger { color: #dc3545; }

.font-weight-bold { font-weight: bold; }
.font-weight-normal { font-weight: normal; }
.font-italic { font-style: italic; }

.text-uppercase { text-transform: uppercase; }
.text-lowercase { text-transform: lowercase; }
.text-capitalize { text-transform: capitalize; }
```
**使用ページ:** 全ページ  
**説明:** テキストの配置、色、太さ、スタイル、変換のユーティリティ

### 9.2 背景色関連 <a id="92-背景色関連"></a>
```css
.bg-primary { background-color: #FF5192; }
.bg-secondary { background-color: #6c757d; }
.bg-success { background-color: #28a745; }
.bg-info { background-color: #17a2b8; }
.bg-warning { background-color: #ffc107; }
.bg-danger { background-color: #dc3545; }
.bg-light { background-color: #f8f9fa; }
.bg-dark { background-color: #343a40; }
.bg-white { background-color: white; }
```
**使用ページ:** 全ページ  
**説明:** 背景色のユーティリティ

### 9.3 余白関連 <a id="93-余白関連"></a>
```css
.m-0 { margin: 0; }
.m-1 { margin: 0.25rem; }
.m-2 { margin: 0.5rem; }
.m-3 { margin: 1rem; }
.m-4 { margin: 1.5rem; }
.m-5 { margin: 3rem; }

.mt-0 { margin-top: 0; }
.mt-1 { margin-top: 0.25rem; }
.mt-2 { margin-top: 0.5rem; }
.mt-3 { margin-top: 1rem; }
.mt-4 { margin-top: 1.5rem; }
.mt-5 { margin-top: 3rem; }

.mb-0 { margin-bottom: 0; }
.mb-1 { margin-bottom: 0.25rem; }
.mb-2 { margin-bottom: 0.5rem; }
.mb-3 { margin-bottom: 1rem; }
.mb-4 { margin-bottom: 1.5rem; }
.mb-5 { margin-bottom: 3rem; }

.ml-0 { margin-left: 0; }
.ml-1 { margin-left: 0.25rem; }
.ml-2 { margin-left: 0.5rem; }
.ml-3 { margin-left: 1rem; }
.ml-4 { margin-left: 1.5rem; }
.ml-5 { margin-left: 3rem; }

.mr-0 { margin-right: 0; }
.mr-1 { margin-right: 0.25rem; }
.mr-2 { margin-right: 0.5rem; }
.mr-3 { margin-right: 1rem; }
.mr-4 { margin-right: 1.5rem; }
.mr-5 { margin-right: 3rem; }

.p-0 { padding: 0; }
.p-1 { padding: 0.25rem; }
.p-2 { padding: 0.5rem; }
.p-3 { padding: 1rem; }
.p-4 { padding: 1.5rem; }
.p-5 { padding: 3rem; }

.pt-0 { padding-top: 0; }
.pt-1 { padding-top: 0.25rem; }
.pt-2 { padding-top: 0.5rem; }
.pt-3 { padding-top: 1rem; }
.pt-4 { padding-top: 1.5rem; }
.pt-5 { padding-top: 3rem; }

.pb-0 { padding-bottom: 0; }
.pb-1 { padding-bottom: 0.25rem; }
.pb-2 { padding-bottom: 0.5rem; }
.pb-3 { padding-bottom: 1rem; }
.pb-4 { padding-bottom: 1.5rem; }
.pb-5 { padding-bottom: 3rem; }

.pl-0 { padding-left: 0; }
.pl-1 { padding-left: 0.25rem; }
.pl-2 { padding-left: 0.5rem; }
.pl-3 { padding-left: 1rem; }
.pl-4 { padding-left: 1.5rem; }
.pl-5 { padding-left: 3rem; }

.pr-0 { padding-right: 0; }
.pr-1 { padding-right: 0.25rem; }
.pr-2 { padding-right: 0.5rem; }
.pr-3 { padding-right: 1rem; }
.pr-4 { padding-right: 1.5rem; }
.pr-5 { padding-right: 3rem; }
```
**使用ページ:** 全ページ  
**説明:** マージンとパディングのユーティリティクラス

### 9.4 表示関連 <a id="94-表示関連"></a>
```css
.d-none { display: none; }
.d-block { display: block; }
.d-inline { display: inline; }
.d-inline-block { display: inline-block; }
.d-flex { display: flex; }
.d-grid { display: grid; }

.visible { visibility: visible; }
.invisible { visibility: hidden; }

.opacity-0 { opacity: 0; }
.opacity-25 { opacity: 0.25; }
.opacity-50 { opacity: 0.5; }
.opacity-75 { opacity: 0.75; }
.opacity-100 { opacity: 1; }
```
**使用ページ:** 全ページ  
**説明:** 表示と可視性のユーティリティクラス

### 9.5 位置関連 <a id="95-位置関連"></a>
```css
.position-static { position: static; }
.position-relative { position: relative; }
.position-absolute { position: absolute; }
.position-fixed { position: fixed; }
.position-sticky { position: sticky; }

.float-left { float: left; }
.float-right { float: right; }
.float-none { float: none; }

.clearfix::after {
    content: "";
    display: table;
    clear: both;
}
```
**使用ページ:** 全ページ  
**説明:** 位置とフロートのユーティリティクラス

---

## まとめ

第1部では、アプリケーションの基本スタイル、レイアウト、ナビゲーション、フォーム関連のスタイリングを解説しました。

### 主要機能
1. **基本スタイル**: リセット、フォント、色の統一
2. **レイアウト**: コンテナ、セクション、フレックスボックス、グリッド
3. **ナビゲーション**: ヘッダー、メニュー、ドロップダウン
4. **フォーム**: 入力フィールド、ボタン、バリデーション
5. **コンポーネント**: カード、パネル、アラート
6. **ユーティリティ**: テキスト、背景、余白、表示制御

### 技術的特徴
- **レスポンシブ対応**: モバイルファーストデザイン
- **アニメーション**: ホバー効果、トランジション
- **アクセシビリティ**: フォーカス状態、色のコントラスト
- **保守性**: ユーティリティクラス、統一された命名規則

このファイルは、アプリケーション全体の一貫したデザインシステムの基盤を提供しています。
