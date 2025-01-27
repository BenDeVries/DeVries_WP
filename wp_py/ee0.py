import ee
from IPython.display import display, Image

ee.Authenticate()
ee.Initialize(project='ee-bdevries252')

bb_long = 153.3342
bb_lat = -28.5000
bb_point = ee.Geometry.Point(bb_long, bb_lat)

lis_long = 28.4941
lis_lat = 153.1536
lis_point = ee.Geometry.Point(lis_long, lis_lat)

elevation = ee.ImageCollection("JAXA/ALOS/AW3D30/V3_2")
scale = 1000
bb_img = elevation.mosaic()
sampled_data = bb_img.sample(bb_point, scale).first()

bb_elevation = sampled_data.get('DSM').getInfo()
print(f"Elevation at the point: {bb_elevation} meters")

lst = ee.ImageCollection("MODIS/061/MOD11A1")
i_date = '2023-01-01'
f_date = '2024-01-01'
lst = lst.select('LST_Day_1km', 'QC_Day').filterDate(i_date, f_date)
roi = bb_point.buffer(5e4)

lst_img = lst.mean()
lst_img = lst_img.select('LST_Day_1km').multiply(0.02)


url = lst_img.getThumbUrl({
    'min': 150, 'max': 350, 'region': roi, 'dimensions': 512,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']})
Image(url=url)
print(url)

task = ee.batch.Export.image.toDrive(image=lst_img,
                                     description='land_temp_near_Ballina_Byron',
                                     scale=30,
                                     region=roi,
                                     fileNamePrefix='lst_test',
                                     crs='EPSG:4326',
                                     fileFormat='GeoTIFF')
task.start()
task.status()
