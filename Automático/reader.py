import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def ler(imgs):

    for img in imgs:
        # Load the .mat file
        mat_data = scipy.io.loadmat(img)

        # View the keys in the loaded dictionary
        print(mat_data.keys())

        # Access specific variables from the .mat file
        disp_map = mat_data['disp_map']

        # Check the contents
        print(disp_map)

        plt.imshow(disp_map[:, :, 39], cmap='jet')
        plt.colorbar()  # Add a colorbar
        plt.title("Slice 40 of disp_data")
        plt.show()

def xlsx(arquivo):
    df = pd.read_excel(arquivo, engine='openpyxl')
    # print(df.head())
    return df
