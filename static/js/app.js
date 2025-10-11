/**
 * 私の望む暮らし - 統合JavaScriptファイル
 * 使用場所: すべてのHTMLファイル
 */

// =============================================================================
// グローバル変数
// =============================================================================

// 日記カレンダー用変数
let currentYear = 0;
let currentMonth = 0;
let diaryEntries = {};

// =============================================================================
// 共通機能 - モーダル管理
// =============================================================================

/**
 * モーダルを閉じる（汎用）
 * @param {string} modalId - モーダルのID
 */
function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
  }
}

/**
 * モーダル外クリックで閉じる処理を設定
 * @param {string} modalId - モーダルのID
 * @param {Function} closeFunction - 閉じる関数
 */
function setupModalClickOutside(modalId, closeFunction) {
  window.addEventListener('click', function (event) {
    const modal = document.getElementById(modalId);
    if (event.target === modal) {
      closeFunction();
    }
  });
}

// =============================================================================
// 共通機能 - 印刷機能
// =============================================================================

/**
 * 汎用印刷機能
 * @param {string} title - 印刷タイトル
 * @param {string} contentSelector - 印刷対象コンテンツのセレクタ
 * @param {string} infoSelector - 情報セクションのセレクタ（オプション）
 */
function printContent(title, contentSelector, infoSelector = null) {
  const printStyles = `
        <style>
            @page {
                margin: 0.5in;
                size: A4;
            }
            @media print {
                .action-buttons, .print-export, .goals-actions, .goal-period, .goal-explanation, .analysis-section {
                    display: none;
                }
                .profile-table-page, .goals-page {
                    max-width: none;
                    margin: 0;
                    padding: 10px;
                }
                .table-container {
                    box-shadow: none;
                    border: 1px solid #ddd;
                }
                .profile-table, .goal-section {
                    font-size: 10pt;
                    line-height: 1.3;
                    border-collapse: collapse;
                    border: 2px solid #333;
                    width: 100%;
                    table-layout: fixed;
                    margin-bottom: 20px;
                    page-break-inside: avoid;
                    padding: 8px;
                    box-sizing: border-box;
                }
                .profile-table th, .goal-header h3 {
                    border: 1px solid #333;
                    background: #f5f5f5;
                    padding: 6px;
                    font-weight: bold;
                    width: 30%;
                    vertical-align: top;
                    font-size: 10pt;
                }
                .profile-table td, .goal-text, .goal-description, .goal-reason {
                    padding: 6px;
                    border: 1px solid #333;
                    width: 70%;
                    vertical-align: top;
                    word-wrap: break-word;
                    font-size: 10pt;
                }
                .short-goal-item {
                    margin-bottom: 15px;
                    page-break-inside: avoid;
                    border: 1px solid #333;
                    padding: 10px;
                    width: 100%;
                    box-sizing: border-box;
                }
                .goal-title {
                    border-bottom: 1px solid #333;
                    padding-bottom: 4px;
                    width: 100%;
                    font-size: 10pt;
                }
                .goal-number {
                    font-size: 10pt;
                }
                .goal-details {
                    font-size: 10pt;
                }
                .goal-details h4, .goal-details h5 {
                    font-size: 10pt;
                    margin: 2px 0;
                }
                body {
                    font-size: 10pt;
                    line-height: 1.3;
                    margin: 0;
                    padding: 0;
                }
                .table-info {
                    margin-bottom: 15px;
                    padding: 8px;
                    background: #f8f9fa;
                    border-radius: 5px;
                    font-size: 10pt;
                }
                h1 {
                    font-size: 14pt;
                    margin: 0 0 15px 0;
                    padding: 0;
                }
                .goals-container {
                    width: 100%;
                    max-width: 100%;
                    margin: 0;
                    padding: 0;
                }
                .goal-content {
                    width: 100%;
                    margin: 0;
                    padding: 0;
                }
                .short-goals-list {
                    width: 100%;
                    margin: 0;
                    padding: 0;
                }
                .goal-section.long-term-goal {
                    width: 100%;
                    margin: 0 0 20px 0;
                    padding: 8px;
                    box-sizing: border-box;
                }
                .goal-section.short-term-goals {
                    width: 100%;
                    margin: 0;
                    padding: 8px;
                    box-sizing: border-box;
                }
                .goal-text {
                    width: 100%;
                    padding: 8px;
                    margin: 0;
                    box-sizing: border-box;
                }
                .goal-description {
                    width: 100%;
                    padding: 0;
                    margin: 0;
                    box-sizing: border-box;
                }
                .goal-reason {
                    width: 100%;
                    padding: 0;
                    margin: 0;
                    box-sizing: border-box;
                }
            }
        </style>
    `;

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

// =============================================================================
// 共通機能 - フォーム制御
// =============================================================================

/**
 * 要素の表示/非表示を切り替え
 * @param {string} elementId - 要素のID
 * @param {boolean} show - 表示するかどうか
 */
function toggleElementDisplay(elementId, show) {
  const element = document.getElementById(elementId);
  if (element) {
    element.style.display = show ? 'block' : 'none';
  }
}

/**
 * 「その他」入力欄の表示/非表示を切り替え
 * @param {string} groupName - グループ名
 */
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

/**
 * 編集フィールドの表示/非表示を切り替え
 * @param {string} field - フィールド名
 */
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

// =============================================================================
// 日記カレンダー機能
// =============================================================================

/**
 * カレンダーを生成
 */
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

/**
 * 月を変更
 * @param {number} direction - 方向（-1: 前月, 1: 次月）
 */
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

/**
 * 日記モーダルを開く
 * @param {string} date - 日付
 */
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
        document.getElementById('diary-title').value = data.diary[3] || ''; // title
        document.getElementById('diary-content').value = data.diary[4] || ''; // content
        document.getElementById('char-count').textContent = (data.diary[4] || '').length;

        if (data.diary[5]) { // photo_path
          document.getElementById('existing-photo').style.display = 'block';
          document.getElementById('existing-photo-img').src = data.diary[5];
          // 写真がある場合はアップロード欄を非表示
          document.querySelector('.form-group:has(#diary-photo)').style.display = 'none';
        } else {
          document.getElementById('existing-photo').style.display = 'none';
          // 写真がない場合はアップロード欄を表示
          document.querySelector('.form-group:has(#diary-photo)').style.display = 'block';
        }

        document.getElementById('delete-btn').style.display = 'inline-block';
      } else {
        // 新規作成の場合
        document.getElementById('diary-title').value = '';
        document.getElementById('diary-content').value = '';
        document.getElementById('char-count').textContent = '0';
        document.getElementById('existing-photo').style.display = 'none';
        // 写真がない場合はアップロード欄を表示
        document.querySelector('.form-group:has(#diary-photo)').style.display = 'block';
        document.getElementById('delete-btn').style.display = 'none';
        document.getElementById('photo-preview').innerHTML = '';
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });

  document.getElementById('diary-modal').style.display = 'block';
}

