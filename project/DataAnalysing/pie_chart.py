import matplotlib.pyplot as plt
import numpy as np





def pie_plot_nave_bayes(a,b):
    labels = ['NEGATIVE','POSITIVE']
    views = [a,b]
    colors=['r', 'g']
    explode = [0,0.2]
    plt.title('RESULT',fontweight="bold" ,color="r" ,fontname="Times New Roman")

    plt.pie(views, labels = labels,explode = explode,autopct = '%1.1f%%',shadow = True, colors=colors)
    plt.savefig('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\results/result.png')
    plt.show()



#pie_plot_nave_bayes(2,3)




