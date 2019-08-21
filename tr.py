from passporteye.mrz.image import MRZPipeline
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, help="image path")

args = vars(ap.parse_args())

# so your preprocessing code would enter here, the image file is in args["doc"],
# then pass the result into MRZPipeline(*,extra_cmdline_params="--oem 0")

mrz = MRZPipeline(args["image"],extra_cmdline_params="--oem 0")
print(mrz.result)
