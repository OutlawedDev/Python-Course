import math

angle_deg = float(input("Enter an angle in degrees: "))

angle_rad = math.radians(angle_deg)

sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)

print(f"\nFor angle {angle_deg} degrees:")
print(f"Sin({angle_deg}) = {sin_val:.4f}")
print(F"Cos({angle_deg}) = {cos_val:.4f}")
print(f"Tan({angle_deg}) = {tan_val:.4f}")
