import Bonus


if __name__ == "__main__":

    print("Test Case 1:")

    orders = [
        {
            "_id": "1-5feb-4b39-bde7-a07285969ffb",
            "status": "complete",
            "basePoints": 10000,
            "bonusPoints": 5000,
            "memberId": "1",
            "loyaltyProgramName": "Miles and Rewards",
            "offerName": "50% Bonus promo"
        },
        {
            "_id": "2-5feb-4b39-bde7-a07285969ffb",
            "status": "pending",
            "basePoints": 5000,
            "bonusPoints": 2500,
            "memberId": "2",
            "loyaltyProgramName": "Miles and Rewards",
            "offerName": "50% Bonus promo"
        },
        {
            "_id": "3-5feb-4b39-bde7-a07285969ffb",
            "status": "complete",
            "basePoints": 10000,
            "bonusPoints": 6000,
            "memberId": "3",
            "loyaltyProgramName": "Rewards and More",
            "offerName": "60% Bonus promo"
        },
        {
            "_id": "4-5feb-4b39-bde7-a07285969ffb",
            "status": "complete",
            "basePoints": 15000,
            "bonusPoints": 9000,
            "memberId": "4",
            "loyaltyProgramName": "Rewards and More",
            "offerName": "60% Bonus promo"
        },
    ]

    print(Bonus.bonus_calculation(orders))
