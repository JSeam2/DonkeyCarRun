from skimage import io
from skimage import color

class Preprocess(object):
    def run(self, img):
        return self.frame()

    def run_threaded(self, img):
        img_lab = color.rgb2lab(img) # Image into HSV colorspace
        b = img_lab[:,:,2] # Value aka Lightness

        channel = b
        binary_output = np.zeros_like(channel)
        binary_output[(channel > 20)] = 1
 
        return binary_output


