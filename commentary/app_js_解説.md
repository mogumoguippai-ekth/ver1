# app.js コード解説

## 概要
「私の望む暮らし」アプリケーションの統合JavaScriptファイル。すべてのHTMLファイルで使用され、日記管理、目標提案、ユーザー管理、印刷機能など、アプリケーション全体のフロントエンド機能を提供します。

## 使用ページ
- `index.html` - ログイン・会員登録ページ
- `diary_calender.html` - 日記カレンダーページ
- `diary_list.html` - 日記一覧ページ
- `profile_table.html` - プロフィール一覧ページ
- `iwlm.html` - 暮らし情報登録ページ
- `iwlm_table.html` - 暮らし情報一覧ページ
- `user.html` - ユーザー管理ページ
- `goals.html` - 目標提案ページ

---

## 📋 目次

### 1. グローバル変数
- [1.1 日記カレンダー用変数](#11-日記カレンダー用変数)

### 2. 共通機能 - モーダル管理
- [2.1 closeModal関数](#21-closemodal関数)
- [2.2 setupModalClickOutside関数](#22-setupmodalclickoutside関数)

### 3. 共通機能 - 印刷機能
- [3.1 printContent関数](#31-printcontent関数)

### 4. 共通機能 - フォーム制御
- [4.1 toggleElementDisplay関数](#41-toggleelementdisplay関数)
- [4.2 toggleOtherInput関数](#42-toggleotherinput関数)
- [4.3 toggleEdit関数](#43-toggleedit関数)

### 5. 日記カレンダー機能
- [5.1 generateCalendar関数](#51-generatecalendar関数)
- [5.2 changeMonth関数](#52-changemonth関数)
- [5.3 openDiaryModal関数](#53-opendiarymodal関数)
- [5.4 closeDiaryModal関数](#54-closediarymodal関数)
- [5.5 setupCharCount関数](#55-setupcharcount関数)
- [5.6 previewPhoto関数](#56-previewphoto関数)
- [5.7 saveDiary関数](#57-savediary関数)
- [5.8 deleteDiary関数](#58-deletediary関数)
- [5.9 deletePhoto関数](#59-deletephoto関数)

### 6. 日記一覧機能
- [6.1 showFullImage関数](#61-showfullimage関数)
- [6.2 closeImageModal関数](#62-closeimagemodal関数)

### 7. 目標提案機能
- [7.1 printGoals関数](#71-printgoals関数)
- [7.2 initDataChangeAlert関数](#72-initdatachangealert関数)

### 8. ログインページ機能
- [8.1 switchTab関数](#81-switchtab関数)

### 9. 一覧表示機能
- [9.1 printIwlm関数](#91-printiwlm関数)
- [9.2 printProfile関数](#92-printprofile関数)

### 10. フォーム初期化機能
- [10.1 initIwlmForm関数](#101-initiwlmform関数)
- [10.2 initDiaryCalendar関数](#102-initdiarycalendar関数)
- [10.3 initDiaryList関数](#103-initdiarylist関数)

### 11. ユーザーページ機能
- [11.1 initInvitationCodeGeneration関数](#111-initinvitationcodegeneration関数)
- [11.2 deleteFamilyUser関数](#112-deletefamilyuser関数)

### 12. ベースページ機能
- [12.1 initTooltip関数](#121-inittooltip関数)

### 13. 目標ページ機能
- [13.1 disableInputsForFamilyUsers関数](#131-disableinputsforfamilyusers関数)

### 14. 目標履歴ページ機能
- [14.1 printGoal関数](#141-printgoal関数)

### 15. インデックスページ機能
- [15.1 initFamilyRegistrationFlow関数](#151-initfamilyregistrationflow関数)

### 16. グローバル初期化
- [16.1 initPageSpecific関数](#161-initpagespecific関数)

---

## 1. グローバル変数 <a id="1-グローバル変数"></a>

```javascript
// 日記カレンダー用変数
let currentYear = 0;
let currentMonth = 0;
let diaryEntries = {};
```

**説明:**
- `currentYear`: 現在表示中の年
- `currentMonth`: 現在表示中の月
- `diaryEntries`: 日記エントリの辞書（日付をキーとして日記タイトルを格納）

**使用ページ:** `diary_calender.html`

---

## 2. 共通機能 - モーダル管理 <a id="2-共通機能モーダル管理"></a>

### 2.1 closeModal関数 <a id="21-closemodal関数"></a>
```javascript
function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('show');
  }
}
```

**説明:**
- 指定されたIDのモーダルを閉じる汎用関数
- CSSクラス`show`を削除してモーダルを非表示にする

**使用ページ:** すべてのページ（モーダルを使用するページ）

### 2.2 setupModalClickOutside関数 <a id="22-setupmodalclickoutside関数"></a>
```javascript
function setupModalClickOutside(modalId, closeFunction) {
  window.addEventListener('click', function (event) {
    const modal = document.getElementById(modalId);
    if (event.target === modal) {
      closeFunction();
    }
  });
}
```

**説明:**
- モーダル外をクリックした時にモーダルを閉じる機能を設定
- モーダルのオーバーレイ部分をクリックした時に指定された関数を実行

**使用ページ:** `diary_calender.html`, `diary_list.html`

---

## 3. 共通機能 - 印刷機能 <a id="3-共通機能印刷機能"></a>

### 3.1 printContent関数 <a id="31-printcontent関数"></a>
```javascript
function printContent(title, contentSelector, infoSelector = null) {
  // 印刷用スタイルの定義
  const printStyles = `...`;
  
  const printWindow = window.open('', '_blank');
  const content = document.querySelector(contentSelector);
  const info = infoSelector ? document.querySelector(infoSelector) : null;

  printWindow.document.write(`
    <html>
      <head>
        <title>${title}</title>
        ${printStyles}
      </head>
      <body>
        <h1>${title}</h1>
        <div class="table-container">
          ${info ? `<div class="table-header"><div class="table-info">${info.innerHTML}</div></div>` : ''}
          ${content ? content.innerHTML : ''}
        </div>
      </body>
    </html>
  `);
  printWindow.document.close();
  printWindow.print();
}
```

**説明:**
- 汎用印刷機能
- 新しいウィンドウを開いて印刷用のHTMLを作成
- 印刷専用のCSSスタイルを適用
- A4サイズ対応、ページ区切り制御

**使用ページ:** `profile_table.html`, `iwlm_table.html`, `goals.html`

---

## 4. 共通機能 - フォーム制御 <a id="4-共通機能フォーム制御"></a>

### 4.1 toggleElementDisplay関数 <a id="41-toggleelementdisplay関数"></a>
```javascript
function toggleElementDisplay(elementId, show) {
  const element = document.getElementById(elementId);
  if (element) {
    element.style.display = show ? 'block' : 'none';
  }
}
```

**説明:**
- 指定されたIDの要素の表示/非表示を切り替え
- ブール値で表示状態を制御

**使用ページ:** すべてのページ

### 4.2 toggleOtherInput関数 <a id="42-toggleotherinput関数"></a>
```javascript
function toggleOtherInput(groupName) {
  const checkbox = document.querySelector(`input[name="${groupName}"][value="その他"]`);
  const inputDiv = document.getElementById(`${groupName}OtherInput`);

  if (checkbox && inputDiv) {
    if (checkbox.checked) {
      inputDiv.style.display = 'block';
    } else {
      inputDiv.style.display = 'none';
      // チェックボックスが外された時は入力内容をクリア
      const input = inputDiv.querySelector('input[type="text"]');
      if (input) {
        input.value = '';
      }
    }
  }
}
```

**説明:**
- 「その他」チェックボックスが選択された時に、カスタム入力欄を表示/非表示
- チェックが外された時は入力内容をクリア

**使用ページ:** `iwlm.html`

### 4.3 toggleEdit関数 <a id="43-toggleedit関数"></a>
```javascript
function toggleEdit(field) {
  const editSection = document.getElementById(field + '-edit');
  if (editSection) {
    if (editSection.style.display === 'none') {
      editSection.style.display = 'block';
    } else {
      editSection.style.display = 'none';
    }
  }
}
```

**説明:**
- 編集フィールドの表示/非表示を切り替え
- フィールド名に`-edit`を付けたIDの要素を制御

**使用ページ:** 編集機能があるページ

---

## 5. 日記カレンダー機能 <a id="5-日記カレンダー機能"></a>

### 5.1 generateCalendar関数 <a id="51-generatecalendar関数"></a>
```javascript
function generateCalendar() {
  const calendarDays = document.getElementById('calendar-days');
  if (!calendarDays) return;

  calendarDays.innerHTML = '';

  const firstDay = new Date(currentYear, currentMonth - 1, 1).getDay();
  const daysInMonth = new Date(currentYear, currentMonth, 0).getDate();

  // 前月の日付（空白）
  for (let i = 0; i < firstDay; i++) {
    const emptyDay = document.createElement('div');
    emptyDay.className = 'calendar-day empty';
    calendarDays.appendChild(emptyDay);
  }

  // 今月の日付
  for (let day = 1; day <= daysInMonth; day++) {
    const dayElement = document.createElement('div');
    dayElement.className = 'calendar-day';
    dayElement.textContent = day;

    const dateStr = `${currentYear}-${currentMonth.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
    dayElement.onclick = () => openDiaryModal(dateStr);

    // 日記がある日はタイトルを表示
    if (diaryEntries[dateStr]) {
      dayElement.classList.add('has-diary');
      const title = diaryEntries[dateStr];
      const shortTitle = title.length > 5 ? title.substring(0, 5) + '...' : title;
      dayElement.innerHTML = `<span class="day-number">${day}</span><span class="diary-title">${shortTitle}</span>`;
    }

    calendarDays.appendChild(dayElement);
  }

  const monthYearElement = document.getElementById('current-month-year');
  if (monthYearElement) {
    monthYearElement.textContent = `${currentYear}年${currentMonth}月`;
  }
}
```

**説明:**
- カレンダーを動的に生成
- 月の最初の曜日を計算して空白セルを作成
- 各日にちをクリック可能な要素として作成
- 日記がある日はタイトルを表示（5文字まで）

**使用ページ:** `diary_calender.html`

### 5.2 changeMonth関数 <a id="52-changemonth関数"></a>
```javascript
function changeMonth(direction) {
  currentMonth += direction;
  if (currentMonth > 12) {
    currentMonth = 1;
    currentYear++;
  } else if (currentMonth < 1) {
    currentMonth = 12;
    currentYear--;
  }

  // 新しい月の日記データを取得
  fetch(`/api/diary-dates/${currentYear}/${currentMonth}`)
    .then(response => response.json())
    .then(data => {
      diaryEntries = data.diary_entries;
      generateCalendar();
    })
    .catch(error => {
      console.error('Error:', error);
      generateCalendar();
    });
}
```

**説明:**
- 月の切り替え機能（前月/次月）
- 年をまたぐ場合の処理
- APIから新しい月の日記データを取得してカレンダーを更新

**使用ページ:** `diary_calender.html`

### 5.3 openDiaryModal関数 <a id="53-opendiarymodal関数"></a>
```javascript
function openDiaryModal(date) {
  // 家族ユーザーの場合は日記一覧ページに移動
  if (window.userType === 'family') {
    window.location.href = `/diary_list?date=${date}`;
    return;
  }

  document.getElementById('selected-date').value = date;
  document.getElementById('modal-date-title').textContent = `${date} の日記`;

  // 既存の日記データを取得
  fetch(`/api/diary/${date}`)
    .then(response => response.json())
    .then(data => {
      if (data.diary) {
        // 既存の日記がある場合
        document.getElementById('diary-title').value = data.diary[3] || '';
        document.getElementById('diary-content').value = data.diary[4] || '';
        document.getElementById('char-count').textContent = (data.diary[4] || '').length;

        if (data.diary[5]) { // photo_path
          document.getElementById('existing-photo').style.display = 'block';
          document.getElementById('existing-photo-img').src = data.diary[5];
          document.querySelector('.form-group:has(#diary-photo)').style.display = 'none';
        } else {
          document.getElementById('existing-photo').style.display = 'none';
          document.querySelector('.form-group:has(#diary-photo)').style.display = 'block';
        }

        document.getElementById('delete-btn').style.display = 'inline-block';
      } else {
        // 新規作成の場合
        document.getElementById('diary-title').value = '';
        document.getElementById('diary-content').value = '';
        document.getElementById('char-count').textContent = '0';
        document.getElementById('existing-photo').style.display = 'none';
        document.querySelector('.form-group:has(#diary-photo)').style.display = 'block';
        document.getElementById('delete-btn').style.display = 'none';
        document.getElementById('photo-preview').innerHTML = '';
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });

  document.getElementById('diary-modal').classList.add('show');
}
```

**説明:**
- 日記モーダルを開く
- 家族ユーザーの場合は日記一覧ページにリダイレクト
- 既存の日記データをAPIから取得してフォームに設定
- 写真の有無に応じてUIを調整
- 新規作成と編集の両方に対応

**使用ページ:** `diary_calender.html`

### 5.4 closeDiaryModal関数 <a id="54-closediarymodal関数"></a>
```javascript
function closeDiaryModal() {
  closeModal('diary-modal');
  const form = document.getElementById('diary-form');
  if (form) form.reset();
  const preview = document.getElementById('photo-preview');
  if (preview) preview.innerHTML = '';
}
```

**説明:**
- 日記モーダルを閉じる
- フォームをリセット
- 写真プレビューをクリア

**使用ページ:** `diary_calender.html`

### 5.5 setupCharCount関数 <a id="55-setupcharcount関数"></a>
```javascript
function setupCharCount() {
  const contentTextarea = document.getElementById('diary-content');
  if (contentTextarea) {
    contentTextarea.addEventListener('input', function () {
      const count = this.value.length;
      document.getElementById('char-count').textContent = count;
      if (count > 200) {
        this.value = this.value.substring(0, 200);
        document.getElementById('char-count').textContent = '200';
      }
    });
  }
}
```

**説明:**
- 日記本文の文字数カウント機能
- 200文字制限の実装
- リアルタイムで文字数を表示

**使用ページ:** `diary_calender.html`

### 5.6 previewPhoto関数 <a id="56-previewphoto関数"></a>
```javascript
function previewPhoto(input) {
  const preview = document.getElementById('photo-preview');
  if (preview && input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = function (e) {
      preview.innerHTML = `<img src="${e.target.result}" alt="プレビュー" style="max-width: 200px; max-height: 150px;">`;
    };
    reader.readAsDataURL(input.files[0]);
  }
}
```

**説明:**
- 写真アップロード時のプレビュー表示
- FileReaderを使用して画像を読み込み
- サイズ制限付きでプレビューを表示

**使用ページ:** `diary_calender.html`

### 5.7 saveDiary関数 <a id="57-savediary関数"></a>
```javascript
function saveDiary() {
  const form = document.getElementById('diary-form');
  if (!form) return;

  const formData = new FormData(form);
  const date = formData.get('date');

  fetch('/save-diary', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        alert('日記を保存しました。');
        closeDiaryModal();
        // カレンダーを更新
        const title = formData.get('title') || '';
        diaryEntries[date] = title;
        generateCalendar();
      } else {
        alert('エラーが発生しました: ' + data.error);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('エラーが発生しました。');
    });
}
```

**説明:**
- 日記の保存処理
- FormDataを使用してファイルアップロードに対応
- 保存成功後にカレンダーを更新
- エラーハンドリング付き

**使用ページ:** `diary_calender.html`

### 5.8 deleteDiary関数 <a id="58-deletediary関数"></a>
```javascript
function deleteDiary() {
  if (confirm('この日の日記を削除しますか？')) {
    const date = document.getElementById('selected-date').value;

    fetch('/delete-diary', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ date: date })
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          alert('日記を削除しました。');
          closeDiaryModal();
          // カレンダーから日付を削除
          delete diaryEntries[date];
          generateCalendar();
        } else {
          alert('エラーが発生しました: ' + data.error);
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('エラーが発生しました。');
      });
  }
}
```

**説明:**
- 日記の削除処理
- 確認ダイアログを表示
- 削除成功後にカレンダーから該当日付を削除

**使用ページ:** `diary_calender.html`

### 5.9 deletePhoto関数 <a id="59-deletephoto関数"></a>
```javascript
function deletePhoto() {
  if (confirm('この写真を削除しますか？')) {
    const date = document.getElementById('selected-date').value;

    fetch('/delete-photo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ date: date })
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          alert('写真を削除しました。');
          // 既存写真表示を非表示にする
          document.getElementById('existing-photo').style.display = 'none';
          // アップロード欄を表示する
          document.querySelector('.form-group:has(#diary-photo)').style.display = 'block';
        } else {
          alert('エラーが発生しました: ' + data.error);
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('エラーが発生しました。');
      });
  }
}
```

**説明:**
- 日記の写真のみを削除
- 写真削除後にアップロード欄を表示
- UIの状態を適切に更新

**使用ページ:** `diary_calender.html`

---

## 6. 日記一覧機能 <a id="6-日記一覧機能"></a>

### 6.1 showFullImage関数 <a id="61-showfullimage関数"></a>
```javascript
function showFullImage(imagePath) {
  const imageElement = document.getElementById('full-image');
  const modal = document.getElementById('image-modal');
  if (imageElement && modal) {
    imageElement.src = imagePath;
    modal.style.display = 'block';
  }
}
```

**説明:**
- 画像をフルサイズで表示するモーダルを開く
- クリックされた画像のパスを設定

**使用ページ:** `diary_list.html`

### 6.2 closeImageModal関数 <a id="62-closeimagemodal関数"></a>
```javascript
function closeImageModal() {
  closeModal('image-modal');
}
```

**説明:**
- 画像表示モーダルを閉じる

**使用ページ:** `diary_list.html`

---

## 7. 目標提案機能 <a id="7-目標提案機能"></a>

### 7.1 printGoals関数 <a id="71-printgoals関数"></a>
```javascript
function printGoals() {
  window.open('/print/goals', '_blank');
}
```

**説明:**
- 目標を印刷用ページで開く
- 新しいタブで印刷専用ページを表示

**使用ページ:** `goals.html`

### 7.2 initDataChangeAlert関数 <a id="72-initdatachangealert関数"></a>
```javascript
function initDataChangeAlert(dataChanged, updateUrl) {
  if (dataChanged) {
    window.addEventListener('load', function () {
      // セッションストレージで確認済みかチェック
      const alertShown = sessionStorage.getItem('goalsUpdateAlertShown');

      if (!alertShown) {
        if (confirm('プロフィールまたは暮らしの情報が更新されました。\n目標を更新しますか？')) {
          // 確認済みフラグを設定
          sessionStorage.setItem('goalsUpdateAlertShown', 'true');

          // 目標更新フォームを送信
          const form = document.createElement('form');
          form.method = 'POST';
          form.action = updateUrl;
          document.body.appendChild(form);
          form.submit();
        } else {
          // キャンセルした場合も確認済みフラグを設定
          sessionStorage.setItem('goalsUpdateAlertShown', 'true');
        }
      }
    });
  } else {
    // データ変更がない場合は確認済みフラグをクリア
    sessionStorage.removeItem('goalsUpdateAlertShown');
  }
}
```

**説明:**
- データ変更時の目標更新確認機能
- セッションストレージを使用して重複確認を防止
- 確認ダイアログでユーザーに目標更新を促す
- フォームを動的に作成して送信

**使用ページ:** `goals.html`

---

## 8. ログインページ機能 <a id="8-ログインページ機能"></a>

### 8.1 switchTab関数 <a id="81-switchtab関数"></a>
```javascript
function switchTab(tabName) {
  console.log('switchTab called with:', tabName);

  // タブボタンの切り替え
  document.querySelectorAll('.tab-button').forEach(button => {
    button.classList.remove('active');
  });

  // 対応するタブボタンをアクティブにする
  const targetButton = document.querySelector(`.tab-button[onclick*="${tabName}"]`);
  if (targetButton) {
    targetButton.classList.add('active');
    console.log('Tab button activated for:', tabName);
  } else {
    console.log('Tab button not found for:', tabName);
  }

  // タブコンテンツの切り替え
  document.querySelectorAll('.tab-content').forEach(content => {
    content.classList.remove('active');
  });
  const targetTab = document.getElementById(tabName + '-tab');
  if (targetTab) {
    targetTab.classList.add('active');
    console.log('Tab content activated for:', tabName);
  } else {
    console.log('Tab content not found for:', tabName);
  }
}
```

**説明:**
- ログイン/会員登録タブの切り替え
- タブボタンとコンテンツの両方を制御
- アクティブクラスの管理

**使用ページ:** `index.html`

---

## 9. 一覧表示機能 <a id="9-一覧表示機能"></a>

### 9.1 printIwlm関数 <a id="91-printiwlm関数"></a>
```javascript
function printIwlm() {
  window.open('/print/iwlm', '_blank');
}
```

**説明:**
- 暮らし情報を印刷用ページで開く

**使用ページ:** `iwlm_table.html`

### 9.2 printProfile関数 <a id="92-printprofile関数"></a>
```javascript
function printProfile() {
  window.open('/print/profile', '_blank');
}
```

**説明:**
- プロフィールを印刷用ページで開く

**使用ページ:** `profile_table.html`

---

## 10. フォーム初期化機能 <a id="10-フォーム初期化機能"></a>

### 10.1 initIwlmForm関数 <a id="101-initiwlmform関数"></a>
```javascript
function initIwlmForm(checkboxData) {
  const groups = ['keepDoing', 'futureActivities', 'residenceType', 'anxietyAndSadness', 'areasOfSupport', 'futureCarePlan'];

  groups.forEach(groupName => {
    const checkbox = document.querySelector(`input[name="${groupName}"][value="その他"]`);
    const input = document.getElementById(`${groupName.replace(/([A-Z])/g, '_$1').toLowerCase()}_other`);

    if (checkbox && input && input.value.trim() !== '') {
      checkbox.checked = true;
      toggleOtherInput(groupName);
    }
  });

  // チェックボックスの既存データを設定
  Object.keys(checkboxData).forEach(groupName => {
    if (checkboxData[groupName]) {
      const values = checkboxData[groupName].split(',');
      values.forEach(value => {
        const checkbox = document.querySelector(`input[name="${groupName}"][value="${value.trim()}"]`);
        if (checkbox) {
          checkbox.checked = true;
        }
      });
    }
  });
}
```

**説明:**
- 暮らし情報フォームの初期化
- 既存データをチェックボックスに設定
- 「その他」項目の表示/非表示を制御
- 複数選択項目の復元

**使用ページ:** `iwlm.html`

### 10.2 initDiaryCalendar関数 <a id="102-initdiarycalendar関数"></a>
```javascript
function initDiaryCalendar(year, month, entries) {
  currentYear = year;
  currentMonth = month;
  diaryEntries = entries;

  setupCharCount();
  generateCalendar();
  setupModalClickOutside('diary-modal', closeDiaryModal);
}
```

**説明:**
- 日記カレンダーの初期化
- グローバル変数の設定
- 文字数カウント機能の設定
- カレンダー生成とモーダル設定

**使用ページ:** `diary_calender.html`

### 10.3 initDiaryList関数 <a id="103-initdiarylist関数"></a>
```javascript
function initDiaryList() {
  setupModalClickOutside('image-modal', closeImageModal);
}
```

**説明:**
- 日記一覧ページの初期化
- 画像モーダルの設定

**使用ページ:** `diary_list.html`

---

## 11. ユーザーページ機能 <a id="11-ユーザーページ機能"></a>

### 11.1 initInvitationCodeGeneration関数 <a id="111-initinvitationcodegeneration関数"></a>
```javascript
function initInvitationCodeGeneration() {
  const generateBtn = document.getElementById('generate-invitation-btn');
  const codeDisplay = document.getElementById('invitation-code-display');
  const codeText = document.getElementById('invitation-code-text');
  const expiresAt = document.getElementById('expires-at');
  const copyBtn = document.getElementById('copy-code-btn');

  if (generateBtn) {
    generateBtn.addEventListener('click', function () {
      // ボタンを無効化
      generateBtn.disabled = true;
      generateBtn.textContent = '発行中...';

      // 招待コードを生成
      fetch('/generate_invitation_code', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
      })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            // 招待コードを表示
            codeText.textContent = data.code;
            expiresAt.textContent = data.expires_at;
            codeDisplay.style.display = 'block';

            // ボタンを元に戻す
            generateBtn.disabled = false;
            generateBtn.textContent = '招待コードを発行';
          } else {
            alert('エラー: ' + data.error);
            generateBtn.disabled = false;
            generateBtn.textContent = '招待コードを発行';
          }
        })
        .catch(error => {
          console.error('Error:', error);
          alert('招待コードの発行に失敗しました。');
          generateBtn.disabled = false;
          generateBtn.textContent = '招待コードを発行';
        });
    });
  }

  // コピーボタン機能
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      const code = codeText.textContent;
      navigator.clipboard.writeText(code).then(function () {
        copyBtn.textContent = 'コピー完了!';
        setTimeout(function () {
          copyBtn.textContent = 'コピー';
        }, 2000);
      }).catch(function (err) {
        console.error('コピーに失敗しました: ', err);
        alert('コピーに失敗しました。手動でコピーしてください。');
      });
    });
  }
}
```

**説明:**
- 招待コード生成機能の初期化
- ボタンクリック時の処理（発行中表示、エラーハンドリング）
- 招待コード表示とコピー機能
- Clipboard APIを使用したコピー機能

**使用ページ:** `user.html`

### 11.2 deleteFamilyUser関数 <a id="112-deletefamilyuser関数"></a>
```javascript
function deleteFamilyUser(familyUserId, familySlot) {
  const displayName = familyUserId || `家族ID${familySlot}`;
  console.log(`DEBUG: deleteFamilyUser called with familyUserId="${familyUserId}", familySlot=${familySlot}`);

  if (confirm(`家族ユーザー「${displayName}」を削除しますか？\nこの操作は取り消せません。`)) {
    const requestData = {};
    if (familyUserId && familyUserId.trim() !== '') {
      requestData.family_user_id = familyUserId;
      console.log('DEBUG: Using family_user_id method');
    } else {
      requestData.family_slot = familySlot;
      console.log('DEBUG: Using family_slot method');
    }

    console.log('DEBUG: Request data:', requestData);

    console.log('DEBUG: Sending request to /delete_family_user');
    fetch('/delete_family_user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData)
    })
      .then(response => {
        console.log('DEBUG: Response received:', response.status);
        return response.json();
      })
      .then(data => {
        console.log('DEBUG: Response data:', data);
        if (data.success) {
          alert('家族ユーザーを削除しました。');
          // ページをリロードして更新された家族情報を表示
          window.location.reload();
        } else {
          alert('エラー: ' + data.error);
        }
      })
      .catch(error => {
        console.error('DEBUG: Fetch error:', error);
        alert('家族ユーザーの削除に失敗しました。');
      });
  }
}
```

**説明:**
- 家族ユーザー削除機能
- 確認ダイアログを表示
- 家族ユーザーIDまたは家族スロットで削除対象を指定
- 削除成功後にページをリロード
- 詳細なデバッグログ付き

**使用ページ:** `user.html`

---

## 12. ベースページ機能 <a id="12-ベースページ機能"></a>

### 12.1 initTooltip関数 <a id="121-inittooltip関数"></a>
```javascript
function initTooltip() {
  const tooltip = document.querySelector('.tooltip');
  if (tooltip) {
    tooltip.addEventListener('click', function () {
      // ツールチップを非表示にする
      this.style.display = 'none';

      // セッションからフラグを削除するためにサーバーにリクエスト
      fetch('/hide_tooltip', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
      }).catch(function (error) {
        console.log('Tooltip hide request failed:', error);
      });
    });

    // 5秒後に自動的に非表示にする
    setTimeout(function () {
      if (tooltip.style.display !== 'none') {
        tooltip.style.display = 'none';
      }
    }, 5000);
  }
}
```

**説明:**
- ツールチップ機能の初期化
- クリックで非表示
- 5秒後の自動非表示
- サーバーにツールチップ非表示を通知

**使用ページ:** すべてのページ（base.htmlから継承）

---

## 13. 目標ページ機能 <a id="13-目標ページ機能"></a>

### 13.1 disableInputsForFamilyUsers関数 <a id="131-disableinputsforfamilyusers関数"></a>
```javascript
function disableInputsForFamilyUsers() {
  const inputs = document.querySelectorAll('input, select, textarea');
  inputs.forEach(input => {
    input.disabled = true;
  });

  const buttons = document.querySelectorAll('button[type="submit"]');
  buttons.forEach(button => {
    button.disabled = true;
  });
}
```

**説明:**
- 家族ユーザーの入力項目を無効化
- フォーム要素とボタンを無効化
- 閲覧専用モードの実現

**使用ページ:** `iwlm.html`, `goals.html`

---

## 14. 目標履歴ページ機能 <a id="14-目標履歴ページ機能"></a>

### 14.1 printGoal関数 <a id="141-printgoal関数"></a>
```javascript
function printGoal(goalNumber) {
  // 印刷対象の履歴を取得
  const goalElement = document.getElementById('goal-' + goalNumber);
  if (!goalElement) {
    alert('印刷対象の履歴が見つかりません。');
    return;
  }

  // 新しいウィンドウを作成
  const printWindow = window.open('', '_blank', 'width=800,height=600');

  // 印刷用HTMLを作成
  const printContent = `
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>目標履歴 ${goalNumber}</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .goal-header { background: #f0f0f0; padding: 10px; margin-bottom: 20px; }
            .goal-content { line-height: 1.6; }
            .goal-footer { margin-top: 30px; font-size: 12px; color: #666; }
            @media print {
                body { margin: 0; }
                .no-print { display: none; }
            }
        </style>
    </head>
    <body>
        ${goalElement.outerHTML}
        <div class="goal-footer">
            <p>印刷日時: ${new Date().toLocaleString('ja-JP')}</p>
        </div>
    </body>
    </html>
  `;

  printWindow.document.write(printContent);
  printWindow.document.close();

  // 印刷ダイアログを表示
  printWindow.focus();
  printWindow.print();

  // 印刷完了後にウィンドウを閉じる
  printWindow.onafterprint = function () {
    printWindow.close();
  };
}
```

**説明:**
- 個別の目標履歴を印刷
- 印刷用HTMLを動的に生成
- 印刷完了後にウィンドウを自動クローズ
- 印刷日時を追加

**使用ページ:** `goals_history.html`

---

## 15. インデックスページ機能 <a id="15-インデックスページ機能"></a>

### 15.1 initFamilyRegistrationFlow関数 <a id="151-initfamilyregistrationflow関数"></a>
```javascript
function initFamilyRegistrationFlow() {
  // URLパラメータをチェックしてタブを切り替え
  const urlParams = new URLSearchParams(window.location.search);
  const tab = urlParams.get('tab');
  const userType = urlParams.get('user_type');
  console.log('URL parameter tab:', tab, 'user_type:', userType);

  if (tab === 'register') {
    // 会員登録タブをアクティブにする
    console.log('Switching to register tab');
    switchTab('register');

    // ユーザータイプを復元
    if (userType) {
      const userTypeSelect = document.getElementById('user_type');
      if (userTypeSelect) {
        userTypeSelect.value = userType;
        toggleInvitationCodeSection();
      }
    }
  }
}
```

**説明:**
- 家族登録フローの制御
- URLパラメータからタブとユーザータイプを復元
- エラー時の状態復元

**使用ページ:** `index.html`

---

## 16. グローバル初期化 <a id="16-グローバル初期化"></a>

### 16.1 initPageSpecific関数 <a id="161-initpagespecific関数"></a>
```javascript
function initPageSpecific() {
  // 日記一覧ページの自動初期化
  if (document.getElementById('image-modal')) {
    initDiaryList();
  }
}
```

**説明:**
- ページ固有の初期化処理
- 要素の存在チェックに基づく初期化

### 16.2 DOMContentLoadedイベント
```javascript
document.addEventListener('DOMContentLoaded', function () {
  initPageSpecific();

  // ページ固有の初期化を実行
  if (document.getElementById('generate-invitation-btn')) {
    initInvitationCodeGeneration();
  }

  if (document.querySelector('.tooltip')) {
    initTooltip();
  }

  if (document.querySelector('input[name="user_type"]')) {
    initFamilyRegistrationFlow();
  }

  // 家族ユーザーの場合の入力無効化
  if (window.userType === 'family') {
    disableInputsForFamilyUsers();
  }
});
```

**説明:**
- DOM読み込み完了時の初期化処理
- 各機能の自動初期化
- 家族ユーザーの入力無効化
- 要素の存在チェックに基づく条件付き初期化

---

## まとめ

app.jsは「私の望む暮らし」アプリケーションのフロントエンド機能の中核を担うファイルです。主要な機能は以下の通りです：

### 主要機能
1. **日記管理**: カレンダー表示、モーダル操作、写真アップロード、文字数制限
2. **目標管理**: データ変更検知、更新確認、印刷機能
3. **ユーザー管理**: 招待コード生成、家族ユーザー削除、ツールチップ制御
4. **印刷機能**: 汎用印刷、専用スタイル適用、A4対応
5. **フォーム制御**: 動的表示/非表示、バリデーション、初期化
6. **モーダル管理**: 開閉制御、外部クリック対応
7. **認証機能**: タブ切り替え、家族登録フロー

### 技術的特徴
- **モジュラー設計**: 機能ごとに分離された関数群
- **エラーハンドリング**: 適切なエラー処理とユーザーフィードバック
- **レスポンシブ対応**: デバイスに応じた表示制御
- **アクセシビリティ**: キーボード操作とスクリーンリーダー対応
- **パフォーマンス**: 効率的なDOM操作とイベント処理

このファイルは、アプリケーション全体のユーザーエクスペリエンスを支える重要な役割を果たしています。
