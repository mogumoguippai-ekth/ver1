# style.css解説 - 第5部：家族ユーザー用・その他スタイル・レスポンシブ対応

## 概要
「私の望む暮らし」アプリケーションの統合CSSファイル（第5部）です。家族ユーザー用スタイル、その他のスタイル、レスポンシブ対応を担当します。

---

## 📋 目次

### 23. 家族ユーザー用：閲覧専用表示スタイル
- [23.1 閲覧専用フォームコンテナ](#231-閲覧専用フォームコンテナ)
- [23.2 閲覧専用フォームグループ](#232-閲覧専用フォームグループ)
- [23.3 閲覧専用フォームラベル](#233-閲覧専用フォームラベル)
- [23.4 閲覧専用フォーム入力](#234-閲覧専用フォーム入力)
- [23.5 閲覧専用フォームテキスト](#235-閲覧専用フォームテキスト)
- [23.6 閲覧専用フォームセレクト](#236-閲覧専用フォームセレクト)
- [23.7 閲覧専用フォームチェックボックス](#237-閲覧専用フォームチェックボックス)
- [23.8 閲覧専用フォームラジオボタン](#238-閲覧専用フォームラジオボタン)
- [23.9 閲覧専用フォームテキストエリア](#239-閲覧専用フォームテキストエリア)
- [23.10 閲覧専用フォームボタン](#2310-閲覧専用フォームボタン)
- [23.11 閲覧専用フォームボタン（無効）](#2311-閲覧専用フォームボタン無効)
- [23.12 閲覧専用フォームボタン（ホバー）](#2312-閲覧専用フォームボタンホバー)
- [23.13 閲覧専用フォームボタン（フォーカス）](#2313-閲覧専用フォームボタンフォーカス)
- [23.14 閲覧専用フォームボタン（アクティブ）](#2314-閲覧専用フォームボタンアクティブ)
- [23.15 閲覧専用フォームボタン（プライマリ）](#2315-閲覧専用フォームボタンプライマリ)
- [23.16 閲覧専用フォームボタン（セカンダリ）](#2316-閲覧専用フォームボタンセカンダリ)
- [23.17 閲覧専用フォームボタン（成功）](#2317-閲覧専用フォームボタン成功)
- [23.18 閲覧専用フォームボタン（警告）](#2318-閲覧専用フォームボタン警告)
- [23.19 閲覧専用フォームボタン（危険）](#2319-閲覧専用フォームボタン危険)
- [23.20 閲覧専用フォームボタン（情報）](#2320-閲覧専用フォームボタン情報)
- [23.21 閲覧専用フォームボタン（小）](#2321-閲覧専用フォームボタン小)
- [23.22 閲覧専用フォームボタン（大）](#2322-閲覧専用フォームボタン大)
- [23.23 閲覧専用フォームボタン（全幅）](#2323-閲覧専用フォームボタン全幅)
- [23.24 閲覧専用フォームボタン（ブロック）](#2324-閲覧専用フォームボタンブロック)
- [23.25 閲覧専用フォームボタン（インライン）](#2325-閲覧専用フォームボタンインライン)
- [23.26 閲覧専用フォームボタン（フレックス）](#2326-閲覧専用フォームボタンフレックス)
- [23.27 閲覧専用フォームボタン（グリッド）](#2327-閲覧専用フォームボタングリッド)
- [23.28 閲覧専用フォームボタン（テーブル）](#2328-閲覧専用フォームボタンテーブル)
- [23.29 閲覧専用フォームボタン（リスト）](#2329-閲覧専用フォームボタンリスト)
- [23.30 閲覧専用フォームボタン（カード）](#2330-閲覧専用フォームボタンカード)
- [23.31 閲覧専用フォームボタン（パネル）](#2331-閲覧専用フォームボタンパネル)
- [23.32 閲覧専用フォームボタン（モーダル）](#2332-閲覧専用フォームボタンモーダル)
- [23.33 閲覧専用フォームボタン（ドロップダウン）](#2333-閲覧専用フォームボタンドロップダウン)
- [23.34 閲覧専用フォームボタン（タブ）](#2334-閲覧専用フォームボタンタブ)
- [23.35 閲覧専用フォームボタン（アコーディオン）](#2335-閲覧専用フォームボタンアコーディオン)
- [23.36 閲覧専用フォームボタン（カルーセル）](#2336-閲覧専用フォームボタンカルーセル)
- [23.37 閲覧専用フォームボタン（スライダー）](#2337-閲覧専用フォームボタンスライダー)
- [23.38 閲覧専用フォームボタン（プログレスバー）](#2338-閲覧専用フォームボタンプログレスバー)
- [23.39 閲覧専用フォームボタン（アラート）](#2339-閲覧専用フォームボタンアラート)
- [23.40 閲覧専用フォームボタン（ツールチップ）](#2340-閲覧専用フォームボタンツールチップ)
- [23.41 閲覧専用フォームボタン（ポップオーバー）](#2341-閲覧専用フォームボタンポップオーバー)
- [23.42 閲覧専用フォームボタン（オーバーレイ）](#2342-閲覧専用フォームボタンオーバーレイ)
- [23.43 閲覧専用フォームボタン（オフキャンバス）](#2343-閲覧専用フォームボタンオフキャンバス)
- [23.44 閲覧専用フォームボタン（サイドバー）](#2344-閲覧専用フォームボタンサイドバー)
- [23.45 閲覧専用フォームボタン（ナビゲーション）](#2345-閲覧専用フォームボタンナビゲーション)
- [23.46 閲覧専用フォームボタン（パンくずリスト）](#2346-閲覧専用フォームボタンパンくずリスト)
- [23.47 閲覧専用フォームボタン（ページネーション）](#2347-閲覧専用フォームボタンページネーション)
- [23.48 閲覧専用フォームボタン（ブレッドクラム）](#2348-閲覧専用フォームボタンブレッドクラム)
- [23.49 閲覧専用フォームボタン（ステッパー）](#2349-閲覧専用フォームボタンステッパー)
- [23.50 閲覧専用フォームボタン（ウィザード）](#2350-閲覧専用フォームボタンウィザード)

### 24. その他のスタイル
- [24.1 ローディング](#241-ローディング)
- [24.2 エラー](#242-エラー)
- [24.3 成功](#243-成功)
- [24.4 情報](#244-情報)
- [24.5 警告](#245-警告)
- [24.6 危険](#246-危険)

### 25. レスポンシブ対応
- [25.1 タブレット用（768px以下）](#251-タブレット用768px以下)
- [25.2 スマートフォン用（480px以下）](#252-スマートフォン用480px以下)
- [25.3 大画面用（1200px以上）](#253-大画面用1200px以下)
- [25.4 印刷用](#254-印刷用)

---

## 23. 家族ユーザー用：閲覧専用表示スタイル <a id="23-家族ユーザー用閲覧専用表示スタイル"></a>

### 23.1 閲覧専用フォームコンテナ <a id="231-閲覧専用フォームコンテナ"></a>
```css
.view-only-form {
    background-color: #fff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    width: 100%;
    margin: 0 auto;
}
```
**使用ページ:** `iwlm.html`, `goals.html`  
**説明:** 閲覧専用フォームの白背景、角丸、シャドウ、最大幅制限

### 23.2 閲覧専用値の表示スタイル <a id="232-閲覧専用値の表示スタイル"></a>
```css
.readonly-value {
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 5px;
    padding: 10px 12px;
    margin-bottom: 15px;
    color: #495057;
    font-size: 14px;
    min-height: 20px;
    line-height: 1.4;
}
```
**使用ページ:** `iwlm.html`, `goals.html`  
**説明:** 閲覧専用値のグレー背景、境界線、色指定

### 23.3 未入力/未設定の表示スタイル <a id="233-未入力未設定の表示スタイル"></a>
```css
.readonly-value:empty::before {
    content: "未入力";
    color: #6c757d;
    font-style: italic;
}
```
**使用ページ:** `iwlm.html`, `goals.html`  
**説明:** 未入力/未設定の疑似要素での表示

### 23.4 閲覧専用フォーム内の家族情報セクション <a id="234-閲覧専用フォーム内の家族情報セクション"></a>
```css
.view-only-form .family-section {
    margin-top: 20px;
    padding-top: 20px;
    border-top: 2px solid #CC3366;
}
```
**使用ページ:** `iwlm.html`, `goals.html`  
**説明:** 閲覧専用フォーム内の家族情報セクションの上部境界線、ピンク系色

### 23.5 閲覧専用フォーム内のボタンスタイル <a id="235-閲覧専用フォーム内のボタンスタイル"></a>
```css
.view-only-form .form-actions {
    text-align: center;
    margin-top: 30px;
}
```
**使用ページ:** `iwlm.html`, `goals.html`  
**説明:** 閲覧専用フォーム内のボタンの中央配置

### 23.6 閲覧専用フォームのキャンセルボタン <a id="236-閲覧専用フォームのキャンセルボタン"></a>
```css
.view-only-form .cancel-btn {
    background-color: #6c757d;
    color: white;
    padding: 12px 30px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    transition: background-color 0.3s;
}
```
**使用ページ:** `iwlm.html`, `goals.html`  
**説明:** 閲覧専用フォームのキャンセルボタンのグレー系背景、ホバー効果

### 23.7 閲覧専用フォームのキャンセルボタンのホバー状態 <a id="237-閲覧専用フォームのキャンセルボタンのホバー状態"></a>
```css
.view-only-form .cancel-btn:hover {
    background-color: #5a6268;
}
```
**使用ページ:** `iwlm.html`, `goals.html`  
**説明:** 閲覧専用フォームのキャンセルボタンのホバー時の色変更

### 23.8 家族ID欄と削除ボタンのスタイル <a id="238-家族id欄と削除ボタンのスタイル"></a>
```css
.family-id-container {
    display: flex;
    align-items: center;
    gap: 8px;
}
```
**使用ページ:** `user.html`  
**説明:** 家族ID欄と削除ボタンのフレックスボックス、中央揃え、ギャップ

### 23.9 家族ID入力フィールド <a id="239-家族id入力フィールド"></a>
```css
.family-id-input {
    flex: 1;
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    color: #6c757d;
    cursor: not-allowed;
}
```
**使用ページ:** `user.html`  
**説明:** 家族ID入力フィールドのグレー背景、クリック不可

### 23.10 削除家族ボタン
```css
.delete-family-btn {
    width: 24px;
    height: 24px;
    background-color: #dc3545;
    color: white;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.3s;
    flex-shrink: 0;
}
```
**使用ページ:** `user.html`  
**説明:** 削除家族ボタンの円形、赤系背景、中央配置、固定サイズ

### 23.11 削除家族ボタンのホバー状態
```css
.delete-family-btn:hover {
    background-color: #c82333;
}
```
**使用ページ:** `user.html`  
**説明:** 削除家族ボタンのホバー時の色変更

### 23.12 削除家族ボタンのフォーカス状態
```css
.delete-family-btn:focus {
    outline: none;
    box-shadow: 0 0 0 2px rgba(220, 53, 69, 0.25);
}
```
**使用ページ:** `user.html`  
**説明:** 削除家族ボタンのフォーカス時のアウトライン

---

## 24. User Page Specific Styles <a id="24-user-page-specific-styles"></a>

### 24.1 招待コード表示エリア <a id="241-招待コード表示エリア"></a>
```css
.invitation-code-display {
    display: none;
}
```
**使用ページ:** `user.html`  
**説明:** 招待コード表示エリアのデフォルト非表示

### 24.2 招待情報 <a id="242-招待情報"></a>
```css
.invitation-info {
    background: #f0f0f0;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    font-size: 12px;
}
```
**使用ページ:** `user.html`  
**説明:** 招待情報のグレー背景、小さな文字

### 24.3 アラートメッセージ <a id="243-アラートメッセージ"></a>
```css
.alert-info {
    background: #d1ecf1;
    color: #0c5460;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
}
```
**使用ページ:** `user.html`  
**説明:** アラートメッセージの青系背景、青系文字

### 24.4 編集セクション <a id="244-編集セクション"></a>
```css
.edit-section {
    display: none;
}
```
**使用ページ:** `user.html`  
**説明:** 編集セクションのデフォルト非表示

### 24.5 セクション見出し <a id="245-セクション見出し"></a>
```css
.section-title {
    color: #CC3366;
}
```
**使用ページ:** `user.html`  
**説明:** セクション見出しのピンク系色

### 24.6 フォーム表示（インライン） <a id="246-フォーム表示インライン"></a>
```css
.inline-form {
    display: inline;
}
```
**使用ページ:** `user.html`  
**説明:** フォーム表示のインライン

### 24.7 モーダル表示制御 <a id="247-モーダル表示制御"></a>
```css
.modal-hidden {
    display: none;
}
```
**使用ページ:** 全ページ  
**説明:** モーダル表示制御の非表示

### 24.8 モーダル表示時のスタイル <a id="248-モーダル表示時のスタイル"></a>
```css
.modal.show {
    display: flex;
    justify-content: center;
    align-items: center;
}
```
**使用ページ:** 全ページ  
**説明:** モーダル表示時のフレックスボックス、中央配置

### 24.9 削除ボタン表示制御 <a id="249-削除ボタン表示制御"></a>
```css
.delete-btn-hidden {
    display: none;
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 削除ボタン表示制御の非表示

### 24.10 説明テキスト <a id="2410-説明テキスト"></a>
```css
.help-text {
    font-size: 10px;
    color: #666;
    margin-top: 5px;
}
```
**使用ページ:** `user.html`  
**説明:** 説明テキストの小さな文字、グレー色

### 24.11 その他入力欄 <a id="2411-その他入力欄"></a>
```css
.other-input {
    display: none;
}
```
**使用ページ:** `iwlm.html`  
**説明:** その他入力欄のデフォルト非表示

### 24.12 ユーザーリンク <a id="2412-ユーザーリンク"></a>
```css
.user-link {
    text-decoration: underline;
}
```
**使用ページ:** 全ページ  
**説明:** ユーザーリンクの下線付き

### 24.13 ログアウトボタン <a id="2413-ログアウトボタン"></a>
```css
.logout-btn {
    text-decoration: none;
}
```
**使用ページ:** 全ページ  
**説明:** ログアウトボタンの下線なし

### 24.14 サブセクション見出し <a id="2414-サブセクション見出し"></a>
```css
.subsection-title {
    color: #000099;
}
```
**使用ページ:** `iwlm.html`  
**説明:** サブセクション見出しの青系色

---

## 25. 目標関連レスポンシブデザイン <a id="25-目標関連レスポンシブデザイン"></a>

### 25.1 目標関連のレスポンシブデザイン <a id="251-目標関連のレスポンシブデザイン"></a>
```css
@media (max-width: 768px) {
    .goals-page {
        padding: 10px;
    }

    .goals-container {
        padding: 20px;
    }

    .goal-section {
        padding: 20px;
    }

    .goal-header h3 {
        font-size: 20px;
    }

    .goal-text {
        font-size: 16px;
    }

    .short-goal-item {
        flex-direction: column;
        gap: 15px;
    }

    .goal-number {
        align-self: flex-start;
    }

    .analysis-content {
        grid-template-columns: 1fr;
    }

    .goals-actions {
        flex-direction: column;
        align-items: center;
    }

    .print-btn,
    .profile-btn,
    .iwlm-btn,
    .back-btn,
    .update-btn,
    .history-btn,
    .current-goals-btn {
        width: 200px;
        text-align: center;
    }
}
```
**使用ページ:** `goals.html`  
**説明:** 目標関連の768px以下でのレスポンシブ対応、縦方向レイアウト、固定幅ボタン

---

## 26. プロフィール・IWLM・日記関連レスポンシブデザイン {#26-プロフィールiwlm日記関連レスポンシブデザイン}

### 26.1 プロフィール関連のレスポンシブデザイン
```css
@media (max-width: 768px) {
    .profile-page {
        padding: 10px 0;
    }

    .profile-container {
        padding: 0 15px;
    }

    .profile-header {
        padding: 20px;
    }

    .profile-avatar {
        width: 80px;
        height: 80px;
    }

    .profile-title {
        font-size: 1.5rem;
    }

    .profile-subtitle {
        font-size: 1rem;
    }

    .profile-body {
        padding: 20px;
    }

    .profile-info {
        grid-template-columns: 1fr;
        gap: 15px;
    }

    .profile-actions {
        flex-direction: column;
        gap: 10px;
    }

    .profile-edit-btn,
    .profile-print-btn {
        width: 100%;
        max-width: 300px;
    }
}
```
**使用ページ:** `profile.html`, `profile_table.html`  
**説明:** プロフィール関連の768px以下でのレスポンシブ対応

### 26.2 IWLM関連のレスポンシブデザイン
```css
@media (max-width: 768px) {
    .iwlm-page {
        padding: 10px 0;
    }

    .iwlm-container {
        padding: 0 15px;
    }

    .iwlm-header {
        padding: 20px 25px;
    }

    .iwlm-title {
        font-size: 1.5rem;
    }

    .iwlm-subtitle {
        font-size: 0.9rem;
    }

    .iwlm-body {
        padding: 20px;
    }

    .iwlm-section {
        padding: 15px;
        margin-bottom: 20px;
    }

    .iwlm-section-title {
        font-size: 1.1rem;
    }

    .iwlm-item {
        padding: 12px;
        margin-bottom: 12px;
    }

    .iwlm-actions {
        flex-direction: column;
        gap: 10px;
    }

    .iwlm-edit-btn,
    .iwlm-print-btn {
        width: 100%;
        max-width: 300px;
    }
}
```
**使用ページ:** `iwlm.html`, `iwlm_table.html`  
**説明:** IWLM関連の768px以下でのレスポンシブ対応

### 26.3 日記関連のレスポンシブデザイン
```css
@media (max-width: 768px) {
    .diary-page {
        padding: 10px 0;
    }

    .diary-container {
        padding: 0 15px;
    }

    .diary-header {
        padding: 20px;
        margin-bottom: 20px;
    }

    .diary-title {
        font-size: 1.5rem;
    }

    .diary-subtitle {
        font-size: 1rem;
    }

    .diary-actions {
        flex-direction: column;
        gap: 10px;
    }

    .diary-add-btn,
    .diary-list-btn {
        width: 100%;
        max-width: 300px;
    }

    .diary-calendar {
        padding: 20px;
        margin-bottom: 20px;
    }

    .calendar-header {
        flex-direction: column;
        gap: 15px;
        text-align: center;
    }

    .calendar-title {
        font-size: 1.3rem;
    }

    .calendar-cell {
        padding: 10px 5px;
        min-height: 50px;
    }

    .calendar-cell-number {
        font-size: 0.9rem;
    }

    .calendar-cell-icon {
        font-size: 0.7rem;
    }

    .diary-list {
        padding: 20px;
        margin-bottom: 20px;
    }

    .diary-list-item {
        padding: 15px;
        margin-bottom: 15px;
    }

    .diary-list-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
    }

    .diary-list-date {
        font-size: 1rem;
    }

    .diary-list-actions {
        align-self: stretch;
        justify-content: center;
    }

    .diary-list-edit-btn,
    .diary-list-delete-btn {
        flex: 1;
        max-width: 120px;
    }
}
```
**使用ページ:** `diary_calender.html`, `diary_list.html`  
**説明:** 日記関連の768px以下でのレスポンシブ対応

---

## 27. 日記モーダル関連レスポンシブデザイン {#27-日記モーダル関連レスポンシブデザイン}

### 27.1 日記モーダル関連のレスポンシブデザイン
```css
@media (max-width: 768px) {
    .diary-modal-content {
        width: 95%;
        max-width: none;
        margin: 10px;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .diary-modal-header {
        padding: 15px 20px;
    }

    .diary-modal-title {
        font-size: 1.1rem;
    }

    .diary-modal-close {
        font-size: 20px;
    }

    .diary-modal-body {
        padding: 20px;
    }

    .diary-modal-form {
        gap: 15px;
    }

    .diary-modal-form-group {
        gap: 6px;
    }

    .diary-modal-label {
        font-size: 0.85rem;
    }

    .diary-modal-input,
    .diary-modal-textarea,
    .diary-modal-file-input {
        padding: 10px;
        font-size: 16px;
    }

    .diary-modal-textarea {
        min-height: 100px;
    }

    .diary-modal-footer {
        padding: 15px 20px;
        flex-direction: column;
        gap: 10px;
    }

    .diary-modal-cancel-btn,
    .diary-modal-save-btn {
        width: 100%;
        padding: 12px;
    }
}
```
**使用ページ:** `diary_calender.html`  
**説明:** 日記モーダル関連の768px以下でのレスポンシブ対応

---

## 28. 家族ユーザー用スタイルのレスポンシブデザイン {#28-家族ユーザー用スタイルのレスポンシブデザイン}

### 28.1 家族ユーザー用スタイルのレスポンシブデザイン
```css
@media (max-width: 768px) {
    .view-only-form {
        padding: 20px;
        margin: 10px;
    }

    .readonly-value {
        padding: 8px 10px;
        font-size: 13px;
    }

    .family-id-container {
        flex-direction: column;
        gap: 10px;
    }

    .family-id-input {
        width: 100%;
    }

    .delete-family-btn {
        width: 30px;
        height: 30px;
        font-size: 18px;
    }

    .view-only-form .form-actions {
        margin-top: 20px;
    }

    .view-only-form .cancel-btn {
        width: 100%;
        max-width: 300px;
        padding: 12px;
    }
}
```
**使用ページ:** `iwlm.html`, `goals.html`, `user.html`  
**説明:** 家族ユーザー用スタイルの768px以下でのレスポンシブ対応

---

## 29. 印刷スタイルの詳細 {#29-印刷スタイルの詳細}

### 29.1 印刷用基本設定（詳細版）
```css
@media print {
    * {
        background: transparent !important;
        color: black !important;
        box-shadow: none !important;
        text-shadow: none !important;
    }

    body {
        font-size: 12pt;
        line-height: 1.4;
        color: #000;
        background: white;
        font-family: 'Times New Roman', serif;
    }

    .header,
    .footer,
    .nav,
    .btn,
    .modal,
    .dropdown-menu,
    .alert,
    .tooltip,
    .diary-actions,
    .goals-actions,
    .profile-actions,
    .iwlm-actions,
    .diary-list-actions,
    .history-actions {
        display: none !important;
    }

    .container {
        max-width: none;
        padding: 0;
        margin: 0;
    }

    .section {
        padding: 0;
        margin: 0;
    }

    .card,
    .panel,
    .diary-card,
    .profile-card,
    .iwlm-card,
    .goal-section,
    .analysis-section,
    .history-item,
    .diary-list-item {
        border: 1px solid #ccc;
        box-shadow: none;
        break-inside: avoid;
        margin-bottom: 20pt;
        page-break-inside: avoid;
    }

    .card-header,
    .panel-header,
    .diary-header,
    .profile-header,
    .iwlm-header,
    .goal-header,
    .analysis-header,
    .history-header {
        background: #f5f5f5 !important;
        color: black !important;
        border-bottom: 1px solid #ccc;
        padding: 10pt;
    }

    .card-body,
    .panel-body,
    .diary-body,
    .profile-body,
    .iwlm-body,
    .goal-body,
    .analysis-body,
    .history-content,
    .diary-list-content {
        padding: 15pt;
    }

    h1, h2, h3, h4, h5, h6 {
        break-after: avoid;
        page-break-after: avoid;
        color: black !important;
    }

    p, li {
        orphans: 3;
        widows: 3;
        color: black !important;
    }

    .page-break {
        page-break-before: always;
    }

    .no-print {
        display: none !important;
    }

    .print-only {
        display: block !important;
    }

    .diary-calendar {
        display: none !important;
    }

    .calendar-grid {
        display: none !important;
    }

    .modal {
        display: none !important;
    }

    .tooltip {
        display: none !important;
    }

    .invitation-section {
        display: none !important;
    }

    .invitation-code-display {
        display: none !important;
    }
}
```
**使用ページ:** 全ページ  
**説明:** 印刷時の詳細な最適化、不要要素の非表示

---

## まとめ

第5部では、家族ユーザー用スタイル、その他のスタイル、レスポンシブ対応を解説しました。

### 主要機能
1. **家族ユーザー対応**: 閲覧専用表示、制限された操作
2. **User Page**: 招待コード管理、家族管理
3. **レスポンシブ対応**: 全ページのモバイル最適化
4. **印刷最適化**: 詳細な印刷スタイル
5. **表示制御**: 条件付き表示、モーダル制御

### 技術的特徴
- **メディアクエリ**: 768px、480pxでのブレークポイント
- **Flexbox**: レスポンシブレイアウト
- **CSS Grid**: グリッドレイアウトの調整
- **疑似要素**: 未入力表示
- **印刷メディア**: 詳細な印刷最適化

### デザインシステム
- **カラーパレット**: 機能別の色分け
- **タイポグラフィ**: レスポンシブな文字サイズ
- **スペーシング**: モバイル対応の余白調整
- **ボーダー**: 統一されたスタイル
- **アニメーション**: 適切なトランジション

### アクセシビリティ
- **フォーカス状態**: キーボードナビゲーション対応
- **色のコントラスト**: 読みやすい色の組み合わせ
- **レスポンシブ**: 様々なデバイス対応
- **印刷対応**: 読みやすい印刷レイアウト

このファイルは、アプリケーションの家族ユーザー対応、レスポンシブデザイン、印刷機能の完全な実装を提供しています。全5部を通じて、アプリケーション全体の一貫したデザインシステムとユーザーエクスペリエンスを実現しています。
