import matplotlib.pyplot as plt

def view(data: list) -> list:
    """
    Interactive viewer for a series of DICOM slices using Matplotlib.

    Displays the first slice in the given dataset and allows the user to
    navigate through the slices using the left and right arrow keys and
    can delete slices with delete 'd' key.

    Parameters
    ----------
    data : list of pydicom.dataset.FileDataset
        A list of DICOM slices, typically belonging to a single series.

    Returns
    -------
    list of pydicom.dataset.FileDataset
        A new list of slices with the user-marked slices removed.

    Behavior
    --------
    - Press the right arrow key to advance to the next slice (up to the last slice).
    - Press the left arrow key to go back to the previous slice (down to the first slice).
    - Press the 'd' key to mark the current slice for deletion.
    """
    
    index = [0]
    delete = set()
    fig, ax = plt.subplots()
    im = ax.imshow(data[index[0]].pixel_array, cmap=plt.cm.gray)
    ax.set_title(f"Series {data[index[0]].SeriesNumber}")

    def on_press(event):
        size = len(data)
        if event.key == "right":
            if not (index[0] == size - 1):
                index[0] += 1
                
        elif event.key == "left":
            if not (index[0] == 0):
                index[0] -= 1
        
        elif event.key == "d":
            delete.add(index[0])
                            
        im.set_data(data[index[0]].pixel_array)
        ax.set_title(f"Series {data[index[0]].SeriesNumber}")
        fig.canvas.draw()

    fig.canvas.mpl_connect("key_press_event", on_press)
    plt.show()

    new_data = [data[i] for i in range(len(data)) if i not in delete]

    print(f"Deleted slices: {delete}")
    print(f"Returning {len(new_data)} slices")

    return new_data
