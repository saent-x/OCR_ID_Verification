from passporteye.mrz.image import MRZPipeline
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, help="image path")

args = vars(ap.parse_args())

# so your preprocessing code would enter here, the image file is in args["doc"],
# then pass the result into MRZPipeline(*,extra_cmdline_params="--oem 0")

mrz = MRZPipeline(args["image"], extra_cmdline_params="--oem 0")
passport_details = mrz.result.to_dict()

# For some stupid reasons the dictionary doesnt work directly when formatted
name = passport_details["names"]
surname = passport_details["surname"]
number = passport_details["number"]
dateofbirth = passport_details["date_of_birth"]
nationality = passport_details["nationality"]
expirationdate = passport_details["expiration_date"]
passporttype = passport_details["mrz_type"]
sex = passport_details["sex"]

print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Passport No: {number}")
print(f"Sex: {sex}")
print(f"Date of Birth: {dateofbirth}")
print(f"Nationality: {nationality}")
print(f"Expiration Date: {expirationdate}")
print(f"Passport Type: {passporttype}")
