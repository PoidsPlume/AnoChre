from typing import List
from pie_extended.cli.utils import get_tagger, get_model
from pie_extended.models.fro.imports import get_iterator_and_processor

# In case you need to download
do_download = False
if do_download:
    for dl in download("fro"):
        x = 1
#set_up
iterator, processor = get_iterator_and_processor()		
model_name = "fro"
tagger = get_tagger(model_name, batch_size=256, device="cuda", model_path=None)

def get_POS_tag(verse):
	output = tagger.tag_str(verse, iterator=iterator, processor=processor))
	POS_list = [entry['POS'] for entry in output]
	return POS_list

print(get_POS_tag("Et la turtre chacier le bievre"))