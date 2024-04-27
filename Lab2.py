from statistics import median
def display_main_menu(listoNume):
    print("List:", listoNume)

def get_user_input(li):
    listoNum1 = li.split(",")
    listoNum = [float(i) for i in listoNum1]
    return listoNum

def calc_average_temperature(listoNume):
    Sum = sum(listoNume)
    Num = len(listoNume)
    average = Sum/Num
    aver = float(average)
    return aver

def calc_min_max_temperature(listoNume):
    Min = min(listoNume)
    Max = max(listoNume)
    return Min, Max

def sort_temperature(listoNume):
    listoNume.sort()
    return listoNume

def calc_median_temperature(listoNume):
    med1 = median(listoNume)
    return med1

def main():
    listoNume = get_user_input(input())
    display_main_menu(listoNume)
    avr = calc_average_temperature(listoNume)
    print("Average: " + str(avr))
    temp = calc_min_max_temperature(listoNume)
    print(f"Minimum and Maximum: {list(temp)}")
    sort1 = sort_temperature(listoNume)
    print("Sorted list:", sort1)
    median1 = calc_median_temperature(listoNume)
    print("Median: " + str(median1))

if __name__ == "__main__":
    main()