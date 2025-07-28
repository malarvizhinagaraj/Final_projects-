def calculate_total_calories(logs):
    return sum(log.calories for log in logs)

def generate_progress_data(measurements):
    return [{"date": m.date.strftime('%Y-%m-%d'), "weight": m.weight} for m in measurements]
