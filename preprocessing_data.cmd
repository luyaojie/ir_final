python src/preprocessing.py -i data/10w_seg_data/user_tag_query.10W.seg.utf8.TEST -o data/processed/10w/10w.data.TEST --keep-alpha --keep-url
python src/preprocessing.py -i data/2w_seg_data/user_tag_query.2W.seg.utf8.TEST -o data/processed/2w/2w.data.TEST --keep-alpha --keep-url
python src/preprocessing.py -i data/10w_seg_data/user_tag_query.10W.seg.utf8.TRAIN -o data/processed/10w/10w.data.TRAIN --keep-alpha --keep-url
python src/preprocessing.py -i data/2w_seg_data/user_tag_query.2W.seg.utf8.TRAIN -o data/processed/2w/2w.data.TRAIN --keep-alpha --keep-url

python src/preprocessing.py -i data/10w_seg_data/user_tag_query.10W.seg.utf8.TRAIN -o data/processed/10w/10w.data.alpha.TRAIN --keep-alpha
python src/preprocessing.py -i data/2w_seg_data/user_tag_query.2W.seg.utf8.TRAIN -o data/processed/2w/2w.data.alpha.TRAIN --keep-alpha

python src/preprocessing.py -i data/10w_seg_data/user_tag_query.10W.seg.utf8.TRAIN -o data/processed/10w/10w.data.num.TRAIN --keep-num
python src/preprocessing.py -i data/2w_seg_data/user_tag_query.2W.seg.utf8.TRAIN -o data/processed/2w/2w.data.num.TRAIN --keep-num


python src/preprocessing.py -i data/10w_seg_data/user_tag_query.10W.seg.utf8.TRAIN -o data/processed/10w/10w.data.url.TRAIN --keep-url
python src/preprocessing.py -i data/2w_seg_data/user_tag_query.2W.seg.utf8.TRAIN -o data/processed/2w/2w.data.url.TRAIN --keep-url

python src/preprocessing.py -i data/10w_seg_data/user_tag_query.10W.seg.utf8.TRAIN -o data/processed/10w/10w.data.url.TRAIN --keep-url --keep-num
python src/preprocessing.py -i data/2w_seg_data/user_tag_query.2W.seg.utf8.TRAIN -o data/processed/2w/2w.data.url.TRAIN --keep-url --keep-num