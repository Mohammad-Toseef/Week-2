from GenerateFiles import *

carbon_api_url = 'https://api.carbonintensity.org.uk/intensity'
obj = generate_files.GenerateFiles(carbon_api_url, file_name='carb_intensity')
obj.load_dataframe()
obj.to_csv()
