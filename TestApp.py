import Bonus
import pandas as pd

if __name__ == "__main__":

    print("Test Case 1: Using the Python List provided")

    order1 = [
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

    df = pd.DataFrame(order1)
    print(df)
    print("Result is aggregated based on OfferName and Statuses:-")
    print(Bonus.bonus_calculation(order1))

    print("Test Case 2: Using the Python List with multiple entries for the same memberId as below")

    order2 = [
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
        {
            "_id": "5-5feb-4b39-bde7-a07285969ffb",
            "status": "complete",
            "basePoints": 5000,
            "bonusPoints": 6000,
            "memberId": "4",
            "loyaltyProgramName": "Rewards and More",
            "offerName": "60% Bonus promo"
        },
        {
            "_id": "6-5feb-4b39-bde7-a07285969ffb",
            "status": "pending",
            "basePoints": 5000,
            "bonusPoints": 5000,
            "memberId": "2",
            "loyaltyProgramName": "Miles and Rewards",
            "offerName": "50% Bonus promo"
        },
    ]

    df2 = pd.DataFrame(order2)
    print(df2)
    print("Result aggregates the Basepoints and Bonuspoint all the records, but the Unique members column should not count the repeated member entries for the same OfferName and Status group:-")
    print(Bonus.bonus_calculation(order2))

    print("Test Case 3: Using the Python List with new OfferNames and Statuses to add to the existing list as below:")

    order3 = [
        {
            "_id": "5-5feb-4b39-bde7-a07285969ffb",
            "status": "canceled",
            "basePoints": 5000,
            "bonusPoints": 6000,
            "memberId": "5",
            "loyaltyProgramName": "Rewards and More",
            "offerName": "60% Bonus promo"
        },
        {
            "_id": "6-5feb-4b39-bde7-a07285969ffb",
            "status": "pending",
            "basePoints": 5000,
            "bonusPoints": 5000,
            "memberId": "6",
            "loyaltyProgramName": "Miles and Rewards",
            "offerName": "70% Bonus promo"
        },
    ]

    print("Existing Python List:-")
    print(df)
    print("Python List with new values for OfferName and Status:-")
    df3 = pd.DataFrame(order3)
    print(df3)
    print("Result aggregates the Basepoints and Bonuspoint all the new records as well")
    print(Bonus.bonus_calculation(order1+order3))

    print("Test Case 4: Using the Python List empty value for BasePoints and BonusPoints:")

    order4 = [
        {
            "_id": "7-5feb-4b39-bde7-a07285969ffb",
            "status": "canceled",
            "basePoints": None,
            "bonusPoints": 6000,
            "memberId": "7",
            "loyaltyProgramName": "Rewards and More",
            "offerName": "60% Bonus promo"
        },
        {
            "_id": "8-5feb-4b39-bde7-a07285969ffb",
            "status": "pending",
            "basePoints": 5000,
            "bonusPoints": None,
            "memberId": "8",
            "loyaltyProgramName": "Miles and Rewards",
            "offerName": "70% Bonus promo"
        },
    ]

    df4 = pd.DataFrame(order4)
    print(df4)
    print("Result aggregates the Basepoints and Bonuspoint even when the values are missing")
    print(Bonus.bonus_calculation(order4))
