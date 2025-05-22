
---

## 🎲 Bonus: Sample Code for the Game

Here’s a simple version of the game logic:

```python
import random

def generate_transaction():
    amount = random.uniform(50, 5000)
    location_risk = random.choice(['low', 'medium', 'high'])
    is_suspicious = random.random() < 0.3  # 30% chance of being fraud
    return {
        'amount': round(amount, 2),
        'location_risk': location_risk,
        'is_fraud': is_suspicious
    }

def evaluate_transaction(tx):
    if tx['amount'] > 3000 and tx['location_risk'] == 'high':
        return True
    elif tx['amount'] > 4000:
        return True
    else:
        return False

def fraud_hunter_game():
    print("🕵️‍♂️ Welcome to Fraud Hunter: The Challenge!")
    print("You are a fraud analyst. Type 'reject' or 'approve'.\n")

    score = 0
    lives = 3

    while lives > 0:
        tx = generate_transaction()
        print(f"Transaction: ${tx['amount']} from {tx['location_risk'].upper()} risk region.")

        choice = input("Your decision (reject/approve): ").strip().lower()
        predicted_fraud = evaluate_transaction(tx)
        actual_fraud = tx['is_fraud']

        if predicted_fraud == actual_fraud:
            print("✅ Correct decision!")
            score += 10
        else:
            print("❌ Wrong decision.")
            lives -= 1

        print(f"Score: {score} | Lives Left: {lives}\n")

    print("💀 Game Over! Final Score:", score)

if __name__ == "__main__":
    fraud_hunter_game()
