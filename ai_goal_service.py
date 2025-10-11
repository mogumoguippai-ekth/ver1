"""
AI Goal Generation Service using Google Gemini API
外部無料AIサービス（Google Gemini API）を使用して動的に目標提案を生成するサービス
"""

import google.generativeai as genai
import os
import json
import logging
import hashlib
from dotenv import load_dotenv
from typing import Dict, Any, Optional


# ログ設定
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv(override=True)


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
以下のユーザー情報を基に、3年後の長期目標とそれを達成するための3つの短期目標を提案してください。
ユーザーの強みを活かし、不安や課題を考慮した実現可能な目標を提案してください。
特に健康管理とライフスタイルの改善に焦点を当てた目標を提案してください。

ユーザー情報:
{user_info}

以下の形式で回答してください：

### 長期目標（3年後）
[健康とライフスタイルを重視した具体的な長期目標の内容]

### 短期目標1
**テーマ**: [健康管理に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標2
**テーマ**: [ライフスタイル改善に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標3
**テーマ**: [継続的な習慣形成に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

注意：必ず上記の形式で回答し、各短期目標にはテーマ、内容、理由を全て含めてください。

注意事項：
- ユーザーの現在の健康状態や生活習慣を考慮した現実的な目標を提案してください
- 運動、食事、睡眠、ストレス管理などの健康要素を含めてください
- 具体的で測定可能な目標にしてください
- 日本語で回答してください
""",
            # パターン2: 社会貢献・人間関係重視
            """
以下のユーザー情報を基に、3年後の長期目標とそれを達成するための3つの短期目標を提案してください。
ユーザーの強みを活かし、不安や課題を考慮した実現可能な目標を提案してください。
特に社会貢献と人間関係の構築に焦点を当てた目標を提案してください。

ユーザー情報:
{user_info}

以下の形式で回答してください：

### 長期目標（3年後）
[社会貢献と人間関係を重視した具体的な長期目標の内容]

### 短期目標1
**テーマ**: [地域社会との関わりに関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標2
**テーマ**: [家族・友人との関係強化に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標3
**テーマ**: [新しい人間関係構築に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

注意：必ず上記の形式で回答し、各短期目標にはテーマ、内容、理由を全て含めてください。

注意事項：
- ユーザーの現在の人間関係や社会的立場を考慮した現実的な目標を提案してください
- ボランティア活動、コミュニティ参加、家族との時間などを含めてください
- 具体的で測定可能な目標にしてください
- 日本語で回答してください
""",
            # パターン3: 学習・スキル向上重視
            """
以下のユーザー情報を基に、3年後の長期目標とそれを達成するための3つの短期目標を提案してください。
ユーザーの強みを活かし、不安や課題を考慮した実現可能な目標を提案してください。
特に学習とスキル向上に焦点を当てた目標を提案してください。

ユーザー情報:
{user_info}

以下の形式で回答してください：

### 長期目標（3年後）
[学習とスキル向上を重視した具体的な長期目標の内容]

### 短期目標1
**テーマ**: [新しい知識習得に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標2
**テーマ**: [実用的なスキル向上に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標3
**テーマ**: [学習習慣の確立に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

注意：必ず上記の形式で回答し、各短期目標にはテーマ、内容、理由を全て含めてください。

注意事項：
- ユーザーの現在の知識レベルや興味分野を考慮した現実的な目標を提案してください
- 読書、オンライン学習、資格取得、趣味の習得などを含めてください
- 具体的で測定可能な目標にしてください
- 日本語で回答してください
""",
            # パターン4: 経済・キャリア重視
            """
以下のユーザー情報を基に、3年後の長期目標とそれを達成するための3つの短期目標を提案してください。
ユーザーの強みを活かし、不安や課題を考慮した実現可能な目標を提案してください。
特に経済的安定とキャリア発展に焦点を当てた目標を提案してください。

ユーザー情報:
{user_info}

以下の形式で回答してください：

### 長期目標（3年後）
[経済的安定とキャリア発展を重視した具体的な長期目標の内容]

### 短期目標1
**テーマ**: [収入向上・経済管理に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標2
**テーマ**: [スキルアップ・専門性向上に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標3
**テーマ**: [ネットワーク構築・機会創出に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

注意：必ず上記の形式で回答し、各短期目標にはテーマ、内容、理由を全て含めてください。

注意事項：
- ユーザーの現在の職業や経済状況を考慮した現実的な目標を提案してください
- 副業、投資、専門資格、人脈構築などを含めてください
- 具体的で測定可能な目標にしてください
- 日本語で回答してください
""",
            # パターン5: 趣味・創造性重視
            """
以下のユーザー情報を基に、3年後の長期目標とそれを達成するための3つの短期目標を提案してください。
ユーザーの強みを活かし、不安や課題を考慮した実現可能な目標を提案してください。
特に趣味と創造性の発揮に焦点を当てた目標を提案してください。

ユーザー情報:
{user_info}

以下の形式で回答してください：

### 長期目標（3年後）
[趣味と創造性を重視した具体的な長期目標の内容]

### 短期目標1
**テーマ**: [新しい趣味・活動開始に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標2
**テーマ**: [創造的表現・作品制作に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標3
**テーマ**: [趣味を通じた交流・コミュニティ参加に関する目標テーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

注意：必ず上記の形式で回答し、各短期目標にはテーマ、内容、理由を全て含めてください。

注意事項：
- ユーザーの現在の趣味や興味分野を考慮した現実的な目標を提案してください
- 芸術、音楽、スポーツ、料理、旅行、読書など様々な趣味を含めてください
- 具体的で測定可能な目標にしてください
- 日本語で回答してください
""",
        ]

        # 選択されたパターンのプロンプトを使用
        template = prompt_templates[pattern]
        user_info = json.dumps(user_data, ensure_ascii=False, indent=2)

        return template.format(user_info=user_info)

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
            # パターン2: 社会貢献・人間関係重視
            {
                "long_term_goal": "地域社会に貢献しながら、家族や友人との絆を深め、豊かな人間関係を築く",
                "short_term_goals": [
                    {
                        "theme": "地域参加",
                        "content": "地域のイベントやボランティア活動に積極的に参加する",
                        "reason": "地域社会との関わりは生活に充実感と意味をもたらすため",
                    },
                    {
                        "theme": "家族関係",
                        "content": "家族や友人との時間を大切にし、関係を深める",
                        "reason": "大切な人との関係は人生の最も重要な財産であるため",
                    },
                    {
                        "theme": "新しい出会い",
                        "content": "趣味や活動を通じて新しい人との出会いを求める",
                        "reason": "新しい人間関係は視野を広げ、人生を豊かにするため",
                    },
                ],
            },
            # パターン3: 学習・スキル向上重視
            {
                "long_term_goal": "継続的な学習を通じて新しい知識とスキルを身につけ、自分自身を成長させ続ける",
                "short_term_goals": [
                    {
                        "theme": "知識習得",
                        "content": "興味のある分野について本やオンライン学習で知識を深める",
                        "reason": "新しい知識は視野を広げ、人生を豊かにするため",
                    },
                    {
                        "theme": "スキル向上",
                        "content": "実用的なスキルや趣味のスキルを段階的に向上させる",
                        "reason": "スキルの向上は自信と達成感をもたらすため",
                    },
                    {
                        "theme": "学習習慣",
                        "content": "毎日少しずつでも学習する時間を作る",
                        "reason": "継続的な学習習慣が長期的な成長につながるため",
                    },
                ],
            },
            # パターン4: 経済・キャリア重視
            {
                "long_term_goal": "経済的な安定を築きながら、自分の専門性を高め、充実したキャリアを形成する",
                "short_term_goals": [
                    {
                        "theme": "経済管理",
                        "content": "家計の見直しと投資の基礎知識を身につける",
                        "reason": "経済的な安定は安心した生活の基盤となるため",
                    },
                    {
                        "theme": "専門性向上",
                        "content": "現在の仕事に関連するスキルや資格を取得する",
                        "reason": "専門性の向上はキャリア発展と収入向上につながるため",
                    },
                    {
                        "theme": "ネットワーク構築",
                        "content": "業界の人脈を広げ、新しい機会を創出する",
                        "reason": "人脈は新しいチャンスと情報をもたらすため",
                    },
                ],
            },
            # パターン5: 趣味・創造性重視
            {
                "long_term_goal": "自分らしい趣味や創造的な活動を通じて、豊かな心の世界を築き、人生を彩り豊かにする",
                "short_term_goals": [
                    {
                        "theme": "新しい趣味",
                        "content": "今まで興味があった新しい趣味や活動を始める",
                        "reason": "新しい趣味は人生に新鮮さと楽しみをもたらすため",
                    },
                    {
                        "theme": "創造的表現",
                        "content": "芸術、音楽、料理などで自分なりの作品を創作する",
                        "reason": "創造的な活動は心の充実感と達成感をもたらすため",
                    },
                    {
                        "theme": "趣味の交流",
                        "content": "同じ趣味を持つ人との交流やコミュニティに参加する",
                        "reason": "趣味を通じた交流は新しい友達と楽しみを創出するため",
                    },
                ],
            },
        ]

        return fallback_goals[pattern]


def create_goal_service() -> AIGoalService:
    """
    AI目標生成サービスのインスタンスを作成する

    Returns:
        AIGoalServiceインスタンス
    """
    return AIGoalService()
