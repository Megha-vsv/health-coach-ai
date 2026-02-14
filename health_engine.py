def analyze_health(steps, sleep_hours, calories, heart_rate):
    recommendations = []
    risk_score = 0

    # Step analysis
    if steps < 5000:
        recommendations.append("Increase daily steps to at least 8000.")
        risk_score += 1

    # Sleep analysis
    if sleep_hours < 6:
        recommendations.append("Improve sleep quality. Aim for 7-8 hours.")
        risk_score += 1

    # Calorie analysis
    if calories > 2500:
        recommendations.append("Reduce calorie intake to maintain balance.")
        risk_score += 1

    # Heart rate analysis
    if heart_rate > 100:
        recommendations.append("High resting heart rate detected. Consider medical consultation.")
        risk_score += 1

    # Final health status
    if risk_score == 0:
        status = "Excellent Health"
    elif risk_score <= 2:
        status = "Moderate Risk"
    else:
        status = "High Risk"

    return status, recommendations