# style.css解説 - 第2部：レスポンシブデザイン・印刷スタイル・ダッシュボード関連

## 概要
「私の望む暮らし」アプリケーションの統合CSSファイル（第2部）です。レスポンシブデザイン、印刷スタイル、ダッシュボード関連のスタイリングを担当します。

---

## 📋 目次

### 10. レスポンシブデザイン
- [10.1 タブレット用（768px以下）](#101-タブレット用768px以下)
- [10.2 スマートフォン用（480px以下）](#102-スマートフォン用480px以下)
- [10.3 大画面用（1200px以上）](#103-大画面用1200px以上)

### 11. 印刷スタイル
- [11.1 印刷用基本設定](#111-印刷用基本設定)
- [11.2 A4サイズ最適化](#112-a4サイズ最適化)

### 12. ダッシュボード関連スタイル
- [12.1 ダッシュボードページ](#121-ダッシュボードページ)
- [12.2 ダッシュボードコンテナ](#122-ダッシュボードコンテナ)
- [12.3 ダッシュボードヘッダー](#123-ダッシュボードヘッダー)
- [12.4 ダッシュボードタイトル](#124-ダッシュボードタイトル)
- [12.5 ダッシュボードサブタイトル](#125-ダッシュボードサブタイトル)
- [12.6 ダッシュボードグリッド](#126-ダッシュボードグリッド)
- [12.7 ダッシュボードカード](#127-ダッシュボードカード)
- [12.8 ダッシュボードカードのホバー効果](#128-ダッシュボードカードのホバー効果)
- [12.9 ダッシュボードカードヘッダー](#129-ダッシュボードカードヘッダー)
- [12.10 ダッシュボードカードタイトル](#1210-ダッシュボードカードタイトル)
- [12.11 ダッシュボードカードコンテンツ](#1211-ダッシュボードカードコンテンツ)
- [12.12 ダッシュボードカードアクション](#1212-ダッシュボードカードアクション)
- [12.13 ダッシュボード統計](#1213-ダッシュボード統計)
- [12.14 ダッシュボード統計アイテム](#1214-ダッシュボード統計アイテム)
- [12.15 ダッシュボード統計値](#1215-ダッシュボード統計値)
- [12.16 ダッシュボード統計ラベル](#1216-ダッシュボード統計ラベル)
- [12.17 ダッシュボードアクション](#1217-ダッシュボードアクション)
- [12.18 ダッシュボードアクションボタン](#1218-ダッシュボードアクションボタン)

### 13. ダッシュボードレスポンシブデザイン
- [13.1 ダッシュボードタブレット用（768px以下）](#131-ダッシュボードタブレット用768px以下)
- [13.2 ダッシュボードスマートフォン用（480px以下）](#132-ダッシュボードスマートフォン用480px以下)

### 14. ダッシュボード印刷スタイル
- [14.1 ダッシュボード印刷用](#141-ダッシュボード印刷用)

---

## 10. レスポンシブデザイン <a id="10-レスポンシブデザイン"></a>

### 10.1 タブレット用（768px以下） <a id="101-タブレット用768px以下"></a>
```css
@media (max-width: 768px) {
    .container {
        padding: 0 15px;
    }

    .header-container {
        flex-direction: column;
        gap: 1rem;
    }

    .nav {
        flex-direction: column;
        width: 100%;
        gap: 0.5rem;
    }

    .nav-item {
        margin-left: 0;
    }

    .nav-link {
        display: block;
        text-align: center;
        padding: 1rem;
        border-radius: 5px;
        background-color: rgba(255, 255, 255, 0.1);
    }

    .user-menu {
        width: 100%;
        text-align: center;
    }

    .section {
        padding: 40px 0;
    }

    .section-lg {
        padding: 60px 0;
    }

    .grid-2,
    .grid-3 {
        grid-template-columns: 1fr;
        gap: 15px;
    }

    .card {
        margin-bottom: 1rem;
    }

    .btn {
        width: 100%;
        margin-bottom: 0.5rem;
    }

    .form-control,
    .form-select,
    .form-textarea {
        font-size: 16px; /* モバイルでのズーム防止 */
    }

    .modal-content {
        width: 95%;
        margin: 10px;
    }

    .dropdown-menu {
        position: static;
        width: 100%;
        box-shadow: none;
        border: 1px solid #e9ecef;
        margin-top: 0.5rem;
    }
}
```
**使用ページ:** 全ページ  
**説明:** タブレット・スマートフォン用のレスポンシブデザイン

### 10.2 スマートフォン用（480px以下） <a id="102-スマートフォン用480px以下"></a>
```css
@media (max-width: 480px) {
    .container {
        padding: 0 10px;
    }

    .header {
        padding: 0.5rem 0;
    }

    .logo {
        font-size: 1.5rem;
    }

    .section {
        padding: 30px 0;
    }

    .section-sm {
        padding: 20px 0;
    }

    .section-lg {
        padding: 40px 0;
    }

    .card-body,
    .panel-body {
        padding: 1rem;
    }

    .btn {
        padding: 0.75rem 1rem;
        font-size: 0.9rem;
    }

    .btn-lg {
        padding: 1rem 1.5rem;
        font-size: 1rem;
    }

    .form-control,
    .form-select,
    .form-textarea {
        padding: 0.75rem;
        font-size: 16px;
    }

    .modal-header,
    .modal-body,
    .modal-footer {
        padding: 15px;
    }

    .dropdown-menu {
        padding: 0.25rem 0;
    }

    .dropdown-item {
        padding: 0.5rem 1rem;
    }

    .alert {
        padding: 0.75rem 1rem;
        font-size: 0.9rem;
    }
}
```
**使用ページ:** 全ページ  
**説明:** スマートフォン用の細かい調整

### 10.3 大画面用（1200px以上） <a id="103-大画面用1200px以上"></a>
```css
@media (min-width: 1200px) {
    .container {
        max-width: 1400px;
    }

    .section {
        padding: 80px 0;
    }

    .section-lg {
        padding: 100px 0;
    }

    .grid-3 {
        grid-template-columns: repeat(4, 1fr);
    }

    .card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    }
}
```
**使用ページ:** 全ページ  
**説明:** 大画面用の最適化

---

## 11. 印刷スタイル <a id="11-印刷スタイル"></a>

### 11.1 印刷用基本設定 <a id="111-印刷用基本設定"></a>
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
    }

    .header,
    .footer,
    .nav,
    .btn,
    .modal,
    .dropdown-menu,
    .alert,
    .tooltip {
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

    .card {
        border: 1px solid #ccc;
        box-shadow: none;
        break-inside: avoid;
        margin-bottom: 20pt;
    }

    .card-header {
        background: #f5f5f5 !important;
        color: black !important;
        border-bottom: 1px solid #ccc;
        padding: 10pt;
    }

    .card-body,
    .panel-body {
        padding: 15pt;
    }

    h1, h2, h3, h4, h5, h6 {
        break-after: avoid;
        page-break-after: avoid;
    }

    p, li {
        orphans: 3;
        widows: 3;
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
}
```
**使用ページ:** 全ページ  
**説明:** 印刷時の最適化、不要要素の非表示

### 11.2 A4サイズ最適化 <a id="112-a4サイズ最適化"></a>
```css
@page {
    size: A4;
    margin: 2cm;
}

@media print {
    .print-container {
        width: 100%;
        max-width: none;
    }

    .print-header {
        text-align: center;
        margin-bottom: 20pt;
        border-bottom: 2pt solid #000;
        padding-bottom: 10pt;
    }

    .print-content {
        columns: 1;
        column-gap: 20pt;
    }

    .print-section {
        margin-bottom: 20pt;
        break-inside: avoid;
    }

    .print-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 15pt;
    }

    .print-table th,
    .print-table td {
        border: 1pt solid #000;
        padding: 5pt;
        text-align: left;
    }

    .print-table th {
        background: #f0f0f0;
        font-weight: bold;
    }

    .print-image {
        max-width: 100%;
        height: auto;
        break-inside: avoid;
    }
}
```
**使用ページ:** `print_profile.html`, `print_iwlm.html`, `print_goals.html`  
**説明:** A4サイズでの印刷最適化

---

## 12. ダッシュボード関連スタイル <a id="12-ダッシュボード関連スタイル"></a>

### 12.1 ダッシュボードページ <a id="121-ダッシュボードページ"></a>
```css
.dashboard-page {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    min-height: 100vh;
    padding: 20px 0;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードの背景グラデーション

### 12.2 ダッシュボードコンテナ <a id="122-ダッシュボードコンテナ"></a>
```css
.dashboard-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードの最大幅制限

### 12.3 ダッシュボードヘッダー <a id="123-ダッシュボードヘッダー"></a>
```css
.dashboard-header {
    text-align: center;
    margin-bottom: 40px;
    padding: 30px 0;
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードヘッダーのスタイル

### 12.4 ダッシュボードタイトル <a id="124-ダッシュボードタイトル"></a>
```css
.dashboard-title {
    font-size: 2.5rem;
    color: #2c3e50;
    margin-bottom: 10px;
    font-weight: bold;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードタイトルのスタイル

### 12.5 ダッシュボードサブタイトル <a id="125-ダッシュボードサブタイトル"></a>
```css
.dashboard-subtitle {
    font-size: 1.2rem;
    color: #7f8c8d;
    margin-bottom: 0;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードサブタイトルのスタイル

### 12.6 ダッシュボードグリッド <a id="126-ダッシュボードグリッド"></a>
```css
.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-bottom: 40px;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードのグリッドレイアウト

### 12.7 ダッシュボードカード <a id="127-ダッシュボードカード"></a>
```css
.dashboard-card {
    background: white;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}

.dashboard-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(135deg, #FF5192 0%, #FF1493 100%);
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードカードのスタイル、上部アクセント

### 12.8 ダッシュボードカードのホバー効果 <a id="128-ダッシュボードカードのホバー効果"></a>
```css
.dashboard-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードカードのホバー効果

### 12.9 ダッシュボードカードヘッダー <a id="129-ダッシュボードカードヘッダー"></a>
```css
.dashboard-card-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.dashboard-card-icon {
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, #FF5192 0%, #FF1493 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 15px;
    color: white;
    font-size: 1.5rem;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードカードのアイコン

### 12.10 ダッシュボードカードタイトル <a id="1210-ダッシュボードカードタイトル"></a>
```css
.dashboard-card-title {
    font-size: 1.5rem;
    color: #2c3e50;
    margin: 0;
    font-weight: bold;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードカードタイトルのスタイル

### 12.11 ダッシュボードカードコンテンツ <a id="1211-ダッシュボードカードコンテンツ"></a>
```css
.dashboard-card-content {
    color: #7f8c8d;
    line-height: 1.6;
    margin-bottom: 20px;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードカードコンテンツのスタイル

### 12.12 ダッシュボードカードアクション <a id="1212-ダッシュボードカードアクション"></a>
```css
.dashboard-card-action {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードカードアクションの配置

### 12.13 ダッシュボード統計 <a id="1213-ダッシュボード統計"></a>
```css
.dashboard-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボード統計のグリッド

### 12.14 ダッシュボード統計アイテム <a id="1214-ダッシュボード統計アイテム"></a>
```css
.dashboard-stat-item {
    background: white;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.dashboard-stat-item:hover {
    transform: translateY(-3px);
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボード統計アイテムのスタイル

### 12.15 ダッシュボード統計値 <a id="1215-ダッシュボード統計値"></a>
```css
.dashboard-stat-value {
    font-size: 2rem;
    font-weight: bold;
    color: #FF5192;
    margin-bottom: 5px;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボード統計値のスタイル

### 12.16 ダッシュボード統計ラベル <a id="1216-ダッシュボード統計ラベル"></a>
```css
.dashboard-stat-label {
    font-size: 0.9rem;
    color: #7f8c8d;
    margin: 0;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボード統計ラベルのスタイル

### 12.17 ダッシュボードアクション <a id="1217-ダッシュボードアクション"></a>
```css
.dashboard-actions {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 40px;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードアクションの配置

### 12.18 ダッシュボードアクションボタン <a id="1218-ダッシュボードアクションボタン"></a>
```css
.dashboard-action-btn {
    background: linear-gradient(135deg, #FF5192 0%, #FF1493 100%);
    color: white;
    padding: 15px 30px;
    border: none;
    border-radius: 25px;
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.dashboard-action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 81, 146, 0.4);
    color: white;
    text-decoration: none;
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードアクションボタンのスタイル

---

## 13. ダッシュボードレスポンシブデザイン <a id="13-ダッシュボードレスポンシブデザイン"></a>

### 13.1 ダッシュボードタブレット用（768px以下） <a id="131-ダッシュボードタブレット用768px以下"></a>
```css
@media (max-width: 768px) {
    .dashboard-page {
        padding: 10px 0;
    }

    .dashboard-container {
        padding: 0 15px;
    }

    .dashboard-header {
        padding: 20px;
        margin-bottom: 30px;
    }

    .dashboard-title {
        font-size: 2rem;
    }

    .dashboard-subtitle {
        font-size: 1rem;
    }

    .dashboard-grid {
        grid-template-columns: 1fr;
        gap: 20px;
        margin-bottom: 30px;
    }

    .dashboard-card {
        padding: 20px;
    }

    .dashboard-card-header {
        flex-direction: column;
        text-align: center;
        gap: 15px;
    }

    .dashboard-card-icon {
        margin-right: 0;
    }

    .dashboard-card-title {
        font-size: 1.3rem;
    }

    .dashboard-stats {
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
        margin-bottom: 30px;
    }

    .dashboard-stat-item {
        padding: 15px;
    }

    .dashboard-stat-value {
        font-size: 1.5rem;
    }

    .dashboard-actions {
        gap: 15px;
        margin-top: 30px;
    }

    .dashboard-action-btn {
        padding: 12px 25px;
        font-size: 1rem;
        width: 100%;
        max-width: 300px;
    }
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードのタブレット用レスポンシブ

### 13.2 ダッシュボードスマートフォン用（480px以下） <a id="132-ダッシュボードスマートフォン用480px以下"></a>
```css
@media (max-width: 480px) {
    .dashboard-container {
        padding: 0 10px;
    }

    .dashboard-header {
        padding: 15px;
        margin-bottom: 20px;
    }

    .dashboard-title {
        font-size: 1.8rem;
    }

    .dashboard-subtitle {
        font-size: 0.9rem;
    }

    .dashboard-grid {
        gap: 15px;
        margin-bottom: 20px;
    }

    .dashboard-card {
        padding: 15px;
    }

    .dashboard-card-title {
        font-size: 1.2rem;
    }

    .dashboard-stats {
        grid-template-columns: 1fr;
        gap: 10px;
        margin-bottom: 20px;
    }

    .dashboard-stat-item {
        padding: 12px;
    }

    .dashboard-stat-value {
        font-size: 1.3rem;
    }

    .dashboard-actions {
        gap: 10px;
        margin-top: 20px;
    }

    .dashboard-action-btn {
        padding: 10px 20px;
        font-size: 0.9rem;
        border-radius: 20px;
    }
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードのスマートフォン用レスポンシブ

---

## 14. ダッシュボード印刷スタイル <a id="14-ダッシュボード印刷スタイル"></a>

### 14.1 ダッシュボード印刷用 <a id="141-ダッシュボード印刷用"></a>
```css
@media print {
    .dashboard-page {
        background: white !important;
        padding: 0 !important;
    }

    .dashboard-header {
        background: white !important;
        box-shadow: none !important;
        border-bottom: 2pt solid #000;
        margin-bottom: 20pt;
    }

    .dashboard-title {
        color: black !important;
        font-size: 18pt;
    }

    .dashboard-subtitle {
        color: black !important;
        font-size: 12pt;
    }

    .dashboard-grid {
        display: block;
        margin-bottom: 20pt;
    }

    .dashboard-card {
        background: white !important;
        box-shadow: none !important;
        border: 1pt solid #ccc;
        margin-bottom: 15pt;
        break-inside: avoid;
    }

    .dashboard-card::before {
        display: none !important;
    }

    .dashboard-card-header {
        border-bottom: 1pt solid #ccc;
        margin-bottom: 10pt;
        padding-bottom: 10pt;
    }

    .dashboard-card-icon {
        background: #f0f0f0 !important;
        color: black !important;
    }

    .dashboard-card-title {
        color: black !important;
        font-size: 14pt;
    }

    .dashboard-card-content {
        color: black !important;
        font-size: 10pt;
    }

    .dashboard-stats {
        display: block;
        margin-bottom: 20pt;
    }

    .dashboard-stat-item {
        background: white !important;
        box-shadow: none !important;
        border: 1pt solid #ccc;
        margin-bottom: 10pt;
        break-inside: avoid;
    }

    .dashboard-stat-value {
        color: black !important;
        font-size: 16pt;
    }

    .dashboard-stat-label {
        color: black !important;
        font-size: 9pt;
    }

    .dashboard-actions {
        display: none !important;
    }

    .dashboard-action-btn {
        display: none !important;
    }
}
```
**使用ページ:** `dashboard.html`  
**説明:** ダッシュボードの印刷最適化

---

## まとめ

第2部では、レスポンシブデザイン、印刷スタイル、ダッシュボード関連のスタイリングを解説しました。

### 主要機能
1. **レスポンシブデザイン**: タブレット・スマートフォン対応
2. **印刷最適化**: A4サイズ対応、不要要素の非表示
3. **ダッシュボード**: カードレイアウト、統計表示、アクションボタン
4. **アニメーション**: ホバー効果、トランジション
5. **グリッドシステム**: CSS Gridによる柔軟なレイアウト

### 技術的特徴
- **メディアクエリ**: 768px、480pxでのブレークポイント
- **CSS Grid**: 自動調整されるグリッドレイアウト
- **印刷メディア**: 印刷時の最適化
- **グラデーション**: 視覚的なアクセント
- **ボックスシャドウ**: 立体感のあるデザイン

### デザインシステム
- **カラーパレット**: ピンク系グラデーション、グレー系
- **タイポグラフィ**: 階層的な文字サイズ
- **スペーシング**: 統一された余白とパディング
- **ボーダー**: 角丸、シャドウの統一
- **アニメーション**: 0.3s easeのトランジション

このファイルは、アプリケーションのレスポンシブ対応と印刷機能、ダッシュボードの美しいデザインを提供しています。
