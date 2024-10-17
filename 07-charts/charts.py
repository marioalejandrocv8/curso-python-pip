import matplotlib.pyplot as plt  

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()  # Cambiar 'subplot' por 'subplots'
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')  # Guardar la imagen como 'pie.png'
    plt.close()  # Cerrar la figura para liberar memoria