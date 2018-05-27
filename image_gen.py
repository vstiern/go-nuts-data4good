# import libs
from keras.preprocessing.image import ImageDataGenerator, array_to_img,
                                      img_to_array, load_img

## specify input_dir with all photos
## for each image in folder
## perform the following pipeline
# load file
img = load_img('train/elephants/adventure-1822636_640.jpg')  # this is a PIL image

# define image generator to rotate, shift, shear, zoom, flip all photos
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        rescale=1./255)

# convert image to np_array w. shape (300, 300, 3)
x = img_to_array(img)
# Numpy array with shape (1, 300, 300, 3)
x = x.reshape((1,) + x.shape)
x.shape

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
# define save_dir
save_dir = '/Users/Mille/GDriveMBD/IE/Term3/go-nuts-data4good/git-go-nuts-data4good/timelapse_dir/generated_data'

i = 0
for batch in datagen.flow(x, batch_size=1,
                            save_to_dir=save_dir, #
                            save_prefix='el', # prefix
                            save_format='jpeg',
                            ): # format
    i += 1
    if i > 20:
        break  # otherwise the generator would loop indefinitely