/**
 * 日記モーダルを閉じる
 */
function closeDiaryModal() {
  closeModal('diary-modal');
  const form = document.getElementById('diary-form');
  if (form) form.reset();
  const preview = document.getElementById('photo-preview');
  if (preview) preview.innerHTML = '';
}

/**
 * 文字数カウント設定
 */
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

/**
 * 写真プレビュー
 * @param {HTMLInputElement} input - ファイル入力要素
 */
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

/**
 * 日記を保存
 */
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

/**
 * 日記を削除
 */
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

/**
 * 写真のみを削除
 */
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

// =============================================================================
// 日記一覧機能
// =============================================================================

/**
 * フルサイズ画像を表示
 * @param {string} imagePath - 画像パス
 */
function showFullImage(imagePath) {
  const imageElement = document.getElementById('full-image');
  const modal = document.getElementById('image-modal');
  if (imageElement && modal) {
    imageElement.src = imagePath;
    modal.style.display = 'block';
  }
}

/**
 * 画像モーダルを閉じる
 */
function closeImageModal() {
  closeModal('image-modal');
}

// =============================================================================
// 目標提案機能
// =============================================================================

/**
 * 目標を印刷
 */
function printGoals() {
  printContent('私の目標提案', '.goals-container');
}

/**
 * データ変更時の確認機能
 * @param {boolean} dataChanged - データが変更されたかどうか
 * @param {string} updateUrl - 更新URL
 */
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

// =============================================================================
// ログインページ機能
// =============================================================================

/**
 * タブ切り替え
 * @param {string} tabName - タブ名
 */
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

// =============================================================================
// 一覧表示機能
// =============================================================================

/**
 * 私の暮らし一覧を印刷
 */
function printIwlm() {
  printContent('私の暮らし一覧', '.table-container', '#printHeaderInfo');
}

/**
 * 私について一覧を印刷
 */
function printProfile() {
  printContent('私について一覧', '.table-container', '.table-info');
}

// =============================================================================
// フォーム初期化機能
// =============================================================================

/**
 * 私の暮らしフォームを初期化
 * @param {Object} checkboxData - チェックボックスデータ
 */
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

/**
 * 日記カレンダーを初期化
 * @param {number} year - 年
 * @param {number} month - 月
 * @param {Object} entries - 日記がある日付とタイトルの辞書
 */
function initDiaryCalendar(year, month, entries) {
  currentYear = year;
  currentMonth = month;
  diaryEntries = entries;

  setupCharCount();
  generateCalendar();
  setupModalClickOutside('diary-modal', closeDiaryModal);
}

/**
 * 日記一覧を初期化
 */
function initDiaryList() {
  setupModalClickOutside('image-modal', closeImageModal);
}

// =============================================================================
// グローバル初期化
// =============================================================================

/**
 * ページ固有の初期化処理
 */
function initPageSpecific() {
  // 日記一覧ページの自動初期化
  if (document.getElementById('image-modal')) {
    initDiaryList();
  }
}

// DOM読み込み完了時の初期化
document.addEventListener('DOMContentLoaded', function () {
  initPageSpecific();
});
