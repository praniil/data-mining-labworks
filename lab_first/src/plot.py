import matplotlib.pyplot as plt

def main():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    laptop_sales = [12000, 15000, 17000, 13000, 16000, 18000]
    smartphone_sales = [10000, 14000, 16000, 12000, 15500, 17500]
    plt.plot(months, laptop_sales, label="laptop_sales")
    plt.plot(months, smartphone_sales, label="smartphone_sales")
    plt.xlabel('months')
    plt.ylabel('sales')
    plt.savefig("months_vs_sales.png")
    plt.close()
    return 0

if __name__ == '__main__':
    main()