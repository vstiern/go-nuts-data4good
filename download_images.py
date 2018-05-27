### function to download all images
# define id (full id account) -> full WMS intance ID
INSTANCE_ID = '042dbf75-1db4-48af-aa2c-beee173d3339'

# import libs
import numpy as np
import datetime
from base64 import b64encode
from ipyleaflet import Map, WMSLayer
from sentinelhub.data_request import WmsRequest, WcsRequest
from sentinelhub.constants import MimeType, CustomUrlParam
from sentinelhub.common import BBox, CRS
from time_lapse import SentinelHubTimelapse
from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox, CustomUrlParam, Data

# define timelampse function
def make_timelapse(msg, bbox, time_interval, *, full_size=(int(1920 / 2), int(1080 / 2)), mask_images=[],
                   max_cc=0.01, scale_factor=0.2, fps=8, instance_id=INSTANCE_ID, layer, **kwargs):

    # call timelapse function
    timelapse = SentinelHubTimelapse(msg, bbox, time_interval, instance_id,
                                     full_size=full_size, layer=layer, **kwargs)
    timelapse.get_previews()
    timelapse.save_fullres_images()
    timelapse.plot_preview(filename='previews.pdf')
    timelapse.mask_cloudy_images(max_cloud_coverage=max_cc)
    timelapse.plot_cloud_masks(filename='cloudmasks.pdf')
    timelapse.plot_preview(filename='previews_with_cc.pdf')
    timelapse.mask_images(mask_images)
    timelapse.create_date_stamps()
    timelapse.create_timelapse(scale_factor=scale_factor)

    timelapse.make_gif(fps=fps)
    # timelapse.make_video(fps=fps)

## static paramenters
# predinfined ids (see gsheet)
loc_id = [1, 2, 3, 4, 5, 6, 7]
# temporal range
time_interval = ['2015-01-01', '2018-05-25'] # arbitary
# layer to iterate over
layers = ['TRUE_COLOR', 'FALSE_COLOR', 'NDVI',
          'MOISTURE_INDEX', 'SWIR']
# list of all central coordinates
#central_coordinates = [(cc_lat, cc_long)]
#central_coordinates =   [(-0.33006, -78.98691),
#                        (-1.410754,	-78.193159),
#                        (-1.399899,	-78.297529),
#                        (-2.189375,	-78.338196),
#                        (-2.289165,	-78.918399),
#                        (-3.689013,	-79.6188219),
#                        (-0.371995,	-78.832596)]

# list of all bboud boxes
bounding_boxes = [((lat1, long1), (lat2, long2)),
                  ((lat1, long1), (lat2, long2)),
                 ]

# zoom level of inputs
zoom_level = 14 # arbitary
# labels
label = 'landslide'
# cc_thres
cc_thres = 0.2
# image size
tl_size = (int(1920/2), int(1080/2))
# save path
save_path = 'timelapse_dir/model_data/'

### produce timelaps for every iteration of layers and coordinates
### interation
for layer in layers:
    for coord in central_coordinates:
        ## get boundry box
        # specify centre of map
        cc_map = Map(center=[coord[0], coord[1]], zoom=zoom_level) # zoom defined
        # view map to get bbox
        cc_map
        # save bbox coords
        map_bbox = BBox(bbox=([cc_map.bounds[0][1],
                                cc_map.bounds[0][0],
                                cc_map.bounds[1][1],
                                cc_map.bounds[1][0]]
                                ),
                        crs=CRS.WGS84
                        )
        # landslide_name
        folder_name = (save_path + loc_id + '_' + layer)

        # execute timelapse
        make_timelapse(msg=landslide_name,
                       bbox=map_bbox,
                       time_interval=time_interval,
                       max_cc=cc_thres,
                       layer=layer,
                       scale_factor=0.2,
                       full_size=tl_size)
