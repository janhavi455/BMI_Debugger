#BMI DEBUGGER
# 1.calculate_BMI
# 2.label_BMI
# 3.categorize_BMI

def calculate_BMI(height,weight):
    """
    Calculate BMI given weight (kg) and height (meters)

    Args:
        weight (float): weight in kg
        height (float): height in meters

    Returns:
        float: BMI value
    """
    if height <=0:
        raise ValueError("Height can't be negative or zero.")
    if weight==0:
        return 0
    return weight/ (height**2)


def label_BMI(bmi):
    """
    labels BMI in "Normal" or "High"
    
    Args:
    bmi (float) : BMI value
    
    Returns:
    str: "Normal" if BMI<25 else "High"
    """
    if bmi==0:
        return "0"
    if bmi>25:
        return "High"
    return "Normal"

def categorize_BMI(height, weight):
    """
    Main function which Categorizes BMI 

    Args:
    height (float)
    weight (float)

    Returns:
    str: BMI category
    """
    bmi= calculate_BMI(height, weight)
    bmi_category= label_BMI(bmi)
    return bmi_category

#Example
if __name__=="__main__":
    samples= [
        (70, 1.75),
        (80,1.6),
        (50,1.5),
        (0,1.7),
        (70,0)
    ]
    for w,h in samples:
        try:
            print(categorize_BMI(h,w))
        except ValueError as e:
            print(f"Error for weight: {w} and Height: {h} -> {e}")
   


    

