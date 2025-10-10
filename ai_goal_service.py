"""
AI Goal Generation Service using Google Gemini API
外部無料AIサービス（Google Gemini API）を使用して動的に目標提案を生成するサービス
"""

import google.generativeai as genai
import os
import json
import logging
from typing import Dict, Any, Optional

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
                self.model = genai.GenerativeModel("gemini-1.5-flash")
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
    ) -> Dict[str, Any]:
        """
        AIを使用して目標を生成する

        Args:
            user_data: ユーザー基本情報
            profile_data: プロフィール詳細情報
            iwlm_data: 私の暮らし情報

        Returns:
            生成された目標データ
        """
        try:
            # AIモデルが利用できない場合はフォールバック
            if not self.model:
                logger.info("AIモデルが利用できません。フォールバック目標を使用します")
                return self._get_fallback_goals()

            # ユーザーデータを整理
            prepared_data = self.prepare_user_data(user_data, profile_data, iwlm_data)

            # AI用のプロンプトを作成
            prompt = self._create_prompt(prepared_data)

            # AIに目標生成を依頼
            response = self.model.generate_content(prompt)

            # レスポンスを解析
            goals_data = self._parse_response(response.text)

            logger.info("AI目標生成が完了しました")
            return goals_data

        except Exception as e:
            logger.error(f"目標生成中にエラーが発生しました: {e}")
            return self._get_fallback_goals()

    def _create_prompt(self, user_data: Dict[str, Any]) -> str:
        """
        AI用のプロンプトを作成する

        Args:
            user_data: 整理されたユーザーデータ

        Returns:
            プロンプト文字列
        """
        prompt = f"""
以下のユーザー情報を基に、3年後の長期目標とそれを達成するための3つの短期目標を提案してください。
ユーザーの強みを活かし、不安や課題を考慮した実現可能な目標を提案してください。

ユーザー情報:
{json.dumps(user_data, ensure_ascii=False, indent=2)}

以下の形式で回答してください：

### 長期目標（3年後）
[具体的な長期目標の内容]

### 短期目標1
**テーマ**: [目標のテーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標2
**テーマ**: [目標のテーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

### 短期目標3
**テーマ**: [目標のテーマ]
**内容**: [具体的な目標内容]
**理由**: [なぜこの目標が重要なのか]

注意事項：
- ユーザーの現在の状況や能力を考慮した現実的な目標を提案してください
- 健康、社会的つながり、趣味・活動のバランスを考慮してください
- 具体的で測定可能な目標にしてください
- 日本語で回答してください
"""
        return prompt

    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """
        AIのレスポンスを解析して構造化データに変換する

        Args:
            response_text: AIからのレスポンス

        Returns:
            構造化された目標データ
        """
        try:
            # 長期目標を抽出
            long_term_goal = ""
            short_term_goals = []

            lines = response_text.split("\n")
            current_section = None
            current_goal = {}

            for line in lines:
                line = line.strip()

                if line.startswith("### 長期目標"):
                    current_section = "long_term"
                    continue
                elif line.startswith("### 短期目標"):
                    if current_goal:
                        short_term_goals.append(current_goal)
                    current_section = "short_term"
                    current_goal = {}
                    continue
                elif line.startswith("**テーマ**:"):
                    current_goal["theme"] = line.replace("**テーマ**:", "").strip()
                elif line.startswith("**内容**:"):
                    current_goal["content"] = line.replace("**内容**:", "").strip()
                elif line.startswith("**理由**:"):
                    current_goal["reason"] = line.replace("**理由**:", "").strip()
                elif current_section == "long_term" and line:
                    long_term_goal += line + " "
                elif current_section == "short_term" and line and not line.startswith("**"):
                    if "content" in current_goal:
                        current_goal["content"] += " " + line

            # 最後の短期目標を追加
            if current_goal:
                short_term_goals.append(current_goal)

            return {
                "long_term_goal": long_term_goal.strip(),
                "short_term_goals": short_term_goals[:3],  # 最大3つまで
            }

        except Exception as e:
            logger.error(f"レスポンス解析中にエラーが発生しました: {e}")
            return self._get_fallback_goals()

    def _get_fallback_goals(self) -> Dict[str, Any]:
        """
        AIが利用できない場合のフォールバック目標

        Returns:
            デフォルトの目標データ
        """
        return {
            "long_term_goal": "健康で充実した毎日を送り、大切な人とのつながりを深めながら、自分らしい生活を築く",
            "short_term_goals": [
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
            ],
        }


def create_goal_service() -> AIGoalService:
    """
    AI目標生成サービスのインスタンスを作成する

    Returns:
        AIGoalServiceインスタンス
    """
    return AIGoalService()
