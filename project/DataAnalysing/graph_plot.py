import matplotlib.pyplot as plt


def plot_bar_graph(a,b):
    #import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    #import matplotlib.pyplot as plt
     
    #objects = ('label1', 'label2', 'label3', 'label4')
    objects = b
    y_pos = np.arange(len(objects))
    #performance = [a,b,c,d]
    performance = a
     
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('positivity')
    plt.title('Result History')
    
    plt.savefig('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37-32\\DataExtraction\\project\\results/previous_analysing_history.png')
     
    plt.show()


#plot_bar_graph([100,400,200,300],['label1','label2','label3','label4'])
