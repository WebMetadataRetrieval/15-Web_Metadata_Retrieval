# !pip install metadata_parser

url = "https://www.flipkart.com/provogue-running-shoes-men/p/itmef95af271c385?pid=SHOFGS3KUB7PYBYR&lid=LSTSHOFGS3KUB7PYBYREUKP7K&marketplace=FLIPKART&store=osp%2Fcil&srno=b_1_3&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_3_3.dealCard.OMU_A69WHD0X6OJM_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_3_NA_view-all_3&fm=neo%2Fmerchandising&iid=eaa456d3-66b3-47f2-ad8c-f8b7edecbf30.SHOFGS3KUB7PYBYR.SEARCH&ppt=browse&ppn=browse&ssid=k8ex9slveo0000001618503140736"

import metadata_parser
import json

page = metadata_parser.MetadataParser(url)

data = page.metadata

print(data)

