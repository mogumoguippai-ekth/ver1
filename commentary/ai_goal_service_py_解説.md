# ai_goal_service.py コード解説

## 概要
Google Gemini APIを使用して、ユーザーの個人情報に基づいた動的な目標提案を生成するAIサービス。ユーザーの基本情報、プロフィール、暮らし情報を分析し、個人化された長期目標（3年後）と短期目標（1年以内）を提案します。

---

## 📋 目次

### 1. インポート・初期設定
- [1.1 必要なライブラリ](#11-必要なライブラリ)
- [1.2 ログ設定](#12-ログ設定)
- [1.3 環境変数読み込み](#13-環境変数読み込み)

### 2. AIGoalServiceクラス
- [2.1 クラス初期化](#21-クラス初期化)

### 3. データ準備機能
- [3.1 prepare_user_data関数](#31-prepare_user_data関数)

### 4. 目標生成メイン機能
- [4.1 generate_goals関数](#41-generate_goals関数)

### 5. パターン管理機能
- [5.1 _get_user_goal_pattern関数](#51-get_user_goal_pattern関数)
- [5.2 パターン別の特徴](#52-パターン別の特徴)

### 6. プロンプト生成機能
- [6.1 _create_prompt関数](#61-create_prompt関数)
- [6.2 各パターンの特徴](#62-各パターンの特徴)

### 7. レスポンス解析機能
- [7.1 _parse_response関数](#71-parse_response関数)

### 8. フォールバック機能
- [8.1 _get_fallback_goals関数](#81-get_fallback_goals関数)
- [8.2 各パターンのフォールバック目標](#82-各パターンのフォールバック目標)

### 9. ファクトリー関数
- [9.1 create_goal_service関数](#91-create_goal_service関数)

---

## 1. インポート・初期設定 <a id="1-インポート初期設定"></a>

### 1.1 必要なライブラリ <a id="11-必要なライブラリ"></a>
```python
import google.generativeai as genai
import os
import json
import logging
import hashlib
from dotenv import load_dotenv
from typing import Dict, Any, Optional
```

**説明:**
- **google.generativeai**: Google Gemini APIのPython SDK
- **os**: 環境変数の取得
- **json**: JSONデータの処理
- **logging**: ログ出力機能
- **hashlib**: ユーザーIDのハッシュ化
- **dotenv**: 環境変数の読み込み
- **typing**: 型ヒントの定義

### 1.2 ログ設定 <a id="12-ログ設定"></a>
```python
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

**説明:**
- **DEBUGレベル**: 詳細なログ出力
- **デバッグ用**: AIレスポンスや解析過程の追跡

### 1.3 環境変数読み込み <a id="13-環境変数読み込み"></a>
```python
load_dotenv(override=True)
```

**説明:**
- `.env`ファイルから環境変数を読み込み
- `override=True`で既存の環境変数を上書き

---

## 2. AIGoalServiceクラス <a id="2-aigoalserviceクラス"></a>

### 2.1 クラス初期化 <a id="21-クラス初期化"></a>
```python
class AIGoalService:
    """AI目標生成サービスクラス"""

    def __init__(self):
        """初期化"""
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model = None

        if self.api_key:
            try:
                # Gemini APIを設定
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel("gemini-flash-latest")
                logger.info("Google Gemini APIが正常に初期化されました")
            except Exception as e:
                logger.error(f"Google Gemini APIの初期化に失敗しました: {e}")
                self.model = None
        else:
            logger.warning("GOOGLE_API_KEY環境変数が設定されていません。フォールバック機能を使用します")
```

**説明:**
- **API設定**: Google Gemini APIの初期化
- **モデル選択**: `gemini-flash-latest`を使用（高速で軽量）
- **エラーハンドリング**: API初期化失敗時のフォールバック対応
- **環境変数チェック**: APIキーの存在確認

---

## 3. データ準備機能 <a id="3-データ準備機能"></a>

### 3.1 prepare_user_data関数 <a id="31-prepare_user_data関数"></a>
```python
def prepare_user_data(
    self,
    user_data: Dict[str, Any],
    profile_data: Optional[Dict[str, Any]],
    iwlm_data: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    ユーザーデータをAI用に整理する

    Args:
        user_data: ユーザー基本情報
        profile_data: プロフィール詳細情報
        iwlm_data: 私の暮らし情報

    Returns:
        整理されたユーザーデータ
    """
    prepared_data = {
        "基本情報": {
            "ユーザーID": user_data.get("user_id", ""),
            "氏名": user_data.get("name", ""),
            "ニックネーム": user_data.get("nickname", ""),
            "性別": user_data.get("gender", ""),
            "生年月日": user_data.get("birth_date", ""),
        }
    }

    # プロフィール情報を追加
    if profile_data:
        prepared_data["プロフィール詳細"] = {
            "住所": profile_data.get("address", ""),
            "家族構成": profile_data.get("family_members", ""),
            "配偶者について": profile_data.get("spouse_info", ""),
            "家族への想い": profile_data.get("family_feelings", ""),
            "友人関係": profile_data.get("friend_relationships", ""),
            "頼れる人": profile_data.get("reliable_people", ""),
            "得意・苦手": profile_data.get("strengths_weaknesses", ""),
            "性格・特徴": profile_data.get("personality", ""),
            "興味・関心": profile_data.get("interests", ""),
            "その他": profile_data.get("others", ""),
        }

    # 私の暮らし情報を追加
    if iwlm_data:
        prepared_data["暮らしの詳細"] = {
            "食事習慣": {
                "食事回数": iwlm_data.get("meal_frequency", ""),
                "朝食": iwlm_data.get("morning_meal_type", ""),
                "昼食": iwlm_data.get("lunch_meal_type", ""),
                "夕食": iwlm_data.get("dinner_meal_type", ""),
                "間食": iwlm_data.get("snac", ""),
                "お酒・タバコ": iwlm_data.get("habits_alc_smoke", ""),
            },
            "生活リズム": {
                "起床時間": iwlm_data.get("wakeup_time", ""),
                "就寝時間": iwlm_data.get("bedtime", ""),
                "家事": iwlm_data.get("daily_chores", ""),
                "自由時間": iwlm_data.get("free_times", ""),
                "会う人": iwlm_data.get("people_met", ""),
            },
            "生活習慣": {
                "トイレ様式": iwlm_data.get("toilet_style", ""),
                "入浴習慣": iwlm_data.get("bathing_habits", ""),
                "身だしなみ": iwlm_data.get("grooming_habits", ""),
                "美容院・散髪": iwlm_data.get("haircut_salon", ""),
            },
            "趣味・嗜好": {
                "好きな色": iwlm_data.get("favorite_color", ""),
                "好きな服装": iwlm_data.get("favorite_clothing", ""),
                "好きな履物": iwlm_data.get("favorite_footwear", ""),
                "好きな音楽": iwlm_data.get("favorite_music", ""),
                "好きなTV・ラジオ": iwlm_data.get("favorite_tv_radio", ""),
                "レジャー活動": iwlm_data.get("leisure_activities", ""),
            },
            "その他詳細": {
                "お気に入りの場所": iwlm_data.get("favorite_place", ""),
                "仕事状況": iwlm_data.get("job_status", ""),
                "興味・関心": iwlm_data.get("interests", ""),
                "得意・苦手": iwlm_data.get("strengths_and_weaknesses", ""),
                "性格・特徴": iwlm_data.get("characteristics", ""),
                "その他習慣": iwlm_data.get("others", ""),
            },
            "希望・不安": {
                "続けたいこと": iwlm_data.get("keep_doing", ""),
                "もっとやりたいこと": iwlm_data.get("future_activities", ""),
                "暮らしたい場所": iwlm_data.get("residence_type", ""),
                "不安・悲しみ": iwlm_data.get("anxiety_and_sadness", ""),
                "手伝ってほしいこと": iwlm_data.get("areas_of_support", ""),
                "将来のケア計画": iwlm_data.get("future_care_plan", ""),
            },
        }

    return prepared_data
```

**説明:**
- **データ構造化**: 3つのテーブルから取得したデータを統合
- **階層化**: 基本情報、プロフィール詳細、暮らしの詳細に分類
- **日本語ラベル**: AIが理解しやすい日本語の項目名
- **null安全**: `.get()`メソッドでデフォルト値を設定
- **包括的**: 食事、生活リズム、趣味、希望・不安まで網羅

---

## 4. 目標生成メイン機能 <a id="4-目標生成メイン機能"></a>

### 4.1 generate_goals関数 <a id="41-generate_goals関数"></a>
```python
def generate_goals(
    self,
    user_data: Dict[str, Any],
    profile_data: Optional[Dict[str, Any]] = None,
    iwlm_data: Optional[Dict[str, Any]] = None,
    user_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    AIを使用して目標を生成する

    Args:
        user_data: ユーザー基本情報
        profile_data: プロフィール詳細情報
        iwlm_data: 私の暮らし情報
        user_id: ユーザーID（パターン決定用）

    Returns:
        生成された目標データ
    """
    try:
        # AIモデルが利用できない場合はフォールバック
        if not self.model:
            logger.info("AIモデルが利用できません。フォールバック目標を使用します")
            return self._get_fallback_goals(user_id)

        # ユーザーデータを整理
        prepared_data = self.prepare_user_data(user_data, profile_data, iwlm_data)

        # AI用のプロンプトを作成（ユーザーIDを渡してパターンを決定）
        prompt = self._create_prompt(prepared_data, user_id)

        # AIに目標生成を依頼
        response = self.model.generate_content(prompt)
        # デバッグ: AIレスポンスをログ出力
        logger.info(f"AIレスポンス:\n{response.text}")

        # レスポンスを解析
        goals_data = self._parse_response(response.text)

        # デバッグ: 解析結果をログ出力
        logger.info(f"解析結果: {goals_data}")

        pattern_num = self._get_user_goal_pattern(user_id) if user_id else 0
        logger.info(f"AI目標生成が完了しました（ユーザーID: {user_id}, パターン: {pattern_num}）")
        return goals_data

    except Exception as e:
        logger.error(f"目標生成中にエラーが発生しました: {e}")
        return self._get_fallback_goals(user_id)
```

**説明:**
- **メイン処理**: AI目標生成の中心的な処理
- **フォールバック対応**: AIが利用できない場合の代替処理
- **エラーハンドリング**: 例外発生時の適切な処理
- **デバッグログ**: AIレスポンスと解析結果の詳細ログ
- **パターン管理**: ユーザーIDに基づく目標パターンの決定

---

## 5. パターン管理機能 <a id="5-パターン管理機能"></a>

### 5.1 _get_user_goal_pattern関数 <a id="51-get_user_goal_pattern関数"></a>
```python
def _get_user_goal_pattern(self, user_id: str) -> int:
    """
    ユーザーIDに基づいて目標提案パターンを決定する

    Args:
        user_id: ユーザーID

    Returns:
        パターン番号（0-4）
    """
    # ユーザーIDのハッシュ値からパターンを決定
    hash_value = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
    return hash_value % 5
```

**説明:**
- **ハッシュ化**: ユーザーIDをMD5ハッシュに変換
- **パターン決定**: ハッシュ値を5で割った余りでパターン番号（0-4）を決定
- **一貫性**: 同じユーザーIDは常に同じパターンに割り当て
- **分散**: ユーザーを5つのパターンに均等に分散

### 5.2 パターン別の特徴 <a id="52-パターン別の特徴"></a>
- **パターン0**: 健康・ライフスタイル重視
- **パターン1**: 社会貢献・人間関係重視
- **パターン2**: 学習・スキル向上重視
- **パターン3**: 経済・投資・貯蓄重視
- **パターン4**: 趣味・創造性重視

---

## 6. プロンプト生成機能 <a id="6-プロンプト生成機能"></a>

### 6.1 _create_prompt関数 <a id="61-create_prompt関数"></a>
```python
def _create_prompt(self, user_data: Dict[str, Any], user_id: str = None) -> str:
    """
    AI用のプロンプトを作成する

    Args:
        user_data: 整理されたユーザーデータ
        user_id: ユーザーID（パターン決定用）

    Returns:
        プロンプト文字列
    """
    # ユーザーIDに基づいてパターンを決定
    pattern = self._get_user_goal_pattern(user_id) if user_id else 0

    # パターン別のプロンプトテンプレート
    prompt_templates = [
        # パターン1: 健康・ライフスタイル重視
        """
以下のユーザー情報を基に、50代以降の人の3年後の長期目標とそれを達成するための3つの短期目標を提案してください。
ユーザーの強みを活かし、不安や課題を考慮した実現可能な目標を提案してください。
特に身体の健康、心の健康、社会的健康(社会参加)に焦点を当てた目標を提案してください。

ユーザー情報:
{user_info}

以下の形式で回答してください：

### 長期目標（3年後）
[健康とライフスタイルを重視した長期目標の内容を100文字以内で記載してください]

### 短期目標1
**テーマ**: [健康管理に関する目標テーマ]
**内容**: [具体的な目標内容]を100文字以内で記載してください]
**理由**: [なぜこの目標が重要なのか]

### 短期目標2
**テーマ**: [ライフスタイルに関する目標テーマ]
**内容**: [具体的な目標内容を100文字以内で記載してください]
**理由**: [なぜこの目標が重要なのか]

### 短期目標3
**テーマ**: [継続的な習慣形成に関する目標テーマ]
**内容**: [具体的な目標内容を100文字以内で記載してください]
**理由**: [なぜこの目標が重要なのか]

注意：必ず上記の形式で回答し、各短期目標にはテーマ、内容、理由を全て含めてください。

注意事項：
- 運動、食事、睡眠、ストレス管理などの健康要素を含めてください
- 具体的で測定可能な目標にしてください
- 日本語で回答してください、長期目標文末と短期目標内容文末に文字数表示は不要です    
""",
        # 他のパターンも同様の構造...
    ]

    # 選択されたパターンのプロンプトを使用
    template = prompt_templates[pattern]
    user_info = json.dumps(user_data, ensure_ascii=False, indent=2)

    return template.format(user_info=user_info)
```

**説明:**
- **パターン別テンプレート**: 5つの異なる目標アプローチ
- **構造化プロンプト**: AIが理解しやすい明確な指示
- **日本語対応**: `ensure_ascii=False`で日本語を正しく処理
- **形式指定**: マークダウン形式での回答要求
- **制約条件**: 文字数制限と具体的な目標要求

### 6.2 各パターンの特徴 <a id="62-各パターンの特徴"></a>

#### パターン0: 健康・ライフスタイル重視
- **焦点**: 身体の健康、心の健康、社会的健康
- **要素**: 運動、食事、睡眠、ストレス管理

#### パターン1: 社会貢献・人間関係重視
- **焦点**: 社会貢献と人間関係の構築
- **要素**: ボランティア活動、コミュニティ参加、近所の人との交流

#### パターン2: 学習・スキル向上重視
- **焦点**: 学習とスキル向上
- **要素**: 読書、オンライン学習、資格取得、趣味の習得

#### パターン3: 経済・投資・貯蓄重視
- **焦点**: 経済的安定と投資・貯蓄
- **要素**: 副業、投資、専門資格、人脈構築

#### パターン4: 趣味・創造性重視
- **焦点**: 趣味と創造性の発揮
- **要素**: 芸術、音楽、スポーツ、料理、旅行、読書

---

## 7. レスポンス解析機能 <a id="7-レスポンス解析機能"></a>

### 7.1 _parse_response関数 <a id="71-parse_response関数"></a>
```python
def _parse_response(self, response_text: str) -> Dict[str, Any]:
    """
    AIのレスポンスを解析して構造化データに変換する

    Args:
        response_text: AIからのレスポンス

    Returns:
        構造化された目標データ
    """
    try:
        logger.info(f"レスポンス解析開始: {len(response_text)}文字")

        # 長期目標を抽出
        long_term_goal = ""
        short_term_goals = []

        lines = response_text.split("\n")
        current_section = None
        current_goal = {}

        for i, line in enumerate(lines):
            line = line.strip()
            logger.debug(f"行 {i}: {line}")

            if line.startswith("### 長期目標") or "長期目標" in line:
                current_section = "long_term"
                continue
            elif line.startswith("### 短期目標") or "短期目標" in line:
                if current_goal and all(key in current_goal for key in ["theme", "content", "reason"]):
                    short_term_goals.append(current_goal)
                    logger.info(f"短期目標追加: {current_goal}")
                current_section = "short_term"
                current_goal = {}
                continue
            elif line.startswith("**テーマ**") or line.startswith("テーマ"):
                theme_text = (
                    line.replace("**テーマ**:", "")
                    .replace("**テーマ**:", "")
                    .replace("テーマ:", "")
                    .strip()
                )
                current_goal["theme"] = theme_text
                logger.debug(f"テーマ設定: {theme_text}")
            elif line.startswith("**内容**") or line.startswith("内容"):
                content_text = (
                    line.replace("**内容**:", "").replace("**内容**:", "").replace("内容:", "").strip()
                )
                current_goal["content"] = content_text
                logger.debug(f"内容設定: {content_text}")
            elif line.startswith("**理由**") or line.startswith("理由"):
                reason_text = (
                    line.replace("**理由**:", "").replace("**理由**:", "").replace("理由:", "").strip()
                )
                current_goal["reason"] = reason_text
                logger.debug(f"理由設定: {reason_text}")
            elif current_section == "long_term" and line and not line.startswith("###"):
                long_term_goal += line + " "
            elif (
                current_section == "short_term"
                and line
                and not line.startswith("**")
                and not line.startswith("###")
            ):
                if "content" in current_goal:
                    current_goal["content"] += " " + line

        # 最後の短期目標を追加
        if current_goal and all(key in current_goal for key in ["theme", "content", "reason"]):
            short_term_goals.append(current_goal)
            logger.info(f"最後の短期目標追加: {current_goal}")

        logger.info(f"解析結果: 長期目標={long_term_goal[:50]}..., 短期目標数={len(short_term_goals)}")

        # データの検証とフォールバック
        if not long_term_goal.strip():
            logger.warning("長期目標が解析できませんでした")
            long_term_goal = "健康で充実した生活を送る"

        if not short_term_goals:
            logger.warning("短期目標が解析できませんでした")
            short_term_goals = [
                {
                    "theme": "健康維持",
                    "content": "適度な運動と規則正しい生活リズムを心がける",
                    "reason": "心身の健康は充実した生活の基盤となるため",
                },
                {
                    "theme": "社会参加",
                    "content": "地域の活動や趣味を通じて人とのつながりを広げる",
                    "reason": "社会的なつながりは生活の充実感を高めるため",
                },
                {
                    "theme": "自己実現",
                    "content": "興味のあることを学んだり、新しい体験に挑戦する",
                    "reason": "成長感や達成感を得ることで生活に張りが出るため",
                },
            ]

        return {
            "long_term_goal": long_term_goal.strip(),
            "short_term_goals": short_term_goals[:3],  # 最大3つまで
        }

    except Exception as e:
        logger.error(f"レスポンス解析中にエラーが発生しました: {e}")
        logger.error(f"レスポンス内容: {response_text}")
        return self._get_fallback_goals()
```

**説明:**
- **行単位解析**: レスポンスを行ごとに分割して解析
- **セクション検出**: 長期目標・短期目標のセクションを識別
- **マークダウン解析**: **テーマ**、**内容**、**理由**の抽出
- **データ検証**: 解析結果の妥当性チェック
- **フォールバック**: 解析失敗時のデフォルト目標提供
- **デバッグログ**: 解析過程の詳細ログ出力

---

## 8. フォールバック機能 <a id="8-フォールバック機能"></a>

### 8.1 _get_fallback_goals関数 <a id="81-get_fallback_goals関数"></a>
```python
def _get_fallback_goals(self, user_id: str = None) -> Dict[str, Any]:
    """
    AIが利用できない場合のフォールバック目標

    Args:
        user_id: ユーザーID（パターン決定用）

    Returns:
        デフォルトの目標データ
    """
    # ユーザーIDに基づいてパターンを決定
    pattern = self._get_user_goal_pattern(user_id) if user_id else 0

    # パターン別のフォールバック目標
    fallback_goals = [
        # パターン1: 健康・ライフスタイル重視
        {
            "long_term_goal": "健康で充実した毎日を送り、規則正しい生活リズムを確立して自分らしいライフスタイルを築く",
            "short_term_goals": [
                {
                    "theme": "健康管理",
                    "content": "毎日の運動習慣とバランスの良い食事を心がける",
                    "reason": "健康的な体づくりは充実した生活の基盤となるため",
                },
                {
                    "theme": "生活リズム",
                    "content": "規則正しい睡眠時間と朝の時間を有効活用する",
                    "reason": "良い生活リズムは心身の健康と生産性を向上させるため",
                },
                {
                    "theme": "習慣形成",
                    "content": "小さな良い習慣を継続的に積み重ねる",
                    "reason": "継続的な習慣が長期的な成果につながるため",
                },
            ],
        },
        # 他のパターンも同様の構造...
    ]

    return fallback_goals[pattern]
```

**説明:**
- **パターン別フォールバック**: 5つのパターンに対応したデフォルト目標
- **一貫性**: AIが利用できない場合でも同じパターンを使用
- **完全性**: 長期目標と3つの短期目標を提供
- **構造化**: テーマ、内容、理由の3要素を含む

### 8.2 各パターンのフォールバック目標 <a id="82-各パターンのフォールバック目標"></a>

#### パターン0: 健康・ライフスタイル重視
- **長期目標**: 健康で充実した毎日と生活リズムの確立
- **短期目標**: 健康管理、生活リズム、習慣形成

#### パターン1: 社会貢献・人間関係重視
- **長期目標**: 地域社会への貢献と人間関係の構築
- **短期目標**: 地域参加、家族関係、新しい出会い

#### パターン2: 学習・スキル向上重視
- **長期目標**: 継続的な学習とスキル向上
- **短期目標**: 知識習得、スキル向上、学習習慣

#### パターン3: 経済・キャリア重視
- **長期目標**: 経済的安定と専門性向上
- **短期目標**: 経済管理、専門性向上、ネットワーク構築

#### パターン4: 趣味・創造性重視
- **長期目標**: 趣味と創造的活動による豊かな心の世界
- **短期目標**: 新しい趣味、創造的表現、趣味の交流

---

## 9. ファクトリー関数 <a id="9-ファクトリー関数"></a>

### 9.1 create_goal_service関数 <a id="91-create_goal_service関数"></a>
```python
def create_goal_service() -> AIGoalService:
    """
    AI目標生成サービスのインスタンスを作成する

    Returns:
        AIGoalServiceインスタンス
    """
    return AIGoalService()
```

**説明:**
- **ファクトリーパターン**: インスタンス作成の統一インターフェース
- **依存性注入**: 他のモジュールからの呼び出し用
- **シンプル**: インスタンス化の簡素化

---

## まとめ

ai_goal_service.pyは「私の望む暮らし」アプリケーションのAI目標生成機能を担当する重要なファイルです。

### 主要機能
1. **AI目標生成**: Google Gemini APIを使用した動的な目標提案
2. **パターン管理**: ユーザーIDに基づく5つの目標パターン
3. **データ統合**: 基本情報、プロフィール、暮らし情報の統合分析
4. **レスポンス解析**: AIレスポンスの構造化データ変換
5. **フォールバック**: AI利用不可時の代替目標提供

### 技術的特徴
- **Google Gemini API**: 最新の生成AI技術の活用
- **パターン分散**: ユーザーIDハッシュによる均等分散
- **構造化プロンプト**: 明確で一貫したAI指示
- **エラーハンドリング**: 包括的な例外処理とフォールバック
- **デバッグ機能**: 詳細なログ出力による問題追跡

### 目標パターン
1. **健康・ライフスタイル重視**: 身体・心・社会的健康
2. **社会貢献・人間関係重視**: 地域参加と人間関係構築
3. **学習・スキル向上重視**: 継続的な成長とスキル開発
4. **経済・投資・貯蓄重視**: 経済的安定と専門性向上
5. **趣味・創造性重視**: 創造的活動と趣味の追求

### データ構造
- **長期目標**: 3年後の具体的な目標
- **短期目標**: 1年以内の3つの具体的な目標
- **構造化**: テーマ、内容、理由の3要素

このサービスは、ユーザーの個性と状況に応じた個人化された目標提案を提供し、より充実した生活の実現をサポートします。
