import time

class AURAEngine:
    def __init__(self):
        print("[INIT] AURA Engine Online - Micro-Friction & Future Lifestyle Simulator")

    def analyze_friction(self, problem_desc, frequency_per_week, minutes_lost):
        monthly_time_lost = (frequency_per_week * minutes_lost * 4) / 60
        print(f"\n[ANALYZING] Problem: '{problem_desc}'")
        print(f"[PATTERN DETECTED] Frequency: {frequency_per_week}x/week")
        print(f"[IMPACT MEASURED] Cumulative Lost Time: {monthly_time_lost:.1f} Hours/Month")
        
        if monthly_time_lost > 5:
            action = "HIGH PRIORITY: Requires immediate intervention / route optimization."
        else:
            action = "MODERATE: Personal routine adjustment recommended."
            
        print(f"[ACTIONABLE INSIGHT] {action}")
        return monthly_time_lost

if __name__ == "__main__":
    aura = AURAEngine()
    # Sample Case Study: Late College Bus
    aura.analyze_friction("College Bus Delay on Route 4", frequency_per_week=5, minutes_lost=15)
