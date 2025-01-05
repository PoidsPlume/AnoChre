from typing import List
from pie_extended.cli.utils import get_tagger, get_model
from pie_extended.models.fro.imports import get_iterator_and_processor

# In case you need to download
do_download = False
if do_download:
    for dl in download("fro"):
        x = 1

modelname = "fro"
tagger = get_tagger(model_name, batch_size=256, device="gpu", model_path=None)


sentences: List[str] = ["Et la turtre chacier le bievre"]
for sentence_group in sentences:
    iterator, processor = get_iterator_and_processor()
    print(tagger.tag_str(sentence_group, iterator=iterator, processor=processor) )