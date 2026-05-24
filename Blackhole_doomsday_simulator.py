import math
from playsound3 import playsound

def Blackhole_doomsday_simulator():


    print("Blackhole doomsday simulator")

    LIGHT_YEAR_TO_KM = 9.461e12 
    AU_TO_KM = 1.496e8
    BH_SPEED_KMS = 200.0 
    SEC_IN_YEAR = 31536000

    try:
        mass = float(input("Please enter the mass of the blackhole(solar masses): "))
        lightyear_distance = float(input("Please enter how many light years far you want the blackhole to be from the solar system: "))
    except ValueError:
        print("Please enter valid numbers")

    event_horizon_km = mass * 3.0
    km =  lightyear_distance * LIGHT_YEAR_TO_KM
    destruction = 5 * AU_TO_KM

    if km <= destruction:
        print("🚨We are done for")
        playsound('ad.mp3')

    Distance_to_travel = km - destruction
    total_seconds = Distance_to_travel / BH_SPEED_KMS
    total_years = total_seconds / SEC_IN_YEAR

    print("\n =========== SIMULATOR RESULTS ===========")
    print(f"Blackhole mass: {mass:,} Solar masses")
    print(f"Event horizon radius: {event_horizon_km:,.2f} km")
    print(f"Destruction triggers at: {destruction:,.0f} km from Earth (5 AU)")
    print("----------------------------------------------------------")

    
    if total_years > 1000000:
        x = 1000000/1e6
        print(f"We are safe for {x:,.2f} amount of years")
    elif total_years > 1:
        print(f"Doomsday in {total_years:,.2f} years")
    else:
        t = total_years * 365
        print(f"Doomsday in {t:,.2f} amount of days")

if __name__ == "__main__":
    Blackhole_doomsday_simulator()
