from ai_goal_service import AIGoalService

test_gemini = AIGoalService()


goal = test_gemini.generate_goals(
    user_data={
        "name": "test",
        "age": 20,
        "gender": "male",
    }
)

print(goal["long_term_goal"])
